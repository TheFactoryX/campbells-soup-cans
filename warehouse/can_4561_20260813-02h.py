"""
Campbell's Soup Can #4561
Produced: 2026-08-13 02:47:00
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen's Existential Crisis Generator
A neurotic little program that ponders the absurdity of existence
while making snarky comments about its own mortality.
"""

import sys
import time
import random
from typing import List, Tuple

# ANSI color codes because even despair has aesthetic preferences
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"

def typewriter(text: str, delay: float = 0.03, color: str = Colors.CYAN) -> None:
    """Prints text with a typewriter effect because anxiety builds slowly."""
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(delay if char not in '.!?;:' else delay * 2)
    print()

def panic_print(text: str, colors: List[str] = [Colors.RED, Colors.YELLOW, Colors.MAGENTA]) -> None:
    """Prints text flickering between panicked colors."""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(f"{color}{char}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def draw_neurotic_character() -> None:
    """Draws a little ASCII character having an existential crisis."""
    character_art = f"""
    {Colors.MAGENTA}          .--.
         |o_o |    {Colors.YELLOW}"Of course I'm depressed,
         |:_/ |     {Colors.CYAN}I mean, have you SEEN
        //   \\ \\    {Colors.MAGENTA}the state of this world?"
       |(||,||) )   {Colors.RED}- Spalding, probably{Colors.RESET}
      /''\\_/''\\_/  
      \\"""---'''{Colors.BOLD}{Colors.DIM}...{Colors.RESET}
    """
    print(character_art)

def draw_thought_bubble(text: str) -> None:
    """Draws a thought bubble around text because overthinking requires containers."""
    border = "=" * 60
    print(f"\n{Colors.BLUE}{border}")
    print(f"║ {text:^56} ║")
    print(f"{border}{Colors.RESET}\n")

def animate_quote(quote: str) -> None:
    """Animates the quote with dramatic flair."""
    # First, the build-up
    typewriter("You ever think about...", delay=0.08, color=Colors.DIM)
    time.sleep(0.5)
    
    # Then the existential dread
    typewriter("The sheer cosmic insignificance...", delay=0.06, color=Colors.YELLOW)
    time.sleep(0.7)
    
    # Then panic
    typewriter("Oh wait, I do that every morning!", delay=0.04, color=Colors.RED)
    time.sleep(0.3)
    
    print()
    
    # The actual quote (the punchline)
    panic_print(quote)
    
    # Pause for reflection (or nervous sweating)
    time.sleep(1)
    
    # Self-deprecating follow-up
    typewriter("But hey, at least I'm consistent in my inconsistency.", 
               delay=0.05, color=Colors.GREEN)

def main() -> None:
    """Main function that brings existential dread to your terminal."""
    # Clear screen (optional, but dramatic)
    print("\033[2J\033[H", end="")
    
    # Welcome with anxiety
    draw_thought_bubble("Welcome to your existential crisis.")
    
    # Introduce the character
    draw_neurotic_character()
    
    # Some nervous pacing
    typewriter("*nervously adjusts glasses*", delay=0.15, color=Colors.DIM)
    time.sleep(0.3)
    
    # The quote - a genuine Woody Allen-style masterpiece
    quote = ("I'm not terrified of the void staring back, "
             "I'm terrified it'll give me a rating of 3 stars "
             "and say 'Could try harder.'")
    
    # Animate delivery
    animate_quote(quote)
    
    # Closing flourish
    print()
    time.sleep(0.5)
    typewriter("..." + " Thanks for listening. I'll be here all week.", 
               delay=0.08, color=Colors.ITALIC + Colors.CYAN)
    time.sleep(0.5)
    
    # Final existential bow
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}")
    print("    .--.")
    print("   (    )")
    print("   |    |   Existential crisis concluded.")
    print("   (o  o)   Please rate your suffering 1-10.")
    print("    \\//   The operator is deeply unsatisfied.")
    print("     \\/    with his life choices.{Colors.RESET}")
    
    print(f"\n{Colors.DIM}Runtime anxiety level: MAXIMUM{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Even your interruption is a metaphor for premature endings!{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}My neurotic programming has crashed - proving once again{Colors.RESET}")
        print(f"{Colors.RED}that we're all just fragile collections of buggy code.{Colors.RESET}")
        print(f"{Colors.DIM}Error: {e}{Colors.RESET}")