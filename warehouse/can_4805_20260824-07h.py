"""
Campbell's Soup Can #4805
Produced: 2026-08-24 07:28:41
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def log(message, color='white'):
    print(f"\x1b[{59 + color}m {message}\x1b[m")

colors = ['red', 'blue', 'green', 'yellow', 'magenta']

for _ in range(3):
    log(random.choice([".", "*", "-"]) + random.choice(" * - ~"), colors[random.randint(0, 4)])
    time.sleep(0.3)

log("""
  _____                      _   _____ _____
 /   _|                     | | / ____|_   _|
|   | | _____      _____  __| | |     ___| |
|   | | | ___ \\    |  __|_/ _` | |   |  _| |
\\   \\_| |_   \\_\\ \\ | (__  (_) | |   | |___|
 \\____/|_____|  |_|\\___|\\__, _| |    \\_____|
                        __/ |
                       |___/|___/

""")

quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "I'm not losing my mind; I'm just letting it roam.",
    "Philosophy? I prefer calling it 'fanciful problem-solving with a sense of dread.'",
    "Reality is merely an illusion, of course, but who has time to enjoy one?"
]

for quote in quotes:
    width = max(len(line) for line in quote.split('\n'))
    frame = '#' * (width + 4)
    quote_lines = quote.split('\n')
    height = len(quote_lines)
    border = ['#' + ' ' * width + '#'] * height
    box = list(zip(border, quote_lines, border))  # Create visual "box"

    for line in box:
        log(frame)
        log(''.join(line[0] + line[1] + line[2]))
    log(frame)
    print()

    rain_chance = 20
    rands = random.sample(range(len(quote_lines)), k=rain_chance)
    drops = {i: 0 for i in range(len(border))}

    while True:
        os.system('clear')  # Clear screen
        time.sleep(0.1)
        
        for y, row in enumerate(box):
            log(frame)
            log(f'# {" " * (len(row[1])//2)}   #')
        
        for y, x in random.sample(range(len(drops)), k=rain_chance):
            drops[x] = y
        
        for line in border:
            log(f'#{ "".join([" #"[y==d] if y > d else "  " for d in drops.values()]).ljust(width) }#')
            drops = {k: v-1 for k,v in drops.items() if v > 0}

# Final output
log("""
        ______
       /      \\
      |   _   |
      \\  [ ]  /
       \\______/
""", color=2)
log("Life, like this ASCII art, eventually crumbles... but at least the diamonds remain", color=3)
log("Hand-drawn in pure (and trembling) Python", color=0)