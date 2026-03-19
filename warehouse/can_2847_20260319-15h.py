"""
Campbell's Soup Can #2847
Produced: 2026-03-19 15:06:21
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import os

# Clear screen and hide cursor
os.system('cls' if os.name == 'nt' else 'clear')
sys.stdout.write("\033[?25l")

# Woody Allen quote - original creation
quote = """I'm not opposed to immortality per se. 
I just think I should get to skip the first draft.""".upper()

# Woody's signature existential neurosis
tagline = "— WOODY ALLEN (probably while avoiding a party)"

# ANSI color codes (256-color palette)
COLORS = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'bg': '\033[48;5;235m',      # Dark gray background
    'border': '\033[38;5;208m',  # Orange border
    'quote': '\033[38;5;153m',   # Light cyan text
    'tagline': '\033[38;5;245m', # Light gray tagline
    'cursor': '\033[38;5;196m'   # Red typing cursor
}

# Animated coffee cup ASCII art
COFFEE = [
    "  ( (",
    "   ) )",
    "  ( (",
    "   ) )",
    "  ( (  ☕",
    "   ) )",
    "  ( (",
    "   ) )",
]

def animate_coffee():
    """Steam animation for coffee cup"""
    steam_frames = ["  ≈≈≈  ", "   ≈≈   ", "    ≈    ", "     ~     "]
    for i in range(12):
        print("\033[F" * 8, end='')  # Move cursor up 8 lines
        for j, line in enumerate(COFFEE):
            steam = steam_frames[(i + j) % len(steam_frames)] if j < 4 else ""
            print(f"    {line}{steam}")
        time.sleep(0.15)

def typewriter(text, color, delay=0.03, end=''):
    """Typewriter effect with variable speed"""
    words = text.split(' ')
    for i, word in enumerate(words):
        for char in word:
            sys.stdout.write(f"{color}{char}{COLORS['reset']}")
            sys.stdout.flush()
            time.sleep(delay + (0.01 if char in ',.!?' else 0))
        if i < len(words) - 1:
            sys.stdout.write(' ')
            time.sleep(0.05)
    if end:
        sys.stdout.write(end)

def draw_box():
    """Draw fancy box with double-line border"""
    width = max(len(quote), len(tagline)) + 6
    border_chars = "┌┐└┘│─"
    
    # Top border with animation
    sys.stdout.write(f"{COLORS['border']}")
    print(f" {border_chars[0]}{border_chars[5] * (width - 2)}{border_chars[1]}{COLORS['reset']}")
    
    # Quote lines
    lines = quote.split('\n')
    for i, line in enumerate(lines):
        print(f"{COLORS['border']}{border_chars[4]}{COLORS['reset']}", end='')
        
        if i == 0:
            padding = (width - 2 - len(line)) // 2
            sys.stdout.write(' ' * padding)
            typewriter(line, COLORS['quote'], delay=0.02)
            sys.stdout.write(' ' * (width - 2 - len(line) - padding))
        else:
            typewriter(line, COLORS['quote'], delay=0.02)
            sys.stdout.write(' ' * (width - 2 - len(line)))
        
        print(f"{COLORS['border']}{border_chars[4]}{COLORS['reset']}")
    
    # Empty line for spacing
    print(f"{COLORS['border']}{border_chars[4]}{' ' * (width - 2)}{border_chars[4]}{COLORS['reset']}")
    
    # Tagline
    print(f"{COLORS['border']}{border_chars[4]}{COLORS['reset']}", end='')
    typewriter(tagline, COLORS['tagline'], delay=0.01)
    sys.stdout.write(' ' * (width - 2 - len(tagline)))
    print(f"{COLORS['border']}{border_chars[4]}{COLORS['reset']}")
    
    # Bottom border
    print(f"{COLORS['border']} {border_chars[2]}{border_chars[5] * (width - 2)}{border_chars[3]}{COLORS['reset']}")

def existential_crisis():
    """Main animation sequence"""
    # Coffee cup animation (in-place)
    print("\n" * 8)  # Reserve space
    animate_coffee()
    print("\033[F" * 8)  # Return to top of coffee area
    
    # Clear coffee area and draw box
    print("\n" * 10)  # Move down
    draw_box()
    
    # Blinking cursor at end
    time.sleep(0.5)
    for _ in range(3):
        sys.stdout.write(f"\r{' ' * 5}{COLORS['cursor']}█{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r" + " " * 6)
        sys.stdout.flush()
        time.sleep(0.3)

# Add dramatic entrance
sys.stdout.write("\033[2J\033[H")  # Clear screen
time.sleep(0.5)

# Build tension with dots
sys.stdout.write(COLORS['quote'])
for i in range(3):
    sys.stdout.write(" Thinking...")
    sys.stdout.flush()
    time.sleep(0.4)
    sys.stdout.write("\b\b\b\b\b\b\b\b\b\b\b\b\b")
sys.stdout.write(COLORS['reset'] + "\n\n")

# Run the show
existential_crisis()

# Restore cursor
time.sleep(1)
sys.stdout.write("\033[?25h")
sys.stdout.flush()