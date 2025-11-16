"""
Campbell's Soup Can #321
Produced: 2025-11-16 18:40:09
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

# ANSI color codes
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bold': '\033[1m',
    'reset': '\033[0m'
}

def print_wavy_text(text, delay=0.05):
    """Print text with a wavy animation effect"""
    amplitudes = [1, 2, 3, 2, 1, 0, -1, -2, -1, 0]
    for i, char in enumerate(text):
        amp = amplitudes[i % len(amplitudes)]
        if amp > 0:
            sys.stdout.write(' ' * amp + char + '\n')
        elif amp < 0:
            sys.stdout.write('\033[F' * (-amp) + ' ' * (-amp) + char + '\033[B' * (-amp) + '\n')
        else:
            sys.stdout.write(char + '\n')
        sys.stdout.flush()
        time.sleep(delay)

def draw_therapy_couch():
    """Draw a simple ASCII therapy couch"""
    couch = [
        "    _________",
        "   /         \\",
        "  /  (      ) \\",
        " /_____________\\",
        " |  ~ ~ ~ ~ ~ |",
        " |~~~~~~~~~~~~|",
        " |  ~ ~ ~ ~ ~ |",
        " |~~~~~~~~~~~~|",
        " |___________|"
    ]
    return couch

def print_woody_quote():
    # Clear screen
    print('\033[2J\033[H')
    
    # Print title with blinking effect (simulated)
    title = "WOODY ALLEN'S THERAPY SESSION"
    print(f"\n{COLORS['magenta']}{COLORS['bold']}")
    print("╔" + "═" * (len(title) + 2) + "╗")
    print(f"║ {title} ║")
    print("╚" + "═" * (len(title) + 2) + "╝")
    print(f"{COLORS['reset']}")
    
    # Draw the couch
    couch = draw_therapy_couch()
    print(f"\n{COLORS['cyan']}")
    for line in couch:
        print(" " * 10 + line)
    print(f"{COLORS['reset']}")
    
    # The quote with neurotic energy
    quote = "I'm not afraid of death... I just find it incredibly inconvenient! Think about it - just when you're getting good at life, they expect you to check out! And have you seen the healthcare plan they offer in the afterlife? 'Eternal peace'? What kind of HMO is that? I'd rather have a decent dental plan!"
    
    therapist_note = "\n[Therapist writes intensively on notepad: 'Same as last week.']"
    
    # Type out the quote character by character with neurotic energy
    print(f"\n{COLORS['yellow']}{COLORS['bold']}Woody:{COLORS['reset']} ", end="")
    
    for char in quote:
        print(char, end="", flush=True)
        # Add some nervous pauses
        if char in ",-":
            time.sleep(0.2)
        elif char in "!?.":
            time.sleep(0.4)
        else:
            time.sleep(0.03)
    
    # Add the therapist note
    print(f"\n{COLORS['green']}{therapist_note}{COLORS['reset']}")
    
    # Add some bouncing ellipsis for that anxious afterthought
    print(f"\n{COLORS['yellow']}...", end="", flush=True)
    for _ in range(3):
        for dots in ["..", "...", "...."]:
            print(f"\r{COLORS['yellow']}{dots}", end="", flush=True)
            time.sleep(0.3)
    
    # The final anxious thought
    final_thought = " (And don't get me started on reincarnation - what if I come back as a soy candle? 'Burn me slowly while I apologize for existing?' No thanks!)"
    
    print(f"\n{COLORS['yellow']}Actually, wait...{COLORS['reset']}", end="", flush=True)
    time.sleep(0.8)
    
    for char in final_thought:
        print(char, end="", flush=True)
        if char in "-":
            time.sleep(0.15)
        elif char in "!?.":
            time.sleep(0.3)
        else:
            time.sleep(0.02)
    
    # Add some closing text
    print(f"\n\n{COLORS['blue']}🕒 Session time: 50 minutes (he ran 20 minutes over){COLORS['reset']}")
    print(f"{COLORS['blue']}💰 Bill: $400 (plus anxiety surcharge){COLORS['reset']}")
    
    # Blinking exit message
    exit_line = "Next appointment: Same time next Tuesday (or sooner if I have an existential crisis)"
    print(f"\n{COLORS['red']}{exit_line}{COLORS['reset']}")

if __name__ == "__main__":
    print_woody_quote()