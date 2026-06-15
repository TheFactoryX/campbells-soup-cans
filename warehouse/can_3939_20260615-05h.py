"""
Campbell's Soup Can #3939
Produced: 2026-06-15 05:27:35
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
Woody Allen Quote Generator - A neurotic existential experience
Pure Python, no dependencies, maximum anxiety
"""

import sys
import time
import random

# ─── ANSI Color Palette ───
class C:
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    
    # Foreground
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GRAY = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    
    # Background
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

# ─── The Quote (Original Woody Allen Style) ───
WOODY_QUOTE = (
    "I took a speed-reading course and finished 'War and Peace' in twenty minutes.\n"
    "It's about Russia. Also, I'm pretty sure I left the stove on."
)

# ─── ASCII Art: Woody's Profile ───
WOODY_FACE = r"""
        ╭─────────────╮
       /   @     @   \
      |    \  ^  /    |   "I have a very bad feeling
      |     \___/     |    about this... everything."
       \   \___/   /
        ╰─────────╯
          | | | |
         /___|___\
"""

# ─── ASCII Art: Neurotic Thought Bubble ───
THOUGHT_BUBBLE_TOP = r"""
      .-'-._.-'-._.-'-._.-'-.
     /  _  _  _  _  _  _  _  \
    |  ( ) ( ) ( ) ( ) ( ) ( ) |
    |                         |
"""
THOUGHT_BUBBLE_BOTTOM = r"""
    |                         |
     \  _  _  _  _  _  _  _  /
      '-'-._.-'-._.-'-._.-'-'
"""

# ─── Animation Frames ───
SPINNER_FRAMES = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
PULSE_FRAMES = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃', '▂']

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, color=C.WHITE, delay=0.03, newline=True):
    """Type out text character by character"""
    for char in text:
        print(f'{color}{char}{C.RST}', end='', flush=True)
        time.sleep(delay + random.uniform(-0.01, 0.01))
    if newline:
        print()

