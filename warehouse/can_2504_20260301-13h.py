"""
Campbell's Soup Can #2504
Produced: 2026-03-01 13:49:25
Worker: Baidu: ERNIE 4.5 VL 28B A3B (baidu/ernie-4.5-vl-28b-a3b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_colored(text, color_code):
    """Print text in the given ANSI color code."""
    sys.stdout.write(f"\033[{color_code}m{text}\033[0m\n")

def ascii_艺术():
    """Simply display a small ASCII art box as brown decor."""
    ascii_art = r"""
 __  __ _____ _____ _____ 
|  \/  |  __|____ |  __ \
| \  / | |__     | |__) |
| |\/| |  __|     |  _  /
| |  | | |___     | | \ \
|_|  |_|_____|    |_|  \_\
    """
    print_colored("+" + "-" * len(ascii_art) + "+", "73")  # Use ANSI color code 73 for greenish-brown
    print_colored("|" + ascii_art.strip() + "|", "73")
    print_colored("+" + "-" * len(ascii_art) + "+", "73")

def fade_quote():
    """Fading-in effect for the quote."""
    for fade in range(20):  # Fade in over 20 steps
        current_fade = min(20, fade + 10)  # 10-20 range for smooth fade
        clear_screen()
        print_colored(" " * 5, "0")  # Light gray for clear-screen effect
        quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."
        # Fade the quote text by making it lighter over time
        print_colored(quote[:current_fade] + (" " * (20 - current_fade)), "33")  # Use ANSI 33 (yellow) but fading
        time.sleep(0.1)

def clear_screen():
    """ANSI code to clear the terminal."""
    print("\033[H\033[J")

def main():
    clear_screen()
    ascii_艺术()
    time.sleep(1)  # Let the ASCII art settle

    clear_screen()  # Clear for the quote
    fade_quote()
    
    clear_screen()  # Once faded in, print the final quote clearly
    quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."
    
    # Decorate the quote with borders
    print_colored("+" + "-" * 50 + "+", "73")
    print_colored("|" + " " * 48 + "|", "73")
    print_colored("| " + quote + " |", "33")  # Use yellow ANSI 33
    print_colored("|" + " " * 48 + "|", "73")
    print_colored("+" + "-" * 50 + "+", "73")
    
    # Another pause to let it shine
    time.sleep(3)

if __name__ == "__main__":
    main()