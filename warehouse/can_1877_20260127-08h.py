"""
Campbell's Soup Can #1877
Produced: 2026-01-27 08:50:09
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

def typewrite(text, delay=0.04):
    """Print each character of text with a cycling foreground color."""
    colors = ['\x1b[31m', '\x1b[34m', '\x1b[95m', '\x1b[32m', '\x1b[33m', '\x1b[97m']
    idx = 0
    for ch in text:
        sys.stdout.write(colors[idx % len(colors)] + ch + '\x1b[0m')
        sys.stdout.flush()
        time.sleep(delay)
        idx += 1
    sys.stdout.write('\n')

def flash(duration=0.5):
    """Briefly flash a small symbol in alternating background colors."""
    bg_colors = ['\x1b[41m', '\x1b[42m', '\x1b[43m', '\x1b[44m', '\x1b[45m', '\x1b[46m']
    for col in bg_colors:
        for _ in range(5):
            for c in '✧':
                sys.stdout.write(col + c + '\x1b[0m')
                sys.stdout.flush()
                time.sleep(duration / (len(bg_colors) * 5))
    time.sleep(0.2)

def main():
    # Give terminal some breathing room
    print('\n' * 2)

    # Opening flash
    flash()
    time.sleep(0.3)

    # Header in bright magenta
    header = "W O O D Y   A L L E N   &   E X I S T E N T I A L   C O M E D Y"
    typewrite(header, delay=0.05)

    # ASCII art of a nervous face (color‑coded)
    face = r"""
   .---.
  /      \
 |  {}   |
  \----. 
      {}
""".format('\x1b[36m I\x1b[0m', '\x1b[33m  . .')
    lines = face.strip().splitlines()
    for line in lines:
        print(line)

    # A simple decorative box
    box = "+" + "-" * 20 + "+"
    sep = "|" + " " * 20 + "|"
    sys.stdout.write("\x1b[97m" + box + "\x1b[0m\n")
    for _ in range(4):
        sys.stdout.write("\x1b[97m" + sep + "\x1b[0m\n")
    sys.stdout.write("\x1b[97m" + box + "\x1b[0m\n")
    time.sleep(0.2)

    # Woody Allen‑style philosophical quote (multiple lines)
    quote = [
        "I have a strange feeling that my life is a sitcom —",
        "but I never read the script.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Meanwhile I’m obsessed with matching my socks.",
        "Because in a universe full of existential dread, the only comfort",
        "is knowing the right foot goes with the left."
    ]
    for line in quote:
        typewrite(line, delay=0.04)

    # Final pause before exit
    print('\n' * 2)
    print("\x1b[35mPress any key to stop... (Ctrl+C to quit)\x1b[0m")

if __name__ == "__main__":
    main()