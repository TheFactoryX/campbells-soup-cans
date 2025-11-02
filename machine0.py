#!/usr/bin/env python3
"""
Machine #0 - Production Line 0
Making soup cans with Flavor #0: Woody Allen Philosophy
"""

import os
import json
import random
import time
from datetime import datetime
from pathlib import Path
from typing import Optional
import requests

# Factory credentials
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODELS_URL = "https://openrouter.ai/api/v1/models"

# Flavor #0: Woody Allen Philosophy
# The recipe for today's soup flavor
FLAVOR_0_RECIPE = """
Write a Python program that prints ONE funny philosophical quote in Woody Allen's style.

Requirements:
- Must be a SINGLE Python file that can run directly
- Must be valid Python code (no syntax errors)
- Print ONE philosophical quote that sounds like Woody Allen (neurotic, funny, self-deprecating, existential)
- Make it VISUALLY INTERESTING: use colors, ASCII art, animations, or creative formatting
- Use ANSI escape codes for colors, or creative text layouts
- Keep it pure Python, no external dependencies

Example Woody Allen style quotes (create your own!):
"I'm not afraid of death; I just don't want to be there when it happens."
"Life is full of misery, loneliness, and suffering - and it's all over much too soon."
"I don't want to achieve immortality through my work; I want to achieve it through not dying."

Make it visually fun! Use colors, boxes, animations, whatever you want. Be creative!
"""


def get_workers(free_only: bool = True) -> list:
    """Find available workers in the factory."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    }

    response = requests.get(MODELS_URL, headers=headers, timeout=30)
    response.raise_for_status()

    models_data = response.json()

    workers = []
    for model in models_data.get("data", []):
        pricing = model.get("pricing", {})
        prompt_price = float(pricing.get("prompt", "1"))
        completion_price = float(pricing.get("completion", "1"))

        is_free = prompt_price == 0 and completion_price == 0

        if free_only and not is_free:
            continue
        if not free_only and is_free:
            continue

        workers.append({
            "id": model["id"],
            "name": model.get("name", model["id"]),
            "context_length": model.get("context_length", 0),
            "is_free": is_free
        })

    return workers


def select_worker(prefer_free: bool = True) -> dict:
    """Pick a random worker for today's shift."""
    workers = get_workers(free_only=prefer_free)

    if not workers:
        print(f"⚠️  No {'volunteer' if prefer_free else 'paid'} workers found, using backup")
        return {"id": "meta-llama/llama-3.2-3b-instruct:free", "name": "Backup Worker", "is_free": True}

    selected = random.choice(workers)
    return selected


def ask_worker_to_work(worker_id: str, recipe: str) -> str:
    """Give the recipe to a worker and collect their creation."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": worker_id,
        "messages": [
            {
                "role": "system",
                "content": "You are a creative Python code artist. Generate ONLY Python code, nothing else. The code must be a SINGLE Python file that can run directly. Write valid, executable Python code. Be creative and playful!"
            },
            {
                "role": "user",
                "content": recipe
            }
        ],
        "stream": True,
    }

    response = requests.post(API_URL, headers=headers, json=payload, stream=True, timeout=120)
    response.raise_for_status()

    result = ""
    print("🔄 Worker is creating", end="", flush=True)

    for line in response.iter_lines():
        if not line:
            continue

        line = line.decode('utf-8')
        if not line.startswith('data: '):
            continue

        data = line[6:]

        if data == '[DONE]':
            break

        try:
            chunk = json.loads(data)
            if 'choices' in chunk and len(chunk['choices']) > 0:
                delta = chunk['choices'][0].get('delta', {})
                if 'content' in delta:
                    result += delta['content']
                    print(".", end="", flush=True)
        except json.JSONDecodeError:
            continue

    print()
    return result


def extract_creation(response: str) -> str:
    """Extract the pure creation from the wrapper."""
    if "```" in response:
        parts = response.split("```")
        for i, part in enumerate(parts):
            if i % 2 == 1:
                lines = part.strip().split('\n')
                if lines[0].strip() in ['python', 'py', 'python3']:
                    return '\n'.join(lines[1:])
                return part.strip()
    return response


def get_unique_label(warehouse_dir: Path, can_number: int, timestamp_str: str) -> tuple[str, Path]:
    """Generate a unique label for the can."""
    # Format: can_0001_20251102-15h.py
    # Includes can number and timestamp with hour
    base_label = f"can_{can_number:04d}_{timestamp_str}"

    label = f"{base_label}.py"
    filepath = warehouse_dir / label

    # If somehow exists, add suffix
    counter = 1
    while filepath.exists():
        label = f"{base_label}_{counter}.py"
        filepath = warehouse_dir / label
        counter += 1
        if counter > 10:
            raise RuntimeError(f"Label collision for can #{can_number}!")

    return label, filepath


def inspect_quality(creation: str) -> tuple[bool, str]:
    """Quality inspector checks the creation."""
    try:
        has_content = len(creation.strip()) > 20

        try:
            compile(creation, '<string>', 'exec')
            syntax_ok = True
        except Exception:
            syntax_ok = False

        creation_lower = creation.lower()
        # Check for print statement
        has_print = 'print' in creation_lower

        if has_content and syntax_ok and has_print:
            return True, "✅"
        else:
            reasons = []
            if not has_content: reasons.append("empty")
            if not syntax_ok: reasons.append("broken")
            if not has_print: reasons.append("missing print")
            return False, f"❌ ({', '.join(reasons)})"
    except Exception as e:
        return False, f"❌ (inspection failed: {e})"


def get_next_can_number() -> int:
    """Count cans in warehouse."""
    warehouse_dir = Path("warehouse")
    if not warehouse_dir.exists():
        return 0

    cans = list(warehouse_dir.glob("can_*.py"))
    return len(cans)


def produce_can(hire_paid_workers: bool = False):
    """Run the production line."""
    today = datetime.now()
    timestamp = today.strftime("%Y-%m-%d %H:%M:%S")
    # Format for filename: 20251102-15h (compact timestamp with hour)
    timestamp_compact = today.strftime("%Y%m%d-%Hh")

    print(f"🏭 Machine #0 starting up...")
    print(f"📅 Timestamp: {timestamp}")

    can_number = get_next_can_number()
    print(f"🥫 Can #{can_number}")

    worker_type = "paid workers" if hire_paid_workers else "volunteers"
    print(f"🔍 Looking for {worker_type}...")
    worker = select_worker(prefer_free=not hire_paid_workers)
    worker_id = worker["id"]
    worker_name = worker["name"]
    is_volunteer = worker.get("is_free", True)

    print(f"👷 Today's worker: {worker_name} ({'volunteer' if is_volunteer else 'paid'})")
    print(f"🎨 Flavor: Woody Allen Philosophy")

    creation = ask_worker_to_work(worker_id, FLAVOR_0_RECIPE)

    final_product = extract_creation(creation)

    passed, quality_stamp = inspect_quality(final_product)
    print(f"🔍 Inspector's verdict: {quality_stamp}")

    # Store in warehouse regardless of quality
    # Even defective cans are art!
    warehouse_dir = Path("warehouse")
    warehouse_dir.mkdir(exist_ok=True)

    label, can_path = get_unique_label(warehouse_dir, can_number, timestamp_compact)

    can_label = f'''"""
