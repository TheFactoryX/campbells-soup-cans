"""
Campbell's Soup Can #4100
Produced: 2026-07-05 12:42:02
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI color codes
class C:
    R = '\033[91m'      # Red
    G = '\033[92m'      # Green
    Y = '\033[93m'      # Yellow
    B = '\033[94m'      # Blue
    M = '\033[95m'      # Magenta
    C = '\033[96m'      # Cyan
    W = '\033[97m'      # White
    D = '\033[90m'      # Dim
    BD = '\033[1m'      # Bold
    IT = '\033[3m'      # Italic
    UL = '\033[4m'      # Underline
    BLINK = '\033[5m'   # Blink
    REV = '\033[7m'     # Reverse
    END = '\033[0m'     # Reset
    
    # Backgrounds
    BG_B = '\033[44m'
    BG_R = '\033[41m'
    BG_Y = '\033[43m'
    BG_M = '\033[45m'

# Woody Allen ASCII art
WOODY = f"""
{C.C}      ╭─────────────╮{C.END}
{C.C}      │  {C.Y}◉   ◉{C.C}  │  {C.D}← Thick black glasses{C.END}
{C.C}      │  {C.Y}  ▽  {C.C}  │  {C.D}← Existential sigh{C.END}
{C.C}      │ {C.Y}╰─────╯{C.C} │  {C.D}← Neurotic smile{C.END}
{C.C}      ╰─────────────╯{C.END}
{C.D}        │     │{C.END}
{C.D}      ╭─╯     ╰─╮{C.END}
{C.D}      │  BODY   │{C.END}
{C.D}      ╰─────────╯{C.END}
"""

# Our original Woody-style quote
QUOTE = "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia."
# Alternative quotes (pick one randomly for variety)
QUOTES = [
    "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia.",
    "My therapist says I have a preoccupation with mortality. I told her, 'Doc, at my age, it's not a preoccupation—it's a schedule.'",
    "I don't believe in an afterlife, but I'm bringing a change of underwear just in case.",
    "The food at this existential café is terrible. And such small portions!",
    "I'm two with nature. Which is one more than I'm comfortable with.",
    "Death is just nature's way of telling you to slow down. Permanently.",
    "I was thrown out of college for cheating on the metaphysics exam. I looked into the soul of the boy next to me.",
    "Life is divided into the horrible and the miserable. The horrible are terminal cases. The miserable is everyone else. So be grateful you're miserable.",
    "I have a gnawing fear that the universe is expanding, but my apartment isn't.",
    "If only God would give me a clear sign! Like making a large deposit in my name at a Swiss bank."
]

def typewriter(text, color="", delay=0.03, end=""):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.END}")
        sys.stdout.flush()
        time.sleep(delay)
    print(end=end)

def clear_screen():
    print("\033[2J\033[H", end="")

def hide_cursor():
    print("\033[?25l", end="")

def show_cursor():
    print("\033[?25h", end="")

def draw_box(content_lines, width=60, title="", color=C.C, title_color=C.Y):
    """Draw a fancy box around content"""
    horizontal = "─" * (width - 2)
    top = f"{color}╭{horizontal}╮{C.END}"
    bottom = f"{color}╰{horizontal}╯{C.END}"
    
    lines = [top]
    
    if title:
        title_line = f" {title} "
        padding = width - 2 - len(title_line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        lines.append(f"{color}│{C.END}{' ' * left_pad}{title_color}{title_line}{C.END}{' ' * right_pad}{color}│{C.END}")
        lines.append(f"{color}├{horizontal}┤{C.END}")
    
    for line in content_lines:
        visible_len = len(line)
        # Strip ANSI codes for length calculation
        import re
        clean = re.sub(r'\033\[[0-9;]*m', '', line)
        clean_len = len(clean)
        padding = width - 2 - clean_len
        lines.append(f"{color}│{C.END} {line}{' ' * padding} {color}│{C.END}")
    
    lines.append(bottom)
    return "\n".join(lines)

def pulse_text(text, color, times=3):
    """Make text pulse"""
    for _ in range(times):
        print(f"\r{color}{C.BD}{text}{C.END}", end="", flush=True)
        time.sleep(0.3)
        print(f"\r{color}{text}{C.END}", end="", flush=True)
        time.sleep(0.3)
    print()

def sparkle_animation(width=60, duration=1.5):
    """Sparkle effect across the screen"""
    chars = ["✦", "✧", "★", "☆", "✨", "⋆", "✢", "✣"]
    colors = [C.Y, C.C, C.M, C.G, C.B]
    end_time = time.time() + duration
    while time.time() < end_time:
        line = ""
        for _ in range(width // 2):
            line += f"{random.choice(colors)}{random.choice(chars)}{C.END} "
        print(f"\r{line}", end="", flush=True)
        time.sleep(0.1)
    print()

def main():
    hide_cursor()
    try:
        # Pick a quote
        quote = random.choice(QUOTES)
        
        # Clear and start
        clear_screen()
        
        # Opening sparkle
        print(f"\n{C.D}{'=' * 70}{C.END}")
        sparkle_animation(70, 1.0)
        
        # Show Woody ASCII
        print(f"\n{WOODY}")
        time.sleep(0.5)
        
        # Typewriter intro
        typewriter(f"\n{C.M}{C.IT}<< Woody Allen enters the chat... >>{C.END}\n", C.M, 0.02)
        time.sleep(0.3)
        
        # Build quote with word-by-word animation
        words = quote.split()
        
        # First, show empty box
        box_lines = [" " * 50]  # placeholder
        print(draw_box(
            [f"{C.W}{C.IT}{' ' * 50}{C.END}"],
            width=64,
            title=f"{C.BD}WOODY'S WISDOM{C.END}",
            color=C.C,
            title_color=C.Y
        ))
        
        time.sleep(0.5)
        
        # Now animate the quote building up
        current = ""
        for i, word in enumerate(words):
            current += word + " "
            # Re-draw box with current text (using carriage return trick)
            # Clear previous lines (box is ~7 lines + title)
            print("\033[9A", end="")  # Move up 9 lines
            
            # Word wrap for box
            display_lines = []
            line = ""
            for w in current.split():
                if len(line) + len(w) + 1 > 50:
                    display_lines.append(line.strip())
                    line = w + " "
                else:
                    line += w + " "
            if line:
                display_lines.append(line.strip())
            
            # Pad to consistent height
            while len(display_lines) < 3:
                display_lines.append("")
            
            colored_lines = [f"{C.W}{C.IT}{l}{C.END}" for l in display_lines]
            
            print(draw_box(
                colored_lines,
                width=64,
                title=f"{C.BD}WOODY'S WISDOM{C.END}",
                color=C.C,
                title_color=C.Y
            ))
            
            time.sleep(0.15)
        
        # Final pause, then pulse the quote
        time.sleep(0.5)
        
        # Pulse effect on final quote
        print("\033[3A", end="")  # Move to quote line
        for _ in range(2):
            print(f"\r{C.C}│{C.END} {C.Y}{C.BD}{current.strip()}{C.END}{' ' * (50 - len(current))} {C.C}│{C.END}", end="", flush=True)
            time.sleep(0.4)
            print(f"\r{C.C}│{C.END} {C.W}{C.IT}{current.strip()}{C.END}{' ' * (50 - len(current))} {C.C}│{C.END}", end="", flush=True)
            time.sleep(0.4)
        
        # Final sparkle
        print("\n")
        sparkle_animation(70, 0.8)
        
        # Closing thought
        print(f"\n{C.D}{'─' * 70}{C.END}")
        typewriter(f"{C.G}{C.IT}\"The universe is indifferent. So am I, mostly. Pass the anxiety medication.\"{C.END}\n", C.G, 0.02)
        typewriter(f"{C.D}         — Also Woody, probably{C.END}\n\n", C.D, 0.03)
        
        # Final signature
        print(f"{C.C}     ╭────────────────────────────────────────╮{C.END}")
        print(f"{C.C}     │{C.END}  {C.Y}◉   ◉{C.C}  {C.D}Thanks for listening to my neurosis{C.C}  │{C.END}")
        print(f"{C.C}     │{C.END}  {C.Y}  ▽  {C.C}  {C.D}Existential dread provided free of charge{C.C}│{C.END}")
        print(f"{C.C}     ╰────────────────────────────────────────╯{C.END}\n")
        
    finally:
        show_cursor()

if __name__ == "__main__":
    main()