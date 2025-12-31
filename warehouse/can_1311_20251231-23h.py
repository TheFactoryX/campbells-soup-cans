"""
Campbell's Soup Can #1311
Produced: 2025-12-31 23:31:22
Worker: Qwen: Qwen2.5-VL 7B Instruct (free) (qwen/qwen-2.5-vl-7b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
import time

def moo():
    print("\033[32m" + """
  _____
 /_   _/ 
   |   \  
   | |\ \  
   | | \ \  
  _| |_ \  __
 |_____| \_\ \  
                \_\
                 \ 
             /\ _  \
            //\_/    \
           //          \
          //            \
         //              \
        //                \
       //                  \
      //                    \
     //                      \
    //                        \
   //                          \
  //                            \
 / \__\                      ___/
          \___                 _/
        /___ \                  \
       //    >                   \
      //                        \  \n
"""\033[0m", end=' ')

def print_quote():
    quotes = [
        "Life is so frail and so short, I wonder why isn’t every moment takes up by beautiful people, 
         reading great books, learning new things. I woke up with a bang! Huh?\n\n",
        "It is hard to look at a loved one’s face and see that final inscription:  
         In Memoriam.\n\n",
        "My latest test was to find out whether I could stand on a rope while 
         being attached to an elecric line providing 175 kilovoltage.\n\n",
        "The only real thing I was completely defenceless against was a baby nappy, 
         which I wore until I was 18, due to a rare condition Vimy abreast conclusion.\n\n",
        "New York is a great city, but is it the one where f*** beat violin?"
    ]
    quote = random.choice(quotes)
    print("\033[33m" + "\n" + "-"*40 + "\n")
    print("| " + "\033[31m" + quote[:-2] + "\n" + "-"*44 + "\n")
    print("\033[0m")
    time.sleep(3)

def main():
    moo()
    print_quote()

if __name__ == "__main__":
    main()