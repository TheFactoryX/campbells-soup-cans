"""
Campbell's Soup Can #1405
Produced: 2026-01-05 10:45:19
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
    Neurotic Stars, Witty Bars
    --------------------------
    A single-file, dependency-free Python script that prints a Woody Allen-esque
    philosophical quote in a visually interesting, ANSI-colorful, and slightly
    animated way. It uses no external libraries—just pure Python magic.
    
    It does the following:
    1. Defines a quote (and some variations) in Woody Allen's style.
    2. Draws an ASCII art microphone and a simple stage.
    3. Prints the quote character-by-character with a "typewriter" effect,
       alternating colors and gently bobbing the text up and down.
    4. Uses standard ANSI escape codes for colors and cursor movement.
    5. Handles terminal resizing gracefully (by checking width).
    6. Cleans up on Ctrl+C.

    Run it directly:
        python3 woody_quote.py

    Or just make it executable:
        chmod +x woody_quote.py
        ./woody_quote.py
"""

import sys
import time
import random
import os
import signal

# --- Configuration & Constants ---

# ANSI Color Codes
FG_COLORS = [
    "\033[38;5;226m",  # Bright Yellow (classic spotlight)
    "\033[38;5;117m",  # Sky Blue
    "\033[38;5;197m",  # Pinkish Red
    "\033[38;5;118m",  # Green
    "\033[38;5;201m",  # Magenta
]
BG_COLORS = [
    "\033[48;5;235m",  # Dark Grey (for the stage)
    "\033[48;5;52m",   # Dark Red
    "\033[48;5;17m",   # Deep Blue
]
RESET = "\033[0m"
BOLD = "\033[1m"
CURSOR_UP = "\033[A"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
CLEAR_LINE = "\033[2K"
CLEAR_SCREEN = "\033[2J"

# --- The Philosophical Content ---

QUOTES = [
    ("I'm not afraid of death; I just don't want to be there when it happens.", "Life is a predicates-only experience, and I want to skip the noun."),
    ("Life is full of misery, loneliness, and suffering - and it's all over much too soon.", "And the credits roll in black and white."),
    ("I don't want to achieve immortality through my work; I want to achieve it through not dying.", "So far, the statistics are discouraging."),
    ("My brain is the second organ in my body that can get excited without my permission.", "The first one is much louder, but less articulate."),
    ("My relationship with death is very simple: I don't want to be there.", "It's the only party I plan on RSVPing 'No' to."),
    ("The world is a comedy to those that think, a tragedy to those that feel.", "And a tax audit to those who fill out forms."),
    ("I'm not paranoid, but I think my toaster is judging my life choices.", "It burns the toast, just like I burn my bridges.")
]

# --- Helpers ---

def get_terminal_size():
    """Returns (width, height) of terminal."""
    try:
        # This is the standard way to get terminal size
        cols, lines = os.get_terminal_size()
        return cols, lines
    except OSError:
        # Fallback for environments where stdout isn't a TTY (like redirection)
        return 80, 24

def clear_terminal():
    """Clears screen and moves cursor to top-left."""
    print(CLEAR_SCREEN, end='')
    print("\033[H", end='') # Move cursor to home

def handle_exit(signum, frame):
    """Ensures clean exit on Ctrl+C."""
    print(SHOW_CURSOR, end='')
    print("\n\n[Exiting gracefully... Don't worry, the existential dread remains.]\n")
    sys.exit(0)

# --- ASCII Art Generator ---

def get_mic_standing(height=6):
    """
    Generates a simple ASCII microphone stand.
    Returns a list of strings.
    """
    # Base: ( )
    # Stand: |
    # Top:  /M\
    
    art = []
    # Top (Mic head)
    art.append("   " + BOLD + FG_COLORS[0] + "/M\\" + RESET)
    # Stem
    for _ in range(height - 2):
        art.append("   |")
    # Stand leg 1
    art.append("  " + FG_COLORS[2] + "/" + RESET + " | " + FG_COLORS[2] + "\\" + RESET)
    # Stand leg 2
    art.append(" " + FG_COLORS[2] + "/" + RESET + "  |  " + FG_COLORS[2] + "\\" + RESET)
    # Base
    art.append("    " + FG_COLORS[2] + "___" + RESET)
    
    return art

