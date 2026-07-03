"""
Campbell's Soup Can #4077
Produced: 2026-07-03 07:36:45
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
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

# Original Woody Allen-style quote
QUOTE = (
    "I told my analyst I'm having an existential crisis. "
    "He said, 'That'll be $300.' I said, 'Can I pay in installments?' "
    "He said, 'Only if you believe in the concept of a future.'"
)

# Woody-ish ASCII portrait
WOODY = [
    "       ▄▄▄▄▄▄▄       ",
    "     ▄█████████▄     ",
    "    ███▀▀▀▀▀███      ",
    "    ██  ●   ●  ██    ",
    "    ██    ▼    ██    ",
    "    ██  \___/  ██    ",
    "     ▀█████████▀     ",
    "        ▀▀▀▀▀        ",
]

# Neurotic thought bubbles
THOUGHTS = [
    "  ( am I breathing correctly? )",
    "  ( did I lock the door? )",
    "  ( what if the universe is a typo? )",
    "  ( my left elbow feels asymmetrical )",
    "  ( is this quote too long? )",
    "  ( should I have ordered the soup? )",
]

def typewriter(text, color=C.WHITE, delay=0.015, jitter=0.01):
    """Type out text with a neurotic, slightly uneven rhythm."""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-jitter, jitter))
    print()

def clear_screen():
    print('\033[2J\033[H', end='')

def draw_box(lines, width=None, color=C.CYAN, padding=1):
    """Draw a pretty box around lines."""
    if width is None:
        width = max(len(line) for line in lines) + padding * 2
    top = f"{color}┌{'─' * (width - 2)}┐{C.RST}"
    bottom = f"{color}└{'─' * (width - 2)}┘{C.RST}"
    print(top)
    for line in lines:
        visible_len = len(line)
        # strip ANSI for length calculation
        import re
        clean = re.sub(r'\033\[[0-9;]*m', '', line)
        pad = width - 2 - len(clean)
        print(f"{color}│{C.RST} {line}{' ' * pad} {color}│{C.RST}")
    print(bottom)

def animate_woody():
    """Show Woody with animated thought bubbles."""
    frames = 3
    for frame in range(frames):
        clear_screen()
        # Title
        print(f"\n{C.BOLD}{C.MAGENTA}╔{'═' * 58}╗{C.RST}")
        print(f"{C.BOLD}{C.MAGENTA}║{C.RST} {C.YELLOW}★  WOODY ALLEN'S DAILY AFFIRMATION  ★{C.RST} {C.BOLD}{C.MAGENTA}║{C.RST}")
        print(f"{C.BOLD}{C.MAGENTA}╚{'═' * 58}╝{C.RST}\n")
        
        # Woody portrait
        for line in WOODY:
            print(f"{C.CYAN}{line}{C.RST}")
        
        # Animated thought bubble
        thought = THOUGHTS[frame % len(THOUGHTS)]
        print(f"\n{C.GRAY}{thought}{C.RST}")
        
        # Neurotic status bar
        anxiety = "█" * (frame + 1) + "░" * (3 - frame - 1)
        print(f"\n{C.RED}Anxiety Level: {C.BOLD}[{anxiety}]{C.RST} {C.DIM}(critical){C.RST}")
        
        time.sleep(0.6)

def main():
    # Hide cursor
    print('\033[?25l', end='')
    
    try:
        # Opening animation
        animate_woody()
        
        # Dramatic pause
        time.sleep(0.4)
        clear_screen()
        
        # The quote reveal with typewriter effect
        print(f"\n{C.BOLD}{C.BLUE}┌{'─' * 68}┐{C.RST}")
        print(f"{C.BOLD}{C.BLUE}│{C.RST} {C.ITALIC}{C.YELLOW}After seventeen minutes of pacing and three glasses of water...{C.RST} {C.BOLD}{C.BLUE}│{C.RST}")
        print(f"{C.BOLD}{C.BLUE}└{'─' * 68}┘{C.RST}\n")
        
        time.sleep(0.8)
        
        # Type the quote in chunks for dramatic effect
        sentences = QUOTE.split('. ')
        for i, sentence in enumerate(sentences):
            if i == len(sentences) - 1:
                sentence = sentence.rstrip('.') + '.'
            else:
                sentence = sentence + '.'
            
            # Color each sentence differently
            colors = [C.WHITE, C.CYAN, C.YELLOW, C.GREEN, C.MAGENTA]
            color = colors[i % len(colors)]
            
            # Indent
            sys.stdout.write("  ")
            typewriter(sentence, color=color, delay=0.012, jitter=0.008)
            
            # Neurotic pause between sentences
            if i < len(sentences) - 1:
                pause_chars = ["...", " *adjusts glasses* ", " *checks pulse* ", " *wonders if mailman judged him* "]
                pause = random.choice(pause_chars)
                sys.stdout.write(f"  {C.GRAY}{C.ITALIC}{pause}{C.RST}\n")
                sys.stdout.flush()
                time.sleep(random.uniform(0.4, 0.9))
        
        print()
        
        # Closing box with attribution
        print(f"\n{C.DIM}{'─' * 70}{C.RST}")
        attribution_lines = [
            f"{C.ITALIC}{C.GRAY}— As dictated to his analyst, Dr. Feldman, 1978 (session #342){C.RST}",
            f"{C.DIM}{C.GRAY}   Prescribed: Two Xanax and a screening of 'The Seventh Seal'{C.RST}",
        ]
        for line in attribution_lines:
            print(f"  {line}")
        print(f"{C.DIM}{'─' * 70}{C.RST}\n")
        
        # Final neurotic footer
        footers = [
            " *exits stage left, returns to check if he left the irony on* ",
            " *wonders if the audience is judging his font choice* ",
            " *realizes he forgot to breathe during the quote* ",
        ]
        print(f"{C.GRAY}{C.ITALIC}{random.choice(footers)}{C.RST}\n")
        
    finally:
        # Show cursor
        print('\033[?25h', end='')

if __name__ == "__main__":
    main()