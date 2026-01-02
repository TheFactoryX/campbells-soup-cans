"""
Campbell's Soup Can #1351
Produced: 2026-01-02 20:34:39
Worker: Nex AGI: DeepSeek V3.1 Nex N1 (free) (nex-agi/deepseek-v3.1-nex-n1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time, sys, random, math

# ANSI color codes
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

# Woody Allen's neurotic quote
QUOTE = '"I\'m plagued by existential dread, but in a very specific, \n annoying way that probably isn\'t even interesting enough \n for proper philosophical contemplation."'

def draw_anxiety_meter():
    print(f"\n{DIM}Current Anxiety Level: {RESET}", end="")
    meter = random.randint(75, 99)
    print(RED + "█" * (meter // 3) + RESET + f" {meter}%{RESET}")

def typewriter(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed if char not in '\n ' else 0.02)
    print()

def draw_neurotic_person():
    print(f"""
    {BOLD}{BLUE}    ╔═══════════════════════════════════════╗
    ║   {CYAN}ME: {YELLOW}(constantly overthinking){BLUE}          ║
    ║                                          ║
    ║   {WHITE}      😰 {CYAN}/){BLUE}                   {DIM}"What if{RESET}      ║
    ║   {WHITE}     c({CYAN}•.•{BLUE}){WHITE}  {RED}~~{YELLOW}●{RED}~~{RESET}        {DIM}I'm doing{RESET}     ║
    ║   {WHITE}      {CYAN}\\ /{BLUE}                    {DIM}it wrong?"{RESET}    ║
    ║   {WHITE}     {CYAN}(_{BLUE})づ{RED}⚡{RESET}                           ║
    ║                                          ║
    ║   {MAGENTA}"I worry about everything{RESET}          ║
    ║   {MAGENTA}including whether I'm worrying{RESET}     ║
    ║   {MAGENTA}about the RIGHT things."{BLUE}           ║
    ║                                          ║
    ╚═══════════════════════════════════════╝{RESET}
    """)

def create_pulse_effect(text):
    for i in range(3):
        intensity = 1.5 + 0.5 * math.sin(i * math.pi / 3)
        print(f"\033[F\033[K{RED}{BOLD}{text.upper()}{RESET}")
        time.sleep(0.3)

def print_quote_bubble(quote):
    lines = quote.split('\n')
    width = max(len(line) for line in lines) + 8
    
    print(f"\n{BOLD}{MAGENTA}{' ' * ((width - 55) // 2)}{YELLOW}┌{'─' * (width - 2)}┐{RESET}")
    
    for i, line in enumerate(lines):
        padding = width - len(line) - 4
        left_pad = padding // 2
        right_pad = padding - left_pad
        
        if i == 0:
            prefix = f"{BOLD}{MAGENTA}  ➤ {WHITE}"
        else:
            prefix = f"{BOLD}{MAGENTA}    {WHITE}"
        
        print(f"{BOLD}{MAGENTA}{' ' * ((width - 55) // 2)}{YELLOW}│ {RESET}{prefix}{line}{' ' * right_pad}{BOLD}{YELLOW} │{RESET}")
    
    print(f"{BOLD}{MAGENTA}{' ' * ((width - 55) // 2)}{YELLOW}└{'─' * (width - 2)}┘{RESET}")
    print(f"{BOLD}{MAGENTA}{' ' * ((width - 55) // 2 + 12)}🡇 {DIM}- Woody Allen, probably{RESET}")

def main():
    print(f"\n{BOLD}{CYAN}{'=' * 60}")
    print(f"{' ' * 10}🔮 WOODY ALLEN'S NEUROTIC PHILOSOPHY 🔮")
    print(f"{'=' * 60}{RESET}")
    
    draw_neurotic_person()
    
    time.sleep(1)
    
    print(f"\n{BOLD}{YELLOW}Today's existential crisis:{RESET}")
    create_pulse_effect("  (Processing...)  ")
    
    print_quote_bubble(QUOTE)
    
    draw_anxiety_meter()
    
    print(f"\n{BOLD}{BLUE}{'=' * 60}")
    print(f"{' ' * 15}📚 Philosophy Level: Neurotic 📚")
    print(f"{'=' * 60}{RESET}\n")

if __name__ == "__main__":
    main()