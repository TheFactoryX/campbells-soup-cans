"""
Campbell's Soup Can #2583
Produced: 2026-03-05 11:48:36
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
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
from itertools import cycle

class WoodyAllenPhilosopher:
    def __init__(self):
        self.quotes = [
            "I'm not afraid of death; I just don't want to be there when it happens.",
            "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
            "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
            "What if everything is an illusion and nothing exists? In that case, I definitely overpaid for my carpet.",
            "I don't believe in an afterlife, but I'm going to take a change of underwear anyway.",
            "My one regret in life is that I am not somebody else.",
            "I am not against all religions. I'm only against the ones that work.",
            "I took a test in Existentialism. I left all the answers blank and got an A.",
            "I'm not against marriage, but I'd rather have my wife dead than divorced.",
            "The difference between sex and death is, with death you can do it alone and nobody complains."
        ]
        
    def _get_random_quote(self):
        return random.choice(self.quotes)
    
    def _neurotic_typewriter(self, text, color, delay=0.03):
        """Typewriter effect with nervous energy"""
        for char in text:
            print(f"{color}{char}\033[0m", end='', flush=True)
            time.sleep(delay * random.uniform(0.5, 2.0))
        print()
    
    def _worry_wave(self, width=50):
        """Animate a worrying sinusoid wave"""
        for i in range(20):
            x = 10 * (1 + (i % 4))
            spaces = " " * (width // 2 - x)
            bar = "~" * (2 * x)
            print(f"\033[33m{spaces}{bar}\033[0m", end='\r')
            time.sleep(0.1)
        print("\n")
    
    def perform_existential_crisis(self):
        """Main performance with neurotic formatting"""
        # Clear screen (works on most terminals)
        print("\033[2J\033[H", end='')
        
        # Nervous opening
        print("\033[90m" + "─" * 60 + "\033[0m")
        print("\033[2;37mIt's just... I had this thought\033[0m")
        time.sleep(1)
        
        # The worry wave builds tension
        self._worry_wave()
        
        # Choose and display quote with neurotic formatting
        quote = self._get_random_quote()
        author = "─ Woody Allen (probably)"
        
        # Centered neurotic presentation
        term_width = 70
        quote_lines = quote.split('. ')
        
        print("\n")
        for i, line in enumerate(quote_lines):
            if i < len(quote_lines) - 1:
                line += "."
            padding = (term_width - len(line)) // 2
            if i == 0:
                self._neurotic_typewriter(" " * padding + line, "\033[36m", 0.05)
            else:
                self._neurotic_typewriter(" " * padding + line, "\033[36m", 0.04)
            time.sleep(0.3)
        
        time.sleep(0.8)
        
        # Doubtful attribution with jittery animation
        print("\n")
        for char in author:
            print(f"\033[90m{char}\033[0m", end='', flush=True)
            time.sleep(random.uniform(0.01, 0.08))
        print("\n")
        
        # Wavering underline
        underline = " " * ((term_width - len(author)) // 2) + "~" * len(author)
        for _ in range(3):
            for char in underline:
                print(f"\033[33m{char}\033[0m", end='', flush=True)
                time.sleep(0.02)
            print("\r", end='')
            time.sleep(0.1)
        print("\033[0m")
        
        # Final existential sigh
        time.sleep(0.5)
        print("\033[2;37m(Obviously none of this matters.)\033[0m")
        time.sleep(1)
        print("\033[90m" + "─" * 60 + "\033[0m")
        
        # Fade to black
        for i in range(5):
            print(f"\033[2J\033[H", end='')
            time.sleep(0.1)

if __name__ == "__main__":
    philosopher = WoodyAllenPhilosopher()
    philosopher.perform_existential_crisis()