def get_curtains(width):
    """
    Returns top and bottom curtain lines based on width.
    """
    if width < 20: return "", ""
    
    # Top curtain: /\/\/\
    curtain_top = (FG_COLORS[2] + "/" + RESET) * (width // 4) + (FG_COLORS[1] + "\\" + RESET) * (width // 4)
    # Bottom curtain: \____/ (simplified)
    curtain_bot = (FG_COLORS[1] + "\\" + RESET) + "_" * (width - 4) + (FG_COLORS[2] + "/" + RESET)
    
    return curtain_top[:width], curtain_bot[:width]

# --- The Animation Engine ---

def draw_stage(screen_w, screen_h, text_lines, text_colors):
    """
    Draws the scene: Curtains, Microphone, and Text.
    
    The strategy:
    1. Calculate layout centers.
    2. Print scene (mics, curtains).
    3. Print text at bottom (Woody style).
    
    NOTE: This function performs a "snapshot" draw. The typewriter effect
    calls this repeatedly to update the frame.
    """
    
    # 1. Calculate Layout
    # We need space for the quote. Let's reserve the bottom 25% for the "stage".
    # The rest is the "sky".
    
    stage_height = max(8, screen_h // 3)
    sky_height = screen_h - stage_height
    
    mic_art = get_mic_standing(4) # A small mic, standing on the stage
    mic_width = max(len(line) for line in mic_art)
    mic_x = (screen_w - mic_width) // 2
    
    # 2. Draw Sky (Empty mostly, just random dots for stars)
    # We only print what's necessary to avoid clearing everything violently.
    # But for simplicity in a single file, we clear screen and rebuild.
    
    output = []
    output.append(CLEAR_SCREEN)
    output.append(HIDE_CURSOR)
    
    # Draw Stars (Random static stars)
    if sky_height > 2:
        stars = min(screen_w * sky_height // 100, 20) # Limit stars
        for _ in range(stars):
            y = random.randint(0, sky_height - 1)
            x = random.randint(0, screen_w - 1)
            # Move cursor to y, x and print a dim star
            output.append(f"\033[{y+1};{x+1}H{BOLD}\033[38;5;245m*{RESET}")

    # 3. Draw Stage (Bottom area)
    stage_top_line = sky_height + 1
    
    # Draw Curtains (Left/Right edges)
    curtain_top, curtain_bot = get_curtains(screen_w)
    if curtain_top:
        output.append(f"\033[{stage_top_line};1H{curtain_top}")
    
    # Draw Microphone (Centered on the stage)
    mic_y_start = stage_top_line + 1
    for i, line in enumerate(mic_art):
        # Center the line of art
        x_pos = mic_x + 1
        y_pos = mic_y_start + i
        output.append(f"\033[{y_pos};{x_pos}H{line}")
    
    # Draw Stage Floor
    floor_y = stage_top_line + len(mic_art) + 1
    if floor_y < screen_h:
        # Draw a floor line
        floor_str = (FG_COLORS[2] + "=" + RESET) * (screen_w // 2)
        output.append(f"\033[{floor_y};1H{floor_str}")

    # 4. Draw The Quote (The "Woody" monologue)
    # It sits at the bottom of the screen, centered.
    
    # We add the text_lines provided. These are partially constructed (typewriter effect).
    # We need to center these lines within the remaining space at the very bottom.
    
    if text_lines:
        # Determine where to start printing text
        # Let's put it just above the very bottom line if possible, or inside the stage area
        
        # Calculate starting row for text (centered in the stage area)
        text_area_height = len(text_lines)
        # Start printing a bit above the floor
        start_text_row = floor_y - text_area_height - 1
        if start_text_row < stage_top_line: 
            start_text_row = stage_top_line + 1
        
        for i, line in enumerate(text_lines):
            # Center the line horizontally
            line_len = len(line.replace('\033', '')) # Approximate visible length
            # Note: Counting visible length correctly with ANSI codes is hard, 
            # but for centering, we just approximate based on screen width.
            # We assume the line is mostly text.
            
            pad_left = (screen_w - len(line)) // 2
            if pad_left < 0: pad_left = 0
            
            # Apply color for this line
            color = text_colors[i % len(text_colors)]
            formatted_line = color + line + RESET
            
            output.append(f"\033[{start_text_row + i + 1};{pad_left + 1}H{formatted_line}")

    # 5. Render everything
    # To minimize flickering, we join all moves and prints into one string
    sys.stdout.write(''.join(output))
    sys.stdout.flush()

# --- Main Logic ---

def run():
    # Register signal handler
    signal.signal(signal.SIGINT, handle_exit)
    
    # 1. Select a quote
    chosen_pair = random.choice(QUOTES)
    # Woody often has a two-part punchline
    line1, line2 = chosen_pair
    
    # 2. Prepare typewriter data
    # We will "type" line 1, pause, then line 2
    # But to make it look like one continuous monologue on screen, 
    # we will treat it as a single block of text that appears line by line.
    
    # We simulate typing by expanding a list of display strings
    full_text_block = [line1, line2]
    displayed_lines = ["", ""] # Start with empty
    
    # Animation parameters
    w, h = get_terminal_size()
    
    # Color palette for text (Woody prefers black and white, but let's add some spotlight drama)
    text_colors = [FG_COLORS[0], FG_COLORS[1], FG_COLORS[4]] # Yellow, Blue, Magenta
    
    # 3. Initial Draw (Empty stage)
    draw_stage(w, h, displayed_lines, text_colors)
    time.sleep(1.5) # Dramatic pause before speaking
    
    # 4. Typewriter Loop
    
    current_line_idx = 0
    current_char_idx = 0
    
    running = True
    while running:
        # Check if terminal resized
        new_w, new_h = get_terminal_size()
        if new_w != w or new_h != h:
            w, h = new_w, new_h
            # On resize, we redraw the scene with whatever text is currently typed
            draw_stage(w, h, displayed_lines, text_colors)
        
        # "Type" a character (or sometimes two for speed)
        if current_line_idx < len(full_text_block):
            target_line = full_text_block[current_line_idx]
            
            if current_char_idx < len(target_line):
                # Add next character(s)
                chars_to_add = 1
                # Randomly type faster or slower
                if random.random() > 0.7: chars_to_add = 2
                
                end_idx = min(current_char_idx + chars_to_add, len(target_line))
                typed_part = target_line[:end_idx]
                
                displayed_lines[current_line_idx] = typed_part
                current_char_idx = end_idx
                
                # Update Scene
                draw_stage(w, h, displayed_lines, text_colors)
                
                # Pause (Variable timing for human feel)
                delay = random.uniform(0.02, 0.09)
                # Punctuation pause
                if target_line[current_char_idx-1] in ['.', ',', ';', '-']:
                    delay += 0.2
                elif target_line[current_char_idx-1] in ['!']:
                    delay += 0.35
                    
                time.sleep(delay)
                
            else:
                # Finished this line, move to next
                current_line_idx += 1
                current_char_idx = 0
                if current_line_idx >= len(full_text_block):
                    # Finished all text
                    running = False
                else:
                    time.sleep(0.8) # Pause between lines
        else:
            running = False

    # 5. Finale (Wait a bit, then add a punchline or exit)
    time.sleep(2)
    
    # Add a "THE END" or a closing visual
    # We'll do a simple fade out or just exit cleanly
    print(SHOW_CURSOR, end='')
    print("\n\n")

if __name__ == "__main__":
    run()