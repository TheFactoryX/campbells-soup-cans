"""
Campbell's Soup Can #375
Produced: 2025-11-19 08:42:23
Worker: TheDrummer: Cydonia 24B V4.1 (thedrummer/cydonia-24b-v4.1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import os
import sys
import time
import random
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text, color=Style.NORMAL):
    terminal_width = os.get_terminal_size().columns
    lines = text.split('\n')
    for line in lines:
        padding = " " * ((terminal_width - len(line) - len(Fore.WHITE)) // 2)
        print(f"{color}{padding}{line}{Style.RESET_ALL}")

def bouncing_dots():
    for i in range(1, 4):
        clear_screen()
        print(f"\n{Back.BLUE}{' ' * 5}{Style.RESET_ALL}")
        print_centered(f"Philosophizing[{'.' * i}{' ' * (3 - i)}]", Fore.GREEN)
        time.sleep(0.5)
    clear_screen()

def print_thought_box(text):
    terminal_width = os.get_terminal_size().columns
    border_length = min(80, terminal_width)
    top_border = '\u2503 ' + ' ' * (border_length - 2) + ' \u2503'
    middle = ' \u2503 ' + f"{text}\n".center(border_length - 4) + ' ' * (border_length - 2) + ' \u2503'
    
    for _ in range(3):
        print_centered(top_border)
        print_centered(middle)
        print_centered(f"\u2503 {' ' * (border_length - 2)} \u2503")
        time.sleep(0.3)
        print(f"\033[F\033[K\033[F\033[K\033[F\033[K", end="")  # Move cursor up and clear line
    
    print_centered(top_border)
    print_centered(middle)
    print_centered(f"\u2503 {' ' * (border_length - 2)} \u2503")

def glitch_effect(text):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    lines = text.split('\n')
    for _ in range(3):
        for line in lines:
            glitched = ''.join(random.choice(colors) + c for c in line)
            print(f"                  {glitched}")
        time.sleep(0.05)
        print(f"\033[F\033[K" * len(lines), end="")  # Move cursor up and clear line

def main():
    clear_screen()
    print_centered("\n\n\u2551\u2551", Fore.BLUE)
    print_centered("    WOODY ALLEN'S", Fore.BLUE)
    print_centered(" PHILOSOPHICAL SHAKE-UP", Fore.BLUE)
    print_centered("\u2551\u2551", Fore.BLUE)
    
    time.sleep(1.5)
    
    philosophers = [
        "Socrates\nand his\nquestionable\n_hygeine_",
        "Nietzsche\ncomplaining\nabout his\n_neighbors_",
        "Descartes\ntrying to\nprove his\nexistence",
        "Kant having\nway too many\nrules for\neverything"
    ]
    
    for i in range(4):
        print_centered(philosophers[i], Fore.CYAN)
        time.sleep(1)
        print(f"\033[F\033[K\033[F\033[K\033[F\033[K\033[F\033[K", end="")  # Clear main screen
    
    bouncing_dots()
    
    # Print the quote with effect
    print_centered("\nWhat I've learned is...", Fore.YELLOW)
    
    time.sleep(1)
    
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "My anxiousness isn't really a thing I want to escape, it's just the only part of me that's interesting.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "I realized I was talking to myself, but that's okay because I'm the only one who truly understands me...",
        "Happiness is just a chemical trick your brain plays to keep you from realizing how insignificant you are.",
        "I used to think my ship was coming in, then I realized I was at the wrong dock."
    ]
    
    # Choose a random quote
    quote = random.choice(quotes)
    
    # Wimpy "thought bubble" animation
    print_centered("[→→→]", Fore.BLUE)
    time.sleep(0.3)
    print(f"\033[F\033[K", end="")  # Clear the thought bubble
    
    # Make the thought bubble grow
    for i in range(1, 5):
        print_centered(f"[{'→' * i}{'→' * i}]", Fore.BLUE)
        time.sleep(0.1)
        print(f"\033[F\033[K", end="")  # Clear the thought bubble
    
    # Display the actual quote
    print_thought_box(quote)
    
    # Glitch effect
    glitch_effect(quote)
    
    # Final colorful message
    final_message = """


               )                       (
              (   (  (    )            ) )
   )    (      )\  )\ )( ( (    (   ( /( 
 ((( ) )\  '(( ))(()((()) )\)))\ ) tremendously
)))))\ )()) )((_)) /((() ((())((_)(()
 / __\(()((((_)_| |(_))_)/ _` / __ `| |
| (__ /(_)) |_  /|_|_)) | (_| \__ \ | |
 \___)\___/  |__|\___/|_| \__,_|___/ |_|



          It's all meaningless anyway.
            """
    
    print_centered("     ", Fore.RED)
    for i in range(20):
        parts = final_message.split("\n")
        colored_parts = [f"{random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])}{part}"
                         for part in parts]
        print("\n".join(colored_parts))
        time.sleep(0.05)
        sys.stdout.buffer write(b"\033[1A" * len(colored_parts))
        sys.stdout.buffer.write(b"\x1b[K\n" * len(colored_parts))

if __name__ == "__main__":
    main()