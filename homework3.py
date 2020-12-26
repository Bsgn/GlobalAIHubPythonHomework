#I can try other techniques for this homework but i want to try this "whatever i learn in lessons" way.
import random as rnd
name = input("What is your name : ")
print(f"Welcome {name};")
print("This is our rules:", "\n", "1. If you want to win, you must find all the letter in the word","\n","2. You can guess 20 times","\n","3. Good luck, Have fun :)")
sel = 0 #a number for determine question
selected = "" #selected word
inp = "" # user's letter input
sl_list = list() #storage of selected word's letter
dp_list = list() #storage of user's guess which is correct
#question list
words = {"PYTHON","ARTIFICIAL","INTELLIGENCE","GLOBAL","COURSE","HUB","DEEP","LEARNING","MACHINE","TURKEY","NATURAL","LANGUAGE","PROCESSING"}
selection = rnd.randint(0,len(words)) #a random number for determine question
# in this loop we find what is the question word(selected)
for i in words:
    if sel == selection:
        selected = i
        break
    else:
        sel += 1

#print(selected) #if you want to test this program you can cancel this comment line

#in this for loop, we append every letter to a list one by one
for i in selected:
    sl_list.append(i)
#in this for loop, we append "__" for all of the unentered letters
for i in range(len(sl_list)):
    dp_list.append("__")
print(dp_list) 
# 20 guessing chance 
for i in range(20):
    #check if all letters found
    if "__" in dp_list:
        sl_list_index = 0
        inp = input("Enter a key : ").upper()
        print(f"guess counter: {i+1}, {20 - (i+1)} remainig ") #guess counter
        # replace "__" and print letter if letter exist in the word 
        for i in sl_list:
            if i == inp:
                dp_list[sl_list_index] = i
                sl_list_index += 1
            else:
                sl_list_index += 1
        print(dp_list)
    else:
        print(f"Congrats {name}!!") #when user wins
        break
print(f"It is {selected}")
print(f"Well play {name}, thanks :)") #Always say "thanks" to users :)

