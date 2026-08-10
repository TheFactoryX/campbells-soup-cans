"""
Campbell's Soup Can #4524
Produced: 2026-08-10 21:58:15
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic, existential Woody Allen-style quote delivered with visual flair.
"""

import sys
import time
import random

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

# Bright variants
BRED = "\033[1;91m"
BYELLOW = "\033[1;93m"
BCYAN = "\033[1;96m"
BWHITE = "\033[1;97m"

def slow_print(text, delay=0.03, color=RESET):
    """Prints text with a typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def flicker_print(text, flicker_chars=".~* ", color=RESET):
    """Prints text with a flickering/typewriter effect with random characters."""
    for char in text:
        # Sometimes show a flicker character before the real one
        if random.random() < 0.2 and char != ' ':
            fc = random.choice(flicker_chars)
            sys.stdout.write(f"{DIM}{color}{fc}{RESET}")
            sys.stdout.flush()
            time.sleep(0.02)
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.04)
    print()

def draw_box(lines, width=70, border_color=BCYAN, inner_color=RESET):
    """Draws a box around lines of text."""
    top = f"{border_color}" + "═" * (width + 2) + f"{RESET}"
    bottom = f"{border_color}" + "═" * (width + 2) + f"{RESET}"
    side = f"{border_color}║{RESET}"
    
    print(top)
    for line in lines:
        # Truncate or pad line to width
        if len(line) > width:
            line = line[:width]
        padding = width - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{side}{' ' * left_pad}{line}{' ' * right_pad}{side}")
    print(bottom)

def animate_divider(length=70, color=BRED):
    """Animates a divider line being drawn."""
    chars = ["═"] * length
    sys.stdout.write(f"{color}")
    for c in chars:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005)
    sys.stdout.write(f"{RESET}\n")
    sys.stdout.flush()

def main():
    # Clear screen and set up
    print("\033[2J\033[H", end="")
    time.sleep(0.3)
    
    # Title art
    title = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║          🧠  W O O D Y   A L L E N   F I L O S O P H Y  🧠   ║
    ║                                                              ║
    ║           "A Neurotic Examination of Existence"               ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    
    # Print title with flair
    flicker_print(title, flicker_chars=". ", color=BRED)
    time.sleep(0.5)
    
    # Animated divider
    animate_divider()
    time.sleep(0.3)
    
    # Build the quote with visual elements
    print()
    
    # ASCII art: a worried thinker
    thinker = f"""
{BDIM}          .-.          {RESET}
{BDIM}         (o.o)        {RESET}
{BDIM}          |:^)       {RESET}
{BDIM}         _|__|       {RESET}
{BDIM}       /     \\      {RESET}
{BDIM}      /|     |\\     {RESET}
{BDIM}     ( |     | )    {RESET}
{BDIM}      \\\\_    \\\\_   {RESET}
{BDIM}       \\\\    \\\\_  {RESET}
{BDIM}        \\\\_    {RESET}
{BDIM}         \\\\_   {RESET}
{BDIM}          {RESET}"""
    
    # Print thinker with flickering effect
    flicker_print(thinker, color=BCYAN)
    time.sleep(0.4)
    
    print()
    
    # The actual quote - built up piece by piece
    quote_parts = [
        f"{BOLD}{BYELLOW}\"I've been thinking about{RESET}",
        f"{BOLD}{BYELLOW}the absurdity of it all...{RESET}",
        f"{BOLD}{BYELLOW}We're born screaming, {RESET}",
        f"{BOLD}{YELLOW}ripping our way{RESET}",
        f"{BOLD}{YELLOW}from the warm dark, {RESET}",
        f"{BOLD}{YELLOW}only to spend{RESET}",
        f"{BOLD}{YELLOW}decades trying{RESET}",
        f"{BOLD}{YELLOW}to get back there —{RESET}",
        f"{BOLD}{BYELLOW}through bad relationships,{RESET}",
        f"{BOLD}{BYELLOW} Existential dread,{RESET}",
        f"{BOLD}{BYELLOW}and{RESET} {BOLD}{RED}uncomfortable shoes.{RESET}",
        f"{BOLD}{BYELLOW}And then it's over —{RESET}",
        f"{BOLD}{YELLOW}{ITALIC}but not before{RESET}",
        f"{BOLD}{YELLOW}{ITALIC} someone{RESET}",
        f"{BOLD}{YELLOW}{ITALIC} tells you{RESET}",
        f"{BOLD}{YELLOW}{ITALIC} to please keep{RESET}",
        f"{BOLD}{YELLOW}{ITALIC} your existential dread{RESET}",
        f"{BOLD}{YELLOW}{ITALIC} in the overhead compartment.{RESET}",
        f"{BOLD}{BYELLOW}\"\"\"{RESET}",
    ]
    
    # Build up the quote in a box
    quote_lines = [
        "\"I've been thinking about",
        "the absurdity of it all...",
        "",
        "We're born screaming,",
        "ripping our way",
        "from the warm dark,",
        "only to spend",
        "decades trying",
        "to get back there",
        "— through bad relationships,",
        "Existential dread,",
        "and uncomfortable shoes.",
        "",
        "And then it's over",
        "— but not before",
        "someone tells you",
        "to please keep",
        "your existential dread",
        "in the overhead compartment.",
        "\"",
    ]
    
    # Print the quote inside a fancy box
    # First, draw the box borders with effect
    box_width = 72
    top_border = f"{BCYAN}╔{'═' * box_width}╗{RESET}"
    bottom_border = f"{BCYAN}╚{'═' * box_width}╝{RESET}"
    
    # Animate top border
    slow_print(top_border, delay=0.008)
    time.sleep(0.1)
    
    # Print quote lines
    for i, line in enumerate(quote_lines):
        if line == "":
            content = " " * 20
        else:
            # Center-ish placement with some color variation
            content = f"  {line}"
        
        side = f"{BCYAN}║{RESET}"
        # Calculate padding
        line_wo_ansi = line  # simplified for layout
        padding = box_width - len(content) - 4
        if padding < 0:
            padding = 2
        
        if i % 3 == 0:
            line_color = BYELLOW
        elif i % 3 == 1:
            line_color = YELLOW
        else:
            line_color = BCYAN
            
        if "dread" in line or "screaming" in line or "over" in line.lower():
            line_color = f"{line_color}{BOLD}"
        
        full_line = f"{side}  {line_color}{content}{RESET}{' ' * (padding - 2 + 4)}{side}"
        
        # Actually let's simplify this
        pass
    
    # Let me just do it more simply with the draw_box function
    print()
    animate_divider(70)
    print()
    time.sleep(0.2)
    
    # Print quote with typewriter + color effects
    quote_text = [
        '"I\'ve been thinking about the absurdity of it all..."',
        '',
        'We\'re born screaming, ripping our way from the warm dark,',
        'only to spend decades trying to get back there',
        '— through bad relationships, existential dread,',
        f'and {BOLD}{RED}uncomfortable shoes.{RESET}',
        '',
        'And then it\'s over — but not before',
        'someone tells you to please keep',
        f'{ITALIC}your existential dread in the overhead compartment.{RESET}',
        '',
        '— {DIM}Woody Allen, probably while waiting for a therapist{RESET}'
        f'{DIM} who is also late, which is itself an existential crisis.{RESET}'
    ]
    
    # Draw the main quote box
    draw_box(quote_text, width=70, border_color=BRED)
    
    print()
    animate_divider(70)
    time.sleep(0.3)
    
    # Add some existential commentary
    commentary = [
        f"{BCYAN}☄{RESET} {DIM}This message was brought to you by the Department of{RESET}",
        f"{DIM} Unnecessary Anxiety and Premature Existential Panic{RESET}",
        f"{DIM}(a division of your own mind, which is why it's so efficient){RESET}",
    ]
    
    for c in commentary:
        flicker_print(c, delay=0.02, color=BWHITE)
        time.sleep(0.1)
    
    print()
    flicker_print(f"{BYELLOW}☕{RESET} {DIM}Now if you'll excuse me, I have a date with{RESET}", delay=0.03)
    flicker_print(f"{DIM} meaninglessness and a therapist I can't afford.{RESET}", delay=0.03)
    print()

if __name__ == "__main__":
    main()