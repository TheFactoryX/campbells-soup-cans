"""
Campbell's Soup Can #5214
Produced: 2026-11-06 17:57:57
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_slow(text, delay=0.03, end='\n'):
    """Print text with a typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def print_banner():
    """Print a cool ASCII banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                              ║
    ║     ██████╗ ██╗      ██████╗  █████╗     ███████╗██╗      ██████╗  █████╗     ║
    ║    ██╔════╝ ██║     ██╔═══╝ ██╔══██╗    ██╔════╝██║     ██╔═══╝ ██╔══██╗    ║
    ║    ██║     ██║     ██║     ████████║    █████╗  ██║     ██║     ████████║    ║
    ║    ██║     ██║     ██║     ██╔══██║    ██╔══╝  ██║     ██║     ██╔══██║    ║
    ║    ╚██████╗██║     ╚██████╗██║  ██║    ███████╗██║     ╚██████╗██║  ██║    ║
    ║     ╚═════╝╚═╝      ╚═════╝╚═╝  ╚═╝    ╚══════╝╚═╝      ╚═════╝╚═╝  ╚═╝    ║
    ║                                                                              ║
    ║                           W O O D Y   A L L E N                             ║
    ║                                                                              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
    """
    
    # Colors for the banner
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    
    for i, line in enumerate(banner.split('\n')):
        if line:  # Skip empty lines
            color = colors[i % len(colors)]
            print(color + line + '\033[0m')
            time.sleep(0.05)

def main():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Print banner
    print_banner()
    print()
    
    # The Woody Allen style quote
    quote = "I've been thinking about the meaning of life, and I've concluded that it's a lot like a bad restaurant: the food is terrible, the service is worse, and yet, somehow, we keep going back. And the worst part? I'm the only one who knows the menu is empty."
    
    # Print quote with dramatic effect
    print_slow("\033[93m" + " "*40 + " existential crisis loading... " + "\033[0m", 0.05)
    time.sleep(0.5)
    
    # Print the quote in a fancy box
    print("\n" + "\033[94m" + "┌" + "─" * 78 + "┐" + "\033[0m")
    print("\033[94m" + "│" + "\033[0m" + " " * 78 + "\033[94m" + "│" + "\033[0m")
    
    # Word wrap the quote
    words = quote.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + word) <= 74:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())
    
    # Print each line centered
    for line in lines:
        padding = (76 - len(line)) // 2
        print("\033[94m" + "│" + "\033[0m" + " " * padding + "\033[93m" + line + "\033[0m" + " " * (76 - padding - len(line)) + "\033[94m" + "│" + "\033[0m")
    
    print("\033[94m" + "│" + "\033[0m" + " " * 78 + "\033[94m" + "│" + "\033[0m")
    print("\033[94m" + "└" + "─" * 78 + "┘" + "\033[0m")
    
    # Add some Woody-isms
    print("\n" + "\033[95m" + " "*30 + "─(scratch head)─" + "\033[0m")
    print_slow("\033[95m" + "You know, I used to think I was part of the universe... now I'm not so sure." + "\033[0m", 0.04)
    print_slow("\033[95m" + "Maybe I'm just a random fluctuation in the void. But then again, so is everything else." + "\033[0m", 0.04)
    
    # Final touch - a blinking cursor effect
    print("\n" + "\033[92m" + " "*50 + "█" + "\033[0m", end='')
    time.sleep(1)
    print("\r" + " " * 50 + "\r", end='', flush=True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[91mWell, I guess even existential dread can be interrupted.\033[0m")
        print("\033[93m...but the void remains.\033[0m")