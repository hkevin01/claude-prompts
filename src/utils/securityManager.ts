import * as crypto from 'crypto';
import * as fs from 'fs';
import * as path from 'path';
import { promisify } from 'util';

const writeFileAsync = promisify(fs.writeFile);
const readFileAsync = promisify(fs.readFile);
const mkdirAsync = promisify(fs.mkdir);

export class SecurityManager {
  private readonly encryptionKey: Buffer;
  private readonly algorithm = 'aes-256-gcm';
  private readonly keyLength = 32;
  private readonly ivLength = 12;
  private readonly authTagLength = 16;

  constructor(key?: string) {
    if (key) {
      this.encryptionKey = Buffer.from(key, 'base64');
    } else {
      this.encryptionKey = crypto.randomBytes(this.keyLength);
    }
  }

  async encryptData(data: string): Promise<string> {
    const iv = crypto.randomBytes(this.ivLength);
    const cipher = crypto.createCipheriv(this.algorithm, this.encryptionKey, iv);

    let encryptedData = cipher.update(data, 'utf8', 'base64');
    encryptedData += cipher.final('base64');

    const authTag = cipher.getAuthTag();

    const complete = JSON.stringify({
      iv: iv.toString('base64'),
      encryptedData,
      authTag: authTag.toString('base64')
    });

    return Buffer.from(complete).toString('base64');
  }

  async decryptData(encryptedString: string): Promise<string> {
    const data = JSON.parse(Buffer.from(encryptedString, 'base64').toString());
    const iv = Buffer.from(data.iv, 'base64');
    const authTag = Buffer.from(data.authTag, 'base64');

    const decipher = crypto.createDecipheriv(this.algorithm, this.encryptionKey, iv);
    decipher.setAuthTag(authTag);

    let decrypted = decipher.update(data.encryptedData, 'base64', 'utf8');
    decrypted += decipher.final('utf8');

    return decrypted;
  }

  async secureStore(data: any, filePath: string): Promise<void> {
    const dir = path.dirname(filePath);
    await mkdirAsync(dir, { recursive: true });

    const encryptedData = await this.encryptData(JSON.stringify(data));
    await writeFileAsync(filePath, encryptedData, 'utf8');
  }

  async secureRetrieve(filePath: string): Promise<any> {
    const encryptedData = await readFileAsync(filePath, 'utf8');
    const decryptedData = await this.decryptData(encryptedData);
    return JSON.parse(decryptedData);
  }

  hashString(input: string): string {
    return crypto.createHash('sha256').update(input).digest('hex');
  }

  generateToken(): string {
    return crypto.randomBytes(32).toString('hex');
  }
}

export interface UserData {
  userId: string;
  settings: {
    customPrompts?: boolean;
    telemetryEnabled?: boolean;
    cloudSync?: boolean;
  };
  customPrompts?: Array<{
    id: string;
    content: string;
    metadata: Record<string, unknown>;
  }>;
}

export class UserDataManager {
  private readonly security: SecurityManager;
  private readonly dataDir: string;

  constructor(dataDir: string, encryptionKey?: string) {
    this.security = new SecurityManager(encryptionKey);
    this.dataDir = dataDir;
  }

  private getUserDataPath(userId: string): string {
    const hashedId = this.security.hashString(userId);
    return path.join(this.dataDir, `${hashedId}.enc`);
  }

  async saveUserData(userId: string, data: UserData): Promise<void> {
    const filePath = this.getUserDataPath(userId);
    await this.security.secureStore(data, filePath);
  }

  async getUserData(userId: string): Promise<UserData | null> {
    try {
      const filePath = this.getUserDataPath(userId);
      return await this.security.secureRetrieve(filePath);
    } catch (error) {
      if ((error as NodeJS.ErrnoException).code === 'ENOENT') {
        return null;
      }
      throw error;
    }
  }

  async updateUserSettings(userId: string, settings: Partial<UserData['settings']>): Promise<void> {
    const userData = await this.getUserData(userId) || {
      userId,
      settings: {},
      customPrompts: []
    };

    userData.settings = { ...userData.settings, ...settings };
    await this.saveUserData(userId, userData);
  }

  async addCustomPrompt(
    userId: string,
    content: string,
    metadata: Record<string, unknown>
  ): Promise<string> {
    const userData = await this.getUserData(userId) || {
      userId,
      settings: {},
      customPrompts: []
    };

    const promptId = this.security.generateToken();
    userData.customPrompts = userData.customPrompts || [];
    userData.customPrompts.push({ id: promptId, content, metadata });

    await this.saveUserData(userId, userData);
    return promptId;
  }

  async deleteCustomPrompt(userId: string, promptId: string): Promise<boolean> {
    const userData = await this.getUserData(userId);
    if (!userData?.customPrompts) return false;

    const index = userData.customPrompts.findIndex(p => p.id === promptId);
    if (index === -1) return false;

    userData.customPrompts.splice(index, 1);
    await this.saveUserData(userId, userData);
    return true;
  }
}
