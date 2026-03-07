"""
Campbell's Soup Can #2619
Produced: 2026-03-07 10:42:20
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
            "What a cruel joke the universe played: that we should yearn for meaning in a cosmos that doesn't care if we live or die.",
            "I took a class on anxiety and it was standing-room only. In fact, it was so crowded, I had to stand outside.",
            "If my wife ever realized how little I think about her, she'd be deeply hurt. And she'd be right.",
            "The difference between sex and death is: with death you can do it alone and nobody complains.",
            "I don't believe in the afterlife, but I'm taking clean underwear just in case I'm wrong."
        ]
        
    def _slow_print(self, text, delay=0.03, color_code='\033[93m'):
        """Print text with typewriter effect and color"""
        reset = '\033[0m'
        for char in text:
            sys.stdout.write(f"{color_code}{char}{reset}")
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def _draw_neurotic_box(self, width=60):
        """Draw an intentionally wobbly box"""
        chars = ['┌', '┐', '└', '┘', '─', '│', '╱', '╲']
        top = chars[0] + chars[4] * (width-2) + chars[1]
        bottom = chars[2] + chars[4] * (width-2) + chars[3]
        middle = chars[5] + ' ' * (width-2) + chars[5]
        return top, middle, bottom
    
    def present_wisdom(self):
        """Present the quote with maximum neurotic flair"""
        # Clear screen with dramatic effect
        sys.stdout.write('\033[2J\033[H')
        
        # Choose random quote
        quote = random.choice(self.quotes)
        
        # Calculate dynamic width
        base_width = min(80, max(40, len(quote) + 10))
        wobble = random.choice([-1, 0, 1])
        width = base_width + wobble
        
        # Draw the box
        top, middle, bottom = self._draw_neurotic_box(width)
        
        # Color schemes
        border_color = '\033[36m'  # Cyan for neurotic tension
        quote_color = '\033[93m'   # Yellow for existential dread
        accent_color = '\033[95m'  # Magenta for drama
        
        print()
        
        # Anxious preamble
        preamble = random.choice([
            "After 47 years of therapy, I've concluded...",
            "My analyst says I should share this...",
            "Between you and me and the lamppost...",
            "I had this thought while waiting for my hypochondria diagnosis..."
        ])
        
        # Print preamble with varying speed
        for i, char in enumerate(preamble):
            speed = 0.02 if char in ',.!' else 0.04
            sys.stdout.write(f"\033[2m{char}\033[0m")
            sys.stdout.flush()
            time.sleep(speed * (1 + (i % 3) * 0.2))
        print("\n")
        
        # Print top border with micro-hesitations
        for char in top:
            sys.stdout.write(f"{border_color}{char}\033[0m")
            sys.stdout.flush()
            time.sleep(0.01)
        print()
        
        # Print middle with text
        print(f"{border_color}{middle[0]}\033[0m", end='')
        
        # Centered quote with breathing room
        padding = (width - 2 - len(quote)) // 2
        print(' ' * padding, end='')
        
        # Typewriter effect with random pauses (neurotic rhythm)
        for i, char in enumerate(quote):
            sys.stdout.write(f"{quote_color}{char}\033[0m")
            sys.stdout.flush()
            # Random pause for dramatic/neurotic effect
            if char in ',;:' or random.random() < 0.15:
                time.sleep(random.uniform(0.08, 0.2))
            else:
                time.sleep(0.03)
            # Occasional backtracking (like he's second-guessing)
            if random.random() < 0.03 and i > 5:
                backspace = '\b \b'
                sys.stdout.write(backspace)
                sys.stdout.flush()
                time.sleep(0.1)
                sys.stdout.write(f"{quote_color}{char}\033[0m")
                sys.stdout.flush()
        print()
        
        # Print bottom of box
        for char in bottom:
            sys.stdout.write(f"{border_color}{char}\033[0m")
            sys.stdout.flush()
            time.sleep(0.01)
        print()
        
        # Dramatic attribution
        time.sleep(0.5)
        print(f"\n{accent_color}— Woody Allen, probably{reset} ", end='')
        # Blinking effect (some terminals support it)
        for _ in range(3):
            sys.stdout.write('\033[5m.\033[0m')
            sys.stdout.flush()
            time.sleep(0.3)
        print("\n")
        
        # Final neurotic note
        time.sleep(0.7)
        footnote = random.choice([
            "(I'm available for bar mitzvahs and existential crises.)",
            "(This quote brought to you by my therapist's yacht.)",
            "(My mother would be so disappointed.)",
            "(I'm not okay, and neither is this quote.)"
        ])
        
        for char in footnote:
            sys.stdout.write(f"\033[2m{char}\033[0m")
            sys.stdout.flush()
            time.sleep(0.02)
        print("\n")
        
        # Dramatic pause before exit
        time.sleep(1)
        print(f"{border_color}No further questions.\033[0m\n")

def main():
    try:
        philosopher = WoodyAllenPhilosopher()
        philosopher.present_wisdom()
    except KeyboardInterrupt:
        print("\n\n\033[91mTypical. I was just getting to the good part.\033[0m")
        sys.exit(0)

if __name__ == "__main__":
    main()