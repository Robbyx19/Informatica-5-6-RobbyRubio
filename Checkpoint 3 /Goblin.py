import random 
print("welcome to the goblin game ")
print ("the best game ever ")
player_name = input("write your name")
print  (player_name,"can you find the goblin ")
print ("|_|"*5)
goblin_position = random.randint(1, 5)
while keep_triying:
while keep_triying:
guessed_position = int(input ("can you guess where the goblin is?") )
if guessed_position == goblin_position:
    print("good luck you find the goblin")
    keep_triying = False
else: print("NO")
keep_triying = any