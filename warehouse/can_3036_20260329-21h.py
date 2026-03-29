"""
Campbell's Soup Can #3036
Produced: 2026-03-29 21:47:29
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
import time
import sys
import os

# ── WOODY ALLEN QUOTES (neurotic, existential, self-deprecating) ─────────────────
quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "I took a test in Existentialism. I left all the answers blank and got a zero.",
    "My only interest in religion is that I'm against it.",
    "I'm not against religion, but I am against the Holy Rollers. They're too enthusiastic.",
    "I'm not against religion. I just don't want anyone who believes in God running the government.",
    "I'm not against God. I'm against the people who believe in Him.",
    "I'm not against God. I'm against the people who believe in Him and then try to make me believe in Him too.",
    "I'm not against God. I'm against the people who believe in Him and then try to make me believe in Him too, and then get mad when I don't.",
    "I don't believe in an afterlife, but I'm going to take a change of underwear anyway.",
    "I don't believe in an afterlife, but I'm taking a change of underwear just in case.",
    "I don't want to be immortal through my work. I want to be immortal through not dying.",
    "I'm not against God. I'm against the people who believe in Him and then try to make me believe in Him too, and then get mad when I don't, and then try to convert me, and then get mad when I won't, and then try to save me, and then get mad when I can't be saved, and then try to pray for me, and then get mad when I don't want to be prayed for, and then try to... you know what I mean?",
    "I'm not against God. I'm against the people who believe in Him and then try to make me believe in Him too, and then get mad when I don't, and then try to convert me, and then get mad when I won't, and then try to save me, and then get mad when I can't be saved, and then try to pray for me, and then get mad when I don't want to be prayed for, and then try to... you know what I mean? I mean, if God exists, why doesn't He just come down and tell us Himself?",
    "I'm not against God. I'm against the people who believe in Him and then try to make me believe in Him too, and then get mad when I don't, and then try to convert me, and then get mad when I won't, and then try to save me, and then get mad when I can't be saved, and then try to pray for me, and then get mad when I don't want to be prayed for, and then try to... you know what I mean? I mean, if God exists, why doesn't He just come down and tell us Himself? And if He doesn't exist, why are we all so worried about it?",
]

# ── ANSI COLORS & UTILITIES ─────────────────────────────────────────────────────
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright foreground colors
    BR_BLACK = '\033[90m'
    BR_RED = '\033[91m'
    BR_GREEN = '\033[92m'
    BR_YELLOW = '\033[93m'
    BR_BLUE = '\033[94m'
    BR_MAGENTA = '\033[95m'
    BR_CYAN = '\033[96m'
    BR_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03, color=Colors.WHITE, end='\n', flush=True):
    """Print text with typewriter effect."""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    if flush:
        sys.stdout.flush()

def flicker_text(text, color=Colors.YELLOW, flicker_count=3, base_delay=0.1):
    """Make text flicker like a neon sign."""
    for _ in range(flicker_count):
        sys.stdout.write(color + text + Colors.RESET)
        sys.stdout.flush()
        time.sleep(base_delay * 0.3)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
        time.sleep(base_delay * 0.2)
    sys.stdout.write(color + text + Colors.RESET + '\n')
    sys.stdout.flush()

def draw_woody_head():
    """ASCII art of Woody Allen's face."""
    return [
        "        .--.",
        "       |o_o |",
        "       |:_/ |",
        "      //   \\ \\",
        "     (|     | )",
        "    /'\\_   _/`\\",
        "    \\___)=(___/"
    ]

# ── MAIN PROGRAM ────────────────────────────────────────────────────────────────
def main():
    clear_screen()
    
    # Get terminal width
    try:
        term_width = os.get_terminal_size().columns
    except:
        term_width = 80
    
    # Randomly select a quote
    quote = random.choice(quotes)
    
    # ── DECORATIVE HEADER ───────────────────────────────────────────────────────
    woody_face = draw_woody_head()
    print(Colors.BR_YELLOW + "=" * term_width + Colors.RESET)
    
    # Center Woody's face
    for line in woody_face:
        padding = (term_width - len(line)) // 2
        print(' ' * padding + Colors.BR_CYAN + line + Colors.RESET)
    
    print(Colors.BR_YELLOW + "=" * term_width + Colors.RESET)
    time.sleep(0.5)
    
    # ── QUOTE PRESENTATION ─────────────────────────────────────────────────────
    # Create decorative box
    box_width = min(70, term_width - 4)
    horizontal = "─" * (box_width - 2)
    
    print(Colors.BG_BLUE + Colors.WHITE + Colors.BOLD)
    print(f"╔{horizontal}╗")
    print(Colors.RESET, end='')
    
    # Split quote into lines that fit the box
    words = quote.split()
    lines = []
    current_line = []
    for word in words:
        test_line = ' '.join(current_line + [word])
        if len(test_line) <= box_width - 6:  # Account for padding and borders
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    
    # Print each line with fancy formatting
    for i, line in enumerate(lines):
        padding = (box_width - 2 - len(line)) // 2
        extra = (box_width - 2 - len(line)) % 2
        
        # Random occasional color shift for neurotic effect
        if random.random() < 0.1:
            line_color = Colors.BR_RED
        else:
            line_color = Colors.BR_WHITE
        
        print(Colors.BG_BLUE + Colors.WHITE + "║" + Colors.RESET, end='')
        print(' ' * (padding + extra), end='')
        
        if i == 0:  # First line with emphasis
            typewriter(line, delay=0.04, color=Colors.BOLD + line_color, end='')
        else:
            typewriter(line, delay=0.03, color=line_color, end='')
        
        print(' ' * padding + Colors.BG_BLUE + Colors.WHITE + "║" + Colors.RESET)
        time.sleep(0.2 if i < len(lines)-1 else 0.5)
    
    print(Colors.BG_BLUE + Colors.WHITE + Colors.BOLD)
    print(f"╚{horizontal}╝")
    print(Colors.RESET)
    
    # ── WOODY'S SIGNATURE STYLE ─────────────────────────────────────────────────
    time.sleep(0.3)
    
    # Flickering attribution
    attribution = "― Woody Allen (probably)"
    flicker_text(attribution, color=Colors.BR_YELLOW, flicker_count=4)
    
    # ── PHILOSOPHICAL POSTSCRIPT ───────────────────────────────────────────────
    time.sleep(0.5)
    
    # Random existential musings
    postscripts = [
        "*(This quote brought to you by existential dread and neurotic commas)*",
        "*(I think, therefore I'm... confused)*",
        "*(My analyst says I'm afraid of commitment. I'm afraid of everything.)*",
        "*(If this makes sense, you've misunderstood it.)*",
        "*(Disclaimer: Not actually funny. Just clinically depressed.)*"
    ]
    
    postscript = random.choice(postscripts)
    typewriter(postscript, delay=0.02, color=Colors.DIM + Colors.BR_BLACK)
    
    # ── FINAL WOODY-ESQUE DISCLAIMER ───────────────────────────────────────────
    time.sleep(1)
    disclaimer = random.choice([
        "So that's it. I'm going to go lie down.",
        "I have to go. My therapist is waiting. She's probably right about everything.",
        "Excuse me. I have to go check if I'm still alive.",
        "Well, that's enough philosophy for one lifetime.",
        "I think I'll go eat something. That usually helps."
    ])
    
    typewriter("\n" + disclaimer, delay=0.05, color=Colors.ITALIC + Colors.BR_CYAN)

# ── EXECUTION ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + Colors.RED + "*(Interrupted by existential crisis)*" + Colors.RESET)
        sys.exit(0)