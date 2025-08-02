import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';
import * as yaml from 'js-yaml';
import { Prompt, PromptCategory } from './types';

export class PromptManager {
    private prompts: Prompt[] = [];
    private categories: PromptCategory[] = [];
    private context: vscode.ExtensionContext;

    constructor(context: vscode.ExtensionContext) {
        this.context = context;
    }

    async refreshPrompts(): Promise<void> {
        this.prompts = [];
        this.categories = [];

        // Get prompts from extension
        const extensionPath = this.context.extensionPath;
        const promptsPath = path.join(extensionPath, 'src', 'prompts');
        
        if (fs.existsSync(promptsPath)) {
            await this.loadPromptsFromDirectory(promptsPath);
        }

        // Load custom prompts if configured
        const config = vscode.workspace.getConfiguration('claude-prompts');
        const customPath = config.get<string>('customPromptsPath');
        
        if (customPath && fs.existsSync(customPath)) {
            await this.loadPromptsFromDirectory(customPath);
        }

        // Organize by categories
        this.organizeByCategories();
    }

    private async loadPromptsFromDirectory(dir: string): Promise<void> {
        const categories = ['coding', 'creative', 'business', 'analysis', 'educational', 'personal'];
        
        for (const category of categories) {
            const categoryPath = path.join(dir, category);
            if (fs.existsSync(categoryPath)) {
                const files = fs.readdirSync(categoryPath).filter(file => file.endsWith('.md'));
                
                for (const file of files) {
                    const filePath = path.join(categoryPath, file);
                    try {
                        const prompt = await this.parsePromptFile(filePath);
                        if (prompt) {
                            this.prompts.push(prompt);
                        }
                    } catch (error) {
                        console.error(`Error parsing prompt file ${filePath}:`, error);
                    }
                }
            }
        }
    }

    private async parsePromptFile(filePath: string): Promise<Prompt | null> {
        const content = fs.readFileSync(filePath, 'utf8');
        
        // Parse frontmatter
        const frontmatterRegex = /^---\n([\s\S]*?)\n---\n([\s\S]*)$/;
        const match = content.match(frontmatterRegex);
        
        if (!match) {
            return null;
        }

        try {
            const frontmatter = yaml.load(match[1]) as any;
            const promptContent = this.extractPromptContent(match[2]);
            
            return {
                title: frontmatter.title || 'Untitled',
                category: frontmatter.category || 'coding',
                tags: frontmatter.tags || [],
                difficulty: frontmatter.difficulty || 'beginner',
                description: frontmatter.description || '',
                author: frontmatter.author,
                date: frontmatter.date,
                version: frontmatter.version,
                content: promptContent,
                filePath: filePath
            };
        } catch (error) {
            console.error(`Error parsing YAML frontmatter in ${filePath}:`, error);
            return null;
        }
    }

    private extractPromptContent(markdownContent: string): string {
        // Look for prompt section between ```text and ```
        const promptRegex = /```text\n([\s\S]*?)\n```/;
        const match = markdownContent.match(promptRegex);
        
        if (match) {
            return match[1].trim();
        }
        
        // Fallback: look for ## Prompt section
        const sections = markdownContent.split(/^## /m);
        const promptSection = sections.find(section => section.startsWith('Prompt'));
        
        if (promptSection) {
            // Remove the "Prompt" heading and extract content
            const lines = promptSection.split('\n').slice(1);
            let content = '';
            let inCodeBlock = false;
            
            for (const line of lines) {
                if (line.startsWith('```')) {
                    inCodeBlock = !inCodeBlock;
                    continue;
                }
                if (inCodeBlock) {
                    content += line + '\n';
                }
            }
            
            return content.trim();
        }
        
        // Last resort: return first paragraph
        const paragraphs = markdownContent.split('\n\n');
        return paragraphs[0] || '';
    }

    private organizeByCategories(): void {
        const categoryMap = new Map<string, Prompt[]>();
        
        this.prompts.forEach(prompt => {
            if (!categoryMap.has(prompt.category)) {
                categoryMap.set(prompt.category, []);
            }
            categoryMap.get(prompt.category)!.push(prompt);
        });
        
        this.categories = Array.from(categoryMap.entries()).map(([name, prompts]) => ({
            name,
            prompts: prompts.sort((a, b) => a.title.localeCompare(b.title))
        }));
        
        this.categories.sort((a, b) => a.name.localeCompare(b.name));
    }

    getAllPrompts(): Prompt[] {
        return this.prompts;
    }

    getCategories(): PromptCategory[] {
        return this.categories;
    }

    async searchPrompts(searchTerm: string): Promise<Prompt[]> {
        const term = searchTerm.toLowerCase();
        
        return this.prompts.filter(prompt => {
            return (
                prompt.title.toLowerCase().includes(term) ||
                prompt.description.toLowerCase().includes(term) ||
                prompt.tags.some(tag => tag.toLowerCase().includes(term)) ||
                prompt.category.toLowerCase().includes(term) ||
                prompt.content.toLowerCase().includes(term)
            );
        }).sort((a, b) => {
            // Prioritize title matches
            const aTitle = a.title.toLowerCase().includes(term);
            const bTitle = b.title.toLowerCase().includes(term);
            
            if (aTitle && !bTitle) return -1;
            if (!aTitle && bTitle) return 1;
            
            return a.title.localeCompare(b.title);
        });
    }

    getPromptByPath(filePath: string): Prompt | undefined {
        return this.prompts.find(prompt => prompt.filePath === filePath);
    }
}
