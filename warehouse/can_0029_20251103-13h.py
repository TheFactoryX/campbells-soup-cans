"""
Campbell's Soup Can #29
Produced: 2025-11-03 13:42:18
Worker: Meituan: LongCat Flash Chat (free) (meituan/longcat-flash-chat:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# Clear screen function (works on most terminals)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ANSI color codes
COLORS = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'PURPLE': '\033[95m',
    'CYAN': '\033[96m',
    'WHITE': '\033[97m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
    'END': '\033[0m'
}

# The quote - Woody Allen style
quote_lines = [
    "I'd love to explore the meaning of life,",
    "but honestly, I'm just trying to",
    "make it through lunch without",
    "dropping my soup.",
    "",
    "The existential crisis is real.",
    "Especially when the waiter forgets",
    "your decaf without sugar, which",
    "is basically symbolic of the universe's",
    "indifference to human suffering.",
    "",
    "I don't know if there's a God,",
    "but I do think He'd understand",
    "if I cancelled my therapy appointment"
]

# ASCII Art of a Neurotic Thinker
thinker_art = [
    "       \o/         ",
    "       /\\          ",
    "      /  \\         ",
    "     |    |    ??  ",
    "     |    |         ",
    "     |    |_________",
    "     \\________      ",
    "          \\  /\\     ",
    "           \\/  \\    ",
    "                \\   ",
    "                 |  ",
    "                /   ",
    "               |    ",
    "              ( )   ",
    "             (   )  "
]

# Function to animate text letter by letter
def animate_text(text, color='WHITE', delay=0.05, centered=True):
    term_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 80
    full_text = f"{COLORS[color]}{text}{COLORS['END']}"
    line = ""
    for char in full_text:
        line += char
        sys.stdout.write('\r' + ' ' * ((term_width - len(line)) // 2) + line)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    time.sleep(0.2)

# Function to print centered line
def print_centered(text, color=None):
    term_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 80
    spaces = ' ' * ((term_width - len(text)) // 2)
    if color:
        print(spaces + f"{COLORS[color]}{text}{COLORS['END']}")
    else:
        print(spaces + text)

# Animation: Pulsing color border
def pulsating_border(duration=6):
    colors = ['RED', 'PURPLE', 'BLUE', 'GREEN', 'YELLOW', 'CYAN']
    width = min(60, os.get_terminal_size().columns - 20)
    start_time = time.time()
    
    while time.time() - start_time < duration:
        term_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 80
        colorshift = int((time.time() * 3) % len(colors))
        current_color = colors[colorshift]
        
        # Draw top border
        border1 = f"{COLORS[current_color]}╔{'═' * (width-2)}╗{COLORS['END']}"
        pad1 = ' ' * ((term_width - width) // 2)
        print(pad1 + border1)
        
        # Empty lines with border
        spaces = ' ' * (width - 2)
        for i in range(3):
            line = f"{COLORS[current_color]}║{COLORS['END']}{' ' * ((width - len(thinker_art[i+6]) - 2) // 2) if i < len(thinker_art) else ' '}{COLORS[colors[(colorshift+i+1)%len(colors)]]}{thinker_art[6+i] if i < len(thinker_art) - 6 else ' ' }{(width - (len(thinker_art[6+i]) if i < len(thinker_art) - 6 else 0) - 2 + ((width - len(thinker_art[6+i]) - 2) % 2)) * ' '}{COLORS[current_color]}║{COLORS['END']}"
            pad = ' ' * ((term_width - width) // 2)
            print(pad + line)
        
        # Draw bottom border
        border2 = f"{COLORS[current_color]}╚{'═' * (width-2)}╝{COLORS['END']}"
        pad2 = ' ' * ((term_width - width) // 2)
        print(pad2 + border2)
        
        time.sleep(0.2)
        # Move cursor up if not last iteration
        if time.time() - start_time < duration - 0.2:
            # ANSI: up 5 lines
            print("\033[5A", end="")
    
    # Final position
    term_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 80
    current_color = colors[int(time.time()) % len(colors)]
    border1 = f"{COLORS[current_color]}╔{'═' * (width-2)}╗{COLORS['END']}"
    pad1 = ' ' * ((term_width - width) // 2)
    print(pad1 + border1)
    
    spaces = ' ' * (width - 2)
    for i in range(3):
        line = f"{COLORS[current_color]}║{COLORS['END']}{' ' * ((width - len(thinker_art[i+6]) - 2) // 2)}{COLORS[colors[i]]}{thinker_art[6+i]}{(width - (len(thinker_art[6+i])) - 2 + ((width - len(thinker_art[6+i]) - 2) % 2)) * ' '}{COLORS[current_color]}║{COLORS['END']}"
        pad = ' ' * ((term_width - width) // 2)
        print(pad + line)
    
    border2 = f"{COLORS[current_color]}╚{'═' * (width-2)}╝{COLORS['END']}"
    pad2 = ' ' * ((term_width - width) // 2)
    print(pad2 + border2)

# Glitch effect for the final madness
def glitch_text(lines, duration=4):
    from random import choice, uniform
    colors = ['RED', 'GREEN', 'YELLOW', 'BLUE', 'PURPLE', 'CYAN']
    chars = "!?.,;:\"'()[]{}"
    start = time.time()
    while time.time() - start < duration:
        term_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 80
        width = min(60, term_width - 20)
        pad = ' ' * ((term_width - width) // 2)
        border = pad + f"{COLORS[choice(colors)]}║{COLORS['END']}"
        
        for i, line in enumerate(lines[-4:]):
            if choice([True, False, False, False]):
                # Normal
                glitch_line = line[:12] + ''.join(choice(line) for _ in range(min(10, len(line)-12))) + line[22:]
                full = pad + f"{COLORS[colors[i]]}{glitch_line:<60}{COLORS['END']}"
                if len(full) > width:
                    full = full[:width]
                print('\r' + f"{COLORS[colors[i+1 if (i+1)%4 < len(colors) else 0]]}║{COLORS['END']}" + full + ' ' * (width - len(full) - 2) + f"{COLORS[colors[i+2 if (i+2)%4 < len(colors) else 1]]}║{COLORS['END']}")
            else:
                # Glitch: random characters
                glitch = ''.join(choice(chars) for _ in range(min(width - 4, len(line))))
                color1, color2 = choice(colors), choice(colors)
                print(f"\r{border}{COLORS[color1]}{glitch[:width//2-2]}{COLORS[color2]}{glitch[width//2-2:]}{' '*(width - len(glitch))}{border[1:]}", end="")
            time.sleep(0.08)
        # Move cursor up
        print("\033[4A", end="")
    
    # Finish normally
    colors_last = ['PURPLE', 'BLUE', 'CYAN', 'GREEN']
    for i, line in enumerate(lines[-4:]):
        term_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 80
        width = min(60, term_width - 20)
        pad = ' ' * ((term_width - width) // 2)
        print(pad + f"{COLORS[current_color]}║{COLORS['END']}" + 
              f"{COLORS[colors_last[i]]}{line:<{width-2}}{COLORS['END']}" + 
              f"{COLORS[current_color]}║{COLORS['END']}")

# Main
if __name__ == "__main__":
    try:
        clear_screen()
        
        # Enter "deep thought" mode
        ascii_prompt = [
            "Initializing philosophical mainframe...",
            "Calibrating anxiety level...",
            "Scrolling Wikipedia on 'existential dread'...",
            "Locating therapist's number...",
        ]
        
        for line in ascii_prompt:
            print_centered(line, 'CYAN')
            time.sleep(0.5)
        
        time.sleep(1)
        clear_screen()
        
        # Draw the pulsating border
        pulsating_border(5)
        
        # Add the thinking man
        term_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 80
        width = min(60, term_width - 20)
        pad = ' ' * ((term_width - width) // 2)
        for i in range(6):
            art_line = thinker_art[i]
            spaces_needed = (width - len(art_line) - 2) // 2
            right_pad = (width - len(art_line) - 2) - spaces_needed
            print(pad + f"{COLORS['BLUE']}║{COLORS['END']}" + ' ' * spaces_needed + 
                  f"{COLORS[['GREEN','YELLOW','PURPLE','RED','BLUE'][i%5]]}{art_line}{COLORS['END']}" + 
                  ' ' * right_pad + f"{COLORS['BLUE']}║{COLORS['END']}")
        
        # Print the quote animating each line
        for i, line in enumerate(quote_lines):
            center_width = width - 4
            centered_line = line.center(center_width).replace("  ", " ")
            animate_text(centered_line, color=['CYAN','GREEN','PURPLE','RED','YELLOW','BLUE','PURPLE'][i % 7], delay=0.02, centered=False)
        
        # Final punchline
        time.sleep(1)
        print_centered("      – Woody Allen (probably, if he had time between panic attacks)", 'YELLOW')
        time.sleep(2)
        
        # Add glitch effect for the final existential dread
        glitch_text(quote_lines)
        
        # Final winky face
        time.sleep(0.5)
        term_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 80
        print('\r'+ ' ' * ((term_width - 5) // 2) + f"{COLORS['GREEN']}Byeeee! ☹{COLORS['END']}")
        time.sleep(1.5)
        
    except (KeyboardInterrupt, SystemExit):
        print('\n\n' + ' ' * ((os.get_terminal_size().columns - 40) // 2 if hasattr(os, 'get_terminal_size') else 20) + 
              f"{COLORS['CYAN']}Even existential crises can be disrupted.{COLORS['END']}\n")
        sys.exit()
    except Exception as e:
        print(f"Oops: {e}")