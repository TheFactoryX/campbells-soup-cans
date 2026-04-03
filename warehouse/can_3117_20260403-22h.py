"""
Campbell's Soup Can #3117
Produced: 2026-04-03 22:53:10
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def typewriter(text, color_code, delay=0.03):
    for ch in text:
        sys.stdout.write(color(ch, color_code))
        sys.stdout.flush()
        time.sleep(delay)

def main():
    quote = "Life is divided into the horrible and the miserable—that's the two categories, and I'm still waiting for the miserable to show up."
    width = len(quote) + 4
    top_bottom = " " + "─" * (width - 2) + " "
    print(color(top_bottom, 96))  # cyan border
    print(color("│ ", 96), end='')  # left border
    typewriter(quote, 93)          # yellow quote
    print(color(" │", 96))         # right border
    print(color(top_bottom, 96))   # bottom border
    # tiny Woody Allen‑ish face
    face = r"""
      (\ /)
     ( . .)
      c(")(")
    """
    print(color(face, 92))  # green face

if __name__ == "__main__":
    main()