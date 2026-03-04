"""
Campbell's Soup Can #2555
Produced: 2026-03-04 02:50:00
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random
import os

# Get terminal width safely
try:
    term_width = os.get_terminal_size().columns
except:
    term_width = 80

# Colors
NEON_GREEN = '\033[92m'
NEON_PINK = '\033[95m'
NEON_YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'
BLINK = '\033[5m'

# Woody Allen-esque philosophical quotes
quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "I'm not anti-social. I'm just not user-friendly.",
    "Eternal nothingness is fine with me. I'm not sure I want to be remembered.",
    "I think crime pays. There's no other way I can explain my accountant.",
    "I wouldn't say I'm neurotic, but I am the kind of person who would take a lie detector test about my own innocence.",
    "My one regret in life is that I am not someone else.",
    "I'm not saying I'm a genius, but I did stay at a Holiday Inn Express last night.",
    "The difference between sex and death is, with death you can do it alone and nobody complains."
]

# Pick a random quote
selected_quote = random.choice(quotes)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_neurotic_border(width, char='░'):
    """Draw a wobbly, neurotic-looking border."""
    return char * width

def typewriter_effect(text, color=NEON_GREEN, delay=0.03, end='\n'):
    """Print text with typewriter effect and random micro-delays."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        # Woody Allen-style micro-anxiety: slightly random delays
        time.sleep(delay + random.uniform(-0.01, 0.01))
    print(end=end)

def print_centered(text, color=CYAN):
    """Print text centered in terminal."""
    padding = max(0, (term_width - len(text)) // 2)
    print(' ' * padding + color + text + RESET)

def animate_thought_bubbles():
    """Animate floating thought bubbles."""
    bubbles = ['?', '!', '...', '⁉', '⚠', '💭']
    for _ in range(5):
        bubble = random.choice(bubbles)
        col = random.choice([NEON_PINK, NEON_YELLOW, CYAN])
        pos = random.randint(10, term_width - 10)
        print('\r' + ' ' * pos + col + bubble + RESET, end='', flush=True)
        time.sleep(0.2)
    print('\r' + ' ' * term_width, end='\r')

def main():
    clear_screen()
    
    # Opening "neurotic" animation
    print_centered("🧠 Woody Allen's Philosophical Dispensary 🧠", NEON_PINK)
    print()
    
    # Wobbly border
    border = draw_neurotic_border(min(60, term_width - 4), '▁▂▃▄▅▆▇')
    print_centered(border, CYAN)
    print()
    
    # The quote with dramatic buildup
    time.sleep(0.5)
    print_centered(" PRESENTS ", NEON_YELLOW + BLINK)
    time.sleep(0.3)
    print()
    
    # Format the quote in a "thought box"
    quote_lines = []
    words = selected_quote.split()
    current_line = ""
    for word in words:
        if len(current_line + word) + 1 <= 50:  # Wrap at 50 chars
            current_line += word + " "
        else:
            quote_lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        quote_lines.append(current_line.strip())
    
    # Print quote in centered box
    for line in quote_lines:
        padded_line = line.center(50)
        print_centered("│ " + padded_line + " │", NEON_GREEN)
    
    print()
    print_centered(border, CYAN)
    print()
    
    # Dramatic pause
    time.sleep(1)
    
    # Animated signature
    signature = "— Woody Allen (probably)"
    typewriter_effect(signature.center(term_width), NEON_PINK, 0.02)
    
    # Thought bubbles animation
    time.sleep(0.5)
    animate_thought_bubbles()
    
    # Final neurotic flourish
    print()
    print_centered("(This quote has been approved by my therapist)", CYAN)
    print_centered("(She's heard worse)", CYAN)
    
    # Prompt for existential contemplation
    time.sleep(1)
    print()
    print_centered("Press Enter to contemplate the void...", NEON_YELLOW + BLINK)
    input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{CYAN}[Existential crisis interrupted]{RESET}")
        sys.exit(0)