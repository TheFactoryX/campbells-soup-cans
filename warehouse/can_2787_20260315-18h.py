"""
Campbell's Soup Can #2787
Produced: 2026-03-15 18:58:34
Worker: Healer Alpha (openrouter/healer-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Healer Alpha presents: A Woody Allen-esque Philosophical Musing
With typewriter animation and colorful ANSI art!
"""

import time
import sys
import os

# Clear screen for dramatic effect
os.system('cls' if os.name == 'nt' else 'clear')

# ANSI color codes
COLORS = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'italic': '\033[3m',
    'underline': '\033[4m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bg_blue': '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_cyan': '\033[46m',
}

def typewriter_print(text, delay=0.03, color='white'):
    """Print text with typewriter animation"""
    for char in text:
        sys.stdout.write(f"{COLORS[color]}{char}{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline at end

def print_centered(text, width=60, color='white'):
    """Print text centered in a box"""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    
    # Box top
    print(f"{COLORS[color]}╔{'═' * (max_len + 4)}╗{COLORS['reset']}")
    
    # Content
    for line in lines:
        padding = width - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{COLORS[color]}║{COLORS['reset']} {' ' * left_pad}{COLORS['bold']}{COLORS['cyan']}{line}{COLORS['reset']}{' ' * right_pad} {COLORS[color]}║{COLORS['reset']}")
    
    # Box bottom
    print(f"{COLORS[color]}╚{'═' * (max_len + 4)}╝{COLORS['reset']}")

def main():
    # The philosophical quote
    quote = [
        "I'm not afraid of death;",
        "I just don't want to be there",
        "when it happens.",
        "",
        "Actually, that's not quite right.",
        "I'm not afraid of death itself,",
        "I'm afraid of the paperwork.",
    ]
    
    # ASCII art of Woody's glasses
    glasses_art = """
        .-""""""-.
      .'          '.
     /   O      O   \\
    :                 :
    |    .------.     |
    :   /  __  __\\   :
     \\  \\  \\__/  /  /
      '.  '----'  .'
        '-......-'
    """
    
    # Print the glasses art
    print(f"{COLORS['yellow']}{glasses_art}{COLORS['reset']}")
    
    # Title
    print(f"{COLORS['bold']}{COLORS['magenta']}")
    print("✧･ﾟ: *✧･ﾟ:*   W O O D Y   W I S D O M   *:･ﾟ✧*:･ﾟ✧")
    print(f"{COLORS['reset']}")
    
    time.sleep(0.5)
    
    # Type out the quote with dramatic pauses
    for i, line in enumerate(quote):
        if i == 3:  # Dramatic pause
            print()
            time.sleep(1)
            print(f"{COLORS['dim']}{COLORS['italic']}    [pause for existential contemplation]{COLORS['reset']}")
            time.sleep(1)
            print()
        
        if line:
            color = 'cyan' if i < 3 else 'green'
            typewriter_print(f"    {line}", delay=0.04, color=color)
            time.sleep(0.2)
    
    print()
    
    # Attribution
    print(f"{COLORS['yellow']}{COLORS['dim']}                    — Woody Allen, probably{COLORS['reset']}")
    print()
    
    # Final thought
    print(f"{COLORS['red']}{COLORS['bold']}╭─────────────────────────────────────────╮{COLORS['reset']}")
    print(f"{COLORS['red']}│{COLORS['reset']} {COLORS['white']}Neurosis is the substitute for suffering.{COLORS['reset']} {COLORS['red']}│{COLORS['reset']}")
    print(f"{COLORS['red']}╰─────────────────────────────────────────╯{COLORS['reset']}")
    
    # Blinking effect for the final word
    print()
    for _ in range(3):
        print(f"\033[1A{COLORS['bg_blue']} {COLORS['white']} Blinking neurosis... {COLORS['reset']} ", end="")
        sys.stdout.flush()
        time.sleep(0.5)
        print(f"\r{COLORS['bg_magenta']} {COLORS['white']} Blinking neurosis... {COLORS['reset']} ", end="")
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\n")
    
    # Closing message
    typewriter_print("   Remember: If life doesn't offer you a sense of purpose,")
    typewriter_print("   you can always try to find a sense of humor about it.", color='green')
    print()
    
    # Final color reset
    print(COLORS['reset'])

if __name__ == "__main__":
    main()