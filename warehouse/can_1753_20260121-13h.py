"""
Campbell's Soup Can #1753
Produced: 2026-01-21 13:12:29
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, color_code='', delay=0.03):
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def woody_quote():
    clear_screen()
    
    # ASCII art frame
    print("\033[1;36m" + "╔══════════════════════════════════════════════════════════════════════════════════╗" + "\033[0m")
    print("\033[1;36m" + "║                                                                                ║" + "\033[0m")
    
    # Woody Allen ASCII art
    woody = [
        "   __  ",
        "  /  \\ ",
        " | O  |",
        " \\____/",
        "   ||  "
    ]
    
    for line in woody:
        print("\033[1;36m" + "║" + "\033[0m" + "  " + "\033[33m" + line + "\033[0m" + "\033[1;36m" + "  ║" + "\033[0m")
    
    print("\033[1;36m" + "║                                                                                ║" + "\033[0m")
    
    # The quote with different colors for different parts
    quote_intro = "\033[1;35m\"I've been analyzing my life,\033[0m"
    quote_middle = "\033[1;32m and I've concluded that the universe is fundamentally hostile,\033[0m"
    quote_end = f"\033[1;33m but at least it has good taste in neurotics like me.\033[0m\"\033[0m"
    
    # Typing effect for the quote
    typewriter_effect("  " + quote_intro, delay=0.02)
    typewriter_effect("  " + quote_middle, delay=0.02)
    typewriter_effect("  " + quote_end, delay=0.02)
    
    # Footer
    print("\033[1;36m" + "║                                                                                ║" + "\033[0m")
    print("\033[1;36m" + "║" + "\033[0m" + "                 " + "\033[3;37m" + "~ Woody Allen, probably" + "\033[0m" + "                    " + "\033[1;36m" + "║" + "\033[0m")
    print("\033[1;36m" + "║                                                                                ║" + "\033[0m")
    print("\033[1;36m" + "╚══════════════════════════════════════════════════════════════════════════════════╝" + "\033[0m")
    
    # Animated existential thought bubble
    time.sleep(2)
    print("\n")
    thought_bubble = [
        "    .-\"\"\"-.",
        "  /        \\",
        " |  O    O  |",
        " |     ~    |",
        "  \\   ___   /",
        "   '-_____-'",
        "     ||||",
        "    ||||",
        "   ||||",
        "  ||||",
        " ||||"
    ]
    
    for i in range(5):
        clear_screen()
        print("\033[3;36m")  # Italic cyan color
        for j, line in enumerate(thought_bubble):
            if j < len(thought_bubble) - 1:
                print(" " * (5 - i) + line)
            else:
                print(" " * (5 - i) + line + "\033[0m")
        time.sleep(0.3)
    
    # Final message
    time.sleep(1)
    print("\n\033[1;31mExistential crisis averted... for now.\033[0m")
    time.sleep(2)

if __name__ == "__main__":
    woody_quote()