"""
Campbell's Soup Can #941
Produced: 2025-12-15 04:53:33
Worker: Google: Gemini 2.5 Flash Lite (google/gemini-2.5-flash-lite)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# Define ANSI escape codes for colors
COLORS = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "MAGENTA": "\033[95m",
    "CYAN": "\033[96m",
    "WHITE": "\033[97m",
    "RESET": "\033[0m",
}

def type_text(text, delay=0.05, color=COLORS["WHITE"]):
    """Types text character by character with a delay."""
    for char in text:
        print(f"{color}{char}{COLORS['RESET']}", end="", flush=True)
        time.sleep(delay)
    print()

def print_box(message, width=60, border_char="#", color=COLORS["YELLOW"]):
    """Prints a message inside a decorative box."""
    lines = message.splitlines()
    max_line_length = max(len(line) for line in lines)
    content_width = max(max_line_length, width - 4)  # -4 for borders and spaces

    print(f"{color}{border_char * (content_width + 4)}{COLORS['RESET']}")
    for line in lines:
        padding = (content_width - len(line)) // 2
        print(f"{color}{border_char} {' ' * padding}{line}{' ' * (content_width - len(line) - padding)} {border_char}{COLORS['RESET']}")
    print(f"{color}{border_char * (content_width + 4)}{COLORS['RESET']}")

def animate_quote():
    """Presents a Woody Allen-esque philosophical quote with animation."""
    quotes = [
        "The universe is under no obligation to make sense to you. Personally, I find this immensely reassuring. It means I don't have to make sense either.",
        "I'm not afraid of death. I just don't want to be there when it happens. Or perhaps, I'll merely be preoccupied with my own existential dread.",
        "Life is a series of events, most of which are deeply disappointing. And then, you die. Yay.",
        "The key to happiness? I think it's a really good mattress. And maybe not thinking too much about the vast, uncaring void.",
        "I'm not trying to be funny. I'm just trying to get through the day. The absurdity is a side effect.",
        "So, what's the meaning of life? My best guess is that it's a bad joke told by a cosmic amateur.",
        "I haven't committed any crimes. I've just been in a lot of compromising situations, which is basically the same thing, isn't it?"
    ]

    chosen_quote = random.choice(quotes)
    animation_delay = 0.03

    print("\n" * 2)
    type_text("Behold! A moment of profound, albeit anxious, introspection:", color=COLORS["CYAN"])
    time.sleep(1)

    for _ in range(3):
        print(f"\r...")
        time.sleep(0.5)
        print(f"\r. . .")
        time.sleep(0.5)
        print(f"\r...")
        time.sleep(0.5)
        print(f"\r   ") # Clear the dots

    print("\n")

    # Create a "thinking" animation
    thinking_chars = ["-", "\\", "|", "/"]
    for _ in range(4):
        for char in thinking_chars:
            print(f"\r{COLORS['MAGENTA']}Thinking... {char}{COLORS['RESET']}", end="", flush=True)
            time.sleep(0.1)
    print("\r" + " " * 20 + "\r", end="") # Clear the thinking message

    print("\n")
    color_cycle = [COLORS["RED"], COLORS["GREEN"], COLORS["YELLOW"], COLORS["BLUE"], COLORS["MAGENTA"], COLORS["CYAN"]]
    line_index = 0
    for char in chosen_quote:
        color = color_cycle[line_index % len(color_cycle)]
        print(f"{color}{char}{COLORS['RESET']}", end="", flush=True)
        time.sleep(animation_delay)
        if char == ' ':
            line_index += 1
    print("\n")

    # Add a subtle animation around the quote
    for _ in range(15):
        print(f"\r{COLORS['GREEN']}***{COLORS['WHITE']}   {COLORS['YELLOW']}***{COLORS['RESET']}", end="", flush=True)
        time.sleep(0.1)
        print(f"\r{COLORS['BLUE']}***{COLORS['WHITE']}   {COLORS['CYAN']}***{COLORS['RESET']}", end="", flush=True)
        time.sleep(0.1)
    print("\r" + " " * 30 + "\r", end="") # Clear the stars

    print("\n")
    print_box(chosen_quote, color=random.choice(list(COLORS.values())[0:6]), border_char=random.choice(["*", "+", "-", "="]))
    print("\n")
    type_text("...\nOr maybe, it's all just a bad dream.", color=COLORS["BLUE"], delay=0.07)

if __name__ == "__main__":
    animate_quote()