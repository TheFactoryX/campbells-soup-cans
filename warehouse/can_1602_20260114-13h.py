"""
Campbell's Soup Can #1602
Produced: 2026-01-14 13:09:08
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

# ANSI Color and Style Escape Codes
class A:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m' # Not widely supported, but included for flavor
    # Colors
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GRAY = '\033[90m'
    ORANGE = '\033[38;5;208m' # 256 color support
    PINK = '\033[38;5;213m'
    BOLD_RED = '\033[1;31m'
    BOLD_YELLOW = '\033[1;33m'
    
    # Backgrounds
    BG_DARK = '\033[48;5;236m'
    BG_LIGHT = '\033[48;5;255m'

def clear_screen():
    """Clears the terminal screen."""
    print("\033[H\033[J", end="")

def set_cursor(x, y):
    """Moves cursor to specific coordinates (1-based)."""
    print(f"\033[{y};{x}H", end="", flush=True)

def hide_cursor():
    print("\033[?25l", end="")

def show_cursor():
    print("\033[?25h", end="")

def get_terminal_size():
    """Returns width, height of terminal."""
    import shutil
    return shutil.get_terminal_size()

def print_centered(text, width):
    """Prints text centered within a width."""
    print(" " * ((width - len(text)) // 2) + text)

def slow_print(text, delay=0.03):
    """Prints text character by character for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_quote():
    """Returns a random Woody Allen style quote."""
    quotes = [
        ("I'm not afraid of death;", "I just don't want to be there when it happens."),
        ("Life is full of misery,", "loneliness, and suffering"),
        ("and it's all over much too soon."),
        ("My brain lives in a constant state", "of panic, like a toddler in a mall."),
        ("I don't want to achieve immortality", "through my work; I want it through not dying."),
        ("I'm two with nature.", "Oops, I mean teamed with nature."),
        ("I'm astounded by people who want to", "know the universe when it's hard enough to figure out your own."),
        ("My relationship with death is", "very casual. We nod when we pass.")
    ]
    return random.choice(quotes)

