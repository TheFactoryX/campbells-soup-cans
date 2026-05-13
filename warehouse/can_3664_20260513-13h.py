"""
Campbell's Soup Can #3664
Produced: 2026-05-13 13:29:01
Worker: Google: Gemma 4 31B (free) (google/gemma-4-31b-it:free)
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

def type_writer(text, delay=0.05, color="\033[37m"):
    for char in text:
        sys.stdout.write(f"{color}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_glasses():
    # ASCII art for those iconic thick-rimmed glasses
    glasses = [
        "\033[33m    XXXXX         XXXXX    \033[0m",
        "\033[33m  XX     XX     XX     XX  \033[0m",
        "\033[33m  XX     XX_____XX     XX  \033[0m",
        "\033[33m    XXXXX         XXXXX    \033[0m",
        "\033[33m          \033[31m  ^  \033[33m          \033[0m",
        "\033[33m       \033[31m  \___/  \033[33m       \033[0m"
    ]
    for line in glasses:
        print(line)

def main():
    # The Quote
    quote = "I’ve decided to live a life of absolute moderation; I’ll only have one existential crisis per hour, and I’ll strictly limit my panic attacks to the early morning."
    
    # Neurotic animation sequence
    clear_screen()
    
    # Simulated "Overthinking" process
    thoughts = [
        "Analyzing the futility of existence...",
        "Checking if I left the stove on...",
        "Questioning my choice of socks...",
        "Wondering if the universe is just a cruel joke...",
        "Actually, I'm just hungry."
    ]
    
    for thought in thoughts:
        sys.stdout.write(f"\r\033[3m\033[90m{thought}... \033[0m")
        sys.stdout.flush()
        time.sleep(random.uniform(0.4, 1.2))
        sys.stdout.write("\r" + " " * len(thought) + "\r")
        sys.stdout.flush()

    clear_screen()
    
    # Visual Presentation
    print("\n" * 2)
    draw_glasses()
    print("\n")
    
    # A decorative box
    border = "═" * 80
    print(f"\033[94m{border}\033[0m")
    print(f"\033[94m║\033[0m")
    
    # The quote typed out with neurotic pacing
    # We split the quote to simulate pauses in speech
    segments = [
        "I’ve decided to live a life of absolute moderation; ",
        "I’ll only have one existential crisis per hour, ",
        "and I’ll strictly limit my panic attacks to the early morning."
    ]
    
    for seg in segments:
        type_writer(f"  {seg}", delay=0.06, color="\033[1;37m")
        time.sleep(0.8)
        
    print(f"\033[94m║\033[0m")
    print(f"\033[94m{border}\033[0m")
    
    print("\n\n\t\t\t\033[3m\033[90m- Probably me, worrying about nothing.\033[0m\n")
    
    # Final nervous twitch effect
    for _ in range(3):
        sys.stdout.write("\r\033[31m(Panic!)\033[0m")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write("\r\033[37m(Calm...)\033[0m")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print("\r" + " " * 12 + "\r")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[31mI can't handle this pressure! I'm leaving!\033[0m")