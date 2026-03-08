"""
Campbell's Soup Can #2639
Produced: 2026-03-08 09:44:49
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

def typewriter_effect(text, delay=0.05, color_code=None):
    """Display text with a typewriter effect"""
    if color_code:
        sys.stdout.write(color_code)
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    if color_code:
        sys.stdout.write('\033[0m')  # Reset color
    sys.stdout.write('\n')

def display_quote():
    # Clear screen
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Colors
    cyan = '\033[1;36m'
    yellow = '\033[0;33m'
    magenta = '\033[1;35m'
    red = '\033[0;31m'
    white = '\033[0;37m'
    
    # ASCII art border
    border_line = "╔══════════════════════════════════════════════════════════════════════════════════════════════╗"
    
    typewriter_effect(magenta + border_line, 0.01)
    typewriter_effect(magenta + "║" + cyan + "             WOODY ALLEN'S PHILOSOPHICAL ANGUISH             " + magenta + "║", 0.01)
    typewriter_effect(magenta + "╠══════════════════════════════════════════════════════════════════════════════════════════════╣", 0.01)
    
    # The quote with typewriter effect - a more Woody Allen-like quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens. Although, I suppose it's better than the alternative, which is being there when it happens to someone else. Which is almost as bad."
    
    # Format the quote with proper padding
    quote_line = "║" + " " * 2 + quote + " " * (75 - len(quote) - 4) + "║"
    
    typewriter_effect(magenta + quote_line, 0.02)
    
    typewriter_effect(magenta + "╚══════════════════════════════════════════════════════════════════════════════════════════════╝", 0.01)
    
    # Anxiety note
    anxiety_note = "\n\nP.S. Actually, I am afraid of death. And taxes. And public speaking. And spiders. And..."
    anxiety_line = "║" + " " * 2 + red + anxiety_note + " " * (75 - len(anxiety_note) - 4) + magenta + "║"
    typewriter_effect(anxiety_line, 0.02)
    
    # Author
    typewriter_effect(white + "\n\n" + "─ " * 20 + "\n" + "─ Woody Allen ─".center(40) + "\n" + "─ " * 20, 0.01)
    
    # Add a final thought after a delay
    time.sleep(2)
    final_thought = "\n\n...I think I need a therapist. Or at least a good therapist's phone number."
    typewriter_effect(white + final_thought.center(75), 0.03)

if __name__ == "__main__":
    display_quote()