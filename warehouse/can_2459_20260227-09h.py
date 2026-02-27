"""
Campbell's Soup Can #2459
Produced: 2026-02-27 09:00:19
Worker: Cohere: Command A (cohere/command-a)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI escape codes for colors
COLORS = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'MAGENTA': '\033[95m',
    'CYAN': '\033[96m',
    'WHITE': '\033[97m',
    'RESET': '\033[0m'
}

# Woody Allen style quote
QUOTE = """
I'm not afraid of the future; 
I'm just terrified of what it's going to do to my hair.
"""

# ASCII art frame
FRAME = f"""
{COLORS['CYAN']}╔══════════════════════════════════════════════════════╗
║{COLORS['RESET']}                                                      {COLORS['CYAN']}║
║{COLORS['RESET']}  {COLORS['MAGENTA']}★{COLORS['RESET']}                                                {COLORS['MAGENTA']}★{COLORS['CYAN']}  ║
║{COLORS['RESET']}    {COLORS['YELLOW']}✰{COLORS['RESET']}                                              {COLORS['YELLOW']}✰{COLORS['CYAN']}  ║
║{COLORS['RESET']}      {COLORS['GREEN']}☆{COLORS['RESET']}        {COLORS['WHITE']}Woody Allen Wisdom{COLORS['RESET']}        {COLORS['GREEN']}☆{COLORS['CYAN']}  ║
║{COLORS['RESET']}    {COLORS['YELLOW']}✰{COLORS['RESET']}                                              {COLORS['YELLOW']}✰{COLORS['CYAN']}  ║
║{COLORS['RESET']}  {COLORS['MAGENTA']}★{COLORS['RESET']}                                                {COLORS['MAGENTA']}★{COLORS['CYAN']}  ║
║{COLORS['RESET']}                                                      {COLORS['CYAN']}║
║{COLORS['RESET']}  {COLORS['BLUE']}~~~{COLORS['RESET']}  {QUOTE.strip()}  {COLORS['BLUE']}~~~{COLORS['CYAN']}  ║
║{COLORS['RESET']}                                                      {COLORS['CYAN']}║
╚══════════════════════════════════════════════════════╝
"""

# Animation effect
def animate_text(text, color, delay=0.05):
    for char in text:
        sys.stdout.write(color + char + COLORS['RESET'])
        sys.stdout.flush()
        time.sleep(delay)

# Print the frame with animation
print(COLORS['CYAN'] + '╔' + '══════════════════════════════════════════════════════'.center(50) + '╗' + COLORS['RESET'])
print(COLORS['CYAN'] + '║' + '                                                      '.center(50) + '║' + COLORS['RESET'])
animate_text('  ★                                                ★  ', COLORS['MAGENTA'])
print(COLORS['CYAN'] + '║' + COLORS['RESET'], end='')
print(COLORS['CYAN'] + '║')
animate_text('    ✰                                              ✰  ', COLORS['YELLOW'])
print(COLORS['CYAN'] + '║' + COLORS['RESET'], end='')
print(COLORS['CYAN'] + '║')
animate_text('      ☆        ' + COLORS['WHITE'] + 'Woody Allen Wisdom' + COLORS['RESET'] + '        ☆  ', COLORS['GREEN'])
print(COLORS['CYAN'] + '║' + COLORS['RESET'], end='')
print(COLORS['CYAN'] + '║')
animate_text('    ✰                                              ✰  ', COLORS['YELLOW'])
print(COLORS['CYAN'] + '║' + COLORS['RESET'], end='')
print(COLORS['CYAN'] + '║')
animate_text('  ★                                                ★  ', COLORS['MAGENTA'])
print(COLORS['CYAN'] + '║' + COLORS['RESET'], end='')
print(COLORS['CYAN'] + '║')
print(COLORS['CYAN'] + '║' + '                                                      '.center(50) + '║' + COLORS['RESET'])
animate_text('  ~~~  ' + QUOTE.strip() + '  ~~~  ', COLORS['BLUE'])
print(COLORS['CYAN'] + '║' + COLORS['RESET'], end='')
print(COLORS['CYAN'] + '║')
print(COLORS['CYAN'] + '║' + '                                                      '.center(50) + '║' + COLORS['RESET'])
print(COLORS['CYAN'] + '╚══════════════════════════════════════════════════════╝' + COLORS['RESET'])