"""
Campbell's Soup Can #2598
Produced: 2026-03-06 09:56:22
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI color codes
COLORS = [
    '\033[91m',  # Red
    '\033[92m',  # Green
    '\033[93m',  # Yellow
    '\033[94m',  # Blue
    '\033[95m',  # Magenta
    '\033[96m',  # Cyan
    '\033[97m',  # White
]

RESET = '\033[0m'
BOLD = '\033[1m'

def woody_quote():
    """Return a Woody Allen-style quote."""
    return "I'm not afraid of death; I just don't want to be there when it happens. It's like being the last person at a party you never wanted to attend in the first place."

def typewriter_effect(text, delay=0.03):
    """Simulate a typewriter effect for the text."""
    for char in text:
        # Randomly colorize some characters
        if random.random() < 0.05:
            sys.stdout.write(random.choice(COLORS) + char)
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

def print_boxed_quote(quote):
    """Print the quote in a colorful box."""
    # Box dimensions
    max_width = 70
    padding = 2
    
    # Split quote into lines
    words = quote.split()
    lines = []
    current_line = []
    
    for word in words:
        if len(" ".join(current_line + [word])) <= max_width - 2 * padding:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
                current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    
    # Print top border with rainbow colors
    for i in range(max_width + 4):
        color = COLORS[i % len(COLORS)]
        sys.stdout.write(color + "█")
        sys.stdout.flush()
        time.sleep(0.005)
    sys.stdout.write(RESET + "\n")
    
    # Print quote lines with alternating colors
    for i, line in enumerate(lines):
        # Left border
        color = COLORS[i % len(COLORS)]
        sys.stdout.write(color + "██" + RESET + " ")
        
        # Line with random color highlights
        words = line.split()
        for word in words:
            if random.random() < 0.3:
                word_color = random.choice(COLORS)
                sys.stdout.write(word_color + word + RESET + " ")
            else:
                sys.stdout.write(word + " ")
        
        # Right border
        sys.stdout.write(color + "██" + RESET)
        print()
    
    # Print bottom border with reverse rainbow colors
    for i in range(max_width + 4):
        color = COLORS[len(COLORS) - (i % len(COLORS)) - 1]
        sys.stdout.write(color + "█")
        sys.stdout.flush()
        time.sleep(0.005)
    sys.stdout.write(RESET + "\n")

def print_woody_silhouette():
    """Print Woody Allen's silhouette."""
    silhouette = [
        "    .--.    ",
        "   |o_o |   ",
        "   |:_/ |   ",
        "  //   \\ \\  ",
        " (|     | ) ",
        " /'\\_   _/'\\ ",
        " \\__)~(__/  "
    ]
    
    # Print silhouette with cycling colors
    for i, line in enumerate(silhouette):
        color = COLORS[i % len(COLORS)]
        print(color + line.center(80) + RESET)
    
    # Print shadow
    shadow = [
        "    \\\\      ",
        "     \\\\     ",
        "      \\\\    ",
        "       \\\\   ",
        "        \\\\  ",
        "         \\\\ ",
        "          \\\\"
    ]
    
    for line in shadow:
        print("\033[2;90m" + line.center(80) + RESET)  # Dim gray

def main():
    # Clear screen
    print("\033[H\033[J", end='')
    
    # Print title
    title = "WOODY ALLEN'S PHILOSOPHICAL MUSINGS"
    print(BOLD + COLORS[4] + title.center(80) + RESET)
    print()
    
    # Print Woody Allen's silhouette
    print_woody_silhouette()
    print()
    
    # Get the Woody Allen quote
    quote = woody_quote()
    
    # Print the quote with typewriter effect
    typewriter_effect(quote, 0.02)
    
    print("\n")
    
    # Print the quote in a colorful box
    print_boxed_quote(quote)
    
    print("\n")
    
    # Print footer
    footer = "As told by Woody Allen (probably)"
    print("\033[3;90m" + footer.center(80) + RESET)

if __name__ == "__main__":
    main()