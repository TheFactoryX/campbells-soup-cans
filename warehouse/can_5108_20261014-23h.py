"""
Campbell's Soup Can #5108
Produced: 2026-10-14 23:55:11
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

RESET = "\033[0m"
CYAN = "\033[96m"
YELLOW = "\033[93m"

def main():
    # Woody Allen‑style quote (original)
    quote = '"Life is like a missing sock: you spend ages looking for it, then realize you were barefoot all along."'
    padding = 2
    inner = f' {quote} '
    width = len(inner)

    top    = f"{CYAN}╔{'═'*width}╗{RESET}"
    middle = f"{CYAN}║{YELLOW}{inner}{CYAN}║{RESET}"
    bottom = f"{CYAN}╚{'═'*width}╝{RESET}"

    face = f"""{YELLOW}
       (\_/)
       ( •̀ᴥ•́ )
        /   \\
{RESET}"""

    lines = [face, top, middle, bottom]

    for line in lines:
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(0.005)  # typewriter‑like delay
        sys.stdout.write('\n')
        sys.stdout.flush()
        time.sleep(0.2)        # pause between lines

if __name__ == "__main__":
    main()