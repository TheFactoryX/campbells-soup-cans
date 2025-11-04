"""
Campbell's Soup Can #52
Produced: 2025-11-04 14:36:57
Worker: ArliAI: QwQ 32B RpR v1 (free) (arliai/qwq-32b-arliai-rpr-v1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

def quote_print():
    quote = "I'm not afraid of life, really — just worried it might be judging me by how many planets are empty."
    import sys
    import time
    
    #Define the colors
    green_color = "\033[1;34;47m"
    reset = "\033[0m"

    #Sizing parameters
    h = 10
    w = 60
    x = (w - len(quote)) // 2
    y = (h - 2)//2
    count = 0

    #Clear the screen for the background
    print(f"\033c\033[{h * 2}B\033[{w}C")

    #Print quote    
    print(f"\033[C\033[1m\033[34m{quote}\033[0m")

    while True:
        #Generate dice
        for _ in range(3):
            print(time.strftime('%H:%M:%S'))
            sys.stdout.write(f'\033[1m\033[32m\033[D\033[2B\033[2B\033[2B\033[24D')
            time.sleep(0.5)
            print('\033[1m\033[34m\033[D\033[D\033[D\033[4B\033[24D')
            #Printtopsqr
            dice = 'four'
            horiz = h
            vert = h
            print(f'\033[s\033[K\033[u', end='')

            top_sqr = f'\033[1m\033[35m\033[{vert}B\033[{horiz}C\033[4m\033[D'
            mid_sqr = f'\033[1m\033[35m\033[D\033[4m\033[D'
            bot_sqr = f'\033[1m\033[35m\033[94m\033[D\033[4m\033[D'
            top = f'\033[1m\033[30m\033[47m\033[D\033[4m\033[D'
            mid = f'\033[1m\033[30m\033[47m\033[D'
            bot = f'\033[1m\033[30m\033[47m\033[D\033[D'
            #Construct the elements

            if dice == 'two':
                top = mid_sqr
                mid = top_sqr
            elif dice == 'three':
                mid = bot_sqr
                bot = top_sqr
            elif dice == 'four':
                top = mid
                mid = mid
                bot = mid
                bot = mid
            elif dice == 'five':
                top = bot_sqr
                mid = bot_sqr
                bot = bot_sqr
            elif dice == 'seven':
                mid = mid_sqr
                bot = mid
            #Print the dice
            print(f'\033[s\033[0m\033[41m{top}{mid}{bot}\033[u', end='')
            #Move cursor back to original position
            print('\033[K\033[u', end='')
            time.sleep(0.5)

        #Move cursor back to original position
        #ghost_sqr = f'\033[1m\033[30m\033[47m\033[D\033[K'
        #print(f'\033[H\033[{vert}B\033[{horiz}C{ghost_sqr}\033[u', end='')
        #time.sleep(0.50)

    #Move to bottom of screen
        #Clear the screen
        #Clear_console()
        
if __name__ == "__main__":
    quote_print()