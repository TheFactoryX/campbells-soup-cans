"""
Campbell's Soup Can #2235
Produced: 2026-02-15 07:49:55
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random
from itertools import cycle

class WoodyAllenPhilosopher:
    def __init__(self):
        self.quotes = [
            "I'm not afraid of death; I just don't want to be there when it happens.",
            "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
            "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
            "What a wonderful world it would be if we could just skip the whole 'being born' business.",
            "I took a test in Existentialism. I left all the answers blank and got a 100.",
            "I'm not neurotic, I'm just a sensitive person in a cruel, uncaring universe.",
            "I believe there's something out there watching us. Unfortunately, it's probably my mother.",
            "The difference between sex and death is, with death you can do it alone and nobody complains."
        ]
        self.colors = [
            '\033[1;33m',  # Yellow
            '\033[1;36m',  # Cyan
            '\033[1;35m',  # Magenta
            '\033[1;32m',  # Green
            '\033[1;31m',  # Red
        ]
        self.reset = '\033[0m'
        self.border_chars = ['▢', '◼', '◻', '▣', '▨', '◱', '◲', '▥']
        
    def animate_text(self, text, delay=0.03, color=None):
        """Typewriter effect with optional color"""
        if color:
            sys.stdout.write(color)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay * random.uniform(0.5, 1.5))
        if color:
            sys.stdout.write(self.reset)
        print()
    
    def create_wavy_border(self, width, height=3):
        """Create animated wavy border"""
        border_lines = []
        for i in range(height):
            line = []
            for j in range(width):
                char = random.choice(self.border_chars)
                line.append(char)
            border_lines.append(''.join(line))
        return border_lines
    
    def display_quote(self):
        """Display the quote with Woody Allen style visuals"""
        quote = random.choice(self.quotes)
        
        # Clear screen
        print("\033[2J\033[H", end="")
        
        # Terminal width detection (fallback to 80)
        try:
            term_width = os.get_terminal_size().columns
        except:
            term_width = 80
            
        # Calculate box dimensions
        max_line_len = len(quote)
        box_width = min(max_line_len + 10, term_width - 4)
        box_height = 5
        
        # Create wavy animated border
        print()
        for border_line in self.create_wavy_border(box_width):
            color = random.choice(self.colors)
            print(f"  {color}{border_line}{self.reset}")
        
        # Print quote with neurotic wobble
        print()
        quote_color = random.choice(self.colors)
        accent_color = random.choice([c for c in self.colors if c != quote_color])
        
        # Split quote for dramatic effect
        words = quote.split()
        mid = len(words) // 2
        line1 = ' '.join(words[:mid])
        line2 = ' '.join(words[mid:])
        
        # Animate first line
        self.animate_text(f"    {quote_color}\"{line1}\"{self.reset}", 
                         delay=0.04, color=quote_color)
        
        # Dramatic pause
        time.sleep(0.3)
        
        # Animate second line with slight wobble
        wobble = random.choice(['  ', '   ', ''])
        self.animate_text(f"    {quote_color}{wobble}{line2}\"{self.reset}", 
                         delay=0.04, color=quote_color)
        
        # Add Woody Allen-esque afterthought
        time.sleep(0.5)
        afterthoughts = [
            "  (I'm probably overthinking this)",
            "  (My analyst will have a field day)",
            "  (Not that I'm complaining... much)",
            "  (This seems like a good time for a sandwich)",
            "  (I should have been a dentist)"
        ]
        afterthought = random.choice(afterthoughts)
        self.animate_text(f"{accent_color}{afterthought}{self.reset}", 
                         delay=0.02, color=accent_color)
        
        print()
        for border_line in self.create_wavy_border(box_width):
            color = random.choice(self.colors)
            print(f"  {color}{border_line}{self.reset}")
        
        # Bottom attribution with wobble
        time.sleep(0.2)
        wobble2 = random.choice(['', '  ', '    '])
        print(f"\n  {accent_color}{wobble2}~ Woody Allen (probably){self.reset}")
        
        # Little existential flourish
        time.sleep(0.5)
        print(f"\n  \033[2m(But what do I know? I'm just a collection of atoms \
that mistakenly believes it's conscious.){self.reset}\n")

if __name__ == "__main__":
    try:
        import os
        philosopher = WoodyAllenPhilosopher()
        philosopher.display_quote()
    except KeyboardInterrupt:
        print(f"\n\033[1;31m(Sometimes it's better to just give up and have a snack.){'\033[0m'}\n")
        sys.exit(0)