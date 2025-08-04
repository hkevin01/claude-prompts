import * as fs from 'fs';
import * as path from 'path';
import Fuse from 'fuse.js';
import { promisify } from 'util';
import { performance } from 'perf_hooks';

const readFileAsync = promisify(fs.readFile);
const writeFileAsync = promisify(fs.writeFile);

interface PromptMetadata {
  title: string;
  description: string;
  tags: string[];
  category: string;
  difficulty: string;
  content: string;
  path: string;
}

export class PromptOptimizer {
  private searchIndex: Fuse<PromptMetadata>;
  private promptCache: Map<string, PromptMetadata>;
  private searchOptions = {
    keys: ['title', 'description', 'tags', 'category'],
    threshold: 0.4,
    includeScore: true,
  };

  constructor() {
    this.promptCache = new Map();
  }

  async buildSearchIndex(promptsDir: string): Promise<void> {
    console.log('Building search index...');
    const startTime = performance.now();

    const prompts = await this.loadPrompts(promptsDir);
    this.searchIndex = new Fuse(prompts, this.searchOptions);

    const endTime = performance.now();
    console.log(`Search index built in ${(endTime - startTime).toFixed(2)}ms`);

    // Cache the index for faster startup
    await this.saveSearchIndex();
  }

  private async loadPrompts(dir: string): Promise<PromptMetadata[]> {
    const prompts: PromptMetadata[] = [];
    const files = await this.walkDirectory(dir);

    for (const file of files) {
      if (path.extname(file) === '.md') {
        const content = await readFileAsync(file, 'utf8');
        const metadata = this.parsePromptMetadata(content, file);
        if (metadata) {
          prompts.push(metadata);
          this.promptCache.set(file, metadata);
        }
      }
    }

    return prompts;
  }

  private async walkDirectory(dir: string): Promise<string[]> {
    const files: string[] = [];
    const items = await fs.promises.readdir(dir, { withFileTypes: true });

    for (const item of items) {
      const fullPath = path.join(dir, item.name);
      if (item.isDirectory()) {
        files.push(...await this.walkDirectory(fullPath));
      } else {
        files.push(fullPath);
      }
    }

    return files;
  }

  private parsePromptMetadata(content: string, filePath: string): PromptMetadata | null {
    try {
      const frontmatterMatch = content.match(/---\n([\s\S]*?)\n---/);
      if (!frontmatterMatch) return null;

      const frontmatter = frontmatterMatch[1];
      const metadata = this.parseFrontmatter(frontmatter);

      return {
        ...metadata,
        content: content.replace(/---\n[\s\S]*?\n---/, '').trim(),
        path: filePath
      };
    } catch (error) {
      console.error(`Error parsing prompt metadata for ${filePath}:`, error);
      return null;
    }
  }

  private parseFrontmatter(frontmatter: string): any {
    const metadata: any = {};
    const lines = frontmatter.split('\n');

    for (const line of lines) {
      const match = line.match(/^(\w+):\s*(.+)$/);
      if (match) {
        const [, key, value] = match;
        try {
          metadata[key] = JSON.parse(value);
        } catch {
          metadata[key] = value.replace(/^["']|["']$/g, '');
        }
      }
    }

    return metadata;
  }

  async search(query: string, limit = 10): Promise<Array<{ item: PromptMetadata; score: number }>> {
    if (!this.searchIndex) {
      await this.loadSearchIndex();
    }

    const startTime = performance.now();
    const results = this.searchIndex.search(query, { limit });
    const endTime = performance.now();

    console.log(`Search completed in ${(endTime - startTime).toFixed(2)}ms`);
    return results;
  }

  private async saveSearchIndex(): Promise<void> {
    const indexPath = path.join(__dirname, '../data/search-index.json');
    await writeFileAsync(indexPath, JSON.stringify(this.searchIndex.toJSON()), 'utf8');
  }

  private async loadSearchIndex(): Promise<void> {
    try {
      const indexPath = path.join(__dirname, '../data/search-index.json');
      const indexData = await readFileAsync(indexPath, 'utf8');
      this.searchIndex = Fuse.parseIndex(JSON.parse(indexData));
    } catch (error) {
      console.error('Error loading search index:', error);
      throw error;
    }
  }

  getPromptFromCache(filePath: string): PromptMetadata | undefined {
    return this.promptCache.get(filePath);
  }

  clearCache(): void {
    this.promptCache.clear();
  }
}
