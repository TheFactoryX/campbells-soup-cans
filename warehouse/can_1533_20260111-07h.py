"""
Campbell's Soup Can #1533
Produced: 2026-01-11 07:32:55
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
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
import random

def woody_allen_quote():
    # A single, selectable existential zinger in pure Woody style
    return (
        "I'm not afraid of death;\n"
        "I just don't want to be there when it happens."
    )

def slow_type(text, delay=0.03, color_seq="\033[38;5;15m"):
    """Typewriter effect with color."""
    sys.stdout.write(color_seq)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Tiny jitter to feel organic
        jitter = delay * (0.8 + random.random() * 0.4)
        time.sleep(jitter)
    sys.stdout.write("\033[0m\n")

def draw_sunglasses_man():
    # Simple, big ASCII art with a neurotic vibe
    art = r"""
          .--.              .--.
         :o o:  (me too)   :o o:
          \_/              \_/
       .--.   .--.       .--.   .--.
      :o o: :o o:       :o o: :o o:
       \_/   \_/         \_/   \_/
      /   \ /   \       /   \ /   \
     |  o  |  o  |     |  o  |  o  |
     |     |     |     |     |     |
     \____/ \____/       \____/ \____/
    """
    # Gradient palette for the ASCII art (soft neon pastels)
    palette = [
        "\033[38;5;111m",  # soft blue
        "\033[38;5;140m",  # warm orange
        "\033[38;5;153m",  # lilac
        "\033[38;5;120m",  # lime
        "\033[38;5;225m"   # pink
    ]
    for line in art.splitlines():
        if not line.strip():
            print()
            continue
        # Cycle colors per line for a fun gradient
        color = palette[len(line) % len(palette)]
        print(f"{color}{line}\033[0m")
        time.sleep(0.05)

def animate_thought_bubble():
    # A blinking "cursor" bubble to set the mood
    bubble = [
        r"    .-~~-.",
        r"   :      :",
        r"   |  ... |",
        r"   |  .o. |",
        r"   |  ... |",
        r"    \____/"
    ]
    eyes = ["o", "O", "o", "-", "O", "o"]
    for _ in range(3):
        for eye in eyes:
            frame = []
            for line in bubble:
                if "|  " in line and " |" in line:
                    # Swap the middle character to simulate blinking
                    frame.append(line[:4] + eye + line[5:])
                else:
                    frame.append(line)
            # Print frame
            sys.stdout.write("\033[2J\033[H")  # Clear screen and home cursor
            sys.stdout.write("\033[38;5;221m")  # Yellow bubble
            for l in frame:
                print(l)
            sys.stdout.write("\033[0m")
            sys.stdout.flush()
            time.sleep(0.15)
        time.sleep(0.35)

def main():
    # Start with a blink; it's neurotic
    animate_thought_bubble()

    # Draw our slightly anxious mascot
    draw_sunglasses_man()

    # Print the quote with a typewriter effect
    quote = woody_allen_quote()
    print("\033[38;5;226m")  # Bright yellow for the prompt
    print("— A whisper from the void:")
    print("\033[0m")

    # Type out the quote with a soft cyan color
    slow_type(quote, delay=0.045, color_seq="\033[38;5;159m")

    # Add a self-deprecating punchline with a sliding effect
    punchline = "I knew it was too short... just like life."
    width = 60
    for i in range(width):
        pad = " " * (width - i)
        sys.stdout.write(f"\033[38;5;245m{pad}{punchline}\033[0m\r")
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\033[38;5;245m" + punchline + "\033[0m\n")
    time.sleep(0.2)

    # Move cursor out of the way cleanly
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write("\033[0m\n")
        sys.exit(0)