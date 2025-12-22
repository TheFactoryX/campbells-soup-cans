"""
Campbell's Soup Can #1105
Produced: 2025-12-22 14:36:52
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

# woody.py - a neurotic little program

def type_text(text, speed=0.04):
    """Typewriter effect with dramatic pauses."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in ',;':
            time.sleep(0.2)
        elif char == '-':
            time.sleep(0.3)
        else:
            time.sleep(speed)
    print()

def flicker(text, color_code):
    """ANSI flickering text effect."""
    return f"\033[{color_code}m{text}\033[0m"

def pulsing_bracket():
    """A pulsing anxiety bracket."""
    for _ in range(3):
        print(f"{flicker('[', '91')}{flicker('(', '93')}{flicker('M', '91')}{flicker(')', '93')}{flicker(']', '91')}", end=" ", flush=True)
        time.sleep(0.2)
        print("\b\b\b\b\b\b", end="", flush=True)
        time.sleep(0.2)
    print()

def main():
    # Clear screen for effect
    print("\033[2J\033[H")
    
    quote = [
        "Time flies like an arrow;",
        "fruit flies like a banana.",
        "I'm not afraid of death;",
        "I just don't want to be there when it happens."
    ]

    # Animation Start
    print("\n" * 2)
    pulsing_bracket()
    
    # The existential dread unfolds...
    for line in quote:
        # Alternating colors and offsets
        if "Time" in line:
            print(f"\033[1;36m  {line}\033[0m")
        elif "fruit" in line:
            print(f"\033[1;35m    {line}\033[0m")
            time.sleep(0.5)
        elif "I'm" in line:
            print(f"\033[1;33m      {line}\033[0m")
        else:
            # The punchline with red cursor
            print(f"\033[1;31m        {line}\033[0m")
        
        # Dramatic pause
        time.sleep(0.8)
        
        # Random anxious blinking cursor
        if "death" in line:
            for _ in range(5):
                sys.stdout.write("\033[1;31m█\033[0m")
                sys.stdout.flush()
                time.sleep(0.1)
                print("\b \b", end="", flush=True)
                time.sleep(0.1)
            print()
    
    # The grand finale
    print("\n" * 1)
    print("\033[1;37m" + "-"*50 + "\033[0m")
    
    # Sudden exclamation
    sys.stdout.write("\033[1;31m[!!!]\033[0m ")
    sys.stdout.flush()
    time.sleep(0.5)
    
    # Typewriter the sub-quote
    type_text("And yet, I still forget to take out the trash.", 0.05)
    
    # ASCII Art Neurosis
    art = """
       _     _
      (o)___(o)
      /    U \\
     /  \\___/  \\
    /           \\
   (_____________)
       ||    ||
       ''    ''
    *twitch*
    """
    
    # Print art with random colors
    colors = ['92', '93', '94', '95']
    for line in art.split('\n'):
        color = random.choice(colors)
        print(f"\033[{color}m{line}\033[0m")
        time.sleep(0.1)
    
    print("\n\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[1;31m[Interrupted by existential crisis]\033[0m")