def woody_animation():
    """Main animation controller."""
    width, height = get_terminal_size()
    
    # Frame dimensions
    box_w = min(60, width - 6)
    box_h = 8
    box_x = (width - box_w) // 2 + 1
    box_y = (height - box_h) // 2 + 1
    
    hide_cursor()
    clear_screen()

    # 1. The Quote appears in fragments (typewriter effect)
    # We render into a buffer and then print the whole frame to avoid flicker
    
    line1, line2 = get_quote()
    
    # Build the ASCII Art Frame
    def draw_frame(msg_l1, msg_l2, style="normal"):
        set_cursor(1, 1)
        
        # Top border
        top = f"{A.GRAY}┌{'─' * (box_w - 2)}┐{A.RESET}"
        print(" " * (box_x - 1) + top)
        
        # Side borders with text
        empty_row = " " * (box_w - 2)
        
        # Calculate text padding to center it
        pad_l1 = (box_w - 2 - len(msg_l1)) // 2
        pad_l2 = (box_w - 2 - len(msg_l2)) // 2
        
        # Style choices
        if style == "neurotic":
            color = A.PINK
            frame_color = A.BOLD_RED
            stress = " ! "
        elif style == "existential":
            color = A.BLUE
            frame_color = A.CYAN
            stress = " ? "
        elif style == "final":
            color = A.ORANGE
            frame_color = A.YELLOW
            stress = " X "
        else:
            color = A.WHITE
            frame_color = A.GRAY
            stress = " | "
        
        # Middle rows
        for i in range(box_h - 2):
            row_text = " " * (box_w - 2)
            row_display = f"{frame_color}│{A.RESET}{row_text}{frame_color}│{A.RESET}"
            
            if i == 1:
                # Decoration line top
                row_display = f"{frame_color}│{A.GRAY}{'=' * (box_w - 2)}{frame_color}│{A.RESET}"
            elif i == 2:
                # Quote Line 1
                txt = color + A.BOLD + msg_l1 + A.RESET
                filler = " " * (box_w - 2 - len(msg_l1))
                row_text = " " * pad_l1 + txt + filler
                row_display = f"{frame_color}│{A.RESET}{row_text}{frame_color}│{A.RESET}"
            elif i == 3:
                # Quote Line 2
                txt = color + A.ITALIC + msg_l2 + A.RESET
                filler = " " * (box_w - 2 - len(msg_l2))
                row_text = " " * pad_l2 + txt + filler
                row_display = f"{frame_color}│{A.RESET}{row_text}{frame_color}│{A.RESET}"
            elif i == 4:
                # Decoration line bottom
                row_display = f"{frame_color}│{A.GRAY}{'-' * (box_w - 2)}{frame_color}│{A.RESET}"
            elif i == 5:
                # Neurotic signature
                sig = " - Woody (anxious)"
                if style == "existential": sig = " - W. Allen"
                if style == "final": sig = " - THE END"
                
                row_text = " " * (box_w - 2 - len(sig)) + sig
                row_display = f"{frame_color}│{A.GRAY}{row_text}{frame_color}│{A.RESET}"

            print(" " * (box_x - 1) + row_display)
        
        # Bottom border
        bottom = f"{frame_color}└{'─' * (box_w - 2)}┘{A.RESET}"
        print(" " * (box_x - 1) + bottom)
        
        # Add some "nervous" decorations around the box
        if style == "neurotic":
            set_cursor(box_x - 4, box_y + 2)
            print(f"{A.RED}!!{A.RESET}", end="")
            set_cursor(box_x + box_w + 1, box_y + 3)
            print(f"{A.RED}?{A.RESET}", end="")
        elif style == "existential":
            set_cursor(box_x - 2, box_y + 4)
            print(f"{A.BLUE}o{A.RESET}", end="")
            set_cursor(box_x + box_w + 2, box_y + 5)
            print(f"{A.BLUE}o{A.RESET}", end="")

    # --- ANIMATION SEQUENCE ---

    # 1. Start with a blank, shaking frame
    for _ in range(5):
        draw_frame(" ", " ", style="normal")
        time.sleep(0.05)
        set_cursor(box_x, box_y)
        print(" " * box_w * box_h, end="") # quick clear of box area
    
    # 2. Type out line 1 (Neurotic phase)
    current_l1 = ""
    for char in line1:
        current_l1 += char
        draw_frame(current_l1, " ", style="neurotic")
        time.sleep(0.05 + (random.random() * 0.1)) # Inconsistent typing speed (nervous)
    
    time.sleep(0.5)
    
    # 3. Type out line 2 (Existential phase)
    current_l2 = ""
    for char in line2:
        current_l2 += char
        draw_frame(line1, current_l2, style="existential")
        time.sleep(0.04)
    
    # 4. Pause for effect
    time.sleep(1.2)
    
    # 5. Shake and fade out (Neurotic breakdown)
    for _ in range(8):
        style = "existential" if _ % 2 == 0 else "neurotic"
        draw_frame(line1, line2, style=style)
        # Create a visual shake by moving cursor randomly within the box
        rx = random.randint(box_x + 2, box_x + box_w - 4)
        ry = random.randint(box_y + 2, box_y + box_h - 3)
        set_cursor(rx, ry)
        print(f"{A.GRAY}*{A.RESET}", end="", flush=True)
        time.sleep(0.05)
        
    # 6. Final state (Quiet acceptance)
    time.sleep(0.2)
    draw_frame("I have no answer.", "The silence is loud.", style="final")
    
    # Leave the cursor at the bottom
    print("\n" * (height - (box_y + box_h + 2)))
    show_cursor()

if __name__ == "__main__":
    try:
        woody_animation()
    except KeyboardInterrupt:
        show_cursor()
        print(f"\n{A.RESET}Exiting gracefully... (or not)")
    except Exception as e:
        show_cursor()
        print(f"{A.RESET}\nAn existential error occurred: {e}")