"""
Campbell's Soup Can #428
Produced: 2025-11-21 17:31:36
Worker: OpenAI: GPT-5.1-Codex (openai/gpt-5.1-codex)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import itertools
import time

RESET = "\033[0m"

frames = [
r'''
            ☁ neurotic forecast ☁
                .-""""-.
              / -   -  \
             |  .-. .-. |
             |  \o| |o/ |
             \     ^    /
              '.  )--. '
                '-....-'
''',
r'''
            ☁ neurotic forecast ☁
                .-""""-.
              / -   -  \
             |  .-. .-. |
             |  /o| |o\ |
             \     ^    /
              '.  (--. '
                '-....-'
'''
]

frame_palette = [198, 197, 196, 202, 208, 214, 220, 221]
wave_palette = [33, 39, 45, 51, 87, 123, 159, 195, 201, 165, 129, 93, 57]
rainbow_palette = [196, 202, 208, 214, 220, 190, 154, 118, 82, 46, 47, 48, 49, 51, 39, 33, 69, 99, 135, 171, 207, 201]

def color_wave(width, offset=0, glyph="≈"):
    return ''.join(f"\033[38;5;{wave_palette[(offset + j) % len(wave_palette)]}m{glyph}" for j in range(width)) + RESET

def rainbow(text):
    return ''.join(f"\033[38;5;{rainbow_palette[i % len(rainbow_palette)]}m{ch}" for i, ch in enumerate(text)) + RESET

def animate_neurosis():
    spinner = itertools.cycle(["⥀", "⥂", "⥁", "⥃"])
    for i in range(12):
        color = f"\033[38;5;{frame_palette[i % len(frame_palette)]}m"
        print("\033[2J\033[H", end="")
        print(color + frames[i % len(frames)] + RESET)
        wave_line = color_wave(50, i)
        print("       " + wave_line)
        spin = next(spinner)
        status = f"\033[38;5;244mExistential buffering {spin} Please hold while doubts hyperventilate...{RESET}"
        print(status)
        time.sleep(0.13)
    print("\033[2J\033[H", end="")

def display_quote():
    quote = "I tried to align with the cosmos, but my neurosis showed up first, took attendance, and asked if the abyss validated parking."
    plain_line = f"  {quote}  "
    width = len(plain_line)
    indent = " " * 6
    aura_top = color_wave(width + 2, 5, glyph="⟡")
    top = f"\033[38;5;219m╭{'─'*width}╮{RESET}"
    bottom = f"\033[38;5;219m╰{'─'*width}╯{RESET}"
    middle = f"│{rainbow(plain_line)}│"
    print(indent + aura_top)
    print(indent + top)
    print(indent + middle)
    print(indent + bottom)
    print(indent + color_wave(width + 2, 11, glyph="⟡"))
    twinkle = ''.join(f"\033[38;5;{wave_palette[(i*2) % len(wave_palette)]}m✺{RESET}" for i in range(12))
    print(indent + " " * ((width // 2) - 6) + twinkle)

def main():
    animate_neurosis
    animate_neurosis()
    display_quote()

if __name__ == "__main__":
    main()