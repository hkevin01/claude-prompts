import * as vscode from 'vscode';
import { PromptManager } from './promptManager';
import { Prompt, PromptCategory } from './types';

export class PromptsProvider implements vscode.TreeDataProvider<PromptItem> {
    private _onDidChangeTreeData: vscode.EventEmitter<PromptItem | undefined | null | void> = new vscode.EventEmitter<PromptItem | undefined | null | void>();
    readonly onDidChangeTreeData: vscode.Event<PromptItem | undefined | null | void> = this._onDidChangeTreeData.event;

    constructor(private promptManager: PromptManager) {}

    refresh(): void {
        this._onDidChangeTreeData.fire();
    }

    getTreeItem(element: PromptItem): vscode.TreeItem {
        return element;
    }

    getChildren(element?: PromptItem): Thenable<PromptItem[]> {
        if (!element) {
            // Return categories
            const categories = this.promptManager.getCategories();
            return Promise.resolve(categories.map(category => new PromptCategoryItem(category)));
        } else if (element.contextValue === 'category') {
            // Return prompts in category
            const categoryItem = element as PromptCategoryItem;
            return Promise.resolve(categoryItem.category.prompts.map(prompt => new PromptFileItem(prompt)));
        }

        return Promise.resolve([]);
    }
}

class PromptCategoryItem extends vscode.TreeItem {
    constructor(public readonly category: PromptCategory) {
        super(category.name, vscode.TreeItemCollapsibleState.Expanded);
        
        this.tooltip = `${category.name} (${category.prompts.length} prompts)`;
        this.description = `${category.prompts.length} prompts`;
        this.contextValue = 'category';
        this.iconPath = new vscode.ThemeIcon('folder');
    }
}

class PromptFileItem extends vscode.TreeItem {
    constructor(public readonly prompt: Prompt) {
        super(prompt.title, vscode.TreeItemCollapsibleState.None);
        
        this.tooltip = prompt.description;
        this.description = this.getDifficultyIcon(prompt.difficulty) + prompt.category;
        this.contextValue = 'prompt';
        this.command = {
            command: 'claude-prompts.insertPrompt',
            title: 'Insert Prompt',
            arguments: [this]
        };

        // Set icon based on difficulty
        this.iconPath = this.getDifficultyThemeIcon(prompt.difficulty);
    }

    private getDifficultyIcon(difficulty: string): string {
        switch (difficulty) {
            case 'beginner': return '🟢 ';
            case 'intermediate': return '🟡 ';
            case 'advanced': return '🔴 ';
            default: return '';
        }
    }

    private getDifficultyThemeIcon(difficulty: string): vscode.ThemeIcon {
        switch (difficulty) {
            case 'beginner': return new vscode.ThemeIcon('circle-filled', new vscode.ThemeColor('charts.green'));
            case 'intermediate': return new vscode.ThemeIcon('circle-filled', new vscode.ThemeColor('charts.yellow'));
            case 'advanced': return new vscode.ThemeIcon('circle-filled', new vscode.ThemeColor('charts.red'));
            default: return new vscode.ThemeIcon('circle-outline');
        }
    }
}

export type PromptItem = PromptCategoryItem | PromptFileItem;
