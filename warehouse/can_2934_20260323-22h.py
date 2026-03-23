"""
Campbell's Soup Can #2934
Produced: 2026-03-23 22:51:46
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

class WoodyAllenPhilosopher:
    def __init__(self):
        self.quotes = [
            "I'm not afraid of death; I just don't want to be there when it happens.",
            "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
            "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
            "I was born at a very early age. I remember the experience vividly, though I've tried to forget it ever since.",
            "I'm not against religion, but I do think it's a crutch for people who can't handle the fact that we're all going to die.",
            "I told my therapist that I have a fear of commitment. She said, 'You mean to relationships?' I said, 'No, to any kind of decision. Even choosing what to have for lunch causes me existential dread.'",
            "I'm not lazy, I'm in energy-saving mode. The universe is expanding, and eventually everything will be so far apart that it won't matter if I make my bed.",
            "I'm not.a vegetarian because I love animals. I'm a vegetarian because I hate plants.",
            "The difference between sex and death is, with death you can do it alone and nobody calls you a pervert.",
            "I don't believe in the afterlife, but I'm taking a change of underwear just in case."
        ]
        
        self.colors = [
            '\033[91m',  # Red
            '\033[93m',  # Yellow
            '\033[92m',  # Green
            '\033[96m',  # Cyan
            '\033[95m',  # Magenta
            '\033[94m',  # Blue
        ]
        self.reset = '\033[0m'
        self.bold = '\033[1m'
        
    def dramatic_entrance(self):
        """Create a dramatic entrance with animated text"""
        stages = [
            "    .--.",
            "    |o_o |",
            "    |:_/ |",
            "   //   \\ \\",
            "  (|     | )",
            " /'\\_   _/`\\",
            " \\___)=(___/",
            "",
            "   🎭 WOODY ALLEN'S PHILOSOPHY 🎭"
        ]
        
        for stage in stages:
            print(f"\033[2J\033[H", end='')  # Clear screen
            for line in stages[:stages.index(stage)+1]:
                print(self.colors[4] + self.bold + line + self.reset)
            time.sleep(0.15)
        time.sleep(1)
    
    def typewriter_effect(self, text, color, delay=0.03):
        """Type out text with random minor pauses for human-like effect"""
        for char in text:
            sys.stdout.write(color + char + self.reset)
            sys.stdout.flush()
            # Random tiny pauses for "neurotic" typing rhythm
            time.sleep(delay + random.uniform(-0.01, 0.02))
        print()
    
    def create_quote_box(self, quote):
        """Create a fancy ASCII art box around the quote"""
        # Remove ANSI codes to calculate actual text length
        clean_quote = ''.join([c for c in quote if 32 <= ord(c) <= 126])
        width = min(70, max(50, len(clean_quote) + 10))
        
        box_top = self.colors[2] + "╔" + "═" * (width-2) + "╗" + self.reset
        box_bottom = self.colors[2] + "╚" + "═" * (width-2) + "╝" + self.reset
        
        print()
        print(box_top)
        
        # Split quote into lines
        words = clean_quote.split()
        lines = []
        current_line = []
        current_len = 0
        
        for word in words:
            if current_len + len(word) + (1 if current_line else 0) <= width - 6:
                current_line.append(word)
                current_len += len(word) + (1 if current_line else 0)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_len = len(word)
        if current_line:
            lines.append(' '.join(current_line))
        
        for line in lines:
            padding = width - 6 - len(line)
            left_pad = padding // 2
            right_pad = padding - left_pad
            
            # Random color for each line
            line_color = random.choice(self.colors[:3])
            brag_color = random.choice(self.colors[3:])
            
            print(self.colors[2] + "║" + self.reset, end='')
            print(' ' * left_pad, end='')
            self.typewriter_effect(line, line_color, 0.02)
            print(' ' * right_pad + self.colors[2] + "║" + self.reset)
        
        print(box_bottom)
        
    def existential_crisis(self):
        """Create a mini-crisis animation before the quote"""
        crisis_phrases = [
            "What's the point?",
            "Why are we here?",
            "Is anyone listening?",
            "Does anyone care?",
            "What's it all mean?",
            "I should have been a dentist..."
        ]
        
        for phrase in crisis_phrases:
            print(f"\r{self.colors[1]}{phrase}{self.reset}", end='')
            sys.stdout.flush()
            time.sleep(0.3)
            print('\r' + ' ' * 40, end='')
        print('\r', end='')
    
    def deliver_quote(self):
        """Main delivery method with dramatic flair"""
        self.dramatic_entrance()
        
        print("\n" + self.colors[3] + "🧠 CONNECTING TO EXISTENTIAL HOTLINE... " + self.reset)
        time.sleep(1)
        
        self.existential_crisis()
        time.sleep(0.5)
        
        quote = random.choice(self.quotes)
        
        print("\n" + self.colors[0] + self.bold + "📞 INCOMING TRANSMISSION:" + self.reset)
        time.sleep(1)
        
        self.create_quote_box(quote)
        
        print("\n" + self.colors[4] + "💡 " + self.reset, end='')
        self.typewriter_effect("(press any key to accept your existential dread)", 
                              self.colors[5], 0.01)
        
        try:
            input()
        except:
            pass
        
        # Final fade out
        print("\n" + self.colors[1] + "☠️  Remember: The universe is expanding, but your problems are local. ☠️" + self.reset)
        time.sleep(2)
        print("\033[2J\033[H", end='')  # Clear screen on exit

if __name__ == "__main__":
    philosopher = WoodyAllenPhilosopher()
    philosopher.deliver_quote()