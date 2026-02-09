"""
Campbell's Soup Can #2129
Produced: 2026-02-09 03:21:28
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

# Woody Allen style quote - created specifically for this program
quote = ("I'm not afraid of death. I just don't want to be there when it happens. "
         "Besides, what if the afterlife is just one long Woody Allen movie? "
         "And the worst part? I'd have to critique it from the front row.")

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def typewriter(text, delay=0.03, color=Colors.CYAN):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.END}")
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    print()

def draw_border(width, char='─', color=Colors.BLUE):
    """Draw a horizontal border"""
    print(f"{color}{char * width}{Colors.END}")

def draw_woody_hat():
    """Draw a simple Woody Allen face with glasses"""
    hat = [
        "      _______",
        "     /       \\",
        "    /         \\",
        "   |    o o    |",
        "   |     ^     |",
        "    \\  ˈaudioˈ /",
        "     \\_________/"
    ]
    for line in hat:
        print(f"{Colors.BOLD}{Colors.YELLOW}{line}{Colors.END}")

def philosophical_box():
    """Main display function"""
    # Clear screen (works on most terminals)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    
    width = 70
    inner_width = width - 4
    
    # Draw Woody's face
    draw_woody_hat()
    print()
    
    # Top border with some wobble effect
    draw_border(width, '═', Colors.HEADER)
    
    # Empty line
    print(f"{Colors.BLUE}│{' ' * inner_width}│{Colors.END}")
    
    # Centered title
    title = "A WOODY ALLEN PHILOSOPHICAL MOMENT"
    padding = (inner_width - len(title)) // 2
    print(f"{Colors.BOLD}{Colors.YELLOW}│{' ' * padding}{title}{' ' * (inner_width - len(title) - padding)}│{Colors.END}")
    
    # Empty line
    print(f"{Colors.BLUE}│{' ' * inner_width}│{Colors.END}")
    
    # Draw quote with dynamic wrapping
    words = quote.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= inner_width:
            current_line = f"{current_line} {word}".strip()
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    # Print each line with typewriter effect
    for i, line in enumerate(lines):
        padding = (inner_width - len(line)) // 2
        print(f"{Colors.BLUE}│{' ' * padding}{Colors.END}", end="")
        
        # Add dramatic pause before quote starts
        if i == 0:
            time.sleep(0.8)
            sys.stdout.write(f"{Colors.DIM}(sigh){' ' * 3}{Colors.END}")
            time.sleep(0.5)
        
        typewriter(line, delay=0.04 if i == len(lines)-1 else 0.03)
        
        # Add existential ellipsis at end
        if i == len(lines)-1:
            time.sleep(0.3)
            print(f"{Colors.DIM}{' ' * (inner_width - len(line) - padding - 3)}...{Colors.END}")
        else:
            print(f"{Colors.BLUE}│{' ' * (inner_width - len(line) - padding)}│{Colors.END}")
    
    # Empty line
    print(f"{Colors.BLUE}│{' ' * inner_width}│{Colors.END}")
    
    # Bottom border
    draw_border(width, '═', Colors.HEADER)
    
    # Attribution with fade effect
    time.sleep(0.5)
    fade_colors = [Colors.DIM, Colors.DIM, Colors.YELLOW, Colors.BOLD, Colors.YELLOW]
    for i, char in enumerate("— Woody Allen (probably)"):
        color = fade_colors[min(i // 5, len(fade_colors)-1)]
        sys.stdout.write(f"{color}{char}{Colors.END}")
        sys.stdout.flush()
        time.sleep(0.06)
    print("\n")

def existential_crisis():
    """Add a little existential anxiety at the end"""
    anxieties = [
        "(Is this even funny?)",
        "(Did I just waste 5 seconds of my life?)",
        "(What is the meaning of this ASCII art?)",
        "(My therapist will hear about this.)",
        "(I should be working.)"
    ]
    
    time.sleep(0.8)
    print(f"{Colors.DIM}{random.choice(anxieties)}{Colors.END}")
    time.sleep(1)

def main():
    try:
        philosophical_box()
        existential_crisis()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}⟨Interrupted by existential panic⟩{Colors.END}")
        sys.exit(0)

if __name__ == "__main__":
    main()