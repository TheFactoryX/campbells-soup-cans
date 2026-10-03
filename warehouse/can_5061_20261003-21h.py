"""
Campbell's Soup Can #5061
Produced: 2026-10-03 21:16:30
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen-inspired Philosophical Quote Display
A visually rich, animated presentation of a single existential musing.
"""

import os
import time

# ─── THE QUOTE ──────────────────────────────────────────────
QUOTE = (
    "I've spent forty years wondering if the universe "
    "is trying to communicate with us, or if we're merely "
    "the cosmic equivalent of someone who keeps asking "
    "'Why?' while the answer remains beautifully silent. "
    "Perhaps existence itself is the punchline we can't "
    "stop laughing at."
)

# ─── COLOR CODES (ANSI Escape Sequences) ───────────────────
BLUE   = "\033[94m"      # Deep blue — contemplative
YELLOW = "\033[93m"      # Bright yellow — anxious wonder
RED    = "\033[91m"      # Bold red — existential sting
CYAN   = "\033[96m"      # Cyan — intellectual sparkle
GREEN  = "\033[92m"      # Lime green — resolution
RESET  = "\033[0m"       # Reset to default

# ─── HELPER FUNCTIONS ────────────────────────────────────────

def clear_screen():
    """Clear the terminal screen in a cross‑platform way."""
    os.system('cls' if os.name == 'nt' else 'clear')

def blink(text, count=3):
    """Blink a character for a few seconds."""
    for _ in range(count):
        print(YELLOW + text + RESET)
        time.sleep(0.6)
        print(CYAN + text + RESET)
        time.sleep(0.6)

def animated_print(text, duration=2):
    """
    Print ``text`` after a short delay, then repeat it once more
    with a different color scheme for extra drama.
    """
    time.sleep(duration)
    print(QUOTE, end="\n")
    time.sleep(0.3)
    print(QUOTE, end="\n")
    time.sleep(0.3)
    # Recolor based on position
    if duration < 1.7:
        print(QUOTE, end="\n")
        time.sleep(0.3)
        print(QUOTE, end="\n")
    else:
        print(QUOTE, end="\n")
        time.sleep(0.3)
        print(QUOTE, end="\n")

def draw_decorative_frame(title, body):
    """
    Render a stylized pillar/box around the given strings.
    Uses Unicode box-drawing characters for a polished look.
    """
    # Top border
    top = "╔" + "═" * (len(title) + 4) + "╗"
    # Middle separator
    mid = "╠" + "─" * (max(len(body), 12) + 4) + "╣"
    # Bottom border
    bot = "╚" + "═" * (len(title) + 4) + "╝"
    
    # Center the body inside the box
    inner = "║" + " │ ".join(
        " " * min(i, max(len(body) - 4, 0)) 
        for i, ch in enumerate(body[:30])
    ) + " │"
    
    print(top)
    print(f"  {CYAN}{title}[{RESET}]")
    print(mid.replace("─", inner).replace("│", inner))
    print(bot)

# ─── MAIN ────────────────────────────────────────────────────

def main():
    clear_screen()
    
    print("\n" + "=" * 55)
    print("   A MOMENT OF WOODY ALLEN'S THOUGHTS")  
    print("=" * 55 + "\n")
    
    # First reveal — cool blue, contemplative
    print("\n" + "▓" * 40)
    print("  " + CYAN + "EXISTENCE WHISPERS..." + RESET)
    print("▓" * 40)
    animated_print(QUOTE, duration=1.8)
    
    # Second reveal — warm yellow, slightly more frantic
    print("\n" + "▓" * 40)
    print("  " + YELLOW + "AND NOW WE LAUGH AT THE SILENCE" + RESET)
    print("▓" * 40)
    animated_print(QUOTE, duration=1.8)
    
    # Closing flourish — lime green, resolved
    print("\n" + "=" * 55)
    print(GREEN + "THE END IS JUST A BEGINNING TO THINK ABOUT." + RESET)
    print("=" * 55 + "\n")

if __name__ == "__main__":
    main()