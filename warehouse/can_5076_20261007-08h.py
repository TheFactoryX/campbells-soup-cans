"""
Campbell's Soup Can #5076
Produced: 2026-10-07 08:40:05
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import time
import random

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_width():
    """Get terminal width for centering"""
    try:
        return os.get_terminal_size().columns
    except:
        return 80

def type_text(text, delay=0.03, color=""):
    """Type text out like a typewriter"""
    for char in text:
        print(f"{color}{char}", end="", flush=True)
        time.sleep(delay)
    print()

def print_gradient_text(text, start_color=(255, 0, 0), end_color=(0, 0, 255)):
    """Print text with a color gradient"""
    # Simple gradient simulation using ANSI colors
    colors = [
        "\033[31m",  # Red
        "\033[33m",  # Yellow
        "\033[32m",  # Green
        "\033[36m",  # Cyan
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
    ]
    
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(f"{color}{char}", end="", flush=True)
        time.sleep(0.02)
    print("\033[0m")

def create_woodo_allen_quote():
    """Create and display a Woody Allen style quote with visual flair"""
    
    # Woody Allen style quotes
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens. But then again, given my luck, I probably will be - and it'll be raining.",
        "The question is not whether I believe in God, but whether God believes in me. And from the looks of it, I'm not getting a callback.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon. Now if you'll excuse me, I need to go stare at a wall and contemplate my navel.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying. But given my genetic makeup, that seems unlikely.",
        "My therapist says I have an avoidance personality disorder. I told him I'd like to avoid discussing it.",
        "I'm not a good person, but I'm not a bad person either. I'm just a neurotic, anxious, depressed individual who happens to be Jewish.",
        "The heart wants what the heart wants, but the heart also has terrible taste in relationships and is easily manipulated by anxiety.",
        "I used to be paranoid, but now I'm just realistically anxious. There's a difference."
    ]
    
    # Select a random quote
    quote = random.choice(quotes)
    
    # ASCII art frame
    frame_top = "╔" + "═" * 78 + "╗"
    frame_bottom = "╚" + "═" * 78 + "╝"
    frame_side = "║"
    
    # Colors
    title_color = "\033[1;33m"  # Bold yellow
    quote_color = "\033[1;36m"  # Bold cyan
    frame_color = "\033[1;31m"  # Bold red
    accent_color = "\033[1;32m" # Bold green
    reset = "\033[0m"
    
    # Clear screen for dramatic effect
    clear_screen()
    
    # Print top frame
    print(f"{frame_color}{frame_top}{reset}")
    
    # Print title
    title = " WOODY ALLEN STYLE PHILOSOPHY "
    print(f"{frame_color}{frame_side}{reset}{title_color}{title.center(76)}{reset}{frame_color}{frame_side}{reset}")
    
    # Print separator
    separator = "─" * 78
    print(f"{frame_color}{frame_side}{reset}{accent_color}{separator}{reset}{frame_color}{frame_side}{reset}")
    
    # Print quote with typewriter effect
    print(f"{frame_color}{frame_side}{reset}  ", end="")
    type_text(quote, delay=0.04, color=quote_color)
    
    # Print bottom padding
    print(f"{frame_color}{frame_side}{reset}{' ' * 78}{frame_color}{frame_side}{reset}")
    
    # Print bottom frame
    print(f"{frame_color}{frame_bottom}{reset}")
    
    # Print some existential dread
    print(f"\n{accent_color}* existential crisis level: HIGH *{reset}")
    print(f"{title_color}© Woody Allen's Neurotic Philosophy Club{reset}")
    
    # Blinking effect for extra anxiety
    for _ in range(3):
        print(f"\r{accent_color}Processing existential dread...{reset}", end="", flush=True)
        time.sleep(0.5)
        print(f"\r{accent_color}Processing existential dread... DONE{reset}", flush=True)
        time.sleep(0.5)

if __name__ == "__main__":
    # Set terminal title for extra flair
    print("\033]2;Woody Allen's Neurotic Philosophy\007", end="")
    
    # Create and display the quote
    create_woodo_allen_quote()
    
    # Final existential message
    print(f"\n{quote_color}Remember: The universe is indifferent, but at least we have comedy.{reset}")