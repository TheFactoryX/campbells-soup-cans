"""
Campbell's Soup Can #1135
Produced: 2025-12-23 22:34:57
Worker: Google: Gemini 2.0 Flash Experimental (free) (google/gemini-2.0-flash-exp:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def animate_text(text, speed=0.1):
    for i in range(len(text)):
        print(text[:i+1], end='\r')
        time.sleep(speed)
    print(text)

def box_text(text,color_code):
    lines = text.split('\n')
    width = max(len(line) for line in lines) + 4
    horizontal_border = "+" + "-" * (width - 2) + "+"

    boxed_text = color_text(horizontal_border + "\n", color_code)
    for line in lines:
        padded_line = color_text("| {} |".format(line.center(width - 4)),color_code)
        boxed_text += padded_line + "\n"
    boxed_text += color_text(horizontal_border, color_code)

    return boxed_text


def main():
    woody_quote = "I'm terrified of my own mortality, which is why I only eat organic ice cream.  \nIt's not much, but it's all I've got between me and the void."

    colors = [31, 32, 33, 34, 35, 36, 91, 92, 93, 94, 95, 96]
    chosen_color = random.choice(colors)

    print("\n")
    animate_text(color_text("A Woody Allen-esque Thought:", chosen_color),speed = 0.05)
    print("\n")
    print(box_text(woody_quote,chosen_color))
    print("\n\n")

if __name__ == "__main__":
    main()