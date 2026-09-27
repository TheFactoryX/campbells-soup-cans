"""
Campbell's Soup Can #5032
Produced: 2026-09-27 08:11:26
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# ANSI color codes
class Colors:
    NEUROTIC_BLUE = '\033[94m'
    ANXIOUS_YELLOW = '\033[93m'
    DEPRESSIVE_CYAN = '\033[96m'
    PARANOID_MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    ITALIC = '\033[3m'

def print_typewriter(text, delay=0.03, color=Colors.RESET):
    """Print text with a typewriter effect"""
    for char in text:
        print(color + char + Colors.RESET, end='', flush=True)
        time.sleep(delay)
    print()

def create_anxiety_burst():
    """Create a burst of anxious thoughts"""
    thoughts = [
        "What if they know?",
        "I should have said something else.",
        "Are they judging me right now?",
        "Why did I say that?",
        "This is a mistake.",
        "They're all staring.",
        "I'm going to fail.",
        "What is the meaning of this?"
    ]
    return random.choice(thoughts)

def main():
    # Clear screen for dramatic effect
    print("\033[2J\033[H", end="")
    
    # ASCII Art border
    border = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║                    WOODY ALLEN'S EXISTENTIAL CORNER          ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    
    print(Colors.NEUROTIC_BLUE + border + Colors.RESET)
    
    # The philosophical quote
    quote = (
        "I'm not afraid of death. I'm just afraid of dying alone "
        "in a room with a broken lamp, contemplating the futility "
        "of my existence while eating a cold sandwich. The universe "
        "is a vast, indifferent machine, and I'm just a neurotic cog "
        "trying to find meaning in the grease. But hey, at least I have "
        "this sandwich... though it's probably stale too."
    )
    
    # Print quote with dramatic pauses
    print("\n" + Colors.ANXIOUS_YELLOW + "He clears his throat nervously..." + Colors.RESET)
    time.sleep(1)
    
    print_typewriter(quote, delay=0.04, color=Colors.PARANOID_MAGENTA + Colors.ITALIC)
    
    # Additional neurotic commentary
    print("\n" + Colors.DEPRESSIVE_CYAN + "*Sighs deeply and adjusts glasses*" + Colors.RESET)
    time.sleep(1)
    
    random_thought = create_anxiety_burst()
    print_typewriter(f"Actually, {random_thought.lower()}.", delay=0.05, color=Colors.ANXIOUS_YELLOW)
    
    # Final existential punchline
    print("\n" + Colors.NEUROTIC_BLUE + "The End... or is it?" + Colors.RESET)
    print(Colors.BOLD + "Probably it is." + Colors.RESET)
    
    # Dramatic exit
    print("\n" + Colors.DEPRESSIVE_CYAN + "Fade to black..." + Colors.RESET)
    for i in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

if __name__ == "__main__":
    main()