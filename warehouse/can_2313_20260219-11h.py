"""
Campbell's Soup Can #2313
Produced: 2026-02-19 11:55:10
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# Clear screen and hide cursor for cleaner animation
def setup_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write("\033[?25l")  # Hide cursor

# Restore cursor
def cleanup_terminal():
    sys.stdout.write("\033[?25h")  # Show cursor
    sys.stdout.flush()

# Woody Allen style quote generator
def get_woody_quote():
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "What if everything is an illusion and nothing exists? In that case, I definitely overpaid for my carpet.",
        "I'm not against religion. I just think it would have been better if it had been invented by somebody else.",
        "I'm at the age where I want to be young, but I'm not. It's a very difficult age.",
        "I don't believe in the afterlife, but I'm going to take a change of underwear anyway.",
        "If my film makes one more person miserable, I'll be satisfied.",
        "I'm not saying I'm Batman. I'm just saying no one has ever seen me and Batman in the same room together.",
        "I took an IQ test and the results were negative."
    ]
    return "✨ " + quotes[int(time.time()) % len(quotes)] + " ✨"

def animate_quote():
    setup_terminal()
    
    colors = [
        '\033[38;5;208m',  # Orange
        '\033[38;5;226m',  # Yellow
        '\033[38;5;45m',   # Cyan
        '\033[38;5;129m',  # Purple
        '\033[38;5;46m',   # Green
    ]
    
    reset = '\033[0m'
    bold = '\033[1m'
    
    try:
        quote = get_woody_quote()
        
        # Create ASCII art frame
        frame_top = "╔" + "═" * 78 + "╗"
        frame_bottom = "╚" + "═" * 78 + "╝"
        side = "║"
        
        # Print decorative header
        print("\n" * 3)
        for i, char in enumerate("✧･ﾟ: *✧･ﾟ:* WOODY ALLEN SIMULATOR 3000 *:･ﾟ✧*:･ﾟ✧"):
            color_idx = i % len(colors)
            sys.stdout.write(colors[color_idx] + char + reset)
            sys.stdout.flush()
            time.sleep(0.05)
        print("\n")
        
        # Print top frame
        sys.stdout.write(colors[2] + frame_top + reset + "\n")
        
        # Print empty lines with animation
        for _ in range(2):
            sys.stdout.write(side + " " * 76 + side + "\n")
            time.sleep(0.1)
        
        # Animate quote with color cycling and typewriter effect
        words = quote.split()
        current_line = ""
        line_count = 0
        
        for word in words:
            test_line = current_line + " " + word if current_line else word
            if len(test_line) <= 70:
                current_line = test_line
            else:
                # Print current line with animation
                padding = (70 - len(current_line)) // 2
                line_str = " " * padding + bold + current_line + reset
                sys.stdout.write(side + line_str + " " * (76 - len(line_str)) + side + "\n")
                time.sleep(0.3)
                current_line = word
                line_count += 1
        
        # Print last line
        if current_line:
            padding = (70 - len(current_line)) // 2
            line_str = " " * padding + bold + current_line + reset
            sys.stdout.write(side + line_str + " " * (76 - len(line_str)) + side + "\n")
            time.sleep(0.3)
        
        # Print empty lines with animation
        for _ in range(2):
            sys.stdout.write(side + " " * 76 + side + "\n")
            time.sleep(0.1)
        
        # Print bottom frame
        sys.stdout.write(colors[2] + frame_bottom + reset + "\n\n")
        
        # Print signature with color cycle
        for i, char in enumerate("- Woody Allen (probably)"):
            color_idx = (i + 4) % len(colors)
            sys.stdout.write(colors[color_idx] + char + reset)
            sys.stdout.flush()
            time.sleep(0.03)
        print("\n")
        
        # Add blinking cursor effect
        for _ in range(3):
            sys.stdout.write("\033[5m" + " [press any key to exit] " + "\033[0m")
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write("\r" + " " * 28 + "\r")
            sys.stdout.flush()
            time.sleep(0.5)
        
    finally:
        cleanup_terminal()
        print("\n" + colors[0] + "Come back when you're more neurotic." + reset)

if __name__ == "__main__":
    animate_quote()