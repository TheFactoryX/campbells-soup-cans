"""
Campbell's Soup Can #475
Produced: 2025-11-23 19:26:05
Worker: Qwen: Qwen3 Coder Flash (qwen/qwen3-coder-flash)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
import time
import sys

def print_colored_text(text, color_code):
    """Print text with ANSI color code"""
    print(f"\033[{color_code}m{text}\033[0m")

def print_quote_box(quote):
    """Print quote in an ascii art box"""
    lines = quote.split('\n')
    max_length = max(len(line) for line in lines) + 4
    
    # Top border
    print("┌" + "─" * (max_length - 2) + "┐")
    
    # Quote content
    for line in lines:
        padding = " " * (max_length - len(line) - 2)
        print(f"│ {line}{padding} │")
    
    # Bottom border
    print("└" + "─" * (max_length - 2) + "┘")

def print_woody_animation():
    """Print animated woody face"""
    faces = [
        "( ._.)",
        "( o.o)",
        "( >.<)",
        "( ^.^)",
        "( -.-)"
    ]
    
    for _ in range(3):
        for face in faces:
            print(f"\r{face}", end="", flush=True)
            time.sleep(0.2)
    print()

def main():
    # Woody Allen inspired quotes
    quotes = [
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "I'm so nervous about the future that I can barely enjoy the present.",
        "The problem with most people is that they don't know what they're talking about.",
        "I've had a perfectly wonderful evening, but this wasn't it.",
        "I'm not neurotic; I'm just highly sensitive to the absurdity of existence.",
        "I would rather be a human being than a human being who is aware of the meaninglessness of life.",
        "I'm not lazy; I'm on energy-saving mode.",
        "I find myself in a state of constant anxiety about things that will never happen."
    ]
    
    # Select random quote
    selected_quote = random.choice(quotes)
    
    # Print animated face
    print_woody_animation()
    
    # Print quote with some visual flair
    print("\n" + "="*50)
    print_colored_text("    WOODY ALLEN'S PHILOSOPHICAL THOUGHTS", "1;35")  # Bold magenta
    print("="*50)
    
    # Split quote into lines for better formatting
    quote_lines = []
    words = selected_quote.split()
    current_line = ""
    
    for word in words:
        if len(current_line + word) < 40:
            current_line += word + " "
        else:
            quote_lines.append(current_line.strip())
            current_line = word + " "
    
    if current_line:
        quote_lines.append(current_line.strip())
    
    # Create box with colored edges
    print_colored_text("┌" + "─" * 48 + "┐", "1;36")  # Bold cyan
    
    for line in quote_lines:
        padded_line = f"│ {line:<46} │"
        print_colored_text(padded_line, "1;33")  # Bold yellow
    
    print_colored_text("└" + "─" * 48 + "┘", "1;36")  # Bold cyan
    
    # Add philosophical footer
    print()
    print_colored_text("    -- The Existentialist's Dilemma", "1;37")  # Bold white
    print()
    
    # Add some ASCII art
    print("    ╭━━━╮")
    print("    ┃   ┃")
    print("    ╰┳┳╯")
    print("     ┃┃")
    print("     ┃┃")
    print("    ╭┻┻╮")
    print("    ╰──╯  *Philosophy makes me anxious...*")
    
    print()
    print_colored_text("         [Press Enter to continue]", "1;32")  # Bold green
    input()

if __name__ == "__main__":
    main()