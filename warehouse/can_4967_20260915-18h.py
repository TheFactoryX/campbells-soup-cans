"""
Campbell's Soup Can #4967
Produced: 2026-09-15 18:12:33
Worker: MoonshotAI: Kimi K2.7 Code (moonshotai/kimi-k2.7-code)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import textwrap

# ANSI color codes — no external dependencies needed
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
ITALIC = "\033[3m"

def typewrite(text, delay=0.025, end="\n"):
    """Print text one character at a time for dramatic neurotic effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def main():
    width = 62
    quote = ("I don't want to achieve immortality through my work. "
             "I want to achieve it by not dying... "
             "ideally while eating a pastrami sandwich.")
    attribution = "— Woody Allen, more or less"

    # Wrap the existential dread neatly inside the box
    lines = textwrap.wrap(quote, width=width - 4)
    if len(lines) == 1:  # force at least a little suspense
        mid = len(lines[0]) // 2
        lines = [lines[0][:mid].rstrip(), lines[0][mid:].lstrip()]

    print("\n" * 2)

    # Build and draw the fancy box
    typewrite(f"{CYAN}╭{'═' * width}╮{RESET}", delay=0.003)
    typewrite(f"{CYAN}║{' ' * width}║{RESET}", delay=0.003)

    # Type out the quote like an anxious confession
    for line in lines:
        pad = (width - len(line)) // 2
        right_pad = width - len(line) - pad
        typewrite(
            f"{CYAN}║{RESET}{' ' * pad}{YELLOW}{ITALIC}{line}{RESET}"
            f"{' ' * right_pad}{CYAN}║{RESET}",
            delay=0.002
        )
        time.sleep(0.18)

    # Attribution on the right, naturally
    attr_pad = width - len(attribution) - 3
    typewrite(
        f"{CYAN}║{RESET}{' ' * attr_pad}{MAGENTA}{attribution}{RESET}  "
        f"{CYAN}║{RESET}",
        delay=0.002
    )

    typewrite(f"{CYAN}║{' ' * width}║{RESET}", delay=0.003)
    typewrite(f"{CYAN}╰{'═' * width}╯{RESET}", delay=0.003)

    # A tiny, bespectacled existential companion
    time.sleep(0.3)
    print(f"\n{GREEN}"
          f"            .--.          \n"
          f"           /  -  \\     *stares into abyss*\n"
          f"          | (o)(o)|        *over lunch*\n"
          f"           \\  ==  /       \n"
          f"            |____|        \n"
          f"           /|    |\\      \"It's not that I'm afraid\n"
          f"          (_/    \\_)      of death... I just have plans.\"\n"
          f"{RESET}")

if __name__ == "__main__":
    main()