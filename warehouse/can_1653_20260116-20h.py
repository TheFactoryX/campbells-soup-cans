"""
Campbell's Soup Can #1653
Produced: 2026-01-16 20:36:19
Worker: AllenAI: Molmo2 8B (free) (allenai/molmo-2-8b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import time

def print_woodo_color(txt, color='white', blurred=False):
    from itertools import zip_longest
    code = {'white': '0', 'black': '1', 'red': '31', 'green': '32', 'yellow': '33', 'blue': '34', 
            'purple': '35', 'cyan': '36', 'magenta':'38'}
    text_len = len(txt)
    divider = '_' if blurred else '—'
    blur = '๐' if blurred else ' '

    if color in code:
        sql = f"\033[1;{code[color]}m{text}\033[0m"
    else:
        sql = txt

    first = divider.join((' ' + i + ' ') for i in txt[::1])
    second = divider.join((' ' + c + ' ') for c in txt[1::2])
    third = ' '.join((c for c in txt[2::3] if c))
    fourth = divider.join((' ' + b + ' ') for b in txt[3::4])
    fifth  = ' '.join((txt[-1], txt[-2]))
    sixth  = divider.join((' ' + t + ' ') for t in reversed(txt[1:3]))
    
    damages = [first, second, third, fourth, fifth, sixth]
    delim = ''.join(('/--\\/-/--\\/-/--\\/-/--\\')) + ' '
    deco = ''.join((' | ' + c + ' | ' for c in txt[::4])) if text_len %4 == 0 else ''.join((' | ' + c + ' | ' for c in txt[::5]))
    
    upper = f"\n {deco}"
    
    print(f'''
      +----+----+----+----+
 {upper}
     |    |    |    |    |
     |    |    |    |    |
     {sql}
     |    |    |    |    |
     |    |    |    |    |
    +----+----+----+----+
''')

 witty_quotes = [
   "Time flies like an arrow, but my car’s tires aren't touching the ground.",
   "If you want to be happy, just go out and enjoy the little things, like making someone else happy.",
   "I don’t mind growing older. I just hope nobody notices or copyrights my youth.",
   "Life is not a fair game, but it is a good game, if you play it well, even then it’s not a fair game.",
   "I used to think a well-lived life was one gram heavier than yesterday. Now I understand it's one gram lighter."
]

def random_quote():
    return witty_quotes[random.randint(0, len(witty_quotes)-1)]

# ASCII WoodyAllen
woody_ascii = '''
 _ 
 ( o_  (_) 
  ( ) (
 /`   `\
@@@@@@@@@
/   '   \
@@@@@@@@@
'   '   '
'''

um = "\u001b[90m"
# print_woodo_color(woody_ascii, 'black', True)

# Animation Function
def animate_quote(quote, delay=0.07):
    for letter in quote:
        print_woodo_color(letter)
        time.sleep(delay)

# Clear
os.system('cls' if os.name == 'nt' else 'clear')
animate_quote(random_quote())

# ASCII Woody Alert!
def woody_alert(x = 1):
    print_woodo_color('.\n|\n).\n|\n.\n') 
    time.sleep(0.3)
    print_woodo_color("   |\n   |\n  ----_\ ")
    time.sleep(0.2)

woody_alert()

# Scientific Necktie!
def necktie(x):
    print_woodo_color('     ,--._,-.---. ,---_,-.---.\n     \`\::__/\__/ __/\`\::__/\__/ ')
    print_woodo_color('|                 |                 |\n     /,\n    /  \\ \n   /    \n  / \n \\\n  \\                 \\ \n   \\                 \\\ \n ' + ' '.join(['_' for i in range(x)]))
    time.sleep(0.1)

necktie(10)