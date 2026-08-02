"""
Campbell's Soup Can #4414
Produced: 2026-08-02 18:13:40
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def colored(text, code):
    return f"\033[{code}m{text}\033[0m"

def main():
    box_width = 70
    top_border = colored("╔" + "═" * box_width + "╗", "1;36")
    bottom_border = colored("╚" + "═" * box_width + "╝", "1;36")
    interior_color = "1;33"

    # ASCII art
    art_lines = [
        "   .-'''''-.",
        "  /  o   o  \\",
        " |   _>^<_   |",
        "  \\.'/ \\.'/ ",
        "   |||||",
        "   |||||"
    ]

    # Quote
    raw_quote = (
        "“I'm not afraid of death; I just don't want to be there when it happens "
        "while I'm still debating the meaning of life over a slice of pizza.”"
    )

    # Wrap quote to fit the box
    words = raw_quote.split()
    wrapped_quote_lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + (1 if current else 0) <= box_width - 2:
            if current:
                current += " " + w
            else:
                current = w
        else:
            wrapped_quote_lines.append(current)
            current = w
    if current:
        wrapped_quote_lines.append(current)

    # Combine art and quote with a blank line between
    combined_lines = art_lines + [""] + wrapped_quote_lines

    # Print the box
    print(top_border)
    for line in combined_lines:
        padded = line.ljust(box_width - 2)
        print(colored(f"║ {padded} ║", interior_color))
        time.sleep(0.07)  # slight animation delay
    print(bottom_border)

    # Attribution
    print(colored("\n— Woody Allen‑ish", "0;37"))

if __name__ == "__main__":
    main()