"""
Campbell's Soup Can #3546
Produced: 2026-05-03 08:57:13
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.03, color_code=None):
    """Prints text with a typewriter effect, optionally with color."""
    if color_code:
        sys.stdout.write(color_code)
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    if color_code:
        sys.stdout.write('\033[0m')  # Reset color
    sys.stdout.write('\n')

def print_ascii_frame():
    """Prints an ASCII art frame around the quote."""
    frame_width = 70
    frame_corners = '+' + '-' * (frame_width - 2) + '+'
    
    # ANSI color codes
    color_frame = '\033[95m'  # Purple
    color_quote = '\033[92m'  # Green
    color_author = '\033[96m'  # Cyan
    color_thought = '\033[93m'  # Yellow
    
    # Print top frame
    typewriter_effect(f"{color_frame}{frame_corners}", delay=0.01)
    
    # Print empty line with vertical bars
    typewriter_effect(f"{color_frame}|{' ' * (frame_width - 2)}|", delay=0.01)
    
    # Print quote with proper indentation
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    typewriter_effect(f"{color_frame}|{color_quote}{' ' * 5}{' ' * (frame_width - 12)}{color_frame}|", delay=0.01)
    typewriter_effect(f"{color_frame}|{color_quote}{' ' * 5}{quote[:frame_width - 12]}{color_frame}|", delay=0.03)
    typewriter_effect(f"{color_frame}|{color_quote}{' ' * 5}{' ' * (frame_width - 12)}{color_frame}|", delay=0.01)
    
    # Print author line
    author = " - Woody Allen"
    typewriter_effect(f"{color_frame}|{color_author}{' ' * (frame_width - 10)}{author}{color_frame}|", delay=0.03)
    
    # Print bottom frame
    typewriter_effect(f"{color_frame}{frame_corners}", delay=0.01)
    
    # Reset color
    sys.stdout.write('\033[0m')
    
    # Print additional commentary with delays
    time.sleep(1)
    
    thought1 = "Actually, I'm more afraid of what comes after death. The paperwork must be dreadful."
    typewriter_effect(f"\n{color_thought}{thought1}", delay=0.05)
    
    time.sleep(1)
    thought2 = "And the waiting room! Eternity in a plastic chair with outdated magazines..."
    typewriter_effect(f"{color_thought}{thought2}", delay=0.05)
    
    time.sleep(1)
    thought3 = "What if there's no Wi-Fi in the afterlife? That would be the real tragedy."
    typewriter_effect(f"{color_thought}{thought3}", delay=0.05)

def print_final_thought():
    """Prints a final neurotic thought with animation."""
    color_final = '\033[91m'  # Red
    final_thought = "I should probably write my will... but I can't find a pen. Typical."
    
    # Animate the final thought with blinking cursor
    typewriter_effect(f"\n{color_final}{final_thought}", delay=0.05)
    
    # Blinking cursor effect
    for i in range(5):
        sys.stdout.write('\033[91m_\033[0m')
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write('\r\033[K')  # Clear line and move cursor to beginning
        time.sleep(0.3)
    
    # Final blinking cursor
    sys.stdout.write('\033[91m_\033[0m')
    time.sleep(1)
    sys.stdout.write('\n')

def print_title():
    """Prints a title with animation."""
    title = "WOODY ALLEN ON LIFE AND DEATH"
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m']
    
    # Print title with color cycling
    for char in title:
        color = colors[int(time.time() * 2) % len(colors)]
        sys.stdout.write(f"{color}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)
    
    sys.stdout.write('\n\n')

def print_neurotic_animation():
    """Prints a simple animation to represent neurotic thoughts."""
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m']  # Red, Green, Yellow, Blue, Purple
    thoughts = ["Hmm...", "What if...", "Maybe...", "I should...", "But what if..."]
    
    for i in range(5):
        color = colors[i % len(colors)]
        thought = thoughts[i % len(thoughts)]
        sys.stdout.write(f"{color}*{thought}*")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write('\r')
    
    sys.stdout.write('\033[0m\n')  # Reset color and move to next line

if __name__ == "__main__":
    clear_screen()
    
    # Print title with animation
    print_title()
    time.sleep(1)
    
    # Print neurotic animation
    print_neurotic_animation()
    time.sleep(1)
    
    # Print ASCII frame with quote
    print_ascii_frame()
    
    # Final thought with animation
    print_final_thought()