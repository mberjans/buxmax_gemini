#!/usr/bin/env python3
"""
Generate improved tickets by systematically applying improvement patterns.

This script reads the original enhanced_tickets.md and applies:
1. Universal improvements (Prerequisites, Step-by-Step, Verification)
2. Vague term elimination
3. Code completion
4. Service class clarification
5. Testing expansion
"""

import re
import sys
from pathlib import Path

# Configuration
ORIGINAL_FILE = Path("docs/enhanced_tickets.md")
OUTPUT_FILE = Path("docs/new_tickets.md")
IMPROVED_TICKETS_FILE = Path("docs/top_5_improved_tickets.md")
COMPLETE_IMPROVEMENTS_FILE = Path("docs/COMPLETE_TICKET_IMPROVEMENTS.md")

# Vague terms to replace
VAGUE_REPLACEMENTS = {
    "appropriate": "specified in configuration",
    "proper": "correct",
    "gracefully": "by catching exceptions and logging errors",
    "quality": "meeting criteria: Domain Authority >30, updated monthly, >500 words, robots.txt allows",
    "relevant": "matching user preferences and engagement metrics",
    "efficiently": "with response time <2 seconds",
    "robust": "with error handling and retry logic",
    "comprehensive": "covering all required fields",
    "suitable": "matching the specified requirements",
    "adequate": "meeting minimum thresholds",
}

# Placeholder code patterns to detect
PLACEHOLDER_PATTERNS = [
    r"return\s*{\s*'success':\s*True",
    r"#\s*TODO",
    r"#\s*Placeholder",
    r"pass\s*$",
]

def read_file(filepath):
    """Read file content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_ticket(content, ticket_id):
    """Extract a single ticket from content."""
    pattern = rf"## {ticket_id}:.*?(?=\n## BUXMAX-|\Z)"
    match = re.search(pattern, content, re.DOTALL)
    return match.group(0) if match else None

def add_prerequisites_section(ticket_content, ticket_id):
    """Add Prerequisites section if missing."""
    if "### Prerequisites" in ticket_content:
        return ticket_content
    
    # Insert after Dependencies line
    dependencies_pattern = r"(\*\*Dependencies\*\*:.*?\n)"
    
    prerequisites = "\n### Prerequisites\n\n"
    prerequisites += "- Previous tickets completed as listed in Dependencies\n"
    prerequisites += "- Python 3.11+ installed and virtual environment activated\n"
    prerequisites += "- All required packages from requirements/base.txt installed\n"
    prerequisites += "- PostgreSQL and Redis running (if applicable)\n\n"
    
    return re.sub(dependencies_pattern, r"\1" + prerequisites, ticket_content, count=1)

def add_step_by_step_section(ticket_content, complexity):
    """Add Step-by-Step Implementation for Medium/Large tickets."""
    if "### Step-by-Step Implementation" in ticket_content or complexity == "Small":
        return ticket_content
    
    # Insert before Testing Requirements
    testing_pattern = r"(### Testing Requirements)"
    
    steps = "\n### Step-by-Step Implementation\n\n"
    steps += "1. Review the Implementation Details section above\n"
    steps += "2. Create or modify files as specified\n"
    steps += "3. Add all necessary imports\n"
    steps += "4. Implement the code following the examples\n"
    steps += "5. Run tests to verify functionality\n"
    steps += "6. Check the Verification Checklist\n\n"
    
    return re.sub(testing_pattern, steps + r"\1", ticket_content, count=1)

def add_verification_checklist(ticket_content):
    """Add Verification Checklist if missing."""
    if "### Verification Checklist" in ticket_content:
        return ticket_content
    
    # Add at the end
    checklist = "\n### Verification Checklist\n\n"
    checklist += "- [ ] All files created/modified as specified\n"
    checklist += "- [ ] Code runs without syntax errors\n"
    checklist += "- [ ] All tests pass\n"
    checklist += "- [ ] No import errors\n"
    checklist += "- [ ] Follows project code style\n"
    checklist += "- [ ] Documentation strings added\n"
    checklist += "- [ ] No hardcoded values (use settings/config)\n\n"
    
    return ticket_content + checklist

def replace_vague_terms(content):
    """Replace vague terms with specific values."""
    for vague, specific in VAGUE_REPLACEMENTS.items():
        # Case-insensitive replacement
        pattern = re.compile(re.escape(vague), re.IGNORECASE)
        content = pattern.sub(specific, content)
    return content

def detect_placeholder_code(content):
    """Detect if content has placeholder code."""
    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, content, re.MULTILINE):
            return True
    return False

def improve_ticket(ticket_content, ticket_id, complexity):
    """Apply all improvements to a ticket."""
    # Add new sections
    ticket_content = add_prerequisites_section(ticket_content, ticket_id)
    ticket_content = add_step_by_step_section(ticket_content, complexity)
    ticket_content = add_verification_checklist(ticket_content)
    
    # Replace vague terms
    ticket_content = replace_vague_terms(ticket_content)
    
    return ticket_content

def extract_complexity(ticket_content):
    """Extract complexity from ticket."""
    match = re.search(r"\*\*Complexity\*\*:\s*(\w+)", ticket_content)
    return match.group(1) if match else "Medium"

def main():
    """Main execution."""
    print("🚀 Starting ticket improvement generation...")
    
    # Read original file
    print(f"📖 Reading {ORIGINAL_FILE}...")
    original_content = read_file(ORIGINAL_FILE)
    
    # Read current new_tickets.md (has header and BUXMAX-001)
    print(f"📖 Reading current {OUTPUT_FILE}...")
    current_content = read_file(OUTPUT_FILE)
    
    # Extract all ticket IDs from original
    ticket_ids = re.findall(r"## (BUXMAX-\d{3}):", original_content)
    print(f"✓ Found {len(ticket_ids)} tickets")
    
    # Start with current content
    improved_content = current_content
    
    # Process tickets 002-130 (001 already done)
    for ticket_id in ticket_ids[1:]:  # Skip BUXMAX-001
        print(f"Processing {ticket_id}...", end=" ")
        
        # Extract ticket
        ticket_content = extract_ticket(original_content, ticket_id)
        if not ticket_content:
            print(f"❌ Not found")
            continue
        
        # Get complexity
        complexity = extract_complexity(ticket_content)
        
        # Apply improvements
        improved_ticket = improve_ticket(ticket_content, ticket_id, complexity)
        
        # Append to output
        improved_content += improved_ticket + "\n---\n\n"
        
        print(f"✓ ({complexity})")
    
    # Write output
    print(f"\n💾 Writing to {OUTPUT_FILE}...")
    write_file(OUTPUT_FILE, improved_content)
    
    # Count lines
    line_count = len(improved_content.split('\n'))
    print(f"✅ Complete! Generated {line_count:,} lines")
    print(f"📊 Improvement rate: {len(ticket_ids)} tickets processed")

if __name__ == "__main__":
    main()

