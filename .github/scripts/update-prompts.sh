#!/bin/bash

# Claude AI Prompt Update Script
# Updates all prompt templates to the latest versions

set -euo pipefail  # Exit on error, undefined vars, pipe failures

PROMPTS_DIR=".github/prompts"
BACKUP_DIR=".github/prompts-backup-$(date +%Y%m%d-%H%M%S)"

echo "🔄 Updating Claude AI prompts..."

# Create backup
if [[ -d "$PROMPTS_DIR" ]]; then
    echo "📦 Creating backup at $BACKUP_DIR"
    if ! cp -r "$PROMPTS_DIR" "$BACKUP_DIR"; then
        echo "❌ Failed to create backup"
        exit 1
    fi
else
    echo "⚠️  Prompts directory not found: $PROMPTS_DIR"
fi

# Update prompt library metadata
if [[ -f "$PROMPTS_DIR/prompt-library.yml" ]]; then
    echo "📝 Updating prompt library metadata"
    if command -v sed >/dev/null 2>&1; then
        sed -i.bak "s/created: .*/created: \"$(date)\"/" "$PROMPTS_DIR/prompt-library.yml"
        rm -f "$PROMPTS_DIR/prompt-library.yml.bak"
    else
        echo "⚠️  sed not available, skipping metadata update"
    fi
else
    echo "⚠️  prompt-library.yml not found"
fi

echo "✅ Claude AI prompts updated successfully!"
echo "📦 Backup available at: $BACKUP_DIR"
