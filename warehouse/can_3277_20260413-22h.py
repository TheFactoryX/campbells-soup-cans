"""
Campbell's Soup Can #3277
Produced: 2026-04-13 22:03:03
Worker: Google: Nano Banana (Gemini 2.5 Flash Image) (google/gemini-2.5-flash-image)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def woody_allen_quote_visualizer():
    quote = "I'm such a perfectionist, I even hate the idea of being perfectly aligned with my own neuroses. It's just… too neat."

    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m",
        "bold": "\033[1m",
        "italic": "\033[3m",
    }

    max_width = 70
    padding = 3
    quote_lines = []
    current_line = ""
    for word in quote.split():
        if len(current_line) + len(word) + 1 > max_width - 2 * padding:
            quote_lines.append(current_line.strip())
            current_line = word + " "
        else:
            current_line += word + " "
    if current_line:
        quote_lines.append(current_line.strip())

    box_width = max(len(line) for line in quote_lines) + 2 * padding
    top_bottom_border = colors["yellow"] + "╔" + "═" * box_width + "╗" + colors["reset"]
    mid_border = colors["yellow"] + "╠" + "═" * box_width + "╣" + colors["reset"]
    empty_line = colors["yellow"] + "║" + " " * box_width + "║" + colors["reset"]
    closing_border = colors["yellow"] + "╚" + "═" * box_width + "╝" + colors["reset"]

    print("\n" * 2) # Add some spacing

    # Animation part 1: Building the box
    print(top_bottom_border)
    time.sleep(0.1)
    print(empty_line)
    time.sleep(0.1)

    for i, line in enumerate(quote_lines):
        if i == len(quote_lines) // 2: # Highlight the middle part
            colored_line = colors["blue"] + colors["bold"] + colors["italic"] + line.center(box_width - 2 * padding) + colors["reset"]
            print(f"{colors['yellow']}║ {' ' * padding}{colored_line}{' ' * padding} ║{colors['reset']}")
        else:
            print(f"{colors['yellow']}║ {' ' * padding}{line.center(box_width - 2 * padding)}{' ' * padding} ║{colors['reset']}")
        time.sleep(0.15)

    print(empty_line)
    time.sleep(0.1)
    print(mid_border)
    time.sleep(0.1)

    # Adding a signature line like a thought trail
    signature = "- A slightly disturbed individual"
    print(f"{colors['yellow']}║ {colors['cyan']}{colors['italic']}{signature.rjust(box_width - padding)}{' ' * padding} ║{colors['reset']}")
    time.sleep(0.2)
    print(closing_border)

    print("\n" * 2) # Add some spacing at the end

if __name__ == "__main__":
    woody_allen_quote_visualizer()