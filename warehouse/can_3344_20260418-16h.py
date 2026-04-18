"""
Campbell's Soup Can #3344
Produced: 2026-04-18 16:57:45
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

def typewriter_effect(text, delay=0.03, color_code=None, end_char='\n'):
    if color_code:
        sys.stdout.write(color_code)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if color_code:
        sys.stdout.write('\033[0m')
    sys.stdout.write(end_char)

def color_wave(text, duration=3):
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    start_time = time.time()
    color_index = 0
    
    while time.time() - start_time < duration:
        sys.stdout.write(colors[color_index])
        sys.stdout.write(text + '\n')
        sys.stdout.write('\033[0m\n')
        sys.stdout.flush()
        
        color_index = (color_index + 1) % len(colors)
        time.sleep(0.3)

def woody_allen_quote():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Woody Allen style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens. Unless there's open bar."
    
    # ASCII art frame
    frame_width = len(quote) + 6
    
    # Colors
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    
    # Title
    title = "WOODY ALLEN'S PHILOSOPHICAL REFLECTIONS"
    
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Animated title
    typewriter_effect(title.center(frame_width), 0.04, BLUE)
    
    # Animated quote reveal with typewriter effect
    typewriter_effect(BLUE + "╔" + "═" * frame_width + "╗", 0.02)
    typewriter_effect(BLUE + "║  " + YELLOW, 0.02, end_char='')
    
    # Typewriter effect for the quote itself
    for char in quote:
        sys.stdout.write(YELLOW + char)
        sys.stdout.flush()
        time.sleep(0.03)
    
    typewriter_effect(BLUE + "  ║", 0.02)
    typewriter_effect(BLUE + "╚" + "═" * frame_width + "╝", 0.02)
    
    # Animated signature
    woody_signature = "─ Woody Allen ─"
    for i in range(3):
        sys.stdout.write(BLUE)
        sys.stdout.write("─" * ((frame_width - len(woody_signature)) // 2))
        sys.stdout.write(PURPLE)
        sys.stdout.write(woody_signature)
        sys.stdout.write(BLUE)
        sys.stdout.write("─" * ((frame_width - len(woody_signature)) // 2))
        sys.stdout.write('\n')
        sys.stdout.flush()
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        typewriter_effect(title.center(frame_width), 0.04, BLUE)
        typewriter_effect(BLUE + "╔" + "═" * frame_width + "╗", 0.02)
        typewriter_effect(BLUE + "║  " + YELLOW, 0.02, end_char='')
        
        for char in quote:
            sys.stdout.write(YELLOW + char)
            sys.stdout.flush()
            time.sleep(0.03)
        
        typewriter_effect(BLUE + "  ║", 0.02)
        typewriter_effect(BLUE + "╚" + "═" * frame_width + "╝", 0.02)
        time.sleep(0.3)
    
    # Final display
    os.system('cls' if os.name == 'nt' else 'clear')
    typewriter_effect(title.center(frame_width), 0.04, BLUE)
    
    typewriter_effect(BLUE + "╔" + "═" * frame_width + "╗", 0.02)
    typewriter_effect(BLUE + "║  " + YELLOW, 0.02, end_char='')
    
    for char in quote:
        sys.stdout.write(YELLOW + char)
        sys.stdout.flush()
        time.sleep(0.03)
    
    typewriter_effect(BLUE + "  ║", 0.02)
    typewriter_effect(BLUE + "╚" + "═" * frame_width + "╝", 0.02)
    
    woody_signature = "─ Woody Allen ─"
    sys.stdout.write(BLUE)
    sys.stdout.write("─" * ((frame_width - len(woody_signature)) // 2))
    sys.stdout.write(PURPLE)
    sys.stdout.write(woody_signature)
    sys.stdout.write(BLUE)
    sys.stdout.write("─" * ((frame_width - len(woody_signature)) // 2))
    sys.stdout.write('\n')
    sys.stdout.write(RESET)
    sys.stdout.flush()
    
    # Add a philosophical disclaimer with color wave
    disclaimer = "This statement has been certified as neurotically profound by the Institute of Existential Dread."
    color_wave(disclaimer.center(frame_width), 3)

if __name__ == "__main__":
    woody_allen_quote()