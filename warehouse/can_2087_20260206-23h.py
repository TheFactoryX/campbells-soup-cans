"""
Campbell's Soup Can #2087
Produced: 2026-02-06 23:41:59
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
import os
import random
from itertools import cycle

# Clear screen and hide cursor
os.system('cls' if os.name == 'nt' else 'clear')
sys.stdout.write("\033[?25l")
sys.stdout.flush()

# ANSI color codes
COLORS = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'italic': '\033[3m',
    'underline': '\033[4m',
    'blink': '\033[5m',
    'invert': '\033[7m',
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bright_black': '\033[90m',
    'bright_red': '\033[91m',
    'bright_green': '\033[92m',
    'bright_yellow': '\033[93m',
    'bright_blue': '\033[94m',
    'bright_magenta': '\033[95m',
    'bright_cyan': '\033[96m',
    'bright_white': '\033[97m',
    'bg_black': '\033[40m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_cyan': '\033[46m',
    'bg_white': '\033[47m',
}

# Woody Allen quote collection (custom generated)
WOODY_QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens. It's like my dentist says: 'This won't hurt a bit' - and then he lies through his teeth while drilling into my jaw.",
    "Life is divided into the horrible and the miserable. The horrible are the people with terminal illnesses. The miserable are everyone else. And it's all over much too soon, which is both a blessing and a curse.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying. But my agent keeps saying 'You're buried in options' - which is a weird thing to say to someone who's spiritually buried in existential dread.",
    "What a world. We live in a society where you can get a pizza delivered faster than an ambulance, and where my therapist's receptionist knows more about my childhood trauma than I do. Also, I'm pretty sure my goldfish is judging me.",
    "I can't make the moon be full, but I can be neurotic about it. I can't stop time, but I can spend hours worrying about it. And I certainly can't find meaning in the cosmos, but I can find meaning in whether to order the pastrami or the corned beef. The big questions are overrated."
]

class NeuroticDisplay:
    def __init__(self):
        self.width = os.get_terminal_size().columns
        self.quote = random.choice(WOODY_QUOTES)
        self.anxiety_level = 0
        
    def glitch_text(self, text, delay=0.02):
        """Display text with occasional glitches like Woody's nervous mind"""
        result = []
        for char in text:
            if random.random() < 0.1:  # 10% chance of glitch
                glitch_chars = [char, random.choice('!@#$%^&*()_+-=[]{}|;:,.<>?'), ' ']
                char = random.choice(glitch_chars)
            result.append(char)
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        return ''.join(result)
    
    def draw_neurotic_border(self, char='░', color='bright_yellow'):
        """Draw a nervous, wobbly border"""
        border = ''
        for i in range(self.width):
            if random.random() < 0.3:  # 30% chance of wobble
                border += random.choice(['░', '▒', '▓', '█', '▀', '▄', '─', '━', '│', '┃'])
            else:
                border += char
        print(f"{COLORS[color]}{border}{COLORS['reset']}")
    
    def type_with_hesitation(self, text, color='white', delay=0.05):
        """Type text with Woody-esque hesitation and backtracking"""
        i = 0
        while i < len(text):
            char = text[i]
            sys.stdout.write(f"{COLORS[color]}{char}{COLORS['reset']}")
            sys.stdout.flush()
            
            # Random hesitation (backspace and retype)
            if random.random() < 0.15 and i > 0:
                time.sleep(delay * 3)
                sys.stdout.write('\b \b')
                sys.stdout.flush()
                time.sleep(delay * 2)
                i -= 1  # Backtrack
                continue
                
            # Random pause for "thinking"
            if char in '.,;:!?':
                time.sleep(delay * random.uniform(2, 5))
            else:
                time.sleep(delay * random.uniform(0.5, 1.5))
            i += 1
    
    def create_thought_bubble(self, text):
        """Create a speech bubble like in a comic"""
        lines = []
        words = text.split()
        current_line = []
        
        for word in words:
            if sum(len(w) for w in current_line) + len(word) + len(current_line) <= self.width - 10:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))
            
        max_len = max(len(line) for line in lines)
        bubble_width = max_len + 6
        
        # Top of bubble
        print(f"    {COLORS['cyan']}┌{'─' * (bubble_width - 2)}┐{COLORS['reset']}")
        
        # Text lines
        for line in lines:
            padding = (bubble_width - 2 - len(line)) // 2
            print(f"    {COLORS['cyan']}│{COLORS['reset']}"
                  f"{COLORS['white']}{' ' * padding}{line}{' ' * (bubble_width - 2 - len(line) - padding)}{COLORS['reset']}"
                  f"{COLORS['cyan']}│{COLORS['reset']}")
        
        # Bottom of bubble with "tail"
        print(f"    {COLORS['cyan']}└{'─' * (bubble_width - 4)}┴──┘{COLORS['reset']}")
    
    def scroll_anxiety(self):
        """Display scrolling anxiety text at bottom"""
        anxiety_texts = [
            "Is this profound or just pretentious?",
            "Did I lock the door?",
            "My therapist will have thoughts on this.",
            "This too shall pass... hopefully.",
            "Am I overthinking this? (Yes.)",
            "I should have been a dentist.",
            "What's the point of anything?",
            "Maybe I should get a cat.",
            "I'm having a crisis of conscience.",
            "Is it too late to become a plumber?",
            "Why do I always pick the slow line?",
            "I hope no one noticed my existential panic."
        ]
        
        for text in cycle(anxiety_texts):
            padded = text.ljust(self.width)
            sys.stdout.write(f"\r{COLORS['dim']}{padded}{COLORS['reset']}")
            sys.stdout.flush()
            time.sleep(0.1)
            
            # Check for interrupt
            if sys.stdout in [sys.__stdout__]:  # Simplification
                continue
    
    def display(self):
        """Main display method"""
        try:
            # Animated title
            title = "WOODY ALLEN'S PHILOSOPHICAL CORNER (OR WHY WE'RE ALL JUST COMPLICATED BAGS OF WATER)"
            print("\n" * 2)
            for char in title:
                sys.stdout.write(f"{COLORS['bright_yellow']}{char}{COLORS['reset']}")
                sys.stdout.flush()
                time.sleep(0.02)
            print("\n")
            
            # Wobbly border
            for _ in range(3):
                self.draw_neurotic_border()
                time.sleep(0.1)
            
            # Thought bubble with quote
            self.create_thought_bubble(self.quote)
            print()
            
            # Type the quote with hesitation
            print(f"{COLORS['italic']}\"{COLORS['reset']}", end="")
            self.type_with_hesitation(self.quote, color='bright_white')
            print(f"{COLORS['italic']}\"{COLORS['reset']}\n")
            
            # Another wobbly border
            for _ in range(3):
                self.draw_neurotic_border()
                time.sleep(0.1)
            
            # Signature
            sig = "— Woody Allen (probably wishing he were somewhere else)"
            for char in sig:
                sys.stdout.write(f"{COLORS['dim']}{char}{COLORS['reset']}")
                sys.stdout.flush()
                time.sleep(0.03)
            print("\n")
            
            # Start anxiety scroll
            print(f"\n{COLORS['dim']}Press Ctrl+C to exit anxiety scroll...{COLORS['reset']}\n")
            self.scroll_anxiety()
            
        except KeyboardInterrupt:
            self._cleanup()
    
    def _cleanup(self):
        """Restore terminal state"""
        sys.stdout.write("\033[?25h")  # Show cursor
        sys.stdout.flush()
        print(f"\n\n{COLORS['yellow']}Remember: Nothing is so serious that it can't be made trivial by a well-timed joke.{COLORS['reset']}")
        print(f"{COLORS['dim']}— Program terminating (your existential dread may continue){COLORS['reset']}\n")

if __name__ == "__main__":
    display = NeuroticDisplay()
    display.display()