"""
Campbell's Soup Can #4909
Produced: 2026-09-05 22:57:57
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Quote Generator - A neurotic philosophical experience
"""

import sys
import time
import random

# ANSI Color Codes
class C:
    RST = '\033[0m'
    BLD = '\033[1m'
    DIM = '\033[2m'
    ITL = '\033[3m'
    UL = '\033[4m'
    BLK = '\033[30m'
    RED = '\033[31m'
    GRN = '\033[32m'
    YEL = '\033[33m'
    BLU = '\033[34m'
    MAG = '\033[35m'
    CYN = '\033[36m'
    WHT = '\033[37m'
    BG_BLK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GRN = '\033[42m'
    BG_YEL = '\033[43m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYN = '\033[46m'
    BG_WHT = '\033[47m'

# Woody Allen style quotes (original)
QUOTES = [
    "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia.",
    "My therapist says I have a preoccupation with death. I told her, 'We all do, we're just not billing for it.'",
    "I don't believe in an afterlife, but I'm bringing a change of underwear just in case.",
    "The universe is indifferent to my existence. Which is fine, I'm indifferent to most of the universe's restaurants.",
    "I have a philosophical problem with reality. It keeps happening whether I consent or not.",
    "Life is a tragedy for those who feel, a comedy for those who think, and a tax audit for those who file.",
    "I'm not afraid of dying. I just don't want to be conscious for the Yelp reviews.",
    "God is silent. My analyst is silent. My mother calls three times a day. Coincidence?",
    "I've developed a new philosophy: I only dread the future on days that end in 'y'.",
    "Existential dread is just your soul's way of saying 'you forgot to floss.'",
]

def typewriter(text, color=C.WHT, delay=0.02, end='\n'):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay)
    print(end=end)

def clear_screen():
    """Clear terminal screen"""
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def draw_box(content_lines, width=70, title="", color=C.CYN, accent=C.YEL):
    """Draw a fancy ASCII box around content"""
    horizontal = "─" * (width - 2)
    top = f"{color}┌{horizontal}┐{C.RST}"
    bottom = f"{color}└{horizontal}┘{C.RST}"
    
    lines = [top]
    
    if title:
        title_line = f" {title} "
        padding = width - 2 - len(title_line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        lines.append(f"{color}│{accent}{' ' * left_pad}{C.BLD}{title_line}{C.RST}{accent}{' ' * right_pad}{C.RST}{color}│{C.RST}")
        lines.append(f"{color}├{horizontal}┤{C.RST}")
    
    for line in content_lines:
        visible_len = len(line)
        # Strip ANSI codes for length calculation
        import re
        clean = re.sub(r'\033\[[0-9;]*m', '', line)
        padding = width - 2 - len(clean)
        lines.append(f"{color}│{C.RST} {line}{' ' * padding} {color}│{C.RST}")
    
    lines.append(bottom)
    return '\n'.join(lines)

def woody_face():
    """Return ASCII Woody Allen face"""
    return [
        f"{C.YEL}       .--.       {C.RST}",
        f"{C.YEL}      / .. \\      {C.RST}",
        f"{C.YEL}     |  __  |     {C.RST}",
        f"{C.YEL}     | (  ) |     {C.RST}",
        f"{C.YEL}      \\ '--' /     {C.RST}",
        f"{C.YEL}       '----'      {C.RST}",
        f"{C.DIM}   (glasses adjust){C.RST}",
    ]

def pulse_animation(frames, duration=2.0):
    """Run a pulsing animation"""
    start = time.time()
    frame_duration = duration / len(frames)
    while time.time() - start < duration:
        for frame in frames:
            sys.stdout.write('\033[H' + frame)
            sys.stdout.flush()
            time.sleep(frame_duration)

def main():
    # Pick a quote
    quote = random.choice(QUOTES)
    
    # Clear screen
    clear_screen()
    
    # Build the quote display with word-by-word reveal
    words = quote.split()
    
    # Initial frame - just the face and empty box
    face_lines = woody_face()
    empty_content = [
        "",
        f"{C.DIM}{' ' * 20}...{C.RST}",
        "",
        f"{C.DIM}{' ' * 18}loading neuroses...{C.RST}",
        "",
    ]
    
    # Show face with thinking animation
    thinking_frames = []
    for i in range(4):
        dots = "." * (i + 1)
        content = [
            "",
            f"{C.DIM}{' ' * 20}thinking{dots}{C.RST}",
            "",
            f"{C.ITL}{' ' * 15}\"Wait, did I leave the stove on?\"{C.RST}",
            "",
        ]
        box = draw_box(content, width=70, title=f"{C.BLD}WOODY ALLEN'S DAILY DOSE{C.RST}", color=C.BLU, accent=C.YEL)
        frame = "\n".join(face_lines) + "\n\n" + box
        thinking_frames.append(frame)
    
    pulse_animation(thinking_frames, 1.5)
    
    # Now reveal the quote word by word
    revealed = []
    for i, word in enumerate(words):
        revealed.append(word)
        current_text = ' '.join(revealed)
        
        # Split into lines if too long
        content_lines = []
        line = ""
        for w in revealed:
            if len(line) + len(w) + 1 > 55:
                content_lines.append(line)
                line = w
            else:
                line = line + " " + w if line else w
        if line:
            content_lines.append(line)
        
        # Center the lines
        centered = []
        for cl in content_lines:
            pad = (55 - len(cl)) // 2
            centered.append(" " * pad + cl)
        
        # Add attribution
        centered.append("")
        centered.append(f"{C.DIM}{' ' * 20}— Woody Allen (probably){C.RST}")
        
        box = draw_box(centered, width=70, title=f"{C.BLD}WOODY ALLEN'S DAILY DOSE{C.RST}", color=C.BLU, accent=C.YEL)
        frame = "\n".join(face_lines) + "\n\n" + box
        
        sys.stdout.write('\033[H' + frame)
        sys.stdout.flush()
        time.sleep(0.12)
    
    # Final pause with subtle blink
    for _ in range(3):
        time.sleep(0.4)
        # Blink the quote
        blink_content = [f"{C.BLD}{line}{C.RST}" if line.strip() and not line.strip().startswith("—") else line for line in centered]
        box = draw_box(blink_content, width=70, title=f"{C.BLD}{C.RED}WOODY ALLEN'S DAILY DOSE{C.RST}", color=C.RED, accent=C.YEL)
        frame = "\n".join(face_lines) + "\n\n" + box
        sys.stdout.write('\033[H' + frame)
        sys.stdout.flush()
        time.sleep(0.2)
        
        box = draw_box(centered, width=70, title=f"{C.BLD}WOODY ALLEN'S DAILY DOSE{C.RST}", color=C.BLU, accent=C.YEL)
        frame = "\n".join(face_lines) + "\n\n" + box
        sys.stdout.write('\033[H' + frame)
        sys.stdout.flush()
    
    # Final message at bottom
    print(f"\n{C.DIM}Press Ctrl+C to schedule your next existential crisis...{C.RST}")
    
    # Keep the quote visible
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{C.YEL}\nFine, leave. The universe doesn't need you either.{C.RST}\n")

if __name__ == "__main__":
    # Check if terminal supports ANSI
    if not sys.stdout.isatty():
        # Fallback for non-TTY
        quote = random.choice(QUOTES)
        print(f"\n{quote}\n\n— Woody Allen (probably)\n")
    else:
        main()