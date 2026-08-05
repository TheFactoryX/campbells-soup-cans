"""
Campbell's Soup Can #4442
Produced: 2026-08-05 17:53:28
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
A philosophically neurotic moment, served Woody Allen-style.
"""

import sys
import time
import shutil

# ANSI color codes
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    ITALIC  = "\033[3m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    ORANGE  = "\033[921m"  # 256-color orange (fallback below)
    GREY    = "\033[90m"

# The quote — pure existential neurosis
QUOTE = (
    "Existential dread: I'm terrified that I might not exist at all, "
    "but I'm equally terrified that I do."
)

def get_width():
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 70

def typewriter(text, delay=0.04):
    """Prints text with a typewriter effect, character by character."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_centered(text, color=C.YELLOW):
    width = get_width()
    for line in text.split('\n'):
        stripped = line.strip()
        padding = (width - len(stripped)) // 2
        print(f"{' ' * max(0, padding)}{color}{stripped}{C.RESET}")

def draw_bubble(quote):
    """Draws the quote inside a wavy ASCII thought/dread bubble."""
    width = max(50, min(get_width() - 4, 75))
    # Ensure even width for nicer borders
    if width % 2:
        width += 1

    inner = width - 4
    # Word-wrap
    words = quote.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= inner:
            current = (current + " " + w).strip()
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)

    quote_lines = [f" {l.ljust(inner)} " for l in lines]

    top_waves = " " + "".join("~" if i % 2 == 0 else "～" for i in range(width - 2))
    bottom_waves = " " + "".join("～" if i % 2 == 0 else "~" for i in range(width - 2))

    border_left = "║"
    border_right = "║"

    print(f"{C.CYAN}{' ' * ((get_width() - width)//2)}{top_waves[0]}{top_waves[1:]}{C.RESET}")
    print(f"{C.CYAN}{' ' * ((get_width() - width)//2)}╔{'═' * (width - 2)}╗{C.RESET}")
    for line in quote_lines:
        print(f"{C.CYAN}{' ' * ((get_width() - width)//2)}{border_left}{C.MAGENTA}{line}{C.RESET}{C.CYAN}{border_right}{C.RESET}")
    print(f"{C.CYAN}{' ' * ((get_width() - width)//2)}╚{'═' * (width - 2)}╝{C.RESET}")
    print(f"{C.CYAN}{' ' * ((get_width() - width)//2)} {bottom_waves[1:]}{C.RESET}")

def print_attribution():
    print_centered(f"{C.ITALIC}{C.GREY}— A moment of existential clarity{C.RESET}", color=C.GREY)

def print_ascii_face():
    """A neurotic little face staring at the void."""
    face = f"""
       {C.BOLD}{C.YELLOW}          ,-----.
          |  O O  |
          |   ∆   |     WOODY?
          |  '‿'  |     IS THIS... EXISTENCE?
          '-------'
          /|     |\\
         / |     | \\
        /  |     |  \\
{C.RESET}"""
    print_centered(face, color=C.YELLOW)

def main():
    print("\n" + C.DIM + f"{'=' * get_width()}" + C.RESET)
    print_centered(f"{C.BOLD}{C.MAGENTA} 🎭 A Philosophically Uncomfortable Pause 🎭 {C.RESET}", color=C.MAGENTA)
    print(C.DIM + f"{'=' * get_width()}" + C.RESET)
    print()

    print_ascii_face()
    print()
    time.sleep(0.5)

    draw_bubble(QUOTE)
    print()

    time.sleep(0.3)
    print_centered(f"{C.ORANGE}{C.ITALIC}The universe doesn't care... but you do.{C.RESET}")
    time.sleep(1)
    print()
    print_centered(f"{C.BOLD}{C.GREEN}Press ENTER to confront your insignificance...{C.RESET}", color=C.GREEN)
    try:
        input()
    except EOFError:
        pass
    print_centered(f"{C.DIM}Too late. The void already noticed you.{C.RESET}")

if __name__ == "__main__":
    main()