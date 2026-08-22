"""
Campbell's Soup Can #4774
Produced: 2026-08-22 20:39:59
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
 Woody Allen's Existential Comedy Hour
 A neurotic little program that ponders the absurdity of existence
 and makes a joke about it before hiding under the blanket.

 "The worst thing about getting old is... well, I'm not even
  getting old, I'm just getting NOT-YOUNG, which is different,
  like how 'pre-owned' is different from 'used', though ultimately
  we're all just pre-dead, aren't we?"
"""

import sys
import time
import shutil

# ANSI color codes
class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"


def typewriter(text, delay=0.04, color=None, end="\n"):
    """Print text with a delightful typewriter effect, like a nervous writer
    hitting the same keys over and over, unsure if he's typing or just
    pretending to type."""
    for char in text:
        if color:
            sys.stdout.write(f"{color}{char}{Colors.RESET}")
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()


def slow_dots(duration=1.5, color=Colors.DIM):
    """Those anxious dots... the pause where nothing happens...
    existential dread setting in..."""
    start = time.time()
    dots = 0
    while time.time() - start < duration:
        sys.stdout.write(f"{color}.{Colors.RESET}")
        sys.stdout.flush()
        dots += 1
        time.sleep(0.25)
    print()


def draw_box(width, height, title=None):
    """Draw a shaky philosophical box around the proceedings,
    because even our decorations question their purpose."""
    top = f"{Colors.MAGENTA}╔{'═' * width}╗{Colors.RESET}"
    bottom = f"{Colors.MAGENTA}╚{'═' * width}╝{Colors.RESET}"
    
    if title:
        side = f"║ {Colors.YELLOW}{title}{Colors.RESET}{' ' * (width - len(title) - 2)} ║"
        middle_spacer = f"║{' ' * width}║"
        return top + "\n" + side + "\n" + bottom, middle_spacer
    return top, bottom


def center_text(text, width):
    """Center text like a neurotic philosopher trying to find balance."""
    return text.center(width)


def main():
    # Clear the stage
    print("\033[2J\033[H", end="")
    
    # Get terminal width for nice alignment
    term_width = shutil.get_terminal_size().columns
    width = min(term_width - 4, 70)
    
    # Dramatic opening - the theater of existence awaits
    time.sleep(0.5)
    
    # Fancy title with flair
    title_box, _ = draw_box(width + 4, 3, " WOODY ALLEN'S EXISTENTIAL COMEDY HOUR ")
    print(f"\n{Colors.CYAN}{Colors.BOLD}{title_box}{Colors.RESET}")
    
    # Subtitle
    typewriter(
        center_text(
            f"{Colors.DIM}where every joke is a cry for help that nobody hears{Colors.RESET}",
            width + 12
        ),
        delay=0.02
    )
    
    print()
    time.sleep(0.8)
    
    # Build suspense... or don't, because what's the point?
    typewriter(f"{Colors.DIM}* clears throat nervously *{Colors.RESET}", delay=0.06)
    time.sleep(0.3)
    
    # Here comes the quote - delivered like a man who's thought too much about death
    quote_lines = [
        f"{Colors.YELLOW}{Colors.BOLD}\"I've been thinking about mortality lately,",
        f"{Colors.BOLD}which is funny because I've also been thinking",
        f"{Colors.BOLD}about ordering Chinese food, and honestly,",
        f"{Colors.BOLD}the lo mein is slightly more comforting than{Colors.RESET}",
        f"{Colors.YELLOW}{Colors.ITALIC}the inevitability of my own non-existence.{Colors.RESET}",
        f"{Colors.YELLOW}{Colors.BOLD}I mean, sure, one day I'll be returned to dust,",
        f"{Colors.BOLD}but at least the General Tso's chicken",
        f"{Colors.BOLD}will still exist — and that's the kind of{Colors.RESET}",
        f"{Colors.YELLOW}{Colors.ITALIC}optimism that keeps me going,",
        f"{Colors.YELLOW}{Colors.BOLD}right up until I remember that I'll never{Colors.RESET}",
        f"{Colors.MAGENTA}{Colors.BOLD}taste it again either.{Colors.RESET}\"",
    ]
    
    # Draw a contemplative box around the quote
    inner_width = width
    top_border = f"{Colors.MAGENTA}┌{'─' * (inner_width + 2)}┐{Colors.RESET}"
    bot_border = f"{Colors.MAGENTA}└{'─' * (inner_width + 2)}┘{Colors.RESET}"
    side_border = f"{Colors.MAGENTA}│{Colors.RESET}"
    
    print(f"\n{top_border}")
    for line in quote_lines:
        display_text = line + " " * (inner_width - len(line.replace('\033[0-9m', '').replace('\033[3m', '').replace('\033[1m', '')))
        # Simplified: just pad roughly
        clean_len = len(line.replace(Colors.RESET, '').replace(Colors.YELLOW, '').replace(Colors.BOLD, '').replace(Colors.ITALIC, '').replace(Colors.MAGENTA, '').replace(Colors.RED, '').replace(Colors.GREEN, '').replace(Colors.BLUE, '').replace(Colors.CYAN, '').replace(Colors.WHITE, '').replace(Colors.DIM, ''))
        # Actually, let's just pad naively
        padding = max(1, inner_width + 2 - 10)  # rough estimate
        typewriter(f"{side_border} {line}", delay=0.035)
    print(f"{bot_border}")
    
    print()
    time.sleep(1.2)
    
    # Existential follow-up
    typewriter(f"{Colors.CYAN}— Anonymous (probably{Colors.RESET}", delay=0.05)
    time.sleep(0.3)
    typewriter(f"{Colors.CYAN}Woody Allen, but he'd deny it{Colors.RESET}", delay=0.05)
    time.sleep(0.2)
    typewriter(f"{Colors.CYAN}{Colors.DIM}and then apologize for the denial{Colors.RESET}", delay=0.05)
    
    time.sleep(1.5)
    print()
    typewriter(f"{Colors.RED}{Colors.ITALIC}* exits stage left, trips over existential dread *{Colors.RESET}", delay=0.05)
    
    # Final flourish
    print(f"\n{Colors.MAGENTA}═══════════════════════════════════════════════════════════{Colors.RESET}")
    
    time.sleep(0.8)


if __name__ == "__main__":
    main()