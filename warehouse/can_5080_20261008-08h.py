"""
Campbell's Soup Can #5080
Produced: 2026-10-08 08:59:00
Worker: inclusionAI: Ling 3.0 Flash Sante (free) (inclusionai/ling-3.0-flash-sante:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI color palette
R = '\033[91m'  # Red
Y = '\033[93m'  # Yellow
C = '\033[96m'  # Cyan
G = '\033[92m'  # Green
B = '\033[1m'   # Bold
D = '\033[2m'   # Dim
RESET = '\033[0m'

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewrite(text, color, delay=0.025):
    """Print text with a typewriter effect."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + '\n')
    sys.stdout.flush()

def main():
    cls()
    
    # Header
    print(C + B)
    print("╔════════════════════════════════════════════════════╗")
    print("║          🎭  NEUROTIC PHILOSOPHY CORP  🎭         ║")
    print("╚════════════════════════════════════════════════════╝")
    print(RESET)
    time.sleep(0.4)
    
    # Quote
    print(R + B + "  \"")
    quote = "I've accepted that life has no inherent meaning, which explains why I'm so obsessed with finding a matching sock."
    typewrite(quote, Y, 0.02)
    print(R + B + "\"" + RESET)
    
    time.sleep(0.6)
    
    # Attribution
    print(G + "         -- Woody Allen's unconscious mind\n" + RESET)
    
    time.sleep(0.8)
    
    # ASCII Brain
    print(G + B)
    print("              .--.")
    print("             |o_o |")
    print("             |:_/ |")
    print("            //   \\ \\")
    print("           (|     | )")
    print("          /'\\_   _/`\\")
    print("          \\___)=(___/")
    print(RESET)
    
    time.sleep(0.5)
    
    # Footer
    print(D + "  [ Existential dread successfully loaded ]" + RESET)
    print(R + D + "  [ Press Ctrl+C to abort this existence ]" + RESET + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + R + B + "Good choice. Running away is the only logical response." + RESET)