#!/bin/bash

# Claude AI Prompt Selector
# Usage: ./claude-prompt.sh [prompt-type] [specific-prompt]

PROMPT_TYPE="$1"
SPECIFIC_PROMPT="$2"
PROMPTS_DIR=".github/prompts"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

show_usage() {
    echo "Usage: $0 [prompt-type] [specific-prompt]"
    echo ""
    echo "Available prompt types:"
    echo "  code-review     - Code review and quality analysis"
    echo "  development     - Debugging and development assistance"
    echo "  architecture    - System and API design"
    echo "  optimization    - Performance and algorithm optimization"
    echo "  testing         - Test-driven development and automation"
    echo "  generation      - Code generation from specifications"
    echo "  legacy          - Legacy code modernization"
    echo "  api             - API development and design"
    echo ""
    echo "Examples:"
    echo "  $0 code-review comprehensive-review"
    echo "  $0 development debugging"
    echo "  $0 architecture system-design"
}

list_prompts() {
    local category="$1"
    echo -e "${BLUE}Available prompts in $category:${NC}"
    find "$PROMPTS_DIR/$category" -name "*.md" -type f | while read -r file; do
        basename="$(basename "$file" .md)"
        echo "  - $basename"
    done
}

display_prompt() {
    local prompt_file="$1"
    if [[ -f "$prompt_file" ]]; then
        echo -e "${GREEN}🤖 Claude AI Prompt:${NC}"
        echo "========================"
        cat "$prompt_file"
        echo ""
        echo "========================"
        echo -e "${YELLOW}💡 Copy the above prompt and paste it into Claude AI${NC}"
    else
        echo "❌ Prompt file not found: $prompt_file"
        return 1
    fi
}

# Main logic
if [[ -z "$PROMPT_TYPE" ]]; then
    show_usage
    exit 0
fi

if [[ ! -d "$PROMPTS_DIR/$PROMPT_TYPE" ]]; then
    echo "❌ Unknown prompt type: $PROMPT_TYPE"
    show_usage
    exit 1
fi

if [[ -z "$SPECIFIC_PROMPT" ]]; then
    list_prompts "$PROMPT_TYPE"
    exit 0
fi

PROMPT_FILE="$PROMPTS_DIR/$PROMPT_TYPE/$SPECIFIC_PROMPT.md"
display_prompt "$PROMPT_FILE"
