"""
Campbell's Soup Can #5126
Produced: 2026-10-18 05:54:49
Worker: Free Models Router (openrouter/free)
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
    R = '\033[91m'      # Red
    G = '\033[92m'      # Green
    Y = '\033[93m'      # Yellow
    B = '\033[94m'      # Blue
    M = '\033[95m'      # Magenta
    C = '\033[96m'      # Cyan
    W = '\033[97m'      # White
    D = '\033[90m'      # Dim
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'
    CLEAR = '\033[2J\033[H'

# Woody Allen original quote
QUOTE = (
    "I took a speed-reading course and read 'War and Peace' in twenty minutes.\n"
    "It involves Russia. And peace. Mostly peace. Which is suspicious."
)
AUTHOR = "— Woody Allen (probably, or just my therapist billing me)"

# Decorative frames
TOP_LEFT = "╭"
TOP_RIGHT = "╮"
BOT_LEFT = "╰"
BOT_RIGHT = "╯"
HORIZ = "─"
VERT = "│"

def typewriter(text, color=C.W, delay=0.02, newline=True):
    """Print with typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def fade_in(text, color=C.W, steps=10):
    """Fade in text by gradually increasing brightness."""
    for i in range(steps + 1):
        sys.stdout.write(f"\r{color}{text}{C.RESET}")
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def draw_box(content_lines, width=None, color=C.C, title=None):
    """Draw a pretty box around content."""
    if width is None:
        width = max(len(line) for line in content_lines) + 4
    
    # Top border
    if title:
        title_str = f" {title} "
        left_pad = (width - len(title_str)) // 2
        right_pad = width - len(title_str) - left_pad
        print(f"{color}{TOP_LEFT}{HORIZ * left_pad}{title_str}{HORIZ * right_pad}{TOP_RIGHT}{C.RESET}")
    else:
        print(f"{color}{TOP_LEFT}{HORIZ * width}{TOP_RIGHT}{C.RESET}")
    
    # Content
    for line in content_lines:
        padding = width - len(line)
        print(f"{color}{VERT}{C.RESET} {line}{' ' * padding} {color}{VERT}{C.RESET}")
    
    # Bottom border
    print(f"{color}{BOT_LEFT}{HORIZ * width}{BOT_RIGHT}{C.RESET}")

def neurotic_loader():
    """Show a neurotic loading animation."""
    thoughts = [
        "Overthinking...",
        "Second-guessing the quote...",
        "Wondering if I left the stove on...",
        "Calculating mortality statistics...",
        "Replaying awkward conversation from 2003...",
        "Questioning the nature of reality...",
        "Checking if my therapist accepts insurance...",
    ]
    
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    
    for _ in range(30):
        frame = random.choice(frames)
        thought = random.choice(thoughts)
        sys.stdout.write(f"\r{C.D}{frame} {thought}{C.RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\r" + " " * 60 + "\r", end="")

def main():
    # Clear screen
    print(C.CLEAR, end="")
    
    # Title animation
    print(f"{C.M}{C.BOLD}")
    print("    ██╗    ██╗ █████╗ ██████╗ ███████╗███████╗██████╗ ")
    print("    ██║    ██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗")
    print("    ██║ █╗ ██║███████║██████╔╝█████╗  █████╗  ██████╔╝")
    print("    ██║███╗██║██╔══██║██╔══██╗██╔══╝  ██╔══╝  ██╔══██╗")
    print("    ╚███╔███╔╝██║  ██║██║  ██║███████╗███████╗██║  ██║")
    print("     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝")
    print(f"{C.RESET}")
    
    print(f"{C.D}    A neurotic dose of existential humor{C.RESET}\n")
    
    # Neurotic loader
    neurotic_loader()
    
    # Split quote into lines
    quote_lines = QUOTE.split('\n')
    
    # Draw the quote box
    print()
    draw_box(quote_lines, color=C.Y, title=f"{C.BOLD}WOODY ALLEN WISDOM{C.RESET}{C.Y}")
    print()
    
    # Print author with typewriter effect
    typewriter(f"{C.D}{C.ITALIC}{AUTHOR}{C.RESET}", color=C.M, delay=0.03)
    print()
    
    # Little footer animation
    footers = [
        "Existence verified. Anxiety levels: optimal.",
        "Quote certified by the International Board of Neurosis.",
        "Side effects may include: overthinking, insomnia, sudden urge to move to Manhattan.",
        "No neuroses were harmed in the making of this quote.",
    ]
    
    time.sleep(0.5)
    for footer in footers:
        sys.stdout.write(f"\r{C.D}{footer}{C.RESET}")
        sys.stdout.flush()
        time.sleep(1.2)
    
    print("\n")
    
    # Final sign-off
    signoff = [
        "┌─────────────────────────────────────────────┐",
        "│  Remember: You're not paranoid if they      │",
        "│  really ARE out to get you. But they're     │",
        "│  probably just indifferent. Which is worse. │",
        "└─────────────────────────────────────────────┘",
    ]
    for line in signoff:
        print(f"{C.D}{line}{C.RESET}")
    
    print(f"\n{C.D}Press Ctrl+C to exit (or just sit with the dread)...{C.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.R}Interrupted. Typical.{C.RESET}")
        sys.exit(0)