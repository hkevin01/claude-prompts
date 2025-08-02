import * as vscode from 'vscode';
import { PromptManager } from './promptManager';
import { Prompt } from './types';

export class PromptSearchProvider implements vscode.TreeDataProvider<SearchPromptItem> {
    private _onDidChangeTreeData: vscode.EventEmitter<SearchPromptItem | undefined | null | void> = new vscode.EventEmitter<SearchPromptItem | undefined | null | void>();
    readonly onDidChangeTreeData: vscode.Event<SearchPromptItem | undefined | null | void> = this._onDidChangeTreeData.event;

    private searchResults: Prompt[] = [];
    private searchTerm: string = '';

    constructor(private readonly promptManager: PromptManager) {}

    updateSearchResults(results: Prompt[], searchTerm: string): void {
        this.searchResults = results;
        this.searchTerm = searchTerm;
        this._onDidChangeTreeData.fire();
    }

    refresh(): void {
        this._onDidChangeTreeData.fire();
    }

    getTreeItem(element: SearchPromptItem): vscode.TreeItem {
        return element;
    }

    getChildren(): Thenable<SearchPromptItem[]> {
        if (this.searchResults.length === 0) {
            return Promise.resolve([]);
        }

        return Promise.resolve(
            this.searchResults.map(prompt => new SearchPromptItem(prompt, this.searchTerm))
        );
    }
}

class SearchPromptItem extends vscode.TreeItem {
    constructor(public readonly prompt: Prompt, searchTerm: string) {
        super(prompt.title, vscode.TreeItemCollapsibleState.None);
        
        this.tooltip = prompt.description;
        this.description = `${prompt.category} • ${prompt.difficulty}`;
        this.contextValue = 'prompt';
        this.command = {
            command: 'claude-prompts.insertPrompt',
            title: 'Insert Prompt',
            arguments: [this]
        };

        // Highlight search term in label if it matches
        if (prompt.title.toLowerCase().includes(searchTerm.toLowerCase())) {
            this.iconPath = new vscode.ThemeIcon('search');
        } else {
            this.iconPath = new vscode.ThemeIcon('file-text');
        }
    }
}
