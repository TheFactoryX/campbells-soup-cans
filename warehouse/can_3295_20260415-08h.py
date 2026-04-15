"""
Campbell's Soup Can #3295
Produced: 2026-04-15 08:04:54
Worker: Elephant (openrouter/elephant-alpha)
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

# ANSI color codes
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

# Woody Allen style quote
quote = (
    "I'm not afraid of death; I just don't want to be there "
    "when it happens. Unfortunately, my schedule is completely booked "
    "with other existential crises."
)

def typewriter_effect(text, delay=0.03):
    """Simulate a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))  # Small randomness for organic feel
    print()

def draw_wooden_box(text_lines):
    """Draw an ASCII art box around the text."""
    max_width = max(len(line) for line in text_lines)
    border = "+" + "-" * (max_width + 2) + "+"
    print()
    print(CYAN + border + RESET)
    for line in text_lines:
        print(CYAN + "| " + line.ljust(max_width) + " |" + RESET)
    print(CYAN + border + RESET)
    print()

def draw_speech_bubble(text_lines):
    """Draw a speech bubble around the text."""
    max_width = max(len(line) for line in text_lines)
    print()
    print(" " * (max_width + 4) + "___")
    print("  /" + " " * (max_width + 2) + "\\")
    for line in text_lines:
        print(f" | {line.ljust(max_width)} |")
    print("  \\ " + " " * (max_width + 1) + "/")
    print("   \"\"\"")
    print()

def draw_neurotic_frame(text_lines):
    """Draw a neurotic, glitchy frame."""
    max_width = max(len(line) for line in text_lines)
    glitch_symbols = ["@", "#", "$", "%", "&", "*"]
    glitch = random.choice(glitch_symbols) * (max_width + 4)
    
    print()
    print(MAGENTA + " .--." + RESET)
    print(MAGENTA + " |o_o |" + RESET)
    print(MAGENTA + " |:_/ |" + RESET)
    print()
    print(RED + glitch + RESET)
    print(WHITE + "┌" + "─" * (max_width + 2) + "┐" + RESET)
    for line in text_lines:
        print(WHITE + "│ " + line.ljust(max_width) + " │" + RESET)
    print(RED + "└" + "─" * (max_width + 2) + "┘" + RESET)
    print(WHITE + "  ‾‾‾‾‾‾‾‾‾" + RESET)
    print()
    print(YELLOW + "   (╯°□°）╯︵ ┻━┻   <-- Existential Dread Level: " + 
          str(random.randint(7, 10)) + "/10" + RESET)
    print()

def main():
    # Split quote into lines for formatting
    words = quote.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= 60:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    # Add some padding lines for visual effect
    padding_top = 2
    padding_bottom = 2
    
    print("\n" * padding_top)
    
    # Print title with animation
    title = " WOODY ALLEN'S EXISTENTIAL CRISIS QUOTE "
    print(BOLD + UNDERLINE + MAGENTA + " " + title + " " + RESET)
    time.sleep(0.5)
    
    # Print each line with a slight delay
    print(CYAN + "Life, the universe, and everything really annoying:" + RESET)
    time.sleep(0.3)
    
    # Animate the speech bubble
    for i, line in enumerate(lines):
        # Add random color to each word
        colored_words = []
        for word in line.split():
            color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE])
            colored_words.append(color + word + RESET)
        colored_line = " ".join(colored_words)
        
        # Draw the speech bubble with the line
        draw_speech_bubble([colored_line])
        time.sleep(0.2)
    
    # Draw the neurotic frame around the whole thing
    draw_neurotic_frame(lines)
    
    # Final flourish
    final_message = "The horror... the horror... is that it might actually be true!"
    colored_message = " ".join([random.choice([RED, YELLOW, MAGENTA]) + word + RESET 
                                for word in final_message.split()])
    print(BOLD + UNDERLINE + CYAN + "\n" + centered_text(colored_message, 70) + RESET)
    
    print("\n" * padding_bottom)

def centered_text(text, width):
    """Center text within a given width."""
    lines = text.split('\n')
    centered = []
    for line in lines:
        padding = max((width - len(line)) // 2, 0)
        centered.append(" " * padding + line)
    return "\n".join(centered)

if __name__ == "__main__":
    main()