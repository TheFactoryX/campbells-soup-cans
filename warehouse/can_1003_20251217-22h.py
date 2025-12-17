"""
Campbell's Soup Can #1003
Produced: 2025-12-17 22:36:09
Worker: Qwen: Qwen3 Coder 480B A35B (free) (qwen/qwen3-coder:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def clear_screen():
    print("\033[2J\033[H", end="")

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_border():
    print("\033[38;5;214m" + "=" * 60 + "\033[0m")

def print_centered(text):
    padding = (60 - len(text)) // 2
    print(" " * padding + text)

def print_thought_bubble():
    bubble = [
        "\033[38;5;159m" + "    ____________________________    ",
        "   /                            \\   ",
        "  |                              |  ",
        "  |                              |  ",
        "  |                              |  ",
        "   \\____________________________/   ",
        "        \\   /                     ",
        "         \\ /                      ",
        "          V                       " + "\033[0m"
    ]
    
    for line in bubble:
        print_centered(line)

def print_woody():
    woody_art = [
        "\033[38;5;222m" + "        O        ",
        "       /|\\       ",
        "       / \\       ",
        "     nervous     ",
        "    philosopher  " + "\033[0m"
    ]
    
    for line in woody_art:
        print_centered(line)

def main():
    clear_screen()
    
    # Build up the scene
    typewriter("\033[38;5;117mSetting the stage for profound wisdom...\033[0m", 0.03)
    time.sleep(0.5)
    clear_screen()
    
    # Flash some existential dread
    print("\033[38;5;196m" + "!" * 60 + "\033[0m")
    typewriter("\033[38;5;196mWARNING: The following may cause existential crisis\033[0m", 0.02)
    print("\033[38;5;196m!" * 60 + "\033[0m")
    time.sleep(1)
    
    # Show the philosopher
    clear_screen()
    print("\n" * 2)
    print_woody()
    time.sleep(0.5)
    
    # Thought bubble appears
    print("\n" * 2)
    print_thought_bubble()
    time.sleep(0.5)
    
    # The profound wisdom
    quotes = [
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Double predestination? Isn't that just asking for trouble?",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "Why do they call it rush hour when nothing moves?",
        "I took a speed reading course and read 'War and Peace' in twenty minutes. It involves Russia.",
        "The heart is a wonderful organ. It starts beating the moment we're born and never stops until we fall in love.",
        "I don't believe in the afterlife, although I am bringing a change of underwear.",
        "If it turns out that there is a God, I don't think that he's evil. But the worst that you can say about him is that basically he's an underachiever.",
        "The universe is not only stranger than we imagine, it's stranger than we can imagine. And I haven't even started my day yet!",
        "I was thrown out of college for cheating on the metaphysics exam; I looked into the soul of my fellow student.",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "Eternal nothingness is fine if you happen to be dressed for it.",
        "The only way to deal with an unfree world is to become so absolutely free that your very existence is an act of rebellion."
    ]
    
    chosen_quote = random.choice(quotes)
    
    # Print the quote with flair
    print("\033[38;5;159m" + "\033[1m")
    words = chosen_quote.split()
    line_length = 0
    line = ""
    
    for word in words:
        if line_length + len(word) > 30:
            print_centered("  " + line.strip())
            line = word + " "
            line_length = len(word) + 1
        else:
            line += word + " "
            line_length += len(word) + 1
    
    if line:
        print_centered("  " + line.strip())
    
    print("\033[0m")
    
    # Signature
    print("\n")
    print_centered("\033[38;5;214m-- Woody Allen (probably)\033[0m")
    
    # Final touch
    print("\n" * 2)
    typewriter("\033[38;5;245m(You're welcome for the existential crisis)\033[0m", 0.05)

if __name__ == "__main__":
    main()