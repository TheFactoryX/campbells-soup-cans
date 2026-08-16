"""
Campbell's Soup Can #4639
Produced: 2026-08-16 23:33:43
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

# ANSI Color Codes
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
    BL = '\033[5m'      # Blink
    RV = '\033[7m'      # Reverse
    X = '\033[0m'       # Reset

# Woody Allen quotes (original, in his voice)
QUOTES = [
    "I took a speed-reading course and read War and Peace in twenty minutes.\nIt involves Russia.",
    "My therapist told me I have a narcissistic personality disorder.\nI told him, 'That's impossible — I'm too modest.'",
    "I don't believe in an afterlife, although I am bringing a change of underwear.",
    "The universe is merely a fleeting idea in God's mind —\na pretty uncomfortable thought, especially if you've just paid for a mortgage.",
    "I'm not afraid of death. I just don't want to be there when it happens.\nUnless they serve those little sandwiches. Then I'll stay for the reception.",
    "Life is divided into the horrible and the miserable.\nThe horrible are terminal cases. The miserable is everyone else.\nI'm miserable. You should be so lucky.",
    "I once tried to commit suicide by inhaling next to an insurance salesman.\nTurns out, boredom isn't fatal. Just feels like it.",
    "If only God would give me a clear sign! Like a large deposit in my name\nat a Swiss bank. Or a note: 'Woody, the rash is benign.'",
    "My one regret in life is that I am not someone else.\nPreferably someone with better posture and a trust fund.",
    "You can live to be a hundred if you give up all the things\nthat make you want to live to be a hundred.\nSo I'll die young. But well-fed.",
]

def clear_screen():
    print('\033[2J\033[H', end='')

def typewriter(text, color=C.W, delay=0.02, jitter=0.01):
    for char in text:
        sys.stdout.write(f"{color}{char}{C.X}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-jitter, jitter))
    print()

def sparkle_line(width=60, color=C.Y):
    chars = "✦✧★☆⋆✵✸✹✺✷"
    line = ''.join(random.choice(chars) for _ in range(width))
    print(f"{color}{line}{C.X}")

def draw_box(title, content, title_color=C.M, border_color=C.C, content_color=C.W):
    lines = content.split('\n')
    max_len = max(len(line) for line in lines)
    max_len = max(max_len, len(title) + 4)
    padding = 2
    inner_w = max_len + padding * 2
    
    # Top border with title
    title_pad = (inner_w - len(title) - 2) // 2
    top = f"{border_color}╭{'─' * title_pad} {title_color}{title} {border_color}{'─' * (inner_w - title_pad - len(title) - 2)}╮{C.X}"
    print(top)
    
    # Content lines
    for line in lines:
        pad_right = inner_w - len(line) - padding
        print(f"{border_color}│{C.X}{' ' * padding}{content_color}{line}{C.X}{' ' * pad_right}{border_color}│{C.X}")
    
    # Bottom border
    print(f"{border_color}╰{'─' * inner_w}╯{C.X}")

def neurotic_loader():
    frames = [
        "🧠  Overthinking...",
        "🧠  Replaying conversation from 2003...",
        "🧠  Worrying about mortality...",
        "🧠  Checking if stove is off (it is)...",
        "🧠  Wondering if I locked the door...",
        "🧠  Existential dread loading ████░░░░░░ 40%...",
        "🧠  Questioning all life choices...",
        "🧠  Ah, there it is. A thought.",
    ]
    for frame in frames:
        sys.stdout.write(f"\r{C.D}{frame}{C.X}")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\r" + " " * 50 + "\r", end='')

def woody_face():
    faces = [
        f"""
{C.Y}     ┌─────────┐{C.X}
{C.Y}     │  {C.D}•   •{C.Y}  │{C.X}  {C.IT}"Why is there something{C.X}
{C.Y}     │  {C.D}  ─  {C.Y}  │{C.X}  {C.IT}rather than nothing?{C.X}
{C.Y}     │ {C.D}└───┘ {C.Y} │{C.X}  {C.IT}And why is the rent so high?"{C.X}
{C.Y}     └─────────┘{C.X}
        """,
        f"""
{C.Y}      \\  {C.D}♠ ♠{C.Y}  /{C.X}
{C.Y}       \\ {C.D}  ─  {C.Y} /{C.X}   {C.IT}"I'm not a hypochondriac.{C.X}
{C.Y}        \\{C.D} └─┘ {C.Y}/ {C.X}   {C.IT}I'm an alarmist."{C.X}
{C.Y}         `───'{C.X}
        """,
        f"""
{C.Y}    .─────────.{C.X}
{C.Y}   / {C.D}○   ○ {C.Y} \\{C.X}   {C.IT}"The food here is terrible{C.X}
{C.Y}   | {C.D}  ▲  {C.Y} |{C.X}   {C.IT}and such small portions!"{C.X}
{C.Y}   \\ {C.D}└───┘ {C.Y} /{C.X}
{C.Y}    `─────────'{C.X}
        """,
    ]
    return random.choice(faces)

def main():
    clear_screen()
    
    # Opening sparkle
    sparkle_line(70, C.M)
    
    # Title animation
    title = "WOODY ALLEN WISDOM GENERATOR™"
    for i in range(len(title) + 1):
        sys.stdout.write(f"\r{C.BD}{C.C}{title[:i]}{C.X}")
        sys.stdout.flush()
        time.sleep(0.04)
    print()
    
    sparkle_line(70, C.M)
    print()
    
    # Neurotic loading
    neurotic_loader()
    print()
    
    # Woody face
    print(woody_face())
    print()
    
    # The quote
    quote = random.choice(QUOTES)
    
    # Dramatic pause
    time.sleep(0.5)
    
    # Typewriter the quote inside a box
    draw_box(
        f"{C.BD}PHILOSOPHICAL GEM{C.X}",
        quote,
        title_color=C.Y,
        border_color=C.B,
        content_color=C.W
    )
    
    print()
    
    # Closing neurotic thought
    closers = [
        f"{C.D}...Anyway, I have a doctor's appointment at 3.{C.X}",
        f"{C.D}...Is that a pain in my side? Probably nothing. Or cancer.{C.X}",
        f"{C.D}...I should really floss more.{C.X}",
        f"{C.D}...My mother would have hated this quote.{C.X}",
        f"{C.D}...Time for my nap. And by nap I mean staring at the ceiling.{C.X}",
    ]
    typewriter(random.choice(closers), C.D, delay=0.03)
    
    print()
    sparkle_line(70, C.M)
    print(f"{C.D}    (Press Ctrl+C to escape existence){C.X}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.R}\n    Fine. Leave. See if I care.{C.X}")
        print(f"{C.D}    (Exit stage left, pursued by anxiety){C.X}\n")
        sys.exit(0)