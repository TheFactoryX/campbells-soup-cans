"""
Campbell's Soup Can #5251
Produced: 2026-11-17 04:28:57
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    NEUROTIC_BLUE = '\033[94m'
    ANXIOUS_YELLOW = '\033[93m'
    DEPRESSIVE_CYAN = '\033[96m'
    PARANOID_MAGENTA = '\033[95m'
    EXISTENTIAL_RED = '\033[91m'
    BACKGROUND_BLUE = '\033[44m'
    BACKGROUND_YELLOW = '\033[43m'

def print_slow(text, delay=0.03, color=Colors.RESET, end='\n'):
    """Print text character by character with a delay"""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print(end, end='')

def type_effect(text, delay=0.05):
    """Type effect for the quote"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def create_anxiety_border(width=60):
    """Create a border that looks like nervous hand-drawn lines"""
    border = ""
    for i in range(width):
        if i % 10 == 0:
            border += "～"  # Wavy line for anxiety
        elif i % 5 == 0:
            border += "—"  # Dash for uncertainty
        else:
            border += "—"  # Regular dash
    return border

def woody_allen_quote():
    """Display a Woody Allen style quote with neurotic flair"""
    
    # Clear screen for dramatic effect
    print("\033[2J\033[H", end="")
    
    # Title with existential dread
    print(Colors.BACKGROUND_BLUE + Colors.BOLD + " " * 60 + Colors.RESET)
    print(Colors.BACKGROUND_BLUE + Colors.BOLD + "                    A WOODY ALLEN PHILOSOPHICAL MUSING" + Colors.RESET)
    print(Colors.BACKGROUND_BLUE + Colors.BOLD + " " * 60 + Colors.RESET)
    print()
    
    # Neurotic introduction
    print_slow("You know, I was thinking about this existential crisis I'm having...", 
                delay=0.04, color=Colors.ANXIOUS_YELLOW)
    print_slow("It's not really about the meaning of life - that's too simple.", 
                delay=0.04, color=Colors.ANXIOUS_YELLOW)
    print_slow("It's more about whether I left the oven on, and if that even matters in the grand scheme.", 
                delay=0.04, color=Colors.ANXIOUS_YELLOW)
    print()
    
    # Draw anxious border
    border = create_anxiety_border()
    print(Colors.NEUROTIC_BLUE + border + Colors.RESET)
    print(Colors.NEUROTIC_BLUE + "|" + " " * 58 + "|" + Colors.RESET)
    print(Colors.NEUROTIC_BLUE + "|" + " " * 58 + "|" + Colors.RESET)
    
    # The actual quote with dramatic typing effect
    quote = [
        "",
        "I'm not afraid of death, I'm just not keen on the whole dying process.",
        "I mean, one minute you're here, worrying about whether you should",
        "have ordered the pastrami or the turkey - because let's face it,",
        "the turkey is always a disappointment - and the next thing you know,",
        "you're somewhere else, probably with a very disappointed look on your face.",
        "",
        "The real tragedy isn't that life is short, it's that it's long enough",
        "to realize you've spent most of it being anxious about the wrong things.",
        "Like whether people like you, or if you're successful, or if you're",
        "going to be alone forever because you're too neurotic to commit to",
        "a relationship, but then again, relationships are just two people",
        "agreeing to tolerate each other's quirks until one of them dies first.",
        "",
        "So I guess what I'm saying is: embrace the absurdity, but also",
        "maybe call your therapist, because you're clearly not handling",
        "the existential dread very well. But then again, who does?",
        ""
    ]
    
    for line in quote:
        if line == "":
            print()
        else:
            print_slow(line, delay=0.02, color=Colors.EXISTENTIAL_RED)
    
    # Closing border
    print(Colors.NEUROTIC_BLUE + "|" + " " * 58 + "|" + Colors.RESET)
    print(Colors.NEUROTIC_BLUE + "|" + " " * 58 + "|" + Colors.RESET)
    print(Colors.NEUROTIC_BLUE + border + Colors.RESET)
    print()
    
    # Post-quote existential crisis
    print_slow("But wait, am I even qualified to give philosophical advice?", 
                delay=0.05, color=Colors.PARANOID_MAGENTA)
    print_slow("I mean, I can't even keep a houseplant alive, and now I'm", 
                delay=0.05, color=Colors.PARANOID_MAGENTA)
    print_slow("talking about the meaning of life? This is probably just", 
                delay=0.05, color=Colors.PARANOID_MAGENTA)
    print_slow("another one of my delusions of grandeur. But hey, at least", 
                delay=0.05, color=Colors.PARANOID_MAGENTA)
    print_slow("I'm delusional in a somewhat entertaining way, right?", 
                delay=0.05, color=Colors.PARANOID_MAGENTA)
    print()
    
    # Final neurotic sign-off
    print(Colors.ITALIC + Colors.DEPRESSIVE_CYAN + 
          "— Woody Allen's Anxiety, probably while checking if he locked the door for the third time today" + 
          Colors.RESET)
    print()
    
    # Blinking cursor for existential uncertainty
    for _ in range(3):
        print(Colors.ANXIOUS_YELLOW + "But what if... what if there's no meaning at all?" + Colors.RESET)
        time.sleep(1)
        print("\033[2K\033[1G", end="")  # Clear line and go to beginning
        time.sleep(0.5)
    
    print(Colors.ANXIOUS_YELLOW + "But what if... what if there's no meaning at all? Well, that's what I think about at 3 AM." + Colors.RESET)

if __name__ == "__main__":
    try:
        woody_allen_quote()
    except KeyboardInterrupt:
        print("\n" + Colors.EXISTENTIAL_RED + 
              "Oh great, now you're interrupting my existential crisis. Very typical." + Colors.RESET)
        sys.exit(0)