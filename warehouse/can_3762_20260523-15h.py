"""
Campbell's Soup Can #3762
Produced: 2026-05-23 15:20:01
Worker: Baidu Qianfan: CoBuddy (free) (baidu/cobuddy:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def typewriter_effect(text, color_code, delay=0.05):
    """Print text character by character with color and animation"""
    print(color_code, end='')
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print('\033[0m', end='')

def draw_box():
    """Draw an ASCII art box with colors"""
    # Define colors
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    
    # ASCII box art
    box = [
        f"{BLUE}{'╔' + '═' * 50 + '╗'}{RESET}",
        f"{CYAN}{'║'}{YELLOW}{BOLD}{' ' * 20}Woody Allen-style Philosophy{' ' * 17}{CYAN}{'║'}{RESET}",
        f"{BLUE}{'╠' + '═' * 50 + '╣'}{RESET}",
        f"{CYAN}{'║'}{RESET}",
        f"{CYAN}{'║'}{YELLOW}{BOLD}   I'm not afraid of death; I just don't want to be there when it{RESET}",
        f"{CYAN}{'║'}{YELLOW}{BOLD}   happens. Plus, what if they run out of wine?{' ' * 14}{RESET}",
        f"{CYAN}{'║'}{RESET}",
        f"{BLUE}{'╠' + '═' * 50 + '╣'}{RESET}",
        f"{CYAN}{'║'}{RESET}",
        f"{CYAN}{'║'}{YELLOW}{BOLD}   "I'm not afraid of death; I just don't want to be there{RESET}",
        f"{CYAN}{'║'}{YELLOW}{BOLD}   when it happens.{RESET}",
        f"{CYAN}{'║'}{RESET}",
        f"{BLUE}{'╠' + '═' * 50 + '╣'}{RESET}",
        f"{CYAN}{'║'}{RESET}",
        f"{CYAN}{'║'}{YELLOW}{BOLD}   "I'm not afraid of death; I just don't want to be there{RESET}",
        f"{CYAN}{'║'}{YELLOW}{BOLD}   when it happens.{RESET}",
        f"{CYAN}{'║'}{RESET}",
        f"{BLUE}{'╚' + '═' * 50 + '╝'}{RESET}"
    ]
    
    # Print box with animation
    for line in box:
        typewriter_effect(line, f"{CYAN}", 0.005)
        print()
        time.sleep(0.1)
    
    # Add some flair at the end
    print("\n")
    typewriter_effect("  ", f"{YELLOW}", 0.05)
    time.sleep(0.2)
    print(f"{CYAN}{'║'}{RESET}", end='')
    print(f"{YELLOW}{'═' * 48}{RESET}", end='')
    print(f"{CYAN}{'║'}{RESET}")
    time.sleep(0.2)
    
    # Final quote with dramatic pause
    final_quote = f"{YELLOW}{BOLD}  \"I'm not afraid of death; I just don't want to be there{RESET}"
    final_quote2 = f"{YELLOW}{BOLD}  when it happens. Plus, what if they run out of wine?\"{RESET}"
    
    print()
    typewriter_effect(final_quote, f"{YELLOW}", 0.08)
    print()
    typewriter_effect(final_quote2, f"{YELLOW}", 0.08)
    print()

if __name__ == "__main__":
    draw_box()
    
    # Add a little postscript
    time.sleep(0.5)
    print("\033[92m" + "  •  Woody Allen's last words: 'Is this the real life? Is this just fantasy?'" + "\033[0m")
    print("\033[96m" + "  •  'I don't want to achieve immortality through my work...'" + "\033[0m")
    print("\033[93m" + "  •  'Life is full of misery, loneliness, and suffering - and it's all over much too soon.'" + "\033[0m")