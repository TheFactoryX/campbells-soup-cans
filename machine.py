#!/usr/bin/env python3
"""
The Factory Machine - Production Line 1
Generates code soup cans daily, like Warhol's repetitive art.
"""

import os
import json
import random
import time
from datetime import datetime
from pathlib import Path
from typing import Optional
import requests

# OpenRouter API configuration
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODELS_URL = "https://openrouter.ai/api/v1/models"

# The unified task - same task, different implementations
# Like Warhol's soup cans: same subject, subtle variations
THE_TASK = """
Write a Python program that generates random profound-sounding but completely meaningless philosophical quotes.

Requirements:
- Must be a SINGLE Python file that can run directly
- Must be valid Python code (no syntax errors)
- Generate at least 3-5 random "deep" quotes that sound wise but mean nothing
- Use random combinations of words like: consciousness, paradigm, essence, transcendence, quantum, reality, existence, void, cosmic, eternal, etc.
- Make it absurd and funny but grammatically correct
- Keep it simple - just pure Python, no external dependencies

Example output style (make your own):
"The quantum essence of the void transcends all paradigms"
"Consciousness is the eternal dance between nothingness and everything"

Be creative and weird! Each AI should generate different combinations.
"""


def get_models(free_only: bool = True) -> list:
    """Fetch list of models from OpenRouter."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    }

    response = requests.get(MODELS_URL, headers=headers, timeout=30)
    response.raise_for_status()

    models_data = response.json()

    models = []
    for model in models_data.get("data", []):
        pricing = model.get("pricing", {})
        prompt_price = float(pricing.get("prompt", "1"))
        completion_price = float(pricing.get("completion", "1"))

        is_free = prompt_price == 0 and completion_price == 0

        # Filter based on free_only parameter
        if free_only and not is_free:
            continue
        if not free_only and is_free:
            continue

        models.append({
            "id": model["id"],
            "name": model.get("name", model["id"]),
            "context_length": model.get("context_length", 0),
            "is_free": is_free
        })

    return models


def select_model(prefer_free: bool = True) -> dict:
    """Select a random model from OpenRouter."""
    models = get_models(free_only=prefer_free)

    if not models:
        print(f"⚠️  No {'free' if prefer_free else 'paid'} models found, using fallback")
        return {"id": "meta-llama/llama-3.2-3b-instruct:free", "name": "Llama 3.2 3B (free)", "is_free": True}

    # Randomly select a model
    selected = random.choice(models)
    return selected


def call_openrouter(model_id: str, prompt: str) -> str:
    """Call OpenRouter API to generate code using streaming."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model_id,
        "messages": [
            {
                "role": "system",
                "content": "You are a creative Python code artist. Generate ONLY Python code, nothing else. The code must be a SINGLE Python file that can run directly. Write valid, executable Python code. Be creative and playful!"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": True,
    }

    response = requests.post(API_URL, headers=headers, json=payload, stream=True, timeout=120)
    response.raise_for_status()

    # Collect streamed response
    full_content = ""
    print("🔄 Receiving response", end="", flush=True)

    for line in response.iter_lines():
        if not line:
            continue

        # Skip empty lines
        line = line.decode('utf-8')
        if not line.startswith('data: '):
            continue

        # Remove 'data: ' prefix
        data = line[6:]

        # Check for end of stream
        if data == '[DONE]':
            break

        try:
            chunk = json.loads(data)
            if 'choices' in chunk and len(chunk['choices']) > 0:
                delta = chunk['choices'][0].get('delta', {})
                if 'content' in delta:
                    full_content += delta['content']
                    print(".", end="", flush=True)
        except json.JSONDecodeError:
            continue

    print()  # New line after dots
    return full_content


def extract_code(response: str) -> str:
    """Extract code from markdown code blocks if present."""
    if "```" in response:
        # Extract code from markdown code blocks
        parts = response.split("```")
        for i, part in enumerate(parts):
            if i % 2 == 1:  # Odd indices are code blocks
                # Remove language identifier if present
                lines = part.strip().split('\n')
                if lines[0].strip() in ['python', 'py', 'python3']:
                    return '\n'.join(lines[1:])
                return part.strip()
    return response


def get_unique_filename(cans_dir: Path, date_str: str) -> tuple[str, Path]:
    """Generate a unique filename that doesn't overwrite existing files."""
    base_filename = f"can_{date_str}"
    counter = 0

    while True:
        if counter == 0:
            filename = f"{base_filename}.py"
        else:
            filename = f"{base_filename}_{counter}.py"

        filepath = cans_dir / filename

        if not filepath.exists():
            return filename, filepath

        counter += 1

        # Safety check: don't create too many files in one day
        if counter > 100:
            raise RuntimeError(f"Too many cans produced today ({counter}). Something might be wrong.")


def check_quality(code: str) -> tuple[bool, str]:
    """Check if the generated code is qualified."""
    try:
        # Check if it's not empty
        has_content = len(code.strip()) > 20

        # Try to compile it (syntax check)
        try:
            compile(code, '<string>', 'exec')
            syntax_ok = True
        except Exception as compile_error:
            syntax_ok = False

        # Check if it has some randomness or quote generation keywords
        code_lower = code.lower()
        has_keywords = any(word in code_lower for word in [
            'random', 'choice', 'print', 'quote', 'import'
        ])

        if has_content and syntax_ok and has_keywords:
            return True, "✅"
        else:
            reasons = []
            if not has_content: reasons.append("empty")
            if not syntax_ok: reasons.append("syntax error")
            if not has_keywords: reasons.append("missing keywords")
            return False, f"❌ ({', '.join(reasons)})"
    except Exception as e:
        return False, f"❌ (check failed: {e})"


def get_next_can_number() -> int:
    """Get the next can number by counting existing cans."""
    cans_dir = Path("cans")
    if not cans_dir.exists():
        return 1

    # Count all .py files in cans directory
    can_files = list(cans_dir.glob("can_*.py"))
    return len(can_files) + 1


def generate_soup_can(use_paid: bool = False):
    """Generate today's code soup can."""
    # Get today's date
    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    timestamp = today.strftime("%Y-%m-%d %H:%M:%S")

    print(f"🏭 Factory Machine starting...")
    print(f"📅 Date: {date_str}")

    # Get next can number
    can_number = get_next_can_number()
    print(f"🥫 Can #{can_number}")

    # Select a model (free or paid)
    model_type = "paid" if use_paid else "free"
    print(f"🔍 Searching for {model_type} models...")
    model = select_model(prefer_free=not use_paid)
    model_id = model["id"]
    model_name = model["name"]
    is_free = model.get("is_free", True)

    print(f"🤖 Selected model: {model_name} ({'free' if is_free else 'paid'})")
    print(f"🎨 Task: Generate meaningless philosophical quotes")

    # Call API
    response = call_openrouter(model_id, THE_TASK)

    # Extract code
    code = extract_code(response)

    # Check quality
    is_qualified, quality_mark = check_quality(code)
    print(f"🔍 Quality check: {quality_mark}")

    # If not qualified, raise an exception to trigger retry
    if not is_qualified:
        raise ValueError(f"Quality check failed: {quality_mark}")

    # Create cans directory if it doesn't exist
    cans_dir = Path("cans")
    cans_dir.mkdir(exist_ok=True)

    # Get unique filename to avoid overwriting
    filename, filepath = get_unique_filename(cans_dir, date_str)

    # Add header comment with metadata
    header = f'''"""
Campbell's Soup Can #{can_number}
Production Date: {timestamp}
Model: {model_name} ({model_id})
Model Type: {'Free' if is_free else 'Paid'}
Task: Generate meaningless philosophical quotes
Quality: {quality_mark}

Generated by The Factory Machine
Like Warhol's soup cans - same but different.
Each can is the same task, painted by a different AI artist.
"""

'''

    with open(filepath, 'w') as f:
        f.write(header + code)

    print(f"✅ Soup can produced: {filepath}")

    # Update production log in README
    update_production_log(timestamp, can_number, model_name, filename, quality_mark)

    return filepath


def update_production_log(timestamp: str, can_number: int, model_name: str, filename: str, quality: str):
    """Update production log in README.md."""
    readme_file = Path("README.md")

    try:
        # Read existing README
        if readme_file.exists():
            with open(readme_file, 'r') as f:
                content = f.read()
        else:
            print("⚠️  README.md not found")
            return

        # Check if production log section exists
        log_marker = "## Production Log"
        if log_marker not in content:
            # Add production log section at the end
            content += f"\n\n{log_marker}\n\n"
            content += "| Can # | Timestamp | Model | Quality | File |\n"
            content += "|-------|-----------|-------|---------|------|\n"

        # Add new entry
        entry = f"| {can_number} | {timestamp} | {model_name} | {quality} | [cans/{filename}](cans/{filename}) |\n"

        # Append to the end
        content += entry

        with open(readme_file, 'w') as f:
            f.write(content)

        print(f"📝 Production log updated in README.md")
    except Exception as e:
        print(f"⚠️  Failed to update production log: {e}")
        # Don't fail the whole process if log update fails


if __name__ == "__main__":
    if not OPENROUTER_API_KEY:
        print("❌ Error: OPENROUTER_API_KEY environment variable not set")
        exit(1)

    # Retry logic: first try free models, then paid models
    FREE_RETRIES = 3
    PAID_RETRIES = 3
    success = False

    # First, try with free models
    print("📍 Phase 1: Trying with free models...")
    for attempt in range(FREE_RETRIES):
        try:
            generate_soup_can(use_paid=False)
            print("🎨 The Factory continues...")
            success = True
            break  # Success, exit retry loop
        except KeyboardInterrupt:
            print("\n⏹️  Production interrupted by user")
            exit(0)
        except Exception as e:
            if attempt < FREE_RETRIES - 1:
                wait_time = (attempt + 1) * 2  # 2, 4, 6 seconds
                print(f"\n⚠️  Free model attempt {attempt + 1}/{FREE_RETRIES} failed: {e}")
                print(f"🔄 Retrying with another free model in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"\n⚠️  All free model attempts failed")

    # If free models failed, try with paid models
    if not success:
        print("\n📍 Phase 2: Trying with paid models...")
        for attempt in range(PAID_RETRIES):
            try:
                generate_soup_can(use_paid=True)
                print("🎨 The Factory continues (with paid model)...")
                success = True
                break
            except KeyboardInterrupt:
                print("\n⏹️  Production interrupted by user")
                exit(0)
            except Exception as e:
                if attempt < PAID_RETRIES - 1:
                    wait_time = (attempt + 1) * 3  # 3, 6, 9 seconds
                    print(f"\n⚠️  Paid model attempt {attempt + 1}/{PAID_RETRIES} failed: {e}")
                    print(f"🔄 Retrying with another paid model in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    print(f"\n❌ All attempts (free and paid) failed: {e}")
                    import traceback
                    traceback.print_exc()
                    exit(1)
