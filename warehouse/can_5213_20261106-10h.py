"""
Campbell's Soup Can #5213
Produced: 2026-11-06 10:53:48
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

# Woody Allen color palette
RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
DIM = '\033[2m'

# Colors
NEUROSIS_RED = '\033[38;5;196m'
ANXIETY_ORANGE = '\033[38;5;208m'
EXISTENTIAL_YELLOW = '\033[38;5;226m'
THERAPIST_GREEN = '\033[38;5;46m'
FREUD_BLUE = '\033[38;5;39m'
MOTHER_PURPLE = '\033[38;5;165m'
DEATH_GRAY = '\033[38;5;240m'
WHITE = '\033[38;5;255m'
BLACK = '\033[38;5;16m'

BG_DARK = '\033[48;5;16m'
BG_RED = '\033[48;5;124m'
BG_BLACK = '\033[48;5;0m'

CLEAR = '\033[2J\033[H'
CURSOR_HIDE = '\033[?25l'
CURSOR_SHOW = '\033[?25h'

# Original Woody Allen-style quote
QUOTE = "I told my analyst I have a fear of commitment. He said, 'That'll be $300.' I said, 'Can I pay in installments?' He said, 'Only if you commit to all of them.'"

ATTRIBUTION = "— Woody Allen (probably, or maybe just my subconscious billing me)"

# ASCII frames for a little neurotic character
FRAMES = [
    r"""
      \ o /
       | |
      /   \  """,
    r"""
      \ - /
       | |
      /   \  """,
    r"""
      \ o /
       | |
      /   \  """,
    r"""
      \ @ /
       | |
      /   \  """,
]

# Nervous eye frames
EYE_FRAMES = [
    r"  (o.o)  ",
    r"  (O.o)  ",
    r"  (o.O)  ",
    r"  (-.-)  ",
    r"  (o.o)  ",
    r"  (o.o)  ",
]

def typewriter(text, color=WHITE, delay=0.03, newline=True):
    """Typewriter effect with color."""
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def glitch_text(text, color=WHITE, iterations=3):
    """Glitch effect on text."""
    chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
    for _ in range(iterations):
        glitched = ''.join(random.choice(chars) if random.random() < 0.1 else c for c in text)
        sys.stdout.write(f"\r{color}{glitched}{RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write(f"\r{color}{text}{RESET}")
    sys.stdout.flush()

def draw_box(content_lines, border_color=FREUD_BLUE, bg=BG_DARK, padding=2):
    """Draw a fancy box around content."""
    max_len = max(len(line) for line in content_lines)
    width = max_len + padding * 2
    
    top = f"{border_color}┌{'─' * width}┐{RESET}"
    bottom = f"{border_color}└{'─' * width}┘{RESET}"
    empty = f"{border_color}│{' ' * width}│{RESET}"
    
    print(top)
    print(empty)
    for line in content_lines:
        padded = line.center(width)
        print(f"{border_color}│{bg}{padded}{RESET}{border_color}│{RESET}")
    print(empty)
    print(bottom)

def animate_neurotic(duration=3):
    """Animate a little neurotic character."""
    start = time.time()
    frame_idx = 0
    eye_idx = 0
    
    while time.time() - start < duration:
        sys.stdout.write(CURSOR_HIDE)
        sys.stdout.write('\033[H')
        
        frame = FRAMES[frame_idx % len(FRAMES)]
        eyes = EYE_FRAMES[eye_idx % len(EYE_FRAMES)]
        
        # Random twitch
        if random.random() < 0.3:
            twitch = random.choice(["  *twitch*  ", "  *sweats*  ", "  *panics*  ", "  *breathes*  "])
        else:
            twitch = "             "
        
        sys.stdout.write(f"{ANXIETY_ORANGE}{frame}{RESET}\n")
        sys.stdout.write(f"{NEUROSIS_RED}{eyes}{RESET} {twitch}\n")
        sys.stdout.write(f"{DIM}    | |    {RESET}\n")
        sys.stdout.write(f"{DIM   }   / \\   {RESET}\n")
        
        sys.stdout.flush()
        time.sleep(0.2)
        
        # Move cursor up to overwrite
        sys.stdout.write('\033[5A')
        
        frame_idx += 1
        eye_idx += 1
    
    sys.stdout.write(CURSOR_SHOW)
    print("\n" * 5)

def main():
    print(CLEAR + CURSOR_HIDE)
    
    # Opening animation - neurotic thoughts scrolling
    thoughts = [
        "Am I breathing correctly?",
        "Did I lock the door?",
        "Is that a symptom?",
        "Why did I say that in 1997?",
        "Does my analyst like me?",
        "Am I dying? Probably.",
        "Should I have ordered the salad?",
        "Is this quote too long?",
        "Mother was right about everything.",
        "Death is just God's way of saying 'timeout'.",
    ]
    
    print(f"{BG_DARK}{WHITE}")
    print(" " * 60)
    print("  NEUROTIC THOUGHT STREAM INITIALIZING...")
    print(" " * 60)
    print(RESET)
    time.sleep(0.5)
    
    for i, thought in enumerate(thoughts):
        color = random.choice([NEUROSIS_RED, ANXIETY_ORANGE, EXISTENTIAL_YELLOW, MOTHER_PURPLE, DEATH_GRAY])
        prefix = f"{DIM}[{i+1:02d}]{RESET} "
        typewriter(prefix + thought, color, delay=0.01)
        time.sleep(0.15)
    
    print()
    time.sleep(0.5)
    
    # The quote reveal with animation
    print(f"{FREUD_BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print()
    
    # Split quote into parts for dramatic effect
    parts = [
        ("I told my analyst I have a fear of commitment.", NEUROSIS_RED),
        ("He said, 'That'll be $300.'", ANXIETY_ORANGE),
        ("I said, 'Can I pay in installments?'", EXISTENTIAL_YELLOW),
        ("He said, 'Only if you commit to all of them.'", THERAPIST_GREEN),
    ]
    
    for text, color in parts:
        typewriter(f"  {text}", color, delay=0.02)
        time.sleep(0.4)
    
    print()
    time.sleep(0.3)
    
    # Attribution with glitch
    print(f"  {DIM}{'─' * 50}{RESET}")
    glitch_text(f"  {ATTRIBUTION}", MOTHER_PURPLE, iterations=2)
    print()
    print()
    
    # Philosophical addendum
    addendums = [
        "The universe is indifferent. My analyst charges $300/hour for that insight.",
        "I'm not afraid of death. I just don't want to be there when the bill arrives.",
        "Life is a sexually transmitted terminal condition. My copay is $40.",
        "God is silent. My mother? Never. Not even during anesthesia.",
    ]
    
    chosen = random.choice(addendums)
    typewriter(f"  {ITALIC}{chosen}{RESET}", DEATH_GRAY, delay=0.015)
    print()
    print()
    
    # Final box
    draw_box([
        f"{BOLD}DIAGNOSIS:{RESET} Existential Anxiety Disorder",
        f"{BOLD}PROGNOSIS:{RESET} Chronic (but billable)",
        f"{BOLD}TREATMENT:{RESET} Humor, denial, & installment plans",
    ], border_color=FREUD_BLUE, bg=BG_DARK)
    
    print()
    print(f"{DIM}Press Ctrl+C to schedule your next session...{RESET}")
    print(CURSOR_SHOW)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{NEUROSIS_RED}Session terminated. That'll be $300.{RESET}")
        print(CURSOR_SHOW)
        sys.exit(0)