"""
Campbell's Soup Can #3851
Produced: 2026-06-03 17:17:36
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# A philosophical moment, painted with code.

import time
import sys
import random

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"

# Foreground colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright foreground colors
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Background colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"


def slow_print(text, delay=0.03, end="\n"):
    """Print text character by character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()


def rainbow_text(text):
    """Return text with rainbow ANSI colors cycling through characters."""
    colors = [RED, BRIGHT_RED, YELLOW, BRIGHT_YELLOW, GREEN, BRIGHT_GREEN, CYAN, BRIGHT_CYAN, BLUE, BRIGHT_BLUE, MAGENTA, BRIGHT_MAGENTA]
    result = ""
    for i, char in enumerate(text):
        result += colors[i % len(colors)] + char
    result += RESET
    return result


def gradient_box(text, width=62):
    """Create a beautiful gradient box around text."""
    top_left = "╔"
    top_right = "╗"
    bottom_left = "╚"
    bottom_right = "╝"
    horizontal = "═"
    vertical = "│"

    colors = [BLUE, CYAN, GREEN, YELLOW, MAGENTA, RED]

    # Top border
    top_border = top_left + horizontal * width + top_right
    bottom_border = bottom_left + horizontal * width + bottom_right

    # Center the text
    padding = (width - len(text)) // 2
    left_pad = " " * padding
    right_pad = " " * (width - padding - len(text))
    text_line = vertical + left_pad + text + right_pad + vertical

    return top_border, text_line, bottom_border


def neurotic_typing_effect(text, base_delay=0.04):
    """Simulate neurotic typing with occasional pauses and backspacing."""
    for char in text:
        if char == 'a' or char == 'e':
            # occasional long pause on vowels - like pondering
            pause_extra = random.uniform(0, 0.08)
        else:
            pause_extra = random.uniform(-0.01, 0.02)

        delay = max(0.01, base_delay + pause_extra)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def dramatic_pause_newline(count=1):
    """Print newlines with a dramatic effect."""
    for _ in range(count):
        time.sleep(0.15)
        sys.stdout.write("\n")
        sys.stdout.flush()


def clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def main():
    clear_screen()

    # ═══════════════════ PART 1: DRAMATIC OPENING ═══════════════════
    time.sleep(0.5)

    # Dramatic single-line intro "crash"
    opening_line = "⚡ PHILOSOPHICAL CRISIS DETECTED ⚡"
    print()
    slow_print(f"{BG_BLUE}{BRIGHT_WHITE}{BOLD} {opening_line} {RESET}", delay=0.05)
    print()
    time.sleep(0.8)

    # The cerebral cortex loading animation
    print(f"{DIM}{CYAN}", end="")
    stages = [
        "loading consciousness......",
        "consulting anxiety module..",
        "generating self-doubt.......",
        "questioning existence.......",
        "procrastinating............",
        "panic check................",
        "therapy session missed (again)...",
        "almost forgot how to breathe..",
        "existential dread: ████████░ 98%",
    ]
    for i, stage in enumerate(stages):
        pain = "░" * (10 - i) + "█" * i
        bar = f"  initializing soul [{pain}]"
        slow_print(bar, delay=0.03)
        time.sleep(0.3)
        if i < len(stages) - 1:
            # Clear line and overwrite
            sys.stdout.write("\033[A\033[2K\r")
            sys.stdout.flush()

    time.sleep(0.5)
    dramatic_pause_newline(2)

    # ═══════════════════ PART 2: THE QUOTE ═══════════════════

    quote_parts = [
        "Life is divided into the horrible and the miserable.",
    ]

    # The - Woody Allen

    # Build the ASCIFT ART thermometer of existential sorrow
    print()
    thermo_art = f"""
{DIM}{RESET}    {BG_BLUE}{BRIGHT_WHITE} EXISTENTIAL TIME UNTIL {RESET}
{DIM}{WHITE}    {BG_BLUE}{BRIGHT_WHITE} ANYTHING WORSE {RESET}
{DIM}[{time.strftime('%H:%M:%S')}]{RESET}
{DIM}{WHITE}    {BG_BLUE}{BRIGHT_WHITE}   MEANING    {RESET}
  {DIM}{WHITE}   .─────────────────.{RESET}
  {DIM}{WHITE}   │  ┌─┐   ┌─┐  ┌─┐│{RESET}
  {DIM}{WHITE}   │  └─┘   └─┘  └─┘│{RESET}
  {DIM}{WHITE}   │    {RED}╔═══╗          │{RESET}
  {DIM}{WHITE}   │    {RED}║ ! ║          │{RESET}
  {DIM}{WHITE}   │    {RED}╚═══╝          │{RESET}
  {DIM}{WHITE}   │  ┌────────────────┤{RESET}
  {DIM}{WHITE}   │  │ {RED}██████████{WHITE}░░░░ │{RESET}
  {DIM}{WHITE}   │  │ {YELLOW}anxiety level  │{RESET}
  {DIM}{WHITE}   │  └────────────────┘{RESET}
  {DIM}{WHITE}   │     ||  \\\\{RESET}
  {DIM}{WHITE}   '─────||───\\\\────{RESET}
"""
    for line in thermo_art.split('\n'):
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(0.05)

    time.sleep(0.5)

    # ═══════════════════ PART 3: THE BOX ═══════════════════
    quote_text = "Life is divided into the horrible and the miserable. The horrible are, for example, orphans dying of a rare form of cancer. The miserable are, for example, everybody else."

    # Wrap the quote into lines
    max_line_width = 56
    words = quote_text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_width:
            current_line += (" " if current_line else "") + word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    print()

    # Top border with gradient
    border_color = BRIGHT_YELLOW
    top = f" {border_color}╔{'═' * (max_line_width + 4)}╗{RESET}"
    slow_print(top, delay=0.02)

    # Empty decorative line
    slow_print(f" {border_color}║{BRIGHT_CYAN}  {'✦ THE UNIVERSE SPEAKS (through anxiety) ✦':^{max_line_width}}  {border_color}║{RESET}", delay=0.03)

    # Separator
    slow_print(f" {border_color}║{DIM}  {'─' * max_line_width}  {border_color}║{RESET}", delay=0.02)

    dramatic_pause_newline(1)

    # Quote with color-coded words
    neurotic_words = {
        "horrible": BRIGHT_RED,
        "miserable": MAGENTA,
        "orphans": BG_RED + BRIGHT_WHITE,
        "cancer": RED + UNDERLINE,
        "rare": YELLOW,
        "dying": DIM + WHITE,
    }

    for line in lines:
        # Colorize the line
        display_line = f" {BRIGHT_WHITE}"
        line_lower = line.lower()
        # Simple approach: iterate and color specific words
        colored_line = line.lstrip()
        for word_lower, color in neurotic_words.items():
            # Case insensitive replace
            parts = colored_line.split(word_lower.capitalize()) if word_lower.capitalize() in colored_line else [colored_line]
            if word_lower.capitalize() in colored_line:
                colored_line = (color + word_lower.capitalize() + BRIGHT_WHITE).join(
                    colored_line.split(word_lower.capitalize())
                )
            if word_lower.upper() in colored_line:
                colored_line = colored_line  # already handled
            # Also handle title case
            if word_lower.capitalize() not in line and word_lower in line:
                # handle as-is
                idx = line_lower.index(word_lower) if word_lower in line_lower else -1
                if idx >= 0:
                    actual_word = colored_line[idx:idx+len(word_lower)]
                    colored_line = colored_line[:idx] + color + actual_word + BRIGHT_WHITE + colored_line[idx+len(word_lower):]

        padding = max_line_width - len(line)
        padding_str = " " * padding
        full_line = f" {border_color}║{BRIGHT_WHITE}  {colored_line}{padding_str}  {BRIGHT_WHITE}{border_color}║{RESET}"
        slow_print(full_line, delay=0.025)
        time.sleep(0.05)

    dramatic_pause_newline(1)

    # Bottom quote attribution
    slow_print(f" {border_color}║{DIM}  {'─' * max_line_width}  {border_color}║{RESET}", delay=0.02)

    # Attribution line
    attribution = "(philosophically speaking, of course...)"
    padding = max_line_width - len(attribution)
    padding_str = " " * (padding) + " │"
    slow_print(f"  │{ITALIC}{RED}  {attribution}{padding_str}  │{RESET}", delay=0.03)

    # Final awkward line about how I'm actually a computer program pretending to understand existence
    slow_print(f"  │{ITALIC}{DIM}  (I'm a Python program; I don't really understand{RESET}", delay=0.03)
    slow_print(f"  │{ITALIC}{DIM}   existence, but I'm trying my best.){RESET}", delay=0.03)

    # Bottom border
    slow_print(f" {border_color}╚{'═' * (max_line_width + 4)}╝{RESET}", delay=0.02)

    dramatic_pause_newline(2)

    # ═══════════════════ PART 4: FOOTER ═══════════════════

    # Rainbow footer
    footer_text = " ~ That's the problem with reality ~ "
    slow_print(f"    {rainbow_text(footer_text)}", delay=0.02)

    print()

    # Rain of existential particles
    particles = ["·", "•", "◦", "∙", "∘", "∙", "·", "•"]
    for _ in range(3):
        particle_line = " " * 30
        particle_line = particle_line + "  ".join([BRIGHT_CYAN + random.choice(particles) + RESET for _ in range(15)])
        slow_print(particle_line, delay=0.01)
        time.sleep(0.15)

    slow_print("", end="\n\n")

    # A final line of text
    slow_print(f"  '{rainbow_text('And that... is the joke.')}'{RESET}", delay=0.04)
    time.sleep(0.3)

    slow_print(f"\n   ─ Perhaps. Perhaps not. Probably nothing matters.{RESET}", delay=0.04)
    time.sleep(0.3)

    # the end credits
    credits = [
        "Written after 37 cups of coffee and no therapist.",
        "All rights reserved / No rights reserved (it's all meaningless).",
        "Dedicated to everyone reading this at 3 AM wondering if the semicolons matter.",
    ]
    print()
    for i, credit in enumerate(credits):
        delay = 0.06 if i == 2 else 0.04
        prefix = "   " + ITALIC + DIM
        slow_print(f"{prefix}{credit}{RESET}", delay=delay)
        time.sleep(0.4)

    print()
    slow_print(f"  {BG_BLUE}{BRIGHT_WHITE}{BOLD} [ANXIETY SYSTEM OFFLINE — RECOMMENDED ACTION: MAKE A JOKE ABOUT DEATH] {RESET}", delay=0.02)
    print()

    # Final cursor blink animation
    for _ in range(3):
        sys.stdout.write("   " + BLINK + "█" + RESET)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
        time.sleep(0.3)

    print()
    time.sleep(0.5)
    slow_print(f"\n   {ITALIC}{DIM}good night.{RESET}", delay=0.08)
    print()


if __name__ == "__main__":
    main()