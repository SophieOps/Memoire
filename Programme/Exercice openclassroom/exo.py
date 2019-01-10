# -*- coding: utf8 -*-
import random
import json
#print(7+7)
#print("hello")

def read_values_from_json(path, key):
    values = []
    with open(path) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
    return values

def random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1) # get a random number
    return my_list[rand_numb] # return an item from a list
    
# Return a random value from a json file
def random_value(file, key):
    all_values = read_values_from_json(file, key)
    return random_item_in(all_values)


def main_loop():
    #while True:
        #print_random_sentence()
        #message = ('Voulez-vous voir une autre citation ?'
                   #'Pour sortir du programme, tapez [B].')
        #choice = input(message).upper()
        #if choice == 'B':
            #break # This will stop the loop!
            
    #sinon, autre possibilité :
    user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')
    while user_answer != "B":
        print("{} a dit : {}".format(random_value("characters.json", "character"), random_value("quotes.json", "quote") ))
        user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')



if __name__ == '__main__':
    main_loop()

    





#import turtle
#turtle.forward(100)

#from turtle import *
#color('red', 'yellow')
#begin_fill()
#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#        break
#end_fill()
#done()
