"""
Campbell's Soup Can #2201
Produced: 2026-02-13 15:01:20
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# Define ANSI color codes
BOX_COLOR = '\033[96m'  # Cyan for box
QUOTE_COLOR = '\033[93m'  # Yellow for quote
RESET = '\033[0m'

def print_witty_box():
    width = 60
    top = '╔' + '═' * width + '╗'
    title = '║' + 'WOODY ALLEN'S EXISTENTIAL CRISIS CORNER'.center(width) + '║'
    separator = '╠' + '═' * width + '╣'
    bottom = '╚' + '═' * width + '╝'

    # Custom Woody Allen-style quote (neurotic, self-deprecating, funny)
    quote = "I don't believe in the afterlife, but I'm always carrying an extra pair of socks just in case. What if there's a dress code in the void?"
    
    # Break quote into lines with max width (leaving space for borders)
    max_line = width - 2
    words = quote.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= max_line:
            current += word + " "
        else:
            lines.append(current.rstrip())
            current = word + " "
    lines.append(current.rstrip())
    
    # Center each line
    lines = [line.center(max_line) for line in lines]

    # Print the box with animated quote
    print(BOX_COLOR + top)
    print(BOX_COLOR + title)
    print(BOX_COLOR + separator)
    
    for line in lines:
        # Left border
        print(BOX_COLOR + '║', end='', flush=True)
        # Quote text with typing animation
        print(QUOTE_COLOR, end='', flush=True)
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.015)
        # Right border
        print(BOX_COLOR + '║' + RESET)
    
    print(BOX_COLOR + bottom + RESET)

# Add playful ASCII art of Woody Allen's glasses above the box
def print_glasses():
    glasses = [
        "      _.--._        _.--._",
        "    .'      '.    .'      '.",
        "   /          \\  /          \\",
        "  |   (O)  (O) ||   (O)  (O) |",
        "  |            ||            |",
        "   \\    .--.  /  \\  .--.    /",
        "    '.      .'    '.      .'",
        "      `----'        `----'"
    ]
    for line in glasses:
        print(BOX_COLOR + line + RESET)
        time.sleep(0.05)

# Main execution with fun animation sequence
print_glasses()
print_witty_box()
print(f"\n{QUOTE_COLOR}Why did the neurotic philosopher refuse the afterlife?{RESET}")
print(f"{QUOTE_COLOR}He didn't want to be late for the cosmic bus!{RESET}")