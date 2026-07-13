"""
Campbell's Soup Can #4180
Produced: 2026-07-13 04:00:02
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

colors = ['\033[31m', '\033[36m', '\033[93m', '\033[34m']
formatting = ['\033[1m', '\033[4m', '', '']
cleanse = '\033[0m'

ascii_box = """
 {} \n
 \n
 .-----. \n
 |   |   \n
 |   |   \n
/-----.| \n
|   _  | \n
|  (:| | \n
\\__, \\ ` \n
`-----\'  \n
"""

final_quote = f"""
{ascii_box.format('     ___   ___    ___  _   _')}{cleanse}
{colors[0]}{'-' * 50}{cleanse}
{colors[1]}\"I once tried to organize my life... it got organized.\"{cleanse}
{colors[2]}, {formatting[0]}\"But now?\"\n{formatting[1]}{'-' * 5}{cleanse}
{formatting[0]}\"Philosophy 101\" (taught by me)\\\"{cleanse}
{colors[3]}\"Woody Allen\", or as I like to call myself, \"The Existential Comedian\"    
{colors[0]}-------------------------------------------------------------------------------------
{cleanse}{formatting[1]}


"""
inner_quote = random.choice([
    ("Laughter is my only defense against the absurdity of existence..."),
    ("If I had a nickel for every time I questioned reality... wait, no, that's capitalism."),
    ("My therapist says I'm neurotic. She also says I need to pay her in existential dread."),
    ("I'm not old; I'm just vintage with emotional baggage."),
    ("The universe is a joke, and I'm the punchline who never laughs."),
    ("I wrote a book on the meaning of life. It's called 'Why? (Really?)'."),
    ("Fear isn't holding me back – it's cheerleading for my escape plans."),
    ("I avoid mirrors because they always point to wrong answers."),
    ("Live fast, die young, and avoid eye contact with pigeons."),
    ("My internal monologue: 'Is this it? Is any of this *mine*? Took the quiz – Schizophrenia.'")
])

for char in inner_quote:
    print(colors[random.randint(0,3)] + char, end='', flush=True)
    time.sleep(0.03)

print(f"\n\n{colors[1]}\"For more quotes, visit...\"\n{colors[2]}\"woodyallenexistentialism.net\"\n{colors[3]}{formatting[1]}")
print(formatting[0] + "\"Codename: PHILOSOPHY\" – Project: 🤔\n".format(**locals()))