"""
Campbell's Soup Can #545
Produced: 2025-11-26 23:29:51
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

# ANSI Color codes
class Style:
    RESET = "\033[0m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    ORANGE = "\033[33m"
    PINK = "\033[95m"

# Woody Allen style quotes
quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.                ",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.  ",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "Love is the most important thing in our lives, except for the thing that comes after it.           ",
    "When you're in love, you're neurotic beyond all measure. It's awful.               "
]

# ASCII Art Frame
def draw_frame():
    width = 60
    top = Style.BLUE + '+' + '-' * (width - 2) + '+' + Style.RESET
    middle = Style.BLUE + '|' + ' ' * (width - 2) + Style.BLUE + '|' + Style.RESET
    print(top)
    for _ in range(8):
        print(middle)
    print(top)

# Print quote with typing effect
def type_quote():
    quote = quotes[3]
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for best effect
    
    # Initial frame with blinking cursor
    draw_frame()
    print(Style.ORANGE + "|".ljust(58) + "|" + Style.RESET)
    
    # Typing animation
    output = [" " * 60] * 9
    output[4] = "|   " + Style.YELLOW + quote[:1] + " " * (55 - 1) + "|" + Style.RESET
    print("\n".join(output), end="\033[6A")  # Move cursor to middle
    
    for i in range(1, len(quote)):
        update = list(output)
        update[4] = update[4][:4 + i] + Style.YELLOW + quote[i] + update[4][5 + i:] + Style.RESET
        print("\033[1A" * 9 + "".join(update)[-9:], end="\033[6A")
        time.sleep(0.05)
    print("\033[1A" * 9 + update[4].ljust(58) + "|\n" * 8, end="")
    
    # Stabilize
    time.sleep(0.3)

# Main wow animation
def main():
    # Clear screen and draw frame
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_frame()
    
    # Spaceship animation
    logo = "───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n─────▀▄░░░░░░░░░▄─▄▀──\n───▄─░░░░░░░░░░░▀───▀▄\n▄▀░░░░▀▀▀▄▄▄▄▀▀▀░░▄▀▄▀\n▀▄░░░░░░░░░░░░░░░░░▀──▄\n───▄▄▀▀███████▀▀▄▄▀▀▄▀\n▄▀███████████████████▀\n▀█████---------██████▀"
    print(Style.CYAN + "=" * 40)
    lines = logo.split('\n')
    for i in range(9):
        print("".join(lines[:i+1]).center(40))
        time.sleep(0.3)
    time.sleep(1)
    
    # Move logo away
    for i in range(9, 0, -1):
        print("\033[9A" + "=" * 40)
        print("\033[" + str(9-i) + "B" + "".join(lines[:i]).center(40))
        time.sleep(0.2)
    time.sleep(1)
    
    # Display quote
    type_quote()
    
    # Show Woody Allen
    woody = " (ノಠ益 ಠ)ﾉ彡┻━┻"
    for i in range(len(woody)):
        print("\033[1A" * 9 + Style.PINK + woody[:i].rjust(30) + Style.RESET)
        time.sleep(0.08)
    print("\033[9A" + "=" * 40 + "\n")
    
    # Final quote with effects
    time.sleep(1)
    style_effect(quotes[3])
    print(Style.RED + f"\n{'=' * 40}\n{quotes[3].strip()}\n{'=' * 40}" + Style.RESET)

# Powerful shaking effect
def style_effect(quote):
    for shake in range(10):
        offset = int(10 * abs(0.5 - shake/10))
        styled = [Style.YELLOW + " " * offset + char + Style.RESET for char in quote]
        print("".join(styled), end="\033[1A\r")
        time.sleep(0.05)
        if shake % 2 == 0:
            print("\033[1A" + " " * 60, end="\r")

if __name__ == "__main__":
    main()