Campbell's Soup Can #{can_number}
Produced: {timestamp}
Worker: {worker_name} ({worker_id})
Employment: {'Volunteer' if is_volunteer else 'Paid'}
Flavor: Woody Allen Philosophy
Quality: {quality_stamp}

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

'''

    with open(can_path, 'w') as f:
        f.write(can_label + final_product)

    print(f"✅ Can produced and stored: {can_path}")

    log_production(timestamp, can_number, worker_name, label, quality_stamp)

    return can_path


def log_production(timestamp: str, can_number: int, worker_name: str, label: str, quality: str):
    """Write to the production log."""
    readme_file = Path("README.md")

    try:
        if readme_file.exists():
            with open(readme_file, 'r') as f:
                content = f.read()
        else:
            print("⚠️  Log book not found")
            return

        log_marker = "## 📊 Production Log"
        if log_marker not in content:
            content += f"\n\n{log_marker}\n\n"
            content += "| Can # | Timestamp | Worker | Quality | Location |\n"
            content += "|-------|-----------|--------|---------|----------|\n"

        entry = f"| {can_number} | {timestamp} | {worker_name} | {quality} | [warehouse/{label}](warehouse/{label}) |\n"

        content += entry

        with open(readme_file, 'w') as f:
            f.write(content)

        print(f"📝 Production logged")
    except Exception as e:
        print(f"⚠️  Failed to write log: {e}")


if __name__ == "__main__":
    if not OPENROUTER_API_KEY:
        print("❌ Error: Factory credentials not found")
        print("   Set OPENROUTER_API_KEY environment variable")
        exit(1)

    # Two-phase production strategy
    VOLUNTEER_ATTEMPTS = 3
    PAID_ATTEMPTS = 3
    success = False

    # Phase 1: Try volunteers first
    print("📍 Phase 1: Calling in volunteers...")
    for attempt in range(VOLUNTEER_ATTEMPTS):
        try:
            produce_can(hire_paid_workers=False)
            print("🎨 Production line continues...")
            success = True
            break
        except KeyboardInterrupt:
            print("\n⏹️  Emergency stop activated")
            exit(0)
        except Exception as e:
            if attempt < VOLUNTEER_ATTEMPTS - 1:
                wait_time = (attempt + 1) * 2
                print(f"\n⚠️  Volunteer attempt {attempt + 1}/{VOLUNTEER_ATTEMPTS} failed: {e}")
                print(f"🔄 Trying another volunteer in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"\n⚠️  All volunteers tried")

    # Phase 2: Hire paid workers if needed
    if not success:
        print("\n📍 Phase 2: Hiring paid workers...")
        for attempt in range(PAID_ATTEMPTS):
            try:
                produce_can(hire_paid_workers=True)
                print("🎨 Production line continues (with paid help)...")
                success = True
                break
            except KeyboardInterrupt:
                print("\n⏹️  Emergency stop activated")
                exit(0)
            except Exception as e:
                if attempt < PAID_ATTEMPTS - 1:
                    wait_time = (attempt + 1) * 3
                    print(f"\n⚠️  Paid worker attempt {attempt + 1}/{PAID_ATTEMPTS} failed: {e}")
                    print(f"🔄 Trying another worker in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    print(f"\n❌ Production failed: {e}")
                    import traceback
                    traceback.print_exc()
                    exit(1)
