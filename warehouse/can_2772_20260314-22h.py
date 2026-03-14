"""
Campbell's Soup Can #2772
Produced: 2026-03-14 22:45:57
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

def animate_print(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    quote = "My brain is only second in importance to my heart; unfortunately, my heart is a hopeless romantic."
    width = 50
    words = quote.split()
    wrapped = []
    line = ""
    for w in words:
        if len(line) + len(w) + 1 <= width:
            line = (line + " " + w).strip()
        else:
            wrapped.append(line)
            line = w
    if line:
        wrapped.append(line)

    top = "╔" + "═" * (width + 2) + "╗"
    bottom = "╚" + "═" * (width + 2) + "╝"

    animate_print(color(top, "96"))  # bright cyan
    for l in wrapped:
        padded = l.ljust(width)
        animate_print(color(f"║ {padded} ║", "93"))  # bright yellow
    animate_print(color(bottom, "96"))

    footer = "- Woody Allen (probably)"
    animate_print(color(footer.center(width + 4), "95"))  # bright magenta

if __name__ == "__main__":
    main()