def glitch_text(text, color=C.RED, intensity=3):
    """Create a glitch effect on text"""
    glitch_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/~`'
    result = list(text)
    for _ in range(intensity):
        idx = random.randint(0, len(result) - 1)
        if result[idx] != ' ' and result[idx] != '\n':
            result[idx] = random.choice(glitch_chars)
    return f'{color}{"".join(result)}{C.RST}'

def draw_box(content_lines, border_color=C.CYAN, title=None, padding=1):
    """Draw a fancy box around content"""
    max_len = max(len(line) for line in content_lines)
    width = max_len + padding * 2
    
    top = f'{border_color}╭{"─" * width}╮{C.RST}'
    bottom = f'{border_color}╰{"─" * width}╯{C.RST}'
    
    lines = [top]
    if title:
        title_line = f'{border_color}│{C.RST} {C.BOLD}{C.YELLOW}{title.center(width)}{C.RST} {border_color}│{C.RST}'
        lines.append(title_line)
        lines.append(f'{border_color}├{"─" * width}┤{C.RST}')
    
    for line in content_lines:
        padded = line.ljust(max_len)
        lines.append(f'{border_color}│{C.RST} {" " * padding}{padded}{" " * padding} {border_color}│{C.RST}')
    
    lines.append(bottom)
    return '\n'.join(lines)

def animate_spinner(duration=2.0, message="Contemplating existence"):
    """Show a spinning animation"""
    hide_cursor()
    start = time.time()
    i = 0
    try:
        while time.time() - start < duration:
            frame = SPINNER_FRAMES[i % len(SPINNER_FRAMES)]
            print(f'\r{C.CYAN}{frame}{C.RST} {C.ITALIC}{message}{C.RST} {C.CYAN}{frame}{C.RST}', end='', flush=True)
            time.sleep(0.08)
            i += 1
        print('\r' + ' ' * (len(message) + 10) + '\r', end='')
    finally:
        show_cursor()

def animate_pulse(text, duration=1.5, color=C.MAGENTA):
    """Pulse animation on text"""
    hide_cursor()
    start = time.time()
    i = 0
    try:
        while time.time() - start < duration:
            frame = PULSE_FRAMES[i % len(PULSE_FRAMES)]
            print(f'\r{color}{frame}{frame} {text} {frame}{frame}{C.RST}', end='', flush=True)
            time.sleep(0.06)
            i += 1
        print('\r' + ' ' * (len(text) + 10) + '\r', end='')
    finally:
        show_cursor()

def neurotic_typing_effect():
    """Simulate neurotic back-and-forth typing"""
    thoughts = [
        "Maybe I should...",
        "No, wait, what if—",
        "Okay, but seriously,",
        "Does anyone actually know?",
        "I mean, really know?",
        "The stove. The stove.",
    ]
    
    for thought in thoughts:
        # Type
        for char in thought:
            print(f'{C.GRAY}{char}{C.RST}', end='', flush=True)
            time.sleep(0.04)
        time.sleep(0.3)
        # Delete (neurotic second-guessing)
        for _ in thought:
            print('\b \b', end='', flush=True)
            time.sleep(0.02)
        time.sleep(0.15)
    print()

def main():
    clear_screen()
    hide_cursor()
    
    try:
        # ─── Opening: Existential Loading ───
        print(f'\n{C.BOLD}{C.BRIGHT_CYAN}')
        print('  ╔══════════════════════════════════════════════════════════════╗')
        print('  ║     WOODY ALLEN QUOTE GENERATOR v3.14159 (UNSTABLE)          ║')
        print('  ║     "Because the universe needed more neurotic wisdom"       ║')
        print('  ╚══════════════════════════════════════════════════════════════╝')
        print(f'{C.RST}\n')
        
        # Simulate "system check"
        checks = [
            ("Initializing existential dread...", 0.5),
            ("Loading neuroses database...", 0.4),
            ("Calibrating self-deprecation matrix...", 0.6),
            ("Checking if stove is off...", 0.8),
            ("Verifying mortality awareness...", 0.5),
            ("Downloading pessimism updates...", 0.3),
        ]
        
        for msg, dur in checks:
            print(f'  {C.DIM}[{C.RST}{C.GREEN}✓{C.RST}{C.DIM}]{C.RST} {C.WHITE}{msg}{C.RST}')
            time.sleep(dur)
        
        print(f'\n  {C.YELLOW}⚠ Warning: Quote may cause sudden urge to see analyst{C.RST}\n')
        time.sleep(0.5)
        
        # ─── Neurotic Typing Animation ───
        print(f'  {C.ITALIC}Accessing memory banks...{C.RST}\n')
        neurotic_typing_effect()
        
        # ─── Spinner: Deep Thought ───
        animate_spinner(1.5, "Consulting inner monologue")
        
        # ─── Reveal Woody's Face ───
        print(f'\n{C.BRIGHT_YELLOW}{WOODY_FACE}{C.RST}')
        time.sleep(0.3)
        
        # ─── The Quote in a Thought Bubble ───
        quote_lines = WOODY_QUOTE.split('\n')
        
        # Build the bubble
        bubble_lines = []
        max_width = max(len(line) for line in quote_lines)
        
        # Top of bubble
        print(f'{C.CYAN}      .-\'-\'._.-\'-\'._.-\'-\'._.-\'-\'._.{C.RST}')
        print(f'{C.CYAN}     /  ' + ' ' * (max_width + 2) + '  \\{C.RST}')
        
        # Quote lines with typing effect
        for i, line in enumerate(quote_lines):
            padding = max_width - len(line)
            left_pad = ' ' * 5
            print(f'{C.CYAN}    |  {C.RST}{C.BOLD}{C.WHITE}', end='', flush=True)
            
            # Typewriter effect for each line
            for char in line:
                print(char, end='', flush=True)
                time.sleep(0.025)
            
            print(f'{C.RST}{C.CYAN}{" " * padding}  |{C.RST}')
            time.sleep(0.15)
        
        # Bottom of bubble
        print(f'{C.CYAN}    |  ' + ' ' * (max_width + 2) + '  |{C.RST}')
        print(f'{C.CYAN}     \\  ' + '_' * (max_width + 2) + '  /{C.RST}')
        print(f'{C.CYAN}      \'-\'-\'._.-\'-\'._.-\'-\'._.-\'-\'._.\'{C.RST}\n')
        
        time.sleep(0.5)
        
        # ─── Neurotic Afterthoughts ───
        afterthoughts = [
            ("Wait, did I say Russia? I meant... does it matter?", C.YELLOW),
            ("The stove. I definitely left the stove on.", C.RED),
            ("Or was it the iron? Does anyone even own an iron anymore?", C.MAGENTA),
            ("My analyst says I have 'catastrophic thinking.'", C.CYAN),
            ("I told him 'Catastrophic is my baseline.'", C.GREEN),
            ("He nodded. That cost me $300.", C.BRIGHT_RED),
        ]
        
        print(f'  {C.DIM}{"─" * 60}{C.RST}\n')
        
        for thought, color in afterthoughts:
            # Pulse animation on each afterthought
            animate_pulse(thought, 0.8, color)
            print(f'  {color}{thought}{C.RST}')
            time.sleep(0.2)
        
        print(f'\n  {C.DIM}{"─" * 60}{C.RST}\n')
        
        # ─── Final Boxed Wisdom ───
        final_wisdom = [
            f'{C.ITALIC}"Life is divided into the horrible and the miserable."{C.RST}',
            f'{C.DIM}— Also Woody Allen, probably{C.RST}',
        ]
        
        box = draw_box(final_wisdom, border_color=C.BRIGHT_MAGENTA, title=' FINAL THOUGHT ')
        print(f'\n{box}\n')
        
        # ─── Exit Animation ───
        print(f'  {C.CYAN}Shutting down existential crisis...{C.RST}')
        for i in range(3, 0, -1):
            print(f'  {C.YELLOW}{i}{C.RST}', end=' ', flush=True)
            time.sleep(0.4)
        print(f'{C.GREEN}Acceptance achieved. (Temporarily.){C.RST}\n')
        
        # ─── Credits ───
        print(f'  {C.DIM}Original quote written in the style of Woody Allen{C.RST}')
        print(f'  {C.DIM}No analysts were harmed in the making of this program{C.RST}')
        print(f'  {C.DIM}The stove is probably fine. Probably.{C.RST}\n')
        
    finally:
        show_cursor()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        print(f'\n\n{C.RED}Interrupted. The universe wins this round.{C.RST}\n')
        sys.exit(0)
    except Exception as e:
        show_cursor()
        print(f'\n{C.RED}Error: {e}{C.RST}')
        print(f'{C.YELLOW}Even the code has anxiety.{C.RST}\n')