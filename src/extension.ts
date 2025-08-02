import * as vscode from 'vscode';
import { PromptsProvider } from './extension/promptsProvider';
import { PromptSearchProvider } from './extension/promptSearchProvider';
import { PromptManager } from './extension/promptManager';

let promptsProvider: PromptsProvider;
let promptSearchProvider: PromptSearchProvider;
let promptManager: PromptManager;

export function activate(context: vscode.ExtensionContext) {
    console.log('Claude Prompts extension is now active!');

    // Initialize core components
    promptManager = new PromptManager(context);
    promptsProvider = new PromptsProvider(promptManager);
    promptSearchProvider = new PromptSearchProvider(promptManager);

    // Register tree data providers
    vscode.window.createTreeView('promptsExplorer', {
        treeDataProvider: promptsProvider,
        showCollapseAll: true
    });

    vscode.window.createTreeView('promptsSearch', {
        treeDataProvider: promptSearchProvider,
        showCollapseAll: true
    });

    // Register commands
    const commands = [
        vscode.commands.registerCommand('claude-prompts.showPrompts', () => {
            vscode.commands.executeCommand('workbench.view.extension.claude-prompts');
        }),

        vscode.commands.registerCommand('claude-prompts.insertPrompt', async (promptItem) => {
            if (promptItem && promptItem.prompt) {
                await insertPromptText(promptItem.prompt.content);
            } else {
                // Show quick pick if no specific prompt selected
                const selectedPrompt = await showPromptQuickPick();
                if (selectedPrompt) {
                    await insertPromptText(selectedPrompt.content);
                }
            }
        }),

        vscode.commands.registerCommand('claude-prompts.searchPrompts', async () => {
            const searchTerm = await vscode.window.showInputBox({
                placeHolder: 'Search prompts by title, tags, or description...',
                prompt: 'Enter search terms'
            });

            if (searchTerm) {
                const results = await promptManager.searchPrompts(searchTerm);
                promptSearchProvider.updateSearchResults(results, searchTerm);
                vscode.commands.executeCommand('setContext', 'claude-prompts.hasSearchResults', results.length > 0);
                
                // Show search results view
                vscode.commands.executeCommand('workbench.view.extension.claude-prompts');
                vscode.commands.executeCommand('promptsSearch.focus');
            }
        }),

        vscode.commands.registerCommand('claude-prompts.refreshPrompts', async () => {
            await promptManager.refreshPrompts();
            promptsProvider.refresh();
            vscode.window.showInformationMessage('Claude Prompts refreshed!');
        }),

        vscode.commands.registerCommand('claude-prompts.openPromptFile', async (promptItem) => {
            if (promptItem && promptItem.prompt && promptItem.prompt.filePath) {
                const uri = vscode.Uri.file(promptItem.prompt.filePath);
                await vscode.window.showTextDocument(uri);
            }
        })
    ];

    // Register all commands with context
    commands.forEach(cmd => context.subscriptions.push(cmd));

    // Initialize prompts
    promptManager.refreshPrompts().then(() => {
        promptsProvider.refresh();
    });

    // Show welcome message
    vscode.window.showInformationMessage(
        'Claude Prompts Collection is ready! Use Ctrl+Shift+P then "Claude Prompts" to get started.',
        'Show Prompts'
    ).then(selection => {
        if (selection === 'Show Prompts') {
            vscode.commands.executeCommand('claude-prompts.showPrompts');
        }
    });
}

async function insertPromptText(content: string): Promise<void> {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
        vscode.window.showWarningMessage('No active editor found. Please open a file first.');
        return;
    }

    const position = editor.selection.active;
    await editor.edit(editBuilder => {
        editBuilder.insert(position, content);
    });

    vscode.window.showInformationMessage('Prompt inserted successfully!');
}

async function showPromptQuickPick() {
    const prompts = promptManager.getAllPrompts();
    
    const quickPickItems = prompts.map((prompt: any) => ({
        label: prompt.title,
        description: prompt.category,
        detail: prompt.description,
        prompt: prompt
    }));

    const selected = await vscode.window.showQuickPick(quickPickItems, {
        placeHolder: 'Select a prompt to insert',
        matchOnDescription: true,
        matchOnDetail: true
    });

    return selected?.prompt;
}

export function deactivate() {
    console.log('Claude Prompts extension is deactivated');
}
