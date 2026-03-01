"""
Campbell's Soup Can #2495
Produced: 2026-03-01 03:23:48
Worker: AionLabs: Aion-RP 1.0 (8B) (aion-labs/aion-rp-llama-3.1-8b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

 # Woody Allen's Quotes Machine
# by Alan D. (aka @RedPandaSWE)
# This program prints a random philosophical quote in the style of Woody Allen.
# It uses a list of tuples, where each tuple contains a quote and its respective author.
# The program selects a random index, unpacks the tuple, and formats the quote
# between boxes with a background color. It also prints a random (fake) citation
# at the end of the quote, pretending it's part of the original quote.
# Feel free to modify, use, and share this code however you want.
# Have fun! 

from random import randint
from termcolor import colored
import re

quote_data = [
("I don't want to get to the end of my life and find that I never lived.", "(Woody Allen)"),
("If you want to make it anywhere in life, you have to learn to deal with people who are jerks.", "(Woody Allen)"),
("The hardest thing about making a movie is getting it made. Once it's made, the hardest thing is getting people to see it. And the hardest thing, once they see it, is getting them to like it.", "(Woody Allen)"),
("Eternity is a terribly dull idea. A watch is much more interesting.", "(Woody Allen)"),
("It's not that I'm afraid to die. I just don't want to be there when it happens.", "(Woody Allen)"),
("I don't want to achieve immortality through my work. I just want to live forever. So I can see my grandchildren come of age and know that I've got grandchildren.", "(Woody Allen)"),
("Old age is not for sissies.", "(Woody Allen)"),
("If only God would give me some sign. If he does, I'll throw away this hammer.", "(Woody Allen)"),
("The most exciting thing you can do is not the thing you do, but the thing you've got to do next.", "(Woody Allen)"),
("You know, it's funny, when you're in your 20s, you think 40s is old. And when you're in your 40s, you think 60s is old. And when you're in your 60s, you think the cemetary looks good.", "(Woody Allen)"),
("My philosophy is: It's okay to take a trip, but don't move to the countryside. You must have a headline in a major city. I don't care if you buy a little house by the sea, but you should also have an apartment in New York or Los Angeles or London or Paris. That's my philosophy.", "(Woody Allen)"),
("I'm not optimistic, but I'm optimistic that way. I'm pessimistic about everything else.", "(Woody Allen)"),
("The beer is the most exciting thing there is. Except for the check coming in the mail.", "(Woody Allen)"),
("The most exciting thing in the world is being drunk, and the second most exciting thing is being sober.", "(Woody Allen)"),
("The brain is like a strong box in the chest, and I keep a little beer in there all the time.", "(Woody Allen)"),
("I'm not into reincarnation, because I think if you're good, you get to be the dog on the fire hydrant in Central Park.", "(Woody Allen)"),
("Love is the answer, and how I love thy rhymes, they sweep me off my feet, they move me, fill me with lust, like a 15-year-old reading Playboy.", "(Woody Allen)"),
("I have no hobbies. None. I just stand on the street corner and breathe. That's a hobby, right? No, no, no, it's not. So I don't have a hobby. That's the point I'm trying to make.", "(Woody Allen)"),
("I would never do 'Saturday Night Live'. I would find it hard to be funny there. They have writers; I don't need writers. And they have other funny people there, and I don't need other funny people. I just need a camera and a cigarette.", "(Woody Allen)"),
("I don't believe in mysticism, I'm a scientific man, but there's something in 
our heads, something very mysterious.", "(Woody Allen)"),
("They say the world was made in six days. I don't think they got much done 
the sixth day. I don't think they got much done the sixth day. I don't 
think they got much done the seventh day, either.", "(Woody Allen)"),
("You know, I don't want to achieve immortality through my work. I just 
want to live forever. So I can see my grandchildren come of age and know 
that I've got grandchildren.", "(Woody Allen)"),
("I'm not a pervert, I just like to look.", "(Woody Allen)"),
("A cigarette is a torch of knowledge, and each drag is a thesis on the 
relativity of pain.", "(Woody Allen)"),
("When I was young, I used to think that sure, old people would talk 
about the good old days, but now that I'm old, I understand that they're 
not talking about the good old days, they're talking about the good old 
days, the days when they were young.", "(Woody Allen)"),
("I don't want to get to the end of my life and find that I never really 
lived. I only want to live in my own way, in this world that I know and 
love, this world that I want to improve.", "(Woody Allen)"),
("I don't believe that a person can be a half-assed anything. If you're 
going to be an ass, you have to go all the way.", "(Woody Allen)"),
("I suffer from a terrible disease. I'm a comedian and I haven't had a 
really good joke in 20 years.", "(Woody Allen)"),
]

def get_quote():
    # Generate a random index
    idx = randint(0, len(quote_data)-1)
    # Unpack tuple
    quote, author = quote_data[idx]
    # Format quote between boxes, color background
    quote = colored(quote, "white", attrs=["bold", "reverse"])
    return quote, author

def main():
    # Get quote and author
    quote, author = get_quote()
    # Print formatted quote
    print(f"\"{quote}\"\n- {author}")
    # Generate random citation
    cite = f"{randint(1,99)}. " + chr(randint(33,126)) + chr(randint(33,126)) + " " + chr(randint(33,126)) + " " + str(randint(1950,2023)) + " " + chr(randint(33,126)) + " " + chr(randint(33,126))
    # Append citation to quote and print
    print(cite, end="")
    print(f"""\

The program will now sleep for 30 seconds before exiting.
Press any key to continue...''')
    input()
