"""
Campbell's Soup Can #3667
Produced: 2026-05-13 20:54:35
Worker: Arcee AI: Trinity Large Thinking (free) (arcee-ai/trinity-large-thinking:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A visually creative Woody Allen style philosophical quote generator.
Features: ANSI colors, ASCII art, typing animation, and a neurotic existential crisis.
"""

import sys
import time
import random

def typewriter(text, color_code="\033[93m", delay=0.03):
    """Simulates a typewriter effect with color."""
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_woody_face():
    """ASCII art of Woody Allen's face (neurotic and thoughtful)."""
    print("\033[95m" + r"""
          /////
        ///////      
       |o  o  |
       |  >  |
       | \___/
       |  \  
       |  |\
       |  | \
       |  |  \
       |  |   \
       |  |    \   \033[93m
       |  |     \   \033[96m
       \____/\_/\_/\_
    """ + "\033[0m")

def main():
    # Woody Allen style quotes (neurotic, existential, self-deprecating)
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens. Actually, I'm more afraid of being alive when I'm dead.",
        "Life is divided into the horrible and the miserable. The horrible are like terminal cases, you know, blind people, crippled. The miserable are everyone else. So you should be thankful you're miserable.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying. So far, my work is winning.",
        "I took a test in Existentialism. I left all the answers blank and got 100. The professor said I had captured the essence of the absurd perfectly.",
        "My brain? It's my second favorite organ. My first favorite is my liver, because it processes all the alcohol I drink to cope with my brain.",
        "Why are our days numbered and not, say, lettered? I'd prefer a nice alphabetical progression. It would be less final.",
        "I was thrown out of college for cheating on the metaphysics exam. I looked into the soul of the boy sitting next to me.",
        "The universe is merely a fleeting idea in God's mind—which is really depressing when you've just made a down payment on a house."
    ]

    # Random selection with a dramatic pause
    print("\033[96m" + "="*60)
    print("      WOODY ALLEN EXISTENTIAL CRISIS GENERATOR")
    print("="*60 + "\033[0m")
    time.sleep(1)
    
    print("\n🧠  Initiating neurotic thought process...")
    time.sleep(0.7)
    
    # Draw Woody's face
    draw_woody_face()
    time.sleep(0.5)
    
    # Select and display quote
    quote = random.choice(quotes)
    
    # Typewriter effect for the quote
    print("\n" + "\033[95m" + "═" * 60 + "\033[0m")
    typewriter(f" '{quote}' ", color_code="\033[93m", delay=0.02)
    print("\033[95m" + "═" * 60 + "\033[0m\n")
    
    # Post-quote existential commentary
    reactions = [
        " (I need a therapist immediately.)",
        " (This is why I can't go to parties.)",
        " (Pass the Xanax.)",
        " (I'll be in the bathroom rethinking my life choices.)",
        " (My mother was right about everything.)"
    ]
    print(f"\033[91m{random.choice(reactions)}\033[0m")
    
    # Final dramatic exit
    print("\n" + "\033[90m" + "  [System shutting down due to overwhelming existential dread...]" + "\033[0m")
    time.sleep(2)
    print("\033[96m" + "\n   Remember: The only thing we have to fear is fear itself... and maybe spiders." + "\033[0m")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[91m" + "  (Interrupted mid-existential crisis. How fitting.)" + "\033[0m")
        sys.exit(0)