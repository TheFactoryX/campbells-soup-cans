"""
Campbell's Soup Can #5218
Produced: 2026-11-07 20:53:26
Worker: Crouton Alpha (stealth/crouton-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
GREEN = "\033[92m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

QUOTE = "I don't fear death; I just fear dying before my analyst cashes my last check."

RAIN_FRAMES = [
    "  .  *  .   *    .  *   .    *  .   *   .  *    .",
    " *   .    *   .    *   .    *   .    *   .    *  ",
    "    *   .    *   .    *   .    *   .    *   .   ",
]

ART = [
    "          .-\"\"\"\"\"-.",
    "        .'  _    _  '.",
    "       /   (o)  (o)   \\",
    "      |     ______     |",
    "       \\   /      \\   /",
    "        '-;  AL  ;-'",
    "          '------'",
    "      my glasses: protection from reality",
]

def rain_animation():
    for frame in RAIN_FRAMES:
        sys.stdout.write(CYAN + frame + RESET + "\n")
        sys.stdout.flush()
        time.sleep(0.18)
    sys.stdout.write("\n")
    sys.stdout.flush()

def type_text(text, stdout=sys.stdout):
    for ch in text:
        stdout.write(ch)
        stdout.flush()
        time.sleep(0.035)
    stdout.write("\n")

def main():
    rain_animation()

    for line in ART:
        sys.stdout.write(MAGENTA + BOLD + line + RESET + "\n")
    sys.stdout.write("\n")

    width = 82
    inner = width - 4

    sys.stdout.write(YELLOW + BOLD + "+" + "=" * (width - 2) + "+" + RESET + "\n")
    sys.stdout.write(YELLOW + BOLD + "|" + " " * (width - 2) + "|" + RESET + "\n")
    sys.stdout.write(YELLOW + BOLD + "|" + " " * 12 + "A VERY NEUROTIC THOUGHT" + " " * 12 + "|" + RESET + "\n")
    sys.stdout.write(YELLOW + BOLD + "|" + " " * (width - 2) + "|" + RESET + "\n")

    sys.stdout.write(YELLOW + BOLD + "| " + RESET)
    type_text(QUOTE)
    # pad the typed line to fill the box
    pad = inner - len(QUOTE)
    if pad > 0:
        sys.stdout.write(" " * pad)
    sys.stdout.write(YELLOW + BOLD + " |" + RESET + "\n")

    sys.stdout.write(YELLOW + BOLD + "|" + " " * (width - 2) + "|" + RESET + "\n")
    sys.stdout.write(YELLOW + BOLD + "+" + "=" * (width - 2) + "+" + RESET + "\n")

    sys.stdout.write("\n")
    sys.stdout.write(GREEN + "        ~ in the rain, under an umbrella, overthinking ~" + RESET + "\n")
    sys.stdout.write(BLUE + "        * patter * patter * existential dread *" + RESET + "\n")

if __name__ == "__main__":
    main()