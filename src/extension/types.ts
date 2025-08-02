export interface Prompt {
    title: string;
    category: string;
    tags: string[];
    difficulty: 'beginner' | 'intermediate' | 'advanced';
    description: string;
    author?: string;
    date?: string;
    version?: string;
    content: string;
    filePath: string;
}

export interface PromptCategory {
    name: string;
    prompts: Prompt[];
}

export interface SearchResult {
    prompt: Prompt;
    score: number;
    matches: string[];
}
