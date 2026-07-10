"""
Campbell's Soup Can #4145
Produced: 2026-07-10 15:01:01
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A Woody Allen-style philosophical quote generator with neurotic flair.
Because if you're going to have an existential crisis, it might as well be pretty.
"""

import sys
import time
import random

# ANSI Color Codes - because life is meaningless but at least it can be colorful
class C:
    R = '\033[91m'      # Red - for anxiety
    G = '\033[92m'      # Green - for fleeting hope
    Y = '\033[93m'      # Yellow - for nervous energy
    B = '\033[94m'      # Blue - for melancholy
    M = '\033[95m'      # Magenta - for existential dread
    C = '\033[96m'      # Cyan - for cold comfort
    W = '\033[97m'      # White - for the void
    D = '\033[2m'       # Dim - for mumbling
    BD = '\033[1m'      # Bold - for emphasis
    UL = '\033[4m'      # Underline - for things that matter (nothing)
    BLINK = '\033[5m'   # Blink - for panic attacks
    RESET = '\033[0m'   # Reset - like therapy, but faster
    CLEAR = '\033[2J\033[H'  # Clear screen - fresh start, same problems

# Woody's neurotic masterpiece - original, hand-crafted anxiety
WOODY_QUOTE = (
    "I took a speed-reading course and read 'War and Peace' in twenty minutes.\n"
    "It involves Russia. And suffering. Mostly suffering.\n\n"
    "My analyst says I have a preoccupation with death.\n"
    "I told him, 'Doc, at my age, it's not a preoccupation — it's a scheduling conflict.'\n\n"
    "The universe is indifferent. My landlord is hostile.\n"
    "My cholesterol is winning. And somewhere, a teenager is\n"
    "explaining to me why my favorite movie is 'problematic.'\n\n"
    "I'd like to achieve immortality through not dying.\n"
    "Failing that, through not answering the phone.\n\n"
    "     — Not Woody Allen, but the voice in his head at 3 AM"
)

# ASCII Art: A neurotic little face contemplating the void
NEUROTIC_FACE = r"""
        ╭─────────────────────╮
        │  ░░░░░░░░░░░░░░░░░  │
        │  ░  (•_•)   (?)   ░  │  <-- That's you. That's all of us.
        │  ░  / >☝    ☝\   ░  │
        │  ░                ░  │
        │  ░  "Why?"        ░  │
        │  ░                ░  │
        ╰─────────────────────╯
"""

# A tiny spinning anxiety indicator
SPINNERS = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']

def typewriter(text, color=C.W, delay=0.015, variance=0.01):
    """Print text with a typewriter effect - because thoughts arrive hesitantly."""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-variance, variance))
    print()

def slow_print_lines(lines, base_color=C.W, delay=0.03):
    """Print lines with a thoughtful pause between them."""
    for i, line in enumerate(lines):
        # Alternate colors slightly for that "racing thoughts" feel
        colors = [C.Y, C.C, C.M, C.B, C.G, C.W]
        color = colors[i % len(colors)] if line.strip() else C.D
        typewriter(line, color=color, delay=delay)
        if line.strip():
            time.sleep(0.15)  # Pause for effect. For dread. For comedic timing.

def animate_thinking(duration=2.0):
    """Show a little thinking animation while the existential dread loads."""
    start = time.time()
    msg = "Contemplating the abyss"
    while time.time() - start < duration:
        for spinner in SPINNERS:
            sys.stdout.write(f"\r{C.M}{spinner} {msg}{C.RESET}")
            sys.stdout.flush()
            time.sleep(0.08)
    sys.stdout.write(f"\r{' ' * (len(msg) + 4)}\r")
    sys.stdout.flush()

def draw_box(title, content, color=C.C):
    """Draw a pretty box around content. Like a frame for your neuroses."""
    lines = content.split('\n')
    max_len = max(len(line) for line in lines)
    width = max(max_len, len(title)) + 4
    
    top = f"{color}╭{'─' * (width - 2)}╮{C.RESET}"
    title_line = f"{color}│{C.RESET} {C.BD}{title.center(width - 4)}{C.RESET} {color}│{C.RESET}"
    sep = f"{color}├{'─' * (width - 2)}┤{C.RESET}"
    bottom = f"{color}╰{'─' * (width - 2)}╯{C.RESET}"
    
    print(top)
    print(title_line)
    print(sep)
    for line in lines:
        padding = width - 4 - len(line)
        print(f"{color}│{C.RESET} {line}{' ' * padding} {color}│{C.RESET}")
    print(bottom)

def main():
    # Clear screen for dramatic entrance
    print(C.CLEAR, end='')
    
    # Title banner
    print(f"\n{C.M}{C.BD}{'=' * 60}{C.RESET}")
    print(f"{C.Y}{C.BD}  WOODY ALLEN-STYLE EXISTENTIAL MONOLOGUE GENERATOR v1.0{C.RESET}")
    print(f"{C.D}  (Now with 40% more neurosis and zero therapeutic value){C.RESET}")
    print(f"{C.M}{C.BD}{'=' * 60}{C.RESET}\n")
    
    # Show the neurotic face
    print(f"{C.C}{NEUROTIC_FACE}{C.RESET}")
    
    # Thinking animation
    animate_thinking(1.5)
    
    print(f"\n{C.D}Loading neuroses... {C.G}✓{C.RESET}")
    print(f"{C.D}Calibrating self-deprecation... {C.G}✓{C.RESET}")
    print(f"{C.D}Checking if the stove is off... {C.Y}???{C.RESET}")
    print(f"{C.D}Wondering if that email sounded weird... {C.R}✓{C.RESET}\n")
    
    time.sleep(0.5)
    
    # The main event - typewritten quote in a fancy box
    print(f"{C.BD}And now, a thought:{C.RESET}\n")
    
    # Split quote into paragraphs for the box
    quote_lines = WOODY_QUOTE.split('\n')
    
    # Print with typewriter effect
    slow_print_lines(quote_lines, delay=0.01)
    
    print()
    
    # A final philosophical nugget in a box
    final_thoughts = [
        "The only thing worse than existence",
        "is existence with a stomachache",
        "during a blackout",
        "while your ex texts 'u up?'"
    ]
    draw_box("CLOSING THOUGHT", "\n".join(final_thoughts), C.M)
    
    print(f"\n{C.D}Remember: You're not paranoid if the universe really is")
    print(f"out to get you. It is. It absolutely is.{C.RESET}\n")
    
    # Credits
    print(f"{C.D}{'─' * 50}{C.RESET}")
    print(f"{C.D}No therapists were harmed in the making of this program.{C.RESET}")
    print(f"{C.D}Your anxiety may vary. Void where prohibited by sanity.{C.RESET}")
    print(f"{C.D}{'─' * 50}{C.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.R}Interrupted. Just like my train of thought.{C.RESET}")
        print(f"{C.D}Story of my life...{C.RESET}\n")
        sys.exit(130)
    except Exception as e:
        print(f"\n{C.R}Error: {e}{C.RESET}")
        print(f"{C.D}See? Even the code has existential crises.{C.RESET}\n")
        sys.exit(1)