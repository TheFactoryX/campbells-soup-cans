"""
Campbell's Soup Can #1062
Produced: 2025-12-20 15:31:02
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import time
import sys
import random

# ----------------------------
# ANSI Color & Style Helpers
# ----------------------------
class ANSI:
    """A tiny helper for ANSI escape sequences."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    
    # Foreground colors
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    ORANGE = "\033[38;5;208m"  # Approximation using 256-color palette
    GRAY = "\033[38;5;240m"

def colorize(text, *styles):
    """Wrap text with given ANSI style codes."""
    return f"{''.join(styles)}{text}{ANSI.RESET}"

# ----------------------------
# The Quote
# ----------------------------
QUOTE = """I'm not afraid of death; I just want my
subconscious to schedule it during a good dream."""

# ----------------------------
# ASCII Art Brain (with a tiny thought bubble)
# ----------------------------
BRAIN_ART = r"""
      ______________
     /  _   _   _   \
    |  (.)-(.) (.)-(.)|
    |    \_// \_//    |
     \______________/
          |    |
       ___|____|___
      (____________)
"""

# ----------------------------
# Animation Logic
# ----------------------------
def typewriter(text, speed=0.04, color=ANSI.GRAY):
    """Prints text character by character for a dramatic effect."""
    for char in text:
        sys.stdout.write(color + char + ANSI.RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # newline

def draw_curtains(lines=8, delay=0.03):
    """Draws a dramatic curtain opening."""
    width = 60
    left_char = "/"
    right_char = "\\"
    gap = 0
    for i in range(lines):
        # Calculate spaces for the gap in the middle
        gap = i * 4
        left = left_char * (width - gap) // 2
        right = right_char * (width - gap) // 2
        spacer = " " * gap
        
        # Print the line with color
        line = f"{ANSI.RED}{ANSI.BOLD}{left}{spacer}{right}{ANSI.RESET}"
        sys.stdout.write("\r" + line)
        sys.stdout.flush()
        time.sleep(delay)
        # Move to next line
        print()
    
    # Final opening
    time.sleep(0.2)
    print("\n" * 1)

def display_quote():
    """Orchestrates the visual display of the Woody Allen-style quote."""
    
    # 1. The Dramatic Entrance (Theatrical Curtains)
    typewriter(f"{ANSI.GRAY}... The stage is set ...{ANSI.RESET}", speed=0.03)
    draw_curtains()

    # 2. The Brain (The Source of Angst)
    brain_lines = BRAIN_ART.strip('\n').split('\n')
    for line in brain_lines:
        # Print brain in a flickering cyan/orange
        color = random.choice([ANSI.CYAN, ANSI.ORANGE])
        print(colorize(line, color, ANSI.BOLD))
        time.sleep(0.05)
    
    # 3. The Thought Bubble (Animation)
    print("\n")
    bubble_prefix = " " * 12
    bubble_text = " W O R R Y   A B O U T   D E A T H ? "
    
    # Typewriter the bubble contents
    print(bubble_prefix + colorize("o", ANSI.YELLOW))
    sys.stdout.write(bubble_prefix)
    sys.stdout.flush()
    
    # Animate the text filling the bubble
    for char in bubble_text:
        sys.stdout.write(colorize(char, ANSI.YELLOW, ANSI.BOLD))
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    
    # 4. The Quote (The Punchline) - Scrolling up from the bottom
    print("\n" + " " * 5 + ANSI.WHITE + "-"*40 + ANSI.RESET)
    
    # Break quote into lines for typewriter effect
    lines = QUOTE.split('\n')
    for line in lines:
        # Indent slightly
        sys.stdout.write(" " * 5)
        sys.stdout.flush()
        typewriter(line, speed=0.06, color=ANSI.WHITE)
        time.sleep(0.3)

    # 5. The Existential Sigh (Footer)
    time.sleep(0.5)
    sys.stdout.write(" " * 5 + colorize("... sigh ...", ANSI.GRAY, ANSI.ITALIC))
    sys.stdout.flush()
    time.sleep(1.0)
    
    # 6. The Apology (The Exit)
    print("\n\n")
    apology = " (Sorry, I couldn't decide if I wanted to be alive or just entertaining.) "
    print(ANSI.GRAY + "─" * len(apology) + ANSI.RESET)
    print(ANSI.GRAY + apology + ANSI.RESET)
    print(ANSI.GRAY + "─" * len(apology) + ANSI.RESET)

# ----------------------------
# Main Execution
# ----------------------------
if __name__ == "__main__":
    try:
        display_quote()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n" + colorize("Exiting prematurely? Even my exits are anxious.", ANSI.RED))
    except Exception as e:
        # Fallback for any unexpected existential errors
        print(f"\n{ANSI.RED}System Error: {e}. This was inevitable.{ANSI.RESET}")