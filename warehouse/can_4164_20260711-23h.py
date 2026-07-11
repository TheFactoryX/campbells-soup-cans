"""
Campbell's Soup Can #4164
Produced: 2026-07-11 23:10:51
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI color codes
class C:
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    BG_BLACK = '\033[40m'
    BG_WHITE = '\033[47m'

# Woody Allen ASCII portrait
WOODY = f"""
{C.CYAN}        ╭─────────────╮{C.RST}
{C.CYAN}        │  {C.YELLOW}┌───┐ {C.CYAN}   │{C.RST}
{C.CYAN}        │  {C.YELLOW}│ ● │ {C.CYAN}   │{C.RST}
{C.CYAN}        │  {C.YELLOW}└─┬─┘ {C.CYAN}   │{C.RST}
{C.CYAN}        │  {C.YELLOW}──┼── {C.CYAN}   │{C.RST}
{C.CYAN}        │  {C.YELLOW}  │  {C.CYAN}    │{C.RST}
{C.CYAN}        │ {C.YELLOW}╱{C.GRAY}──┼──{C.YELLOW}╲{C.CYAN}  │{C.RST}
{C.CYAN}        ╰─────────────╯{C.RST}
{C.GRAY}      "Neurosis is just{C.RST}
{C.GRAY}       curiosity with{C.RST}
{C.GRAY}       better funding"{C.RST}
"""

QUOTE = (
    "I don't believe in an afterlife, "
    "but I'm bringing a change of underwear "
    "just in case... and a snack. "
    "You never know how long the line is."
)

QUOTE_LINES = [
    "I don't believe in an afterlife,",
    "but I'm bringing a change of underwear",
    "just in case... and a snack.",
    "You never know how long the line is."
]

def typewriter(text, color=C.WHITE, delay=0.03, newline=True):
    """Print text with typing animation."""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    if newline:
        print()

def print_centered(text, width=60, color=C.WHITE):
    """Print text centered in a given width."""
    padding = (width - len(text)) // 2
    print(' ' * padding + f"{color}{text}{C.RST}")

def rainbow_text(text):
    """Return text with rainbow gradient."""
    colors = [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA]
    result = ""
    for i, char in enumerate(text):
        if char != ' ':
            result += colors[i % len(colors)] + char
        else:
            result += char
    return result + C.RST

def pulse_border(width=60, cycles=2):
    """Animate a pulsing border."""
    chars = ['░', '▒', '▓', '█', '▓', '▒']
    for _ in range(cycles):
        for char in chars:
            line = char * width
            sys.stdout.write(f"\r{C.MAGENTA}{line}{C.RST}")
            sys.stdout.flush()
            time.sleep(0.08)
    print()

def clear_screen():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def main():
    # Clear screen and hide cursor
    clear_screen()
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()
    
    try:
        # Top border pulse
        pulse_border(60, 1)
        
        # Print Woody portrait
        print(WOODY)
        time.sleep(0.5)
        
        # Decorative separator
        print(f"{C.GRAY}{'─' * 60}{C.RST}")
        time.sleep(0.3)
        
        # Title with rainbow effect
        title = " A WOODY ALLEN MOMENT "
        print_centered(f"{C.BOLD}{C.YELLOW}{'▓' * 2}{C.RST} {rainbow_text(title)} {C.BOLD}{C.YELLOW}{'▓' * 2}{C.RST}", 60)
        print(f"{C.GRAY}{'─' * 60}{C.RST}")
        print()
        
        # Type out each line of the quote with different colors
        colors = [C.CYAN, C.GREEN, C.YELLOW, C.MAGENTA]
        delays = [0.04, 0.035, 0.03, 0.025]
        
        for i, (line, color, delay) in enumerate(zip(QUOTE_LINES, colors, delays)):
            # Add bullet/number
            prefix = f"{C.DIM}{C.GRAY}► {C.RST}"
            sys.stdout.write(prefix)
            sys.stdout.flush()
            typewriter(line, color=color, delay=delay, newline=True)
            time.sleep(0.4)
        
        print()
        
        # Bottom philosophical musing
        musings = [
            "(My therapist says this is 'avoidance behavior.'",
            " I told him the universe is also avoiding me.)",
        ]
        for m in musings:
            typewriter(m, color=C.GRAY, delay=0.02, newline=True)
            time.sleep(0.2)
        
        print()
        print(f"{C.GRAY}{'─' * 60}{C.RST}")
        
        # Final sign-off with animation
        signoff = " — Woody (probably) "
        for _ in range(3):
            print_centered(f"{C.BOLD}{C.YELLOW}{signoff}{C.RST}", 60)
            time.sleep(0.3)
            print_centered(f"{C.DIM}{signoff}{C.RST}", 60)
            time.sleep(0.2)
        print_centered(f"{C.BOLD}{C.YELLOW}{signoff}{C.RST}", 60)
        
        print()
        pulse_border(60, 1)
        
        # Easter egg: random neurotic thought
        neurotic_thoughts = [
            "Also, did I lock the door? The stove? My existential dread?",
            "Wait, if I'm not there, who's watching me not be there?",
            "Should I have brought a sweater? The afterlife might be drafty.",
            "Is 'just in case' a valid theological position?",
            "My mother would say: 'You're bringing underwear to eternity?'"
        ]
        time.sleep(0.5)
        print()
        typewriter(f"{C.DIM}{C.CYAN}💭 {random.choice(neurotic_thoughts)}{C.RST}", color=C.CYAN, delay=0.02)
        print()
        
    finally:
        # Show cursor again
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()

if __name__ == "__main__":
    main()