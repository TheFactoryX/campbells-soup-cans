"""
Campbell's Soup Can #4787
Produced: 2026-08-23 10:41:20
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os
import sys

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_width():
    """Get terminal width for centering"""
    try:
        return os.get_terminal_size().columns
    except:
        return 80

def print_slow(text, delay=0.03, color=""):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\033[0m")  # Reset color

def create_box(text, width=60):
    """Create a decorative box around text"""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    box_width = max(max_len + 4, width)
    
    top = "    ╔" + "═" * (box_width - 2) + "╗"
    bottom = "    ╚" + "═" * (box_width - 2) + "╝"
    
    result = [top]
    for line in lines:
        padding = box_width - len(line) - 3
        result.append("    ║ " + line + " " * padding + "║")
    result.append(bottom)
    
    return '\n'.join(result)

# Woody Allen style quote
quote = """I don't want to achieve immortality through my work. 
I want to achieve it through not dying.

But then again, maybe that's just my anxiety talking. 
I'm not afraid of death, I'm just afraid of being alone when it happens.

Which is ironic, because I'm always alone. 
Even when I'm with people. Especially then.

Life is just a series of disappointments, 
but at least the coffee is good."""

def main():
    clear_screen()
    
    # Colors
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    
    # Print title
    title = "WOODY ALLEN'S EXISTENTIAL CRISIS"
    print("\n" + " " * 10 + BLUE + BOLD + "╔" + "═" * (len(title) + 4) + "╗" + RESET)
    print(" " * 10 + BLUE + BOLD + "║" + " " + YELLOW + BOLD + title + " " + BLUE + BOLD + "║" + RESET)
    print(" " * 10 + BLUE + BOLD + "╚" + "═" * (len(title) + 4) + "╝" + RESET)
    
    time.sleep(1)
    
    # Print quote with typewriter effect
    print("\n" + CYAN + "─" * 70 + RESET)
    print_slow(quote, delay=0.02, color=YELLOW)
    print(CYAN + "─" * 70 + RESET)
    
    # Print signature
    time.sleep(0.5)
    print("\n" + " " * 30 + MAGENTA + "─ Woody Allen (probably)" + RESET)
    
    # Print some decorative elements
    print("\n" + RED + "    ★" * 20 + RESET)
    
    # Animated ellipsis
    print("\n" + GREEN + "Thinking" + RESET, end="", flush=True)
    for i in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
    
    # Final joke
    final_line = "P.S. I'm not really Woody Allen. I'm just a Python script having an existential crisis."
    print("\n" + " " * 15 + final_line)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + "Even my code can't escape the existential dread. Goodbye.")
        sys.exit(0)