"""
Campbell's Soup Can #2488
Produced: 2026-02-28 17:34:55
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

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSED = '\033[7m'

def typewriter(text, color=Colors.OKCYAN, delay=0.03, jitter=False):
    """Typewriter effect with optional jitter for neurotic feel"""
    for char in text:
        if jitter and random.random() > 0.8:
            sys.stdout.write(random.choice([' ', '\b', '']))
            sys.stdout.flush()
            time.sleep(0.01)
        sys.stdout.write(f"{color}{char}{Colors.ENDC}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01) if jitter else delay)
    print()

def neurotic_spinner(duration=2):
    """An anxious loading animation"""
    spinners = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    start = time.time()
    i = 0
    while time.time() - start < duration:
        sys.stdout.write(f'\r{Colors.WARNING}Thinking too hard{Colors.ENDC} {spinners[i % len(spinners)]}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\r' + ' ' * 30 + '\r')
    sys.stdout.flush()

def existential_box():
    """Draw a fancy box around the quote"""
    print(f"{Colors.HEADER}{'═' * 60}{Colors.ENDC}")
    print(f"{Colors.HEADER}║{' ' * 58}║{Colors.ENDC}")
    
    # Intro line
    neurotic_spinner(1.5)
    intro = "After careful consideration of my mortality, I've concluded:"
    typewriter(f"{Colors.BOLD}{' ' * 2}{intro}{Colors.ENDC}", Colors.OKBLUE, 0.02)
    print()
    
    # Main quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    typewriter(f"{Colors.BOLD}{' ' * 2}{quote}{Colors.ENDC}", Colors.FAIL, 0.04, jitter=True)
    
    # Add neurotic footnotes
    print()
    footnotes = [
        "(This thought kept me awake for 3.7 minutes last Tuesday)",
        "(I ran the numbers. Statistically, I'm already dead somewhere.)",
        "(My therapist says I should embrace the void. I said 'Which void?')"
    ]
    footnote = random.choice(footnotes)
    typewriter(f"{Colors.WARNING}{' ' * 4}• {footnote}{Colors.ENDC}", Colors.WARNING, 0.015)
    
    print()
    print(f"{Colors.HEADER}║{' ' * 58}║{Colors.ENDC}")
    print(f"{Colors.HEADER}{'═' * 60}{Colors.ENDC}")
    
    # Signature
    time.sleep(0.5)
    sig = "— Woody Allen (probably misattributed)"
    typewriter(f"{Colors.OKGREEN}{' ' * 15}{sig}{Colors.ENDC}", Colors.OKGREEN, 0.01)

def cosmic_dust():
    """Add some floating cosmic dust particles"""
    for _ in range(3):
        x = random.randint(5, 55)
        dust = random.choice(['·', '•', '∘', '⁕', '⁌'])
        color = random.choice([Colors.OKCYAN, Colors.OKBLUE, Colors.WARNING])
        print(f"\033[{x}G{color}{dust}{Colors.ENDC}", end='', flush=True)
        time.sleep(0.1)
    print()

def main():
    # Clear screen (works on most terminals)
    print("\033[2J\033[H", end='')
    
    # Header with some drama
    cosmic_dust()
    time.sleep(0.5)
    
    header = "PHILOSOPHICAL INSIGHTS FROM A NEUROTIC MIND"
    print(f"{Colors.HEADER}{Colors.BOLD}{header.center(60)}{Colors.ENDC}\n")
    
    time.sleep(1)
    existential_box()
    
    # Post-script with another dimension
    time.sleep(1)
    cosmic_dust()
    print()
    typewriter(f"{Colors.REVERSED}{' ' * 10}Existential dread is just anxiety with a philosophy degree.{' ' * 10}{Colors.ENDC}", 
               Colors.HEADER, 0.02)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.FAIL}Too much philosophy? Just like life, abruptly terminated.{Colors.ENDC}")
        sys.exit(0)