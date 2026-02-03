"""
Campbell's Soup Can #2026
Produced: 2026-02-03 21:50:18
Worker: Google: Gemini 2.5 Flash Lite Preview 09-2025 (google/gemini-2.5-flash-lite-preview-09-2025)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# --- ANSI Color Codes ---
class Colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# --- The Quote ---
WOODY_QUOTE = "If you're still waiting for the universe to send you a definitive, satisfying answer... you probably deserve whatever agonizing self-doubt you're currently experiencing. And frankly, I need a bagel."

# --- Visual Elements ---

def create_box(text, width, border_char="█", color=Colors.CYAN):
    """Creates a framed, colored box around the text."""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines) if lines else 0
    
    padding = 4
    box_width = max_len + 2 * padding + 2 
    
    top_bottom = color + border_char * box_width + Colors.END
    
    output = [top_bottom]
    output.append(color + border_char + " " * (box_width - 2) + border_char + Colors.END)

    for line in lines:
        centered_line = line.center(max_len)
        line_content = f"{color}{border_char}{' ' * padding}{centered_line}{' ' * padding}{border_char}{Colors.END}"
        output.append(line_content)

    output.append(color + " " * (box_width - 2) + Colors.END)
    output.append(top_bottom)
    
    return "\n".join(output)

def animate_typing(text, color):
    """Simulates a neurotic, quick typing effect."""
    for char in text:
        print(color + char, end='', flush=True)
        if char in (',', '.', '!', '?'):
            time.sleep(0.15)  # Longer pause for punctuation
        else:
            time.sleep(random.uniform(0.01, 0.05))
    print(Colors.END)

def render_scene():
    """Puts all the visual elements together."""
    
    # Phase 1: Intro Jitters
    print(Colors.YELLOW + "="*60)
    animate_typing("Running existential dread diagnostic...", Colors.YELLOW)
    print("="*60 + Colors.END)
    time.sleep(0.5)
    
    # Phase 2: The Quote Framing (using the Neurotic Font of Truth)
    
    # Split the quote for better formatting within the box
    q_lines = [
        "If you're still waiting for the universe",
        "to send you a definitive, satisfying answer...",
        "",
        "You probably deserve whatever agonizing self-doubt",
        "you're currently experiencing.",
        "",
        "And frankly, I need a bagel."
    ]
    
    formatted_quote = "\n".join(q_lines)
    
    # Create the visual container, using a softer character for thought
    visual_output = create_box(
        formatted_quote, 
        width=60, 
        border_char="▒", 
        color=Colors.PURPLE
    )
    
    print("\n" * 2)
    print(visual_output)
    print("\n" * 2)
    
    # Phase 3: Signature Animation
    print(Colors.CYAN + "--- Analysis Complete ---" + Colors.END)
    time.sleep(0.5)
    
    signature = "W. A. (Currently in Therapy)"
    print(Colors.BOLD + Colors.RED)
    for i in range(len(signature)):
        print(f"\r{signature[:i+1]}", end='', flush=True)
        time.sleep(0.08)
    print(Colors.END)


if __name__ == "__main__":
    # Clears screen for maximum effect (best effort)
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    render_scene()