"""
Campbell's Soup Can #3141
Produced: 2026-04-05 09:00:26
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# Woody Allen style philosophical quote with visual flair
quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."

# ANSI escape codes for colors and formatting
colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "bold": "\033[1m",
    "reset": "\033[0m"
}

def typewriter(text, color="white", delay=0.05):
    """Typewriter effect with color"""
    color_code = colors.get(color, colors["white"])
    for char in text:
        sys.stdout.write(f"{color_code}{char}{colors['reset']}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_boxed(text, border_color="cyan", text_color="yellow"):
    """Print text in a colorful box"""
    border = colors[border_color] + "─" + colors["reset"]
    corner = colors[border_color] + "┌" + colors["reset"]
    corner += colors[border_color] + "┐" + colors["reset"]
    corner += "\n"
    corner += colors[border_color] + "│" + colors["reset"]
    corner += colors[border_color] + "│" + colors["reset"]
    corner += "\n"
    corner += colors[border_color] + "└" + colors["reset"]
    corner += colors[border_color] + "┘" + colors["reset"]

    # Calculate box width
    max_len = max(len(line) for line in text.split('\n'))
    width = max_len + 4

    # Print top border
    print(colors[border_color] + "┌" + "─" * width + "┐" + colors["reset"])

    # Print each line
    for line in text.split('\n'):
        padding = " " * (width - len(line))
        print(f"{colors[border_color]}│{colors['reset']} {colors[text_color]}{line}{colors['reset']}{colors[border_color]}{padding} │{colors['reset']}")

    # Print bottom border
    print(colors[border_color] + "└" + "─" * width + "┘" + colors["reset"])

def falling_characters(text, color="green"):
    """Make characters fall from top to bottom"""
    lines = []
    for i in range(len(text)):
        line = " " * i + text[i]
        lines.append(line)

    for line in lines:
        print(colors[color] + line + colors["reset"])
        time.sleep(0.1)
        print("\033[F" + " " * len(line) + "\033[F")  # Move cursor up and clear

    print(colors[color] + text + colors["reset"])

def wavy_text(text, color="blue"):
    """Print text with a wavy animation"""
    frames = []
    for i in range(3):
        frame = ""
        for j, char in enumerate(text):
            if (j + i) % 3 == 0:
                frame += f"{colors[color]}{char}{colors['reset']}"
            else:
                frame += char
        frames.append(frame)

    for _ in range(3):
        for frame in frames:
            print(frame)
            time.sleep(0.2)
            print("\033[F" * len(text.split('\n')))

# Main program
print("\n" * 2)
falling_characters("Woody Allen Wisdom:", color="magenta")

time.sleep(1)

print("\n" * 2)

# Typewriter effect for the quote
typewriter("I don't want to achieve immortality through my work;", color="yellow", delay=0.1)
typewriter("I want to achieve it through not dying.", color="yellow", delay=0.1)

print("\n" * 2)

# Boxed attribution
print_boxed("- Woody Allen", border_color="red", text_color="white")

print("\n" * 2)

# Wavy animation for "THE END"
wavy_text("THE END", color="cyan")

print("\n" * 2)