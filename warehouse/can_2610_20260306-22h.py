"""
Campbell's Soup Can #2610
Produced: 2026-03-06 22:47:53
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def clear_screen():
    """Clear terminal screen with ANSI code"""
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def typewriter(text, color_code='\033[97m', delay=0.03, end='\n'):
    """Print text with typewriter effect"""
    sys.stdout.write(color_code)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    sys.stdout.write('\033[0m' + end)
    sys.stdout.flush()

def philosophical_wave():
    """Create a wavy philosophical border"""
    border = ""
    for i in range(60):
        wave = int(10 * abs((i % 20) - 10) / 10)
        border += random.choice(['·', '⋅', '∘', '○', '°', '·'])[:1] * max(1, wave)
    return border[:60]

def main():
    clear_screen()
    
    # Woody Allen style quote (original)
    quote = (
        "I don't want to achieve immortality through my work. "
        "I want to achieve it through not dying. "
        "But then I think, what if the afterlife is just one long "
        "Woody Allen movie without the good parts? "
        "So I try to be present, which is difficult when you're "
        "constantly wondering if you left the oven on, "
        "and whether existential dread counts as a pre-existing condition."
    )
    
    # Visual presentation
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[95m', '\033[94m']
    reset = '\033[0m'
    
    # Animated opening
    for _ in range(3):
        sys.stdout.write('\033[?25l')  # Hide cursor
        for i in range(60):
            sys.stdout.write(f'\r{" " * i}🫠')
            sys.stdout.flush()
            time.sleep(0.02)
        sys.stdout.write('\r' + ' ' * 60 + '\r')
        sys.stdout.flush()
    sys.stdout.write('\033[?25h')  # Show cursor
    
    # Philosophical wave border
    wave_border = philosophical_wave()
    print(random.choice(colors) + wave_border + reset)
    
    # Centered title
    time.sleep(0.5)
    title = "✧ WOODY ALLEN ON EXISTENCE ✧"
    print('\033[3m' + title.center(60) + '\033[0m')
    print(philosophical_wave().center(60))
    time.sleep(1)
    
    # Main quote with alternating colors per sentence
    sentences = quote.split('. ')
    for i, sentence in enumerate(sentences):
        if i < len(sentences) - 1:
            sentence += '.'
        color = colors[i % len(colors)]
        
        # Animated quote display
        time.sleep(0.3)
        typewriter(sentence.center(58), color, delay=0.04)
    
    # Philosophical footer with reflection effect
    time.sleep(0.8)
    footer = "│ The universe is infinite, but my anxiety is more so. │"
    print()
    for _ in range(2):
        for i in range(len(footer)):
            if i % 2 == 0:
                sys.stdout.write('\033[2m')  # Dim
            else:
                sys.stdout.write('\033[0m')
            sys.stdout.write(footer[:i+1])
            sys.stdout.flush()
            time.sleep(0.005)
        sys.stdout.write('\033[0m\n')
        time.sleep(0.1)
    
    # Final animated border
    time.sleep(0.5)
    for _ in range(2):
        border_line = philosophical_wave()
        print(random.choice(colors) + border_line + reset)
        time.sleep(0.2)
    
    # Signature
    time.sleep(0.5)
    print('\033[2m' + "— an anxious thought, age 87 ½".rjust(60) + '\033[0m')
    time.sleep(1)
    print('\033[0;90m' + "[Press Enter to contemplate further...]" + '\033[0m')
    input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[93m∅ Even interruption is a philosophical statement ∅\033[0m")
        sys.exit(0)