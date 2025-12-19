"""
Campbell's Soup Can #1037
Produced: 2025-12-19 13:03:04
Worker: Qwen: Qwen3 Coder 480B A35B (qwen/qwen3-coder)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def typewriter_effect(text, delay=0.03):
    """Simulate typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_with_border(text, border_char="*"):
    """Print text with a border"""
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    
    print("\033[33m" + border_char * (max_length + 4) + "\033[0m")
    for line in lines:
        print("\033[33m" + border_char + " \033[0m" + line.ljust(max_length) + " \033[33m" + border_char + "\033[0m")
    print("\033[33m" + border_char * (max_length + 4) + "\033[0m")

def animate_thought():
    """Show thinking animation"""
    thoughts = ["\033[36m...\033[0m", "\033[36m..\033[0m", "\033[36m.\033[0m", " "]
    for _ in range(3):
        for thought in thoughts:
            sys.stdout.write(thought)
            sys.stdout.flush()
            time.sleep(0.2)
            sys.stdout.write("\b\b\b   \b\b\b")
    print()

def print_woody_quote():
    # Clear screen for dramatic effect
    print("\033[2J\033[H", end="")
    
    # Title
    title = """
    \033[35m**********************************************
    *                                            *
    *        WOODY ALLEN'S PHILOSOPHY            *
    *                                            *
    **********************************************\033[0m
    """
    print(title)
    
    time.sleep(1)
    
    # Thinking animation
    print("\033[32mContemplating existential dread...\033[0m")
    animate_thought()
    
    time.sleep(0.5)
    
    # The quote
    quote = """\033[1;37m"I'm not afraid of dying, but I'm in no hurry to 
    become a historical anecdote."\033[0m
    
\033[3m     - Allegedly Woody Allen (but probably made up)\033[0m"""
    
    # Print with typewriter effect
    print_with_border("WOODY'S WISDOM")
    print()
    typewriter_effect(quote, 0.05)
    
    # Add some philosophical decoration
    philosophy_art = """
    \033[34m          ()         ()
           //\\\\       //\\\\
          //  \\\\     //  \\\\
         //    \\\\   //    \\\\
        //      \\\\ //      \\\\
       //        ///        \\\\
      //         | |         \\\\
     //          | |          \\\\
    //___________| |___________\\\\
    |___________________________|
    |   ANXIETY IS FREE THINKING |
    |         WITH ACHIEVEMENT   |
    |___________________________|\033[0m
    """
    
    time.sleep(1)
    print(philosophy_art)
    
    # Final existential note
    note = "\033[32mP.S. Remember: The universe is indifferent to your\n" + \
           "      neuroses, but that's no reason to stop worrying!\033[0m"
    
    typewriter_effect(note, 0.04)

if __name__ == "__main__":
    print_woody_quote()