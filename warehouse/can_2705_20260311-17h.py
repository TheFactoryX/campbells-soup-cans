"""
Campbell's Soup Can #2705
Produced: 2026-03-11 17:11:05
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

# ANSI color codes
COLORS = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'italic': '\033[3m',
    'yellow': '\033[38;5;226m',
    'cyan': '\033[38;5;45m',
    'magenta': '\033[38;5;201m',
    'green': '\033[38;5;118m',
    'red': '\033[38;5;196m',
    'blue': '\033[38;5;27m',
    'orange': '\033[38;5;208m',
    'purple': '\033[38;5;141m',
    'white': '\033[38;5;15m',
    'gray': '\033[38;5;244m'
}

# Woody Allen's existential angst in ASCII art
WOODY_ASCII = r"""
         _____
        /     \
       | () () |
        \  ^  /
         |||||
         |||||
"""

def slow_print(text, delay=0.03, color='yellow', end='\n'):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(f"{COLORS[color]}{char}{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(delay)
    print(end=end)

def neurotic_box(text):
    """Print text in a wobbly neurotic box"""
    width = len(text) + 10
    border_chars = ['-', '=', '~', '^', '*']
    
    # Randomly wobble the borders
    top_border = random.choice(border_chars) * width
    bottom_border = random.choice(border_chars) * width
    
    print(f"\n{COLORS['cyan']}{top_border}{COLORS['reset']}")
    print(f"{COLORS['cyan']}| {COLORS['white']}{text:^{width-2}} {COLORS['cyan']}|{COLORS['reset']}")
    print(f"{COLORS['cyan']}{bottom_border}{COLORS['reset']}\n")

def existential_crisis_animation():
    """Animate existential dread"""
    crisis_phrases = [
        "What is the meaning of it all?",
        "Why are we here?",
        "Is anyone else bothered by the sheer arbitrariness of existence?",
        "I'm overthinking this...",
        "Actually, never mind.",
        "Wait, what was the question?"
    ]
    
    for phrase in crisis_phrases:
        sys.stdout.write('\r' + ' ' * 80)
        sys.stdout.flush()
        sys.stdout.write(f'\r{COLORS["gray"]}{phrase}{COLORS["reset"]}')
        sys.stdout.flush()
        time.sleep(0.7)
    print()

def main():
    # Clear screen and show Woody
    print('\033[2J\033[H')
    
    # Print Woody with wobble
    for line in WOODY_ASCII.split('\n'):
        if line.strip():
            wobble = random.choice(['', COLORS['purple'], COLORS['orange']])
            print(f"{wobble}{line}{COLORS['reset']}")
        time.sleep(0.1)
    
    time.sleep(1)
    print()
    
    # Build quote dynamically with neurotic hesitations
    quote_parts = [
        "I've always been a firm believer",
        " that the only thing that separates",
        " us from the animals",
        " is our ability to",
        " overthink everything.",
        "",
        "I mean, look at a squirrel.",
        " It's just there, being a squirrel.",
        " No existential dread.",
        " No 3 AM panic attacks",
        " about the inevitable heat death",
        " of the universe.",
        "",
        "And don't get me started",
        " on the 'meaning of life'.",
        " I've spent decades",
        " contemplating it,",
        " only to realize",
        " I left the oven on.",
        "",
        "So here's my philosophy:",
        " Life is like a bad Allen film—",
        " 95% talking, 5% plot,",
        " and everyone's wearing",
        " tweed they don't understand.",
        "",
        "The secret?",
        " Embrace the absurdity.",
        " And maybe see a therapist.",
        " I have. 37 of them.",
        " One for each of my personalities.",
        "",
        "Final thought:",
        " If you're looking for meaning,",
        " you're looking in the wrong place.",
        " The meaning is",
        " there's no meaning.",
        " Isn't that liberating?",
        " No?",
        " Okay, fine.",
        " How about this:",
        " The meaning of life",
        " is to find the meaning",
        " you can stomach",
        " before the pizza gets cold.",
        "",
        "I'm not afraid of death;",
        " I just don't want to be there",
        " when it happens.",
        " That's someone else's problem.",
        " Preferably someone",
        " with a better sense of direction.",
        "",
        "And remember:",
        " If you think your problems are big,",
        " just remember",
        " there's a possum somewhere",
        " trying to file for unemployment",
        " because raccoons",
        " keep stealing its identity.",
        "",
        "Now if you'll excuse me,",
        " I have to go worry",
        " about something trivial",
        " to distract myself",
        " from the big things.",
        " Like whether I locked the door.",
        " (I didn't.)"
    ]
    
    # Randomly insert neurotic interruptions
    interruptions = [
        "[sigh]",
        "[fidgets]",
        "[checks watch]",
        "[adjusts glasses]",
        "[unrelated thought about pastrami]",
        "[wipes brow]",
        "[stares into middle distance]",
        "[mumbles]"
    ]
    
    full_quote = []
    for i, part in enumerate(quote_parts):
        if part.strip() and random.random() < 0.3 and i > 0:
            full_quote.append(random.choice(interruptions))
        if part:
            full_quote.append(part)
    
    # Print with dramatic pauses
    slow_print(f"{COLORS['bold']}Woody Allen's{COLORS['reset']} ", color='magenta', delay=0.08)
    time.sleep(0.5)
    slow_print(f"{COLORS['bold']}Philosophical Counsel:{COLORS['reset']}\n", color='orange', delay=0.06)
    time.sleep(1)
    
    # Type out the quote with random color changes
    current_line = ""
    for segment in full_quote:
        if segment.startswith('['):
            # Interruption in gray
            slow_print(f" {segment}", color='gray', delay=0.02)
            time.sleep(0.3)
        else:
            words = segment.split()
            for word in words:
                # Randomly change color for words
                word_color = random.choice(['yellow', 'cyan', 'green', 'orange', 'purple'])
                slow_print(f" {word}", color=word_color, delay=0.04)
                current_line += word + " "
                if len(current_line) > 50 and random.random() < 0.4:
                    print()
                    current_line = ""
                    time.sleep(0.2)
    
    # Final dramatic pause
    time.sleep(1)
    print()
    
    # Neurotic box with final line
    neurotic_box("...and that's why I can't eat at Subway anymore.")
    
    # Existential crisis animation
    print(f"{COLORS['italic']}Processing...{COLORS['reset']}")
    time.sleep(1)
    existential_crisis_animation()
    
    # Final disclaimer
    print(f"{COLORS['gray']}" + "─" * 60 + f"{COLORS['reset']}")
    slow_print("Disclaimer: No possums were harmed in the making of this quote.", 
               color='blue', delay=0.02)
    slow_print("Although one did give me a dirty look.", 
               color='red', delay=0.03)
    print(f"{COLORS['gray']}" + "─" * 60 + f"{COLORS['reset']}")
    
    # wobble exit
    for i in range(3):
        sys.stdout.write('\r' + ' ' * 80)
        sys.stdout.flush()
        time.sleep(0.1)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{COLORS['red']}[Interrupted by your own anxiety, no doubt]{COLORS['reset']}")
        sys.exit(0)