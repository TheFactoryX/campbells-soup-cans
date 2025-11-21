"""
Campbell's Soup Can #431
Produced: 2025-11-21 20:33:48
Worker: Google: Gemini 2.0 Flash Experimental (free) (google/gemini-2.0-flash-exp:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def animate_text(text, color_code):
    """Animates text with color using ANSI escape codes."""
    for char in text:
        print(f"\033[{color_code}m{char}\033[0m", end="", flush=True)
        time.sleep(0.05)
    print()  # Newline after animation
    time.sleep(0.2)


def print_woody_allen_quote():
    """Prints a funny philosophical quote in Woody Allen's style."""

    quote = "I'm so neurotic, even my existential dread has anxiety."

    # ASCII art box
    print("\033[36m" + "-" * 50 + "\033[0m")  # cyan
    print("\033[36m|", end="")  # cyan
    print(" " * 48, end="")
    print("|\033[0m")
    print("\033[36m|", end="")
    print("  A Profound Utterance (Maybe) from Woody's Brain  ", end="")
    print("|\033[0m")
    print("\033[36m|", end="")
    print(" " * 48, end="")
    print("|\033[0m")
    print("\033[36m" + "-" * 50 + "\033[0m")  # cyan
    print()

    animate_text(quote, "33")  # yellow

    print()
    print("\033[35m" + "~ End of Neurosis Transmission ~" + "\033[0m") # magenta


if __name__ == "__main__":
    print_woody_allen_quote()