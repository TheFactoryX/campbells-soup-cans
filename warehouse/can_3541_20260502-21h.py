"""
Campbell's Soup Can #3541
Produced: 2026-05-02 21:58:51
Worker: MiniMax: MiniMax M2.5 (free) (minimax/minimax-m2.5:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════╗
║       🎬 Woody Allen Style Philosophical Quote Generator 🎬          ║
║           (A neurotic, funny, existential experience)                ║
╚══════════════════════════════════════════════════════════════════════╝

Author: The Anxious Python
Purpose:To make you laugh while questioning your existence
"""

import time
import sys
import os

# ═══════════════════════════════════════════════════════════════════════
# ANSI COLOR PALETTE - Because life is colorful (and anxious)
# ═══════════════════════════════════════════════════════════════════════

RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
BLINK   = "\033[5m"

# Foreground colors
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

# Bright foreground
BRIGHT_RED     = "\033[91m"
BRIGHT_GREEN   = "\033[92m"
BRIGHT_YELLOW  = "\033[93m"
BRIGHT_BLUE    = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN    = "\033[96m"
BRIGHT_WHITE   = "\033[97m"

# Background colors
BG_BLACK   = "\033[40m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"

# ═══════════════════════════════════════════════════════════════════════
# THE QUOTE - Woody Allen would be proud (or anxious)
# ═══════════════════════════════════════════════════════════════════════

QUOTE = """
I'm not afraid of death - I've been dead once and it was
just a Tuesday. The real terror is realizing that the
 microwave popcorn will outlast my greatest achievements.
"""

AUTHOR = "— Woody Allen (probably)"

# ═══════════════════════════════════════════════════════════════════════
# ARTISTIC FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════

def clear_screen():
    """Clear the terminal screen (works on most terminals)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer(text, delay=0.03, color=WHITE):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)

def print_slow(text, delay=0.02):
    """Print text line by line with delay."""
    for line in text.split('\n'):
        print(line)
        time.sleep(delay)

def create_frame(text, max_width=70):
    """Create a fancy ASCII frame around text."""
    lines = text.strip().split('\n')
    adjusted_lines = []
    
    for line in lines:
        if len(line) > max_width - 4:
            # Word wrap
            words = line.split()
            current_line = ""
            for word in words:
                if len(current_line) + len(word) + 1 <= max_width - 4:
                    current_line += (" " if current_line else "") + word
                else:
                    adjusted_lines.append(current_line)
                    current_line = word
            adjusted_lines.append(current_line)
        else:
            adjusted_lines.append(line)
    
    max_len = max(len(line) for line in adjusted_lines)
    
    # Decorative corners and borders
    top    = BRIGHT_CYAN + "┌" + "─" * (max_len + 2) + "┐" + RESET
    bottom = BRIGHT_CYAN + "└" + "─" * (max_len + 2) + "┘" + RESET
    side   = BRIGHT_CYAN + "│" + RESET
    
    return top, adjusted_lines, bottom, side, max_len

def print_decorated_box(text, author):
    """Print a beautifully decorated quote box."""
    top, lines, bottom, side, max_len = create_frame(text)
    
    # Print with dramatic pause
    print("\n")
    type_writer("  " + BRIGHT_YELLOW + "✨" + RESET + " " + BRIGHT_WHITE + "PRESENTING" + RESET + " " + BRIGHT_YELLOW + "✨" + RESET + "\n", 0.1)
    time.sleep(0.3)
    
    # Top border
    print(BOLD + top + RESET)
    
    # Quote lines with typewriter effect
    for i, line in enumerate(lines):
        padding = " " * (max_len - len(line))
        if i == 0:
            # First line gets extra emphasis
            print(side + " " + BRIGHT_YELLOW + BOLD + line + padding + " " + side + RESET)
        else