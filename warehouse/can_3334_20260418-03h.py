"""
Campbell's Soup Can #3334
Produced: 2026-04-18 03:30:20
Worker: MoonshotAI: Kimi K2.5 (moonshotai/kimi-k2.5)
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

# ANSI Color Palette - Vintage Cinema Style
class C:
    AMBER = '\033[38;5;214m'      # Old projector amber
    RED = '\033[91m'              # Anxiety red
    CYAN = '\033[96m'             # Clinical blue
    DIM = '\033[2m'               # Faded film
    BOLD = '\033[1m'              # Emphasis
    ITALIC = '\033[3m'            # Internal monologue
    RESET = '\033[0m'             # Back to reality
    CLEAR = '\033[2J\033[H'       # Wipe the slate

def anxious_typewriter(text, base_delay=0.05):
    """
    Types with neurotic precision: occasional stutters, 
    anxiety flashes, and jittery timing
    """
    for i, char in enumerate(text):
        # Random anxiety attack (10% chance)
        if random.random() < 0.1 and char != ' ':
            # Flash of panic
            sys.stdout.write(f"{C.RED}█{C.RESET}")
            sys.stdout.flush()
            time.sleep(0.15)
            sys.stdout.write('\b \b')  # Erase panic
            sys.stdout.flush()
            time.sleep(0.08)
        
        # Jittery typing speed (faster when anxious)
        jitter = random.uniform(-0.03, 0.08)
        delay = max(0.02, base_delay + jitter)
        
        # Occasional bold emphasis on random words
        if random.random() < 0.05 and char.isalpha():
            sys.stdout.write(f"{C.BOLD}{C.AMBER}{char}{C.RESET}")
        else:
            sys.stdout.write(f"{C.AMBER}{char}{C.RESET}")
        
        sys.stdout.flush()
        time.sleep(delay)
    
    print()  # New line at end

def flicker_effect():
    """Simulates old projector flickering"""
    for _ in range(2):
        time.sleep(0.4)
        sys.stdout.write(f"{C.DIM}    *projector whirring*{C.RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write('\r' + ' ' * 25 + '\r')
        sys.stdout.flush()

def print_cinema_frame():
    """Vintage film leader aesthetic"""
    reel_num = random.randint(1920, 1980)  # Woody era
    frame = f"""
{C.DIM}╔{'═'*60}╗{C.RESET}
{C.DIM}║{C.RESET}  {C.CYAN}🎬  CINEMA PARADOX  #{reel_num}  [NEUROTIC VISIONS]{C.RESET}      {C.DIM}║{C.RESET}
{C.DIM}╠{'═'*60}╣{C.RESET}"""
    print(frame)

def print_footer():
    """Closing credits with anxiety meter"""
    anxiety = random.randint(94, 100)
    footer = f"""{C.DIM}╠{'═'*60}╣{C.RESET}
{C.DIM}║{C.RESET}  {C.RED}⚠ ANXIETY LEVEL: {anxiety}% {C.RESET}                    {C.CYAN}[THE END ?]{C.RESET}  {C.DIM}║{C.RESET}
{C.DIM}╚{'═'*60}╝{C.RESET}"""
    print(footer)

# The Philosophy
QUOTE = "I'm not afraid of death; I just don't want to be there when it happens. I've asked my therapist to attend in my place, but she says that's 'counterproductive' and 'legally impossible.'"

if __name__ == "__main__":
    # Clear screen for cinematic immersion
    print(C.CLEAR, end='')
    
    # Dramatic pause (the silence before the neurosis)
    time.sleep(0.5)
    
    # Draw the frame
    print_cinema_frame()
    
    # Indent for text area
    margin = f"{C.DIM}║{C.RESET}  "
    sys.stdout.write(margin)
    
    # The main event: anxious delivery
    anxious_typewriter(QUOTE, base_delay=0.06)
    
    # Close the frame
    print_footer()
    
    # Final existential flicker
    flicker_effect()
    
    # The lingering doubt
    time.sleep(0.5)
    print(f"\n{C.ITALIC}{C.DIM}    *stares into the void, checks watch*{C.RESET}\n")