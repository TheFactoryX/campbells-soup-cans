"""
Campbell's Soup Can #1147
Produced: 2025-12-24 13:02:20
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import sys
import time
import random
import os

# --- Configuration ---
TEXT = "Life is full of suffering, loneliness, and chocolate. I'm not sure which is which."
# Try different themes!
THEMES = {
    'drama': {
        'border': '█',
        'corner': '◆',
        'color': '\033[31m',  # Red
        'bg': '\033[40m',     # Black
    },
    'hopeful': {
        'border': '▓',
        'corner': '✦',
        'color': '\033[33m',  # Yellow
        'bg': '\033[44m',     # Blue
    },
    'cosmic': {
        'border': '░',
        'corner': '★',
        'color': '\033[35m',  # Magenta
        'bg': '\033[45m',     # Magenta
    }
}

# --- Utility Functions ---
def get_terminal_size():
    try:
        cols, rows = os.get_terminal_size()
        return cols, rows
    except:
        return 80, 24

def clear_screen():
    # Clears screen and hides cursor
    sys.stdout.write('\033[2J\033[?25l')
    sys.stdout.flush()

def reset_terminal():
    # Shows cursor and resets colors
    sys.stdout.write('\033[?25h\033[0m')
    sys.stdout.flush()

def get_input_timeout(timeout):
    """Wait for user input, but return after timeout."""
    import select
    
    # Linux/Unix specific implementation for non-blocking input
    if sys.stdin.isatty():
        rlist, _, _ = select.select([sys.stdin], [], [], timeout)
        if rlist:
            return sys.stdin.read(1)
    else:
        # Fallback for non-tty environments (like IDEs), just wait normally
        time.sleep(timeout)
    return None

# --- Animation Logic ---

def type_writer(text, speed=0.03):
    """Types out text like a neurotic thinker."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Randomize typing speed slightly for human effect
        time.sleep(speed * random.uniform(0.8, 1.5))
    print()

def draw_box(text, theme_name='drama'):
    """Draws a fancy box around the text."""
    theme = THEMES[theme_name]
    cols, _ = get_terminal_size()
    
    # Pad text to ensure box fits
    padding = 4
    text_len = len(text)
    box_width = min(cols - 4, text_len + 6)
    
    # Calculate margins to center
    margin = (cols - box_width) // 2
    m_str = " " * margin
    
    # Colors
    reset = '\033[0m'
    style = theme['color'] + theme['bg']
    
    # Construct Box
    top = f"{m_str}{style}{theme['corner']}{theme['border']*(box_width-2)}{theme['corner']}{reset}"
    mid = f"{m_str}{style}{theme['border']} {text.center(box_width-4)} {theme['border']}{reset}"
    bot = f"{m_str}{style}{theme['corner']}{theme['border']*(box_width-2)}{theme['corner']}{reset}"
    
    return top, mid, bot

def bouncing_text(text, theme_name):
    """Bounces the quote around the terminal."""
    cols, rows = get_terminal_size()
    
    # Position
    x, y = cols // 4, rows // 3
    dx, dy = 1, 1
    
    # Get box lines
    theme = THEMES[theme_name]
    reset = '\033[0m'
    
    count = 0
    while count < 30: # Run for a limited duration
        # Clear previous position (approximation)
        # We can't easily do double buffering in pure basic python without libs,
        # so we will use a dirty "wipe" by overwriting with spaces in the next frame.
        # A better way for pure python is to redraw the whole screen, but let's keep it simple.
        
        # Actually, the easiest "bouncer" in pure stdout is to just print spaces
        # to clear the area, but since we don't know exactly where it was,
        # we'll do a full clear and redraw. It's jarring but effective for single file.
        
        clear_screen()
        
        # Build the frame
        # Visual trick: Multiple overlapping lines to look like a 'ghost'
        box_text = f"{theme['color']}{text}{reset}"
        
        # Print spacing
        sys.stdout.write('\n' * y)
        
        # Print left margin
        sys.stdout.write(' ' * x)
        
        # Print the text (with simple bounce effect colors)
        if count % 2 == 0:
            sys.stdout.write(theme['color'])
        else:
            sys.stdout.write('\033[36m') # Cyan alternate
            
        sys.stdout.write(text + reset)
        sys.stdout.write('\n')
        
        # Update Physics
        if x <= 1 or x >= cols - len(text) - 2:
            dx = -dx
        if y <= 1 or y >= rows - 3:
            dy = -dy
            
        x += dx
        y += dy
        
        # Exit if key pressed
        sys.stdout.write("\n\n(Press any key to skip bouncing) ")
        sys.stdout.flush()
        
        # Non-blocking check for input
        key = get_input_timeout(0.08)
        if key:
            return # Stop bouncing
        
        count += 1

def curtain_fall(text, theme_name):
    """A dramatic curtain fall effect."""
    cols, _ = get_terminal_size()
    theme = THEMES[theme_name]
    msg = f"{theme['color']}{text}{reset}"
    
    clear_screen()
    print("\n" * 2)
    
    for i in range(cols // 2 + 2):
        # Create the curtain walls
        left = "█" * i
        right = "█" * i
        
        # Calculate spacing
        space_len = cols - (i * 2)
        if space_len < 0: space_len = 0
        
        # Position text initially in center, then fade
        text_display = ""
        if i < (cols // 4):
            text_display = msg
            # Fade text out by hiding cursor and overwriting
            pass
        
        # Construct Line
        line = f"\r\033[31m{left}\033[0m{text_display.center(space_len)}\033[31m{right}\033[0m"
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(0.03)
        
        # Check for key press to skip
        if i > 2:
            # Just a tiny check, though curtain is fast
            pass

def dramatic_reveal(text, theme_name='cosmic'):
    """Prints the quote with flickering lights."""
    theme = THEMES[theme_name]
    cols, _ = get_terminal_size()
    clear_screen()
    
    lines = [
        " " * (cols // 2 - 10) + f"\033[1;37m*** THE COSMIC TRUTH ***\033[0m",
        "",
        " " * (cols // 2 - 5) + f"{theme['bg']}{theme['color']}{text}{reset}",
        "",
        " " * (cols // 2 - 10) + "\033[3m- A. Anonymous\033[0m"
    ]
    
    # Flicker effect
    for _ in range(5):
        clear_screen()
        sys.stdout.write(random.choice(lines))
        sys.stdout.flush()
        time.sleep(0.05)
        
    # Steady shine
    clear_screen()
    for line in lines:
        print(line)
    
    print("\n\n")


# --- Main Execution ---

def main():
    try:
        # 1. Intro (Matrix/Cyberpunk glitch style)
        sys.stdout.write("\033[32m") # Green
        print(">>> INITIALIZING NEUROTIC PHILOSOPHY ENGINE...")
        time.sleep(0.5)
        print(">>> CALIBRATING ANXIETY LEVELS... [100%]")
        time.sleep(0.3)
        print(">>> QUERYING MEANING OF EXISTENCE...")
        time.sleep(0.7)
        sys.stdout.write("\033[0m")
        
        # 2. Choose Theme randomly
        theme_name = random.choice(list(THEMES.keys()))
        
        # 3. First Effect: Typewriter + Box
        print("\n" * 2)
        typed_text = f"Analyze: '{TEXT}'"
        type_writer(typed_text, speed=0.04)
        time.sleep(0.5)
        
        # Draw static box
        top, mid, bot = draw_box(TEXT, theme_name)
        print(top)
        print(mid)
        print(bot)
        time.sleep(1.5)
        
        # 4. Second Effect: Bouncing Text
        bouncing_text(TEXT, theme_name)
        
        # 5. Third Effect: Dramatic Reveal (Fade in / Curtains)
        print("\n")
        print("\033[3m[Press Enter for final dramatic conclusion...]\033[0m")
        # Wait for enter or timeout
        get_input_timeout(5) 
        
        dramatic_reveal(TEXT, theme_name)
        
    except KeyboardInterrupt:
        print("\n\n\033[31mInterrupted! Just like my plans.\033[0m")
    except Exception as e:
        print(f"\n\033[31mSystem Error: {e}\033[0m")
    finally:
        reset_terminal()

if __name__ == "__main__":
    main()