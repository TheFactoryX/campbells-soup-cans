"""
Campbell's Soup Can #3816
Produced: 2026-05-30 04:17:16
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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
import random

def typewriter_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def moving_dots(duration=3):
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(4):
            sys.stdout.write('\r' + ' ' * 20 + '.' * i + ' ' * (4-i) + ' Processing...')
            sys.stdout.flush()
            time.sleep(0.2)
    sys.stdout.write('\r' + ' ' * 40 + '\r')

def display_quote():
    # ANSI color codes
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    END = '\033[0m'
    
    # ASCII art frame elements
    corner = f"{YELLOW}╔{END}"
    corner_bottom = f"{YELLOW}╚{END}"
    horizontal = f"{YELLOW}═{END}"
    vertical = f"{YELLOW}║{END}"
    
    # Create frames
    top_frame = corner + horizontal * 68 + corner
    bottom_frame = corner_bottom + horizontal * 68 + corner_bottom
    
    # Woody Allen style quotes
    quotes = [
        f"""{RED}{BOLD}I've always believed in the power of positive thinking, 
but then I looked in the mirror and remembered I'm me.{END}""",
        f"""{RED}{BOLD}I tried to find the meaning of life, 
but I got distracted by a sale at Bloomingdale's. 
I'll resume my existential quest tomorrow... probably.{END}""",
        f"""{RED}{BOLD}I'm not afraid of death; I just don't want to be there when it happens. 
It's always so awkward, and the snacks are never good.{END}""",
        f"""{RED}{BOLD}Life is divided into the horrible and the miserable. 
The horrible would be like terminal cases, 
and the miserable is everyone else.{END}"""
    ]
    
    # Select a random quote
    quote = random.choice(quotes)
    
    # Attribution
    attribution = f"{PURPLE}-- Woody Allen{END}"
    
    # Clear screen and display
    clear_screen()
    
    # Title
    title = f"{CYAN}{BOLD}{ITALIC}Woolly Allen's Wisdom{END}"
    print(top_frame)
    typewriter_effect(f"{vertical} {' ' * 25}{title}{' ' * 26}{vertical}")
    
    # Display quote with typewriter effect
    lines = quote.split('\n')
    for line in lines:
        typewriter_effect(f"{vertical} {BLUE}{line}{vertical}")
    
    # Display attribution
    typewriter_effect(f"{vertical} {attribution}{vertical}")
    
    # Bottom frame
    print(bottom_frame)
    
    # Add some final thoughts
    final_thoughts = [
        f"{GREEN}Isn't it ironic that I'm worried about being forgotten, when I can't even remember where I put my keys?{END}",
        f"{GREEN}I'm not a pessimist, I'm just a well-informed optimist. Which explains why I'm always expecting the worst.{END}",
        f"{GREEN}Life is divided into the horrible and the miserable. The horrible would be like terminal cases, and the miserable is everyone else.{END}",
        f"{GREEN}I don't want to achieve immortality through my work; I want to achieve it through not dying. And maybe a good face cream.{END}"
    ]
    
    final_thought = random.choice(final_thoughts)
    
    time.sleep(1)
    typewriter_effect(f"\n{vertical} {final_thought}{vertical}")
    print(bottom_frame)
    
    # Add some moving dots to simulate thinking
    time.sleep(1)
    moving_dots(2)
    
    # Final message
    final_message = f"{YELLOW}{vertical} Thanks for enduring my existential crisis!{vertical}"
    typewriter_effect(final_message)
    print(bottom_frame)
    
    # Add a small ASCII art Woody Allen character
    woody_art = f"""
{WHITE}      o
     /|\\
     / \\{END}
{YELLOW}{vertical}  Woody says: "It's not that I'm afraid to die, I just don't want to be there when it happens!"{vertical}
{YELLOW}{vertical}        (Seriously, have you seen the appetizers at funerals?){vertical}
{corner_bottom}{horizontal * 68}{corner_bottom}
"""
    time.sleep(1)
    for line in woody_art.split('\n'):
        typewriter_effect(line)

if __name__ == "__main__":
    display_quote()