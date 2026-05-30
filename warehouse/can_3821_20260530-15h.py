"""
Campbell's Soup Can #3821
Produced: 2026-05-30 15:35:58
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time, sys, os

def slow_print(text, delay=0.02, color=""):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\033[0m')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

# Colors
YELLOW = '\033[1;33m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
RED = '\033[1;31m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
PURPLE = '\033[0;35m'
RESET = '\033[0m'

# ASCII art "OWL" banner
 owl_banner = f"""
{YELLOW}         ___
        (o,o)  "Let me tell ya..."
   /\\/   \\/
  | \\___/  |  {MAGENTA}Philosophy is like a knife from the drawer
  \\__/   |      you didn't know you needed."{YELLOW}
     \\__/{RESET}
     /  \\
{RESET}"""

# Frame by frame animation
frames = [
    f"""
{RIGHT}           _____
          |  __  |
          | |  | |  *exists*
          |_|  |_|{RESET}
""",
    f"""
{RIGHT}           _____
          | __   |
          | \\\\__  |  *contemplates*
          |_______|{RESET}
""",
    f"""
{RIGHT}           _____
          | ___  |
          |  ___| |  *panics*
          |_|_|_|_|{RESET}
""",
    f"""
{RIGHT}           _____
          |  __  |
          | |__| |  *orders therapy*
          |_|  |_|{RESET}
""",
]

RIGHT = '\033[1;36m'

print(f"{MAGENTA}═" * 60 + RESET)
print(f"{MAGENTA}║{'':^58}║{RESET}")
print(f"{MAGENTA}║{'  OWLY WOODY ALLEN QUOTE GENERATOR  ':^58}{MAGENTA}║{RESET}")
print(f"{MAGENTA}║{'':^58}║{RESET}")
print(f"{MAGENTA}═" * 60 + RESET)

# Animate thought bubbles
for i in range(5):
    clear_screen()
    print(f"{MAGENTA}═" * 60 + RESET)
    print(f"{RIGHT}           _____      ")
    print(f"          |{['○  ○','○  ●']['%2d'%(i)%2==0]}{'':^10}|")
    print(f"          |  {'????' if i==0 else
                          'hmmm' if i==1 else
                          'aaaah' if i==2 else
                          'oh no' if i==3 else
                          'EUREKA!' if i==4 else '':^10}|")
    print(f"          |_|_|_|{' '*10} |")
    print(f"{RESET}")
    sys.stdout.write(frames[i % len(frames)])
    time.sleep(0.4)

# The big reveal
clear_screen()

print(f"{MAGENTA}═" * 60 + RESET)
print(f"""{GREEN}
    ┌─────────────────────────────────────────────────┐
    │                                                 │
    │   "Yesterday I bought a book about           │
    │    catastrophism. I read the whole           │
    │    thing yesterday. The universe              │
    │    doesn't owe me an explanation.             │
    │    That's the problem with the              │
    │    universe: it doesn't owe me                │
    │    anything. But my therapist                 │
    │    does."                                    │
    │                                                 │
    │                                    - me        │
    └─────────────────────────────────────────────────┘
{RESET}""")

time.sleep(1)

# Philosophical thought spiral
thought_text = [
    f"{RIGHT}[thinking about existence...]{RESET}",
    f"{RED}[realizing existence was a mistake]{RESET}",
    f"{MAGENTA}[questioning the therapist's therapist]{RESET}",
    f"{GREEN}[accepting that the universe is a prank]{RESET}",
    f"{CYAN}[ordering another therapy session]{RESET}",
]

print("\n\n")

for line in thought_text:
    sys.stdout.write("  " + "• " * 1 + line + "\n")
    sys.stdout.flush()
    time.sleep(0.45)

print(f"\n{PURPLE}")
print("  ╔═══════════════════════════════════════╗")
print("  ║   Life is a search for meaning       ║")
print("  ║   but meaning is avoiding           ║")
print("  ║   your mother's questions.          ║")
print("  ╚═══════════════════════════════════════╝")
print(RESET)

# Final sad face animation
sad_faces = [
    "  ( _ _ )     \n   -_-\n",
    "  ( ; _ ; )     \n   -_-\n",
    "  ( o _ o )     \n   -_-\n",
    "  ( ~ _ ~ )     \n",
]

for _ in range(3):
    for face in sad_faces:
        print(f"{RIGHT}{face}{RESET}")
        sys.stdout.write(f"{RIGHT}  Any moment now I'll figure it out...\n{RESET}")
        time.sleep(0.6)

final_crisis = f"""{RED}
    ╔═══════════════════════════════════════════╗
    ║                                           ║
    ║   "The only thing standing              ║
    ║   between me and greatness               ║
    ║   is a small voice in my head            ║
    ║   saying 'You're Average.'               ║
    ║                                           ║
    ║   That voice is usually me."             ║
    ║                                           ║
    ╚═══════════════════════════════════════════╝
{RESET}"""

print(final_crisis[0])
time.sleep(0.05)
print(final_crisis)