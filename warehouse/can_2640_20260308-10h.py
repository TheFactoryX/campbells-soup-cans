"""
Campbell's Soup Can #2640
Produced: 2026-03-08 10:44:14
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
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03, color=None):
    """Print text with typewriter effect and optional color."""
    for char in text:
        if color:
            sys.stdout.write(color + char + '\033[0m')
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def wobble_text(text, wobble_chars=['.', ',', '!', '?', ';'], max_wobble=2):
    """Add random wobble characters to text."""
    result = []
    for char in text:
        result.append(char)
        if char == ' ' and random.random() < 0.1:
            result.append(random.choice(wobble_chars) * random.randint(1, max_wobble))
    return ''.join(result)

def draw_wooden_frame():
    """Draw a Woody Allen-esque wooden picture frame."""
    frame = [
        "          ╭───────────────────────────────╮          ",
        "          │                               │          ",
        "          │    WOODY ALLEN'S PHILOSOPHY   │          ",
        "          │         (Unvarnished)         │          ",
        "          │                               │          ",
        "          ╰───────────────────────────────╯          "
    ]
    for line in frame:
        print(f"\033[38;5;178m{line}\033[0m")  # Wood brown color

def existential_crisis_animation():
    """Animate an existential crisis with bouncing dots."""
    crisis_states = [
        "   o   ",
        "  o o  ",
        " o   o ",
        "o     o",
        " o   o ",
        "  o o  ",
        "   o   ",
        "    o  ",
        "     o ",
        "      o"
    ]
    for _ in range(3):
        for state in crisis_states:
            sys.stdout.write(f"\r\033[38;5;21mExistential dread: {state}\033[0m")
            sys.stdout.flush()
            time.sleep(0.1)
        print()

def main():
    clear_screen()
    
    # Woody Allen style quotes (original creation)
    woody_quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens. "
        "It's like the ultimate party you're forced to attend, and everyone's "
        "congratulating you on your excellent performance in the preceding act.",

        "Life is divided into the horrible and the miserable. The horrible are "
        "the terminal cases, the people with diseases. The miserable are everyone "
        "else. I'm miserable. You're miserable. We're all in this together.",

        "I don't want to achieve immortality through my work. I want to achieve "
        "it through not dying. That seems like a more reliable method, though "
        "admittedly less impressive at cocktail parties.",

        "What if everything is an illusion and nothing exists? In that case, I "
        "definitely overpaid for my carpet. Also, my therapist's yacht seems "
        "suspiciously real.",

        "I don't believe in an afterlife, but then again, I'm not exactly "
        "knocking on heaven's door. I'm more like hiding behind the curtains, "
        "hopping they don't notice me and just go away."
    ]
    
    quote = random.choice(woody_quotes)
    
    # Draw decorative frame
    draw_wooden_frame()
    print()
    
    # Animate existential crisis
    existential_crisis_animation()
    print()
    
    # Print the quote with dramatic formatting
    print("\033[38;5;226m" + "╭" + "─" * 68 + "╮" + "\033[0m")
    print("\033[38;5;226m│\033[0m" + " " * 68 + "\033[38;5;226m│\033[0m")
    
    # Center the quote with wobble effect
    centered_quote = wobble_text(quote)
    padding = (70 - len(centered_quote)) // 2
    formatted_quote = " " * padding + centered_quote
    
    # Print quote with alternating colors for dramatic effect
    for i, char in enumerate(formatted_quote):
        if i % 7 == 0:
            color = "\033[38;5;201m"  # Pink
        elif i % 5 == 0:
            color = "\033[38;5;45m"   # Cyan
        elif i % 3 == 0:
            color = "\033[38;5;226m"  # Yellow
        else:
            color = "\033[38;5;15m"   # White
        sys.stdout.write(color + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(0.01)
    print()
    
    print("\033[38;5;226m│\033[0m" + " " * 68 + "\033[38;5;226m│\033[0m")
    print("\033[38;5;226m╰" + "─" * 68 + "╯\033[0m")
    print()
    
    # Dramatic signature
    slow_print("\033[38;5;244m— Woody Allen (probably while avoiding a social engagement)\033[0m", 
               delay=0.05)
    
    # Final existential flourish
    time.sleep(1)
    print()
    slow_print("\033[38;5;242m[Pause for nervous laughter]\033[0m", delay=0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[38;5;196m☠️  Existential crisis interrupted. How fitting.\033[0m")
        sys.exit(0)