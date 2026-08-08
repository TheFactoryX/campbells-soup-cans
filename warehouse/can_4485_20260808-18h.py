"""
Campbell's Soup Can #4485
Produced: 2026-08-08 18:58:25
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
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BG_BLACK = '\033[40m'
    BG_BLUE = '\033[44m'

# Woody Allen style quotes (original)
QUOTES = [
    "I asked the universe for a sign. It sent me a bill for my therapy sessions.",
    "My analyst says I have a death wish. I told him it's more of a death preference.",
    "I don't believe in an afterlife, but I'm bringing a change of underwear just in case.",
    "The universe is indifferent to my suffering. The least it could do is pretend to care.",
    "I have a fear of commitment. And abandonment. And commitment to abandonment.",
    "My therapist fell asleep during our session. I took it as a metaphor for the human condition.",
    "I'm not paranoid. The universe really IS out to get me. It just has terrible aim.",
    "Death is nature's way of telling you to slow down. My doctor says the same thing about cholesterol."
]

# ASCII Art Frames for "Woody" character
WOODY_FRAMES = [
    r"""
     \  |  /
      \ | /
       \|/
    __(@ @)__
   /  ( v )  \
  |   \_/   |
   \        /
    `~~~~~~`
""",
    r"""
     \  |  /
      \ | /
       \|/
    __(o o)__
   /  ( v )  \
  |   \_/   |
   \        /
    `~~~~~~`
""",
    r"""
     \  |  /
      \ | /
       \|/
    __(- -)__
   /  ( v )  \
  |   \_/   |
   \        /
    `~~~~~~`
""",
]

# Decorative elements
STARS = ['✦', '✧', '★', '☆', '✩', '✪', '✫', '✬', '✭', '✮', '✯', '✰']
SPARKLES = ['✨', '✦', '✧', '⋆', '✩', '✪']

def clear_screen():
    print('\033[2J\033[H', end='')

def move_cursor(row, col):
    print(f'\033[{row};{col}H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, color=C.WHITE, delay=0.03, newline=True):
    for char in text:
        print(f'{color}{char}{C.RST}', end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def glitter_text(text, color=C.YELLOW):
    result = ''
    for char in text:
        if char != ' ' and random.random() < 0.15:
            result += f'{C.MAGENTA}{random.choice(SPARKLES)}{C.RST}'
        result += f'{color}{char}{C.RST}'
    return result

def draw_box(width, height, title="", color=C.CYAN):
    top = f'{color}┌{"─" * (width - 2)}┐{C.RST}'
    bottom = f'{color}└{"─" * (width - 2)}┘{C.RST}'
    middle = f'{color}│{" " * (width - 2)}│{C.RST}'
    
    lines = [top]
    if title:
        title_line = f'{color}│ {C.BOLD}{C.YELLOW}{title.center(width - 4)}{C.RST}{color} │{C.RST}'
        lines.append(title_line)
        lines.append(f'{color}├{"─" * (width - 2)}┤{C.RST}')
        for _ in range(height - 4):
            lines.append(middle)
    else:
        for _ in range(height - 2):
            lines.append(middle)
    lines.append(bottom)
    return '\n'.join(lines)

def animated_background(width, height, frame):
    bg = []
    for y in range(height):
        line = ''
        for x in range(width):
            if (x + y + frame) % 7 == 0:
                line += f'{C.DIM}{random.choice(STARS)}{C.RST}'
            elif (x * 2 + y * 3 + frame) % 11 == 0:
                line += f'{C.DIM}·{C.RST}'
            else:
                line += ' '
        bg.append(line)
    return '\n'.join(bg)

def main():
    hide_cursor()
    clear_screen()
    
    quote = random.choice(QUOTES)
    
    # Terminal dimensions (assume reasonable size)
    term_width = 70
    term_height = 24
    
    # Animation frames
    total_frames = 60
    
    for frame in range(total_frames):
        clear_screen()
        
        # Draw animated background
        bg = animated_background(term_width, 12, frame)
        print(bg)
        
        # Draw Woody character (animated)
        woody_frame = WOODY_FRAMES[frame % len(WOODY_FRAMES)]
        woody_colored = ''
        for line in woody_frame.strip('\n').split('\n'):
            woody_colored += f'{C.YELLOW}{line}{C.RST}\n'
        
        # Center the woody art
        woody_lines = woody_colored.strip().split('\n')
        for line in woody_lines:
            padding = (term_width - len(line.replace('\033[93m', '').replace('\033[0m', ''))) // 2
            print(' ' * max(0, padding) + line)
        
        print()
        
        # Draw the quote box
        box_width = 64
        box_height = 7
        
        # Top border with sparkles
        top_border = f'{C.CYAN}┌{"─" * (box_width - 2)}┐{C.RST}'
        print(top_border.center(term_width))
        
        # Title line
        title = f'{C.CYAN}│ {C.BOLD}{C.YELLOW}WOODY ALLEN\'s DAILY DOSE OF EXISTENTIAL DREAD{C.RST}{C.CYAN} │{C.RST}'
        print(title.center(term_width + 10))
        
        # Separator
        sep = f'{C.CYAN}├{"─" * (box_width - 2)}┤{C.RST}'
        print(sep.center(term_width))
        
        # Quote lines (word wrap)
        words = quote.split()
        lines = []
        current_line = []
        current_length = 0
        max_line_width = box_width - 6  # padding
        
        for word in words:
            if current_length + len(word) + 1 <= max_line_width:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word) + 1
        if current_line:
            lines.append(' '.join(current_line))
        
        # Print quote lines with typing effect on final frame
        if frame == total_frames - 1:
            # Typewriter effect for final display
            for i, line in enumerate(lines):
                quote_line = f'{C.CYAN}│ {C.WHITE}{line.center(max_line_width)}{C.RST}{C.CYAN} │{C.RST}'
                print(quote_line.center(term_width + 10))
                time.sleep(0.15)
            
            # Empty lines to fill box
            for _ in range(box_height - 4 - len(lines)):
                empty = f'{C.CYAN}│{" " * (box_width - 2)}│{C.RST}'
                print(empty.center(term_width))
        else:
            # Static display during animation
            for i, line in enumerate(lines):
                # Add subtle color shift
                hue_shift = (frame + i * 3) % 6
                colors = [C.WHITE, C.CYAN, C.GREEN, C.YELLOW, C.MAGENTA, C.BLUE]
                line_color = colors[hue_shift]
                quote_line = f'{C.CYAN}│ {line_color}{line.center(max_line_width)}{C.RST}{C.CYAN} │{C.RST}'
                print(quote_line.center(term_width + 10))
            
            for _ in range(box_height - 4 - len(lines)):
                empty = f'{C.CYAN}│{" " * (box_width - 2)}│{C.RST}'
                print(empty.center(term_width))
        
        # Bottom border
        bottom = f'{C.CYAN}└{"─" * (box_width - 2)}┘{C.RST}'
        print(bottom.center(term_width))
        
        print()
        
        # Decorative footer
        footer_quotes = [
            f'{C.DIM}"I\'d call him a sadist, but he\'d probably enjoy the label."{C.RST}',
            f'{C.DIM}— Probably his mother{C.RST}',
            f'{C.DIM}✦  Neurosis is just consciousness with better marketing  ✦{C.RST}',
        ]
        footer = footer_quotes[frame // 20 % len(footer_quotes)]
        print(footer.center(term_width))
        
        # Sparkle trail
        if frame % 3 == 0:
            sparkle_line = ' '.join([f'{C.MAGENTA}{random.choice(SPARKLES)}{C.RST}' for _ in range(8)])
            print(sparkle_line.center(term_width))
        
        time.sleep(0.08)
    
    # Final pause with subtle animation
    for i in range(10):
        time.sleep(0.3)
        # Blink the quote slightly
        pass
    
    show_cursor()
    print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear_screen()
        print(f'\n{C.YELLOW}The universe has been notified of your interruption.{C.RST}')
        print(f'{C.DIM}It remains indifferent.{C.RST}\n')
    except Exception as e:
        show_cursor()
        print(f'\n{C.RED}Something went wrong. Even the code has anxiety.{C.RST}')
        print(f'{C.DIM}{e}{C.RST}\n')