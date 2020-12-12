this = False
input1 = False
car = False
horse = False
gun = True
ammo = 20
import sys
#from PIL import Image

#read the image
#im = Image.open("IceWorld.jpg") # check
#im1 = Image.open("Wolves.jpg") #chech
#im2 = Image.open("Store.jpg") #check
#im3 = Image.open("ManinStore.jpg") #check
#im4 = Image.open("Bandit1.png") #CHECK
#im5 = Image.open("Bandit2.jpg") #CHECK
#im6 = Image.open("Bandit3.jpeg") #CHECK
#im7 = Image.open("Deer.png") #CHECK
#im8 = Image.open("Crying-Child.jpg") #CHECK
#im9 = Image.open("FrozenRiver.jpg") #CHECK
#im10 = Image.open("Cabin.jpg") #CHECK
#im11 = Image.open("Farm.jpg") #Check
def supplies():
    print("")
    if car == True: 
        if gun == True:
            print("You have a car, a gun and", ammo, "bullets")
        else:
            print("You have a car and", ammo, "bullets")
    elif horse == True:
        if gun == True:
            print("You have a horse, a gun and", ammo, "bullets")
        else:
            print("You have a horse and", ammo, "bullets")
    else:
        if gun == True:
            print("You have a gun and", ammo, "bullets")
        else:
            if ammo != 0:
                print("You have", ammo, "bullets")
            else: print()
            
import os
import time
# for windows
# os.system('cls')
time.sleep(2)
# Ubuntu version 10.10
os.system('clear')
#
#im.show()
supplies()
print("Background: The world has been taken by storm, as a sudden spike in the global temperature causes extremely polar temperatures. The equator is around 150 Degrees Fahrenheit on average while areas like southern Canada are less than -80 in the summer. This has led to an extreme shortage of available land to live on.")
print("This apocalypse causes what is basically the breakdown of all government systems, leaving every man, woman and child to fend for themself. Due to this, the world is in total anarchy, with groups of anarchists traveling around robbing and killing any people they see. ")
print("In a sense, the sins of man have brought their own doom upon them. You are a person who lived in southern Alaska. Since the temperatures have gotten too low to live in, you must now travel south in order to survive.")
print("Your decisions along the way will decide what path you take and whether you even survive.")
Answer = (input("ENTER A TO CONTINUE\n"))

while(this == False):
    if Answer == ("A"):
        answertrue = False
        Answer1 = (input("START - CHOOSE YOUR METHOD OF TRAVEL (Car, Horse, Foot)\n"))
        while answertrue == False:
            
            if (Answer1 == "Car") | (Answer1 == "Horse") | (Answer1 == "Foot"):
                answertrue = True
            else: 
                Answer1 = (input("Answer must be Horse Car or Foot, try again: "))
        input1 = False
        while input1 == False:
            if Answer1 == ("Car"):
                   print("You Leave in a Car")
                   car = True
                   input1 = True                
            elif Answer1 == ("Horse"):
                   print("You leave on a Horse")
                   horse = True
                   input1 = True
            elif Answer1 == ("Foot"):
                print("You leave on foot")
                input1 = True
    else:
        Answer = (input("Answer must be A, try again: "))
    if input1 == True:
        this = True
        
        
print()
print("You notice after about half a day of travel that a blizzard is coming your way.")
blizzard = True
input1 = False
answertrue = False











#Blizzard Encounter
while(blizzard == True):
        if car == True:
            Answer1 = (input("Options:\nA: Double Back and go back to the house\nB: Try to find shelter close\nC: Try to outrun the storm\n"))
            if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C"):
                answertrue = True
            else:
                answertrue = False
                while answertrue == False:
                    Answer1 = (input("Answer must be A B or C, try again: "))
                    if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C"):
                        answertrue = True                     
            if Answer1 == "A":
                print("You beat the blizzard and make it to your original house again. However, the blizzard traps your car in the garage with so much snow, you must now go on foot\n")
                car = False
            elif Answer1 == "B":
                print("You are unable to find a proper place to put the car and are trapped in the blizzard")
                sys.exit("YOU DIE. GAME OVER")    
            else:
                print("You manage to outrun the blizzard in your car")
                blizzard = False
            
        elif horse == True:
            Answer1 = (input("Options:\nA: Double Back and go back to the house\nB: Try to find shelter close\nC: Continue On and Push Through\n"))
            if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C"):
                answertrue = True
            else:
                answertrue = False
                while answertrue == False:
                    Answer1 = (input("Answer must be A B or C, try again: "))
                    if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C"):
                        answertrue = True       
                        
            if Answer1 == "A":
                print("You beat the blizzard and make it to your original house again. You manage to keep you and the horse safe. You continue out again\n")
                blizzard = False
            elif Answer1 == "B":
                print("You are unable to find a proper place to stay and are trapped in the blizzard, you make a last ditch effort to survive and kill the horse and warm yourself inside it (Revenant style). Your horse is now Dead, but you survive")
                horse = False
                blizzard = False
            else:
                print("You fail to beat the blizzard. You are caught in it and die in the storm")
                sys.exit("YOU DIE. GAME OVER")
                

        else:
            Answer1 = (input("Options:\nA: Brave the storm and move on\nB: Try to find shelter close\nC: Double back and take shelter in the house\n"))
            if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C"):
                answertrue = True
            else:
                answertrue = False
                while answertrue == False:
                    Answer1 = (input("Answer must be A B or C, try again: "))
                    if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C"):
                        answertrue = True                
            if Answer1 == "B":
                print("You are still close to home and know the terrain well, you find a nearby cave and wait out the blizzard")
                blizzard = False
            elif Answer1 == "A":
                print("You Fail to brave such a brutal blizzard. You are swept up in the storm and killed")
                sys.exit("You Die. GAME OVER")
            else:
                print("You manage to survive and make it back home safe and sound. You continue on")
        blizzard = False















time.sleep(10)
# Ubuntu version 10.10
os.system('clear')



supplies()
if car == False:
    print("While traveling south, you are startled by a pack of wolves about 100 yards from you. One notices you, so now you must decide your next course of action")
    print("You know that the wolves are especially dangerous since there has been a mass migration of herbivores towards the equator, meaning that predators up north are starving and extremely dangerous for humans")
    wolves = True
    #im1.show()
else: 
    wolves = False
#Wolves Encounter
print()
while(wolves == True):
      if car == True:
          wolves == False
      elif horse == True:
          Answer1 = (input("Options:\nA: Try to outrun them from horseback\nB: Leave the horse as bait and escape\nC: Fight\nD: Hide with the horse\nE: Hide in an immediate tree and make your horse flee\n"))
          if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C") | (Answer1 == "D") | (Answer1 == "E"):
              answertrue = True
          else:
              answertrue = False
              while answertrue == False:
                  Answer1 = (input("Answer must be A B C D or E, try again: "))
                  if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C") | (Answer1 == "D") | (Answer1 == "E"):
                      answertrue = True       
                      
          if Answer1 == "A":
              print("On horseback you manage to escape, the wolves don't pursue you and you make it out with no issues")
              wolves = False
          elif Answer1 == "B":
              print("While your horse is most certainly dead, you did manage to distract the wolves and make a getaway")
              horse = False
              wolves = False
          elif Answer1 == "C":
              print("Fighting from horseback, you are able to kill 3 of them. However, they swarm you and you are killed")
              sys.exit("YOU DIE. GAME OVER")
          elif Answer1 == "D":
              print("You fail to hide, as the horse is startled and makes too much noise.")
              sys.exit("YOU DIE. GAME OVER")
          elif Answer1 == "E":
              print("You manage to hide, and the horse escapes. However, the wolves find you in a tree. With them being unable to reach you, you gun them down from the tree and kill them all. You use ten bullets. You recover the horse")
              ammo = ammo - 10
      else:
          Answer1 = (input("Options:\nA: Charge and take them on\nB: Run Away\nC: Hide in a Tree\nD: Fight them from a tree\n"))
          if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C") | (Answer1 == "D"):
              answertrue = True
          else:
              answertrue = False
              while answertrue == False:
                  Answer1 = (input("Answer must be A B C or D, try again: "))
                  if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C") | (Answer1 == "D"):
                      answertrue = True                
          if Answer1 == "A":
              print("You fool! You are totally wiped out by the wolves with little effort at all")
              sys.exit("You Die. GAME OVER")
          elif Answer1 == "B":
              print("The wolves catch you with ease. Fighting them on foot is a totaly failure")
              sys.exit("You Die. GAME OVER")
          elif Answer1 == "C":
              print("You manage to hide. However, the wolves find you in a tree. With them being unable to reach you, you are forced to gun them down from the tree and kill them all. You use ten bullets.")
              ammo = ammo - 10
          elif Answer1 == "D":
              print("From the tree you are able to shoot a couple and scare the pack. They run away at the unseen threat")
              ammo = ammo - 2
      wolves = False
      
      
      
      
      
      
      
      
      
      
      
if car == False:
    time.sleep(10)
    # Ubuntu version 10.10
    os.system('clear')   
    supplies()
#Store Encounter
#im2.show()
print("You find that you are running out of food. You come across what looks like an abandoned Store")
if horse == True:
    print("Your horse is starving as well, so it will need to be fed soon")
if car == True:
    print("Your car is running out of gas as well. So you may want to search for gas in this store")
enter = True
while(enter == True):
         Answer1 = (input("Do You Enter? \nA: Go in \nB: Stay away and hunt/forage for your food\n"))
         if (Answer1 == "A") | (Answer1 == "B"):
             answertrue = True
         else:
             answertrue = False
             while answertrue == False:
                 Answer1 = (input("Answer must be A or B, try again: "))
                 if (Answer1 == "A") | (Answer1 == "B"):
                     answertrue = True       
                     
         if Answer1 == "A":
            #im3.show()
            if car == True:
                print("You exit the car and enter the store. You find a man living there, clearly a bit mad. You see he has amassed items from the store that could prove useful, including a bit of ammo. You NEED food and some gas")
            if horse == True:
                print("You leave the horse and enter the store. You find a man living there, clearly a bit mad. You see he has amassed items from the store that could prove useful, including a bit of ammo. You NEED food for you and your horse")
            else: 
                print("You enter the store. You find a man living there, clearly a bit mad. You see he has amassed items from the store that could prove useful, including a bit of ammo. You NEED food")
                
            print("Side note: The man is well armed and looks like he has been here for a while. Maybe being the reason for his slight craziness.")
            Store = True
            enter = False
         elif Answer1 == "B":
             if ammo < 3:
                print("You find that you do not have the ammo necessary to get a decent amount of meat, must make use of the store")
                Store = True
                enter = False
             #im7.show()
             ammo = ammo - 3
             print("You manage to hunt for food, but are unable to find any plants, you do find animals to kill")
             if horse == True:
                 print("You cannot find any plants, so you are unable to feed your horse, and it soon dies of starvation")
                 Store = False
             if car == True:
                 print("Your car runs out of gas, so you must abandon it")
                 Store = False
            
         enter = False








while Store == True:
         Answer1 = (input("Options:\nA: Attack the man and take everything\nB: Barter with the man\nC: Steal from him\nD: Leave and go hunt\n"))
         if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C") | (Answer1 == "D"):
             answertrue = True
         else:
             answertrue = False
             while answertrue == False:
                 Answer1 = (input("Answer must be A B C or D, try again: "))
                 if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C") | (Answer1 == "D"):
                     answertrue = True       
         print()
         print()
         if Answer1 == "A":
             print()
             print("Man is well armed and has knowledge of the terrain. You are easily decimated by him as you only have your pistol to compete with him.")
             sys.exit("You Die. GAME OVER")
         elif Answer1 == "B":
            if car == True:
                if ammo >= 8:
                     print("You speak with the man. He offers multiple deals.")
                     print("Deal A: 8 bullets for a Weeks worth of food")
                     print("Deal B: Your gun and ammo for all the food you can carry and gas")
                     print("Deal C: The car for 20 bullets, a new rifle and all the food you can hold")
                     print("For personal choices, you can choose D to fight or E to run away")
                     Answer2 = (input("A, B, C D or E: "))
                     answer2true = False
                     if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C") | (Answer2 == "D") | (Answer2 == "E"):
                        answer2true = True
                     else:
                        answer2true = False
                        while answer2true == False:
                            Answer1 = (input("Answer must be A B C D or E, try again: "))
                            if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C") | (Answer2 == "D") | (Answer2 == "E"):
                                answer2true = True
                     if Answer2 == "A":
                        print("You give him the 8 bullets and receive a weeks worth of food. You leave in peace. However, you are unable to gas your car. You are forced to abandon it")                        
                        ammo = ammo - 8
                        horse = False
                     elif Answer2 == "B":
                        print("You give him the gun and ammo, and he is weirdly honest. You leave with your food in peace. You are now able to feed yourself and have gas for the car")
                        ammo = 0
                        gun = False
                     elif Answer2 == "C":
                         print("You give him you car. You now have a rifle and 20 more bullets along with an insane amount of food")
                         horse = False
                         rifle = True
                     elif Answer2 == "D":
                        print("You attempt to fight him. However, he has much better guns and knowledge of the turf than you. He defeats you")
                        sys.exit("You Die. GAME OVER")
                     elif Answer2 == "E":
                        print("You run away. However, you don't even make it to the door and he guns you down. He only wounds you, but he takes all of your things, leaving you with no way to survive. You starve to death out in the frozen tundra")
                        sys.exit("You Die. GAME OVER")
                     Store = False
                     
                else: 
                    print("You speak with the man. He offers multiple deals.")
                    print("Deal A: Your gun and ammo for all the food you can carry and gas for the car")
                    print("Deal B: The car for 20 bullets, a new rifle and all the food you can hold")
                    print("For personal choices, you can choose D to fight or E to run away")
                    Answer2 = (input("A, B, C or D: "))
                    answer2true = False
                    if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C") | (Answer2 == "D"):
                       answer2true = True
                    else:
                       answer2true = False
                       while answer2true == False:
                           Answer1 = (input("Answer must be A B C or D, try again: "))
                           if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C") | (Answer2 == "D"):
                               answer2true = True
                    if Answer2 == "A":
                       print("You give him the gun and ammo, and he is weirdly honest. You leave with your food in peace. You are now able to feed yourself and have gas for the car")
                       ammo = 0
                       gun = False
                    elif Answer2 == "B":
                        print("You give him you car. You now have a rifle and 20 more bullets along with an insane amount of food")
                        horse = False
                        rifle = True
                    elif Answer2 == "C":
                       print("You attempt to fight him. However, he has much better guns and knowledge of the turf than you. He defeats you")
                       sys.exit("You Die. GAME OVER")
                    elif Answer2 == "D":
                       print("You run away. However, you don't even make it to the door and he guns you down. He only wounds you, but he takes all of your things, leaving you with no way to survive. You starve to death out in the frozen tundra")
                       sys.exit("You Die. GAME OVER")
                    Store = False
            if horse == True:
             if ammo >= 8:
                     print("You speak with the man. He offers multiple deals.")
                     print("Deal A: 8 bullets for a Weeks worth of food")
                     print("Deal B: Your gun and ammo for all the food you can carry and food for the horse")
                     print("Deal C: The Horse for 20 bullets, a new rifle and all the food you can hold")
                     print("For personal choices, you can choose D to fight or E to run away")
                     Answer2 = (input("A, B, C D or E: "))
                     answer2true = False
                     if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C") | (Answer2 == "D") | (Answer2 == "E"):
                        answer2true = True
                     else:
                        answer2true = False
                        while answer2true == False:
                            Answer1 = (input("Answer must be A B C D or E, try again: "))
                            if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C") | (Answer2 == "D") | (Answer2 == "E"):
                                answer2true = True
                     if Answer2 == "A":
                        print("You give him the 8 bullets and receive a weeks worth of food. You leave in peace. However, you are unable to properly feed your horse. It dies")                        
                        ammo = ammo - 8
                        horse = False
                     elif Answer2 == "B":
                        print("You give him the gun and ammo, and he is weirdly honest. You leave with your food in peace. You are now able to feed you and your horse")
                        ammo = 0
                        gun = False
                     elif Answer2 == "C":
                         print("You give him you horse. You now have a rifle and 20 more bullets along with an insane amount of food")
                         horse = False
                         rifle = True
                     elif Answer2 == "D":
                        print("You attempt to fight him. However, he has much better guns and knowledge of the turf than you. He defeats you")
                        sys.exit("You Die. GAME OVER")
                     elif Answer2 == "E":
                        print("You run away. However, you don't even make it to the door and he guns you down. He only wounds you, but he takes all of your things, leaving you with no way to survive. You starve to death out in the frozen tundra")
                        sys.exit("You Die. GAME OVER")
                     Store = False
                     
             else: 
                print("You speak with the man. He offers multiple deals.")
                print("Deal A: Your gun and ammo for all the food you can carry and food for the horse")
                print("Deal B: The Horse for 20 bullets, a new rifle and all the food you can hold")
                print("For personal choices, you can choose D to fight or E to run away")
                Answer2 = (input("A, B, C or D: "))
                answer2true = False
                if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C") | (Answer2 == "D"):
                   answer2true = True
                else:
                   answer2true = False
                   while answer2true == False:
                       Answer1 = (input("Answer must be A B C or D, try again: "))
                       if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C") | (Answer2 == "D"):
                           answer2true = True
                if Answer2 == "A":
                   print("You give him the gun and ammo, and he is weirdly honest. You leave with your food in peace. You are now able to feed you and your horse")
                   ammo = 0
                   gun = False
                elif Answer2 == "B":
                    print("You give him you horse. You now have a rifle and 20 more bullets along with an insane amount of food")
                    horse = False
                    rifle = True
                elif Answer2 == "C":
                   print("You attempt to fight him. However, he has much better guns and knowledge of the turf than you. He defeats you")
                   sys.exit("You Die. GAME OVER")
                elif Answer2 == "D":
                   print("You run away. However, you don't even make it to the door and he guns you down. He only wounds you, but he takes all of your things, leaving you with no way to survive. You starve to death out in the frozen tundra")
                   sys.exit("You Die. GAME OVER")
                Store = False
  
            else:
                if ammo >= 8:
                    print("Give him 8 bullets or your gun, and he will give you enough food to last a few weeks. Because he is senile he threatens to kill you if you don't barter with him")
                    Answer2 = (input("A: Give Gun\nB: 8 Bullets\nC: Fight\nD: Run Away\n"))
                    answer2true = False
                    if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C") | (Answer2 == "D"):
                        answer2true = True
                    else:
                        answer2true = False
                        while answer2true == False:
                            Answer1 = (input("Answer must be A B or C, try again: "))
                            if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C"):
                                answer2true = True
                    if Answer2 == "A":
                        print("You give him the gun, and he is weirdly honest. You leave with your food in peace")
                        
                    elif Answer2 == "B":
                        print("You give him the 8 bullets and receive a weeks worth of food. You leave in peace")
                        ammo = ammo - 8
                    elif Answer2 == "C":
                        print("You attempt to fight him. However, he has much better guns and knowledge of the turf than you. He defeats you")
                        sys.exit("You Die. GAME OVER")
                    elif Answer2 == "D":
                        print("You run away. However, you don't even make it to the door and he guns you down. He only wounds you, but he takes all of your things, leaving you with no way to survive. You starve to death out in the frozen tundra")
                        sys.exit("You Die. GAME OVER")
                    gun = False
                    Store = False
                else:
                    print("He demands your gun in return for the food. Seeing as he is insane, he threatens to kill you if you don't agree. Welcome to Looneyville")
                    Answer2 = (input("A: Give Gun\nB: Fight him\nC: Run away and hope for the best\n"))
                    if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C"):
                        answer2true = True
                    else:
                        answer2true = False
                        while answer2true == False:
                            Answer1 = (input("Answer must be A B or C, try again: "))
                            if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C"):
                                answer2true = True
                    if Answer2 == "A":
                        print("You give him the gun, and he is weirdly honest. You leave with your food in peace")
                        gun = False
                        Store = False
                    elif Answer2 == "B":
                        print("You attempt to fight him. However, he has much better guns and knowledge of the turf than you. He defeats you")
                        sys.exit("You Die. GAME OVER")
                    elif Answer2 == "C":
                        print("You run away. However, you don't even make it to the door and he guns you down. He only wounds you, but he takes all of your things, leaving you with no way to survive. You starve to death out in the frozen tundra")
                        sys.exit("You Die. GAME OVER")

         if Answer1 == "C":
             print("What would you like to steal? Food would be easiest, Gas would be medium while weapons would be hard")
             print("A: Weapon/Ammo")
             if horse == True:
                 print("B: Food for you and horse")
             else:
                 print("B: Just Food")
             print(("C: Weapon/Ammo and Food"))
             if car == True:
                 print("D: Gas")
                 print("E: Gas and Gun/Ammo")
                 print("F: Gas and Food")
                 print("G: All of the Above")
                 print("H: Leave and go Hunt")
             else: 
                 print("D: Leave now and go hunt")
             if car == True:
                Answer2 = (input("A,B,C,D,E, F or G: "))
                answer2true = False
                if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C") | (Answer2 == "D") | (Answer2 == "E") | (Answer2 == "F") | (Answer2 == "G") | (Answer2 == "H"):
                    answer2true = True
                else:
                    answer2true = False
                    while answer2true == False:
                        Answer1 = (input("Answer must be A-G, try again: "))
                        if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C") | (Answer2 == "D") | (Answer2 == "E") | (Answer2 == "F") | (Answer2 == "G") | (Answer2 == "H"):
                            answer2true = True
             else:
                Answer2 = (input("A,B,C or D: "))
                answer2true = False
                if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C") | (Answer2 == "D") | (Answer2 == "E") | (Answer2 == "F") | (Answer2 == "G"):
                    answer2true = True
                else:
                    answer2true = False
                    while answer2true == False:
                        Answer1 = (input("Answer must be A B or C, try again: "))
                        if (Answer2 == "A") | (Answer2 == "B") | (Answer2 == "C") | (Answer2 == "D") | (Answer2 == "E") | (Answer2 == "F") | (Answer2 == "G"):
                            answer2true = True
             if Answer2 == "A":
                print("You search for the guns and attempt to steal them. However, the man keeps them always within eyeshot and catches you")
                sys.exit("You Die. GAME OVER")
             if Answer2 == "B":
                 print("Those items were kept in an area that was easy to steal from. You sneakily snatch a decent amount of food and takeoff")
                 car = False
             if Answer2 == "C":
                print("The food was easy to steal, but you are caught stealing such high value items as the guns and ammo. He immediately attacks and kills you.")
                sys.exit("You Die. GAME OVER")
             if Answer2 == "D":
                if car == True:
                    print("The gas was hard to steal, but you make it out in your getaway car. You now have to hunt though.")
                if ammo < 3: 
                    print("You find that you do not have enough ammo to hunt for the meat required to feed you. After you are unable to find any plants to eat and unable to reenter the store, you succumb to starvation")
                    sys.exit("You Die. GAME OVER")
                else:
                    print("You kill enough animals to feed yourself. It takes 3 bullets")
                    ammo = ammo - 3
                    Store = False
             if Answer2 == "E":
                print("while you were able to get the gas, the guns were kept under too tight of a watch, and you are killed by the man after he catches you")
                sys.exit("You Die. GAME OVER")
             if Answer2 == "F":
                print("You manage to get the Gas and the food and make an escape in your getaway car")
                Store = False
             if Answer2 == "G":
                print("Trying to literally steal everything this man owns. He easily catches you and kills you")
                sys.exit("You Die. Game Over")
             if Answer2 == "H":
                 if ammo < 3:
                    print("You find that you do not have the ammo necessary to get a decent amount of meat, must make use of the store")
                    Store = True
                    
                 
                 else: 
                     ammo = ammo - 3
                     print("You manage to hunt for food, but are unable to find any plants, you do find animals to kill")
                     if horse == True:
                        print("You cannot find any plants, so you are unable to feed your horse, and it soon dies of starvation")
                        
                     if car == True:
                         print("Your car runs out of gas, so you must abandon it")
                         
                     car = False
                     horse = False
                     Store = False
         if Answer1 == "D":
             if ammo < 3:
                print("You find that you do not have the ammo necessary to get a decent amount of meat, must make use of the store")
                Store = True
                
             
             else: 
                 ammo = ammo - 3
                 print("You manage to hunt for food, but are unable to find any plants, you do find animals to kill")
                 if horse == True:
                    print("You cannot find any plants, so you are unable to feed your horse, and it soon dies of starvation")
                    
                 if car == True:
                     print("Your car runs out of gas, so you must abandon it")
                     
                 car = False
                 horse = False
                 Store = False
                 
                 
time.sleep(10)
# Ubuntu version 10.10
os.system('clear')

supplies()



print("During you travels, you are ambushed by a group of bandits. This is one of the savage tribes that have been parading through North America.")
print("From reports you have heard on the radio, you know that they worship battle, as they believe that is the only way to appease their god, or else the Eternal Freeze will continue...")
print("They surround you, and one massive man steps out unarmed from a car to fight you. What do you do?")
bandits = True
#im4.show()
#im5.show()
#im6.show()

while(bandits == True):
         Answer1 = (input("How do you respond? \nA: Attempt to escape \nB: Fight\nC: Talk it out\n"))
         if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C"):
             answertrue = True
         else:
             answertrue = False
             while answertrue == False:
                 Answer1 = (input("Answer must be A B or C, try again: "))
                 if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C"):
                     answertrue = True       
                     
         if Answer1 == "A":
            if (car == True):
                print("You manage to escape")
                bandits = False
            else:
                print("With the amount of them, it is impossible to really escape. You are killed for your cowardice.")
                sys.exit("You Die. GAME OVER")
             
         elif Answer1 == "B":
             Answer2 = (input("You now have to fight this person one on one. Will you \nA: Fight fairly\nB: Fight Dirty, with weapons\n"))
             answer2true = False
             if (Answer2 == "A") | (Answer2 == "B"):
                answer2true = True
             else:
                answer2true = False
                while answer2true == False:
                    Answer1 = (input("Answer must be A or B, try again: "))
                    if (Answer2 == "A") | (Answer2 == "B"):
                        answer2true = True
             if Answer2 == "A":
                 print("Fighting fairly, there is no way that you could beat this guy, however, when he beats you the tribe respects your efforts. You offered a good fight, so they let you live. However, all of you supplies are stolen except for tiny scraps of food.")
                 car = False
                 horse = False
                 gun = False
                 rifle = False
                 ammo = 0
                 bandits = False
             if Answer2 == "B":
                 if ammo > 0:
                     print("You immediately shoot the man in the head with your conceiled weapon. The tribe is amazed at this.")
                     print("A middle aged woman comes to speak to you. You notice that she is the only one who has spoken.")
                     print("She offers you two options: A: Join their tribe and live by the way of their god. B: Leave in peace, leaving the tribe without their strongest")
                     Answer3 = (input("Options: A or B: "))
                     if (Answer3 == "A") | (Answer3 == "B"):
                         answer3true = True
                     else:
                         answer3true = False
                         while answer3true == False:
                             Answer1 = (input("Answer must be A or B, try again: "))
                             if (Answer3 == "A") | (Answer3 == "B"):
                                 answertr3ue = True
                     if Answer3 == "A":
                         print("ENDING: The Game is over. You live on in the tribe, surviving for 5 years until your tribe is wiped out by a stronger one. You find that the life of the anarchist was oddly pleasing, and that an extreme apocalypse called for extreme measures to survive")
                         sys.exit("YOU WIN. Now try again to see what other endings you can come up with.")
                     if Answer3 == "B":
                         print("You leave in peace as the woman said. The tribe leaves and you are left alone thinking about how far down society has gone")
                 else:
                     print("The bandit notices you try to use a knife and then uses his own weapon and easily decimates you. You are killed in seconds")
                     sys.exit("You Die. GAME OVER")
                 bandits = False
         if Answer1 == "C":
             print("These people Don't talk. You are forced to fight.")
             Answer2 = (input("You now have to fight this person one on one. Will you \nA:Fight dirty, with weapons\nB: try to fight fair: "))
             answer2true = False
             if (Answer2 == "A") | (Answer2 == "B"):
                answer2true = True
             else:
                answer2true = False
                while answer2true == False:
                    Answer1 = (input("Answer must be A or B, try again: "))
                    if (Answer2 == "A") | (Answer2 == "B"):
                        answer2true = True
             if Answer2 == "A":
                 print("Fighting fairly, there is no way that you could beat this guy, however, when he beats you the tribe respects your efforts. You offered a good fight, so they let you live. However, all of you supplies are stolen except for tiny scraps of food.")
                 car = False
                 horse = False
                 gun = False
                 rifle = False
                 ammo = 0
                 bandits = False
             if Answer2 == "B":
                 print("You sneakily stab the man in the neck with a small knife you had conceiled. The tribe is amazed at this.")
                 print("A middle aged woman comes to speak to you. You notice that she is the only one who has spoken.")
                 print("She offers you two options: A: Join their tribe and live by the way of their god. B: Leave in peace, leaving the tribe without their strongest")
                 Answer3 = (input("Options: A or B: "))
                 if (Answer3 == "A") | (Answer3 == "B"):
                     answer3true = True
                 else:
                     answer3true = False
                     while answer3true == False:
                         Answer1 = (input("Answer must be A or B, try again: "))
                         if (Answer3 == "A") | (Answer3 == "B"):
                             answertr3ue = True
                 if Answer3 == "A":
                     print("ENDING: The Game is over. You live on in the tribe, surviving for 5 years until your tribe is wiped out by a stronger one. You find that the life of the anarchist was oddly pleasing, and that an extreme apocalypse called for extreme measures to survive")
                     sys.exit("YOU WIN. Now try again to see what other endings you can come up with.")
                 if Answer3 == "B":
                     print("You leave in peace as the woman said. The tribe leaves and you are left alone thinking about how far down society has gone")
                 bandits = False






time.sleep(10)
# Ubuntu version 10.10
os.system('clear')

supplies()
#im9.show()
print("You now feel that the temperature is beginning to become more 'normal'.")
print("You now come to a river that is frozen over. You cannot see how thick the freeze is, but it is going to be dangerous to cross.")
river = True
print("You now have to make a decision on how to cross.")
print("A: Go out to find a bridge. It could take days to find one")
if car == True:
    print("B: Cross with your car")
    print("C: Abandon the car and cross on foot")
elif horse == True:
    print("B: Cross with your horse")
    print("C: Abandon the horse and cross on foot")
else:
    print("B: Cross on foot")
while(river == True):
         if (car == True) | (horse == True):
             Answer1 = (input("Options: A, B or C: "))
             if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C"):
                 answertrue = True
             else:
                 answertrue = False
                 while answertrue == False:
                     Answer1 = (input("Answer must be A B or C, try again: "))
                     if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C"):
                         answertrue = True       
         else:
             Answer1 = (input("Options: A, or B: "))
             if (Answer1 == "A") | (Answer1 == "B"):
                 answertrue = True
             else:
                 answertrue = False
                 while answertrue == False:
                     Answer1 = (input("Answer must be A or B, try again: "))
                     if (Answer1 == "A") | (Answer1 == "B"):
                         answertrue = True            
         if Answer1 == "A":
            print("After a short search, you manage to find a bridge and cross.")
         elif Answer1 == "B":
             if (car == True) | (horse == True):
                 print("The huge amount of weight breaks through the ice. You fall through and are swept up in the current. You drown")
                 sys.exit("You Die. GAME OVER")
             else: 
                 print("You cross on foot with no issue, bringing you supples with you")
         elif Answer1 == "C":
             print("You succesfully cross, but abandon your most valuable resource to do so.")
             car = False
             horse = False
         river = False

time.sleep(10)
# Ubuntu version 10.10
os.system('clear')

supplies()
#im10.show()
print("Now you are in the inhabitable areas. You notice that there is a crazy variety of animals.")
print("It feels like everywhere you look there is something fighting something for space. Elk fighting moose, bobcats fighting lynx, coyotes fighting wolves. It feels like this apocalypse has brought the environment as well as society to an all out war for space")
print("You also find what appears to be a battlefield, with big spots of ash and broken trees signalling that a significant conflict occured there.")
print("You now encounter what looks like an abandoned cabin. You suspect that you can live out your life here, as the cabin appears to have been totally abandoned for years")
Answer1 = (input("Options: \nA: Live there \nB: Continue on\n"))
if (Answer1 == "A") | (Answer1 == "B"):
    answertrue = True
else:
    answertrue = False
    while answertrue == False:
        Answer1 = (input("Answer must be A or B, try again: "))
        if (Answer1 == "A") | (Answer1 == "B"):
            answertrue = True
            
if Answer1 == "A":
    print("You live out you life there. The life of the survivalist seems great for you. You live for 20 years and seem to have no trouble, until you suddenly get an extreme case of Dysentary. You die from it after having lived a relativeley comfortable life of solitude.")            
    sys.exit("You WIN. Now try again to see what other endings you can come up with.")
else:
    print("You continue on...")
    




time.sleep(10)
# Ubuntu version 10.10
os.system('clear')

supplies()
#im8.show()
print("During your travels, you encounter a lone child. The girl looks to be around 12 years old.")
print("The child is alone and crying. You can examine the area around to check for traps if you would like, or you can just walk up to her, or you can run away.")
Answer1 = (input("Options: \nA: Check \nB: Go right in\nC: Continue on\n"))
if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C"):
    answertrue = True
else:
    answertrue = False
    while answertrue == False:
        Answer1 = (input("Answer must be A B or C, try again: "))
        if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C"):
            answertrue = True
            
if Answer1 == "A":
    print("You find that there is a man waiting to ambush anyone that approaches the girl. He hasn't noticed you.")
    Answer3 = (input("Options:\nA: Kill him\nB: Knock Him Out\nC: Leave\n"))
    if (Answer3 == "A") | (Answer3 == "B") | (Answer3 == "C"):
        answer3true = True
    else:
        answer3true = False
        while answer3true == False:
            Answer3 = (input("Answer must be A B or C, try again: "))
            if (Answer3 == "A") | (Answer3 == "B") | (Answer3 == "C"):
                answer3true = True       
    if Answer3 == "A":
        print("You sneak up on the man and kill him with a knife. He falls dead. Do you now approach the child?")
        print("Options: ")
        print("A: Approach, B: Leave")
        Answer2 = (input("Options: A or B: "))
        if (Answer2 == "A") | (Answer1 == "B"):
            answer2true = True
        else:
            answer2true = False
            while answer2true == False:
                Answer2 = (input("Answer must be A or B, try again: "))
                if (Answer2 == "A") | (Answer2 == "B"):
                    answer2true = True
        if Answer2 == "A":
            print("You approach the girl, and she immediately hugs you. She is clearly distraught. She then follows you around, with you being unable to get rid of her. You now have a traveling companion")
            companion = True
        else:
            print("You Continue on, leaving the lone girl to fend for herself.")
            companion = False
    if Answer3 == "B":
        print("You sneak up on the man and attempt to knock him out. You fail and the two of you get into a scuffle. You end up being forced to kill the man. Do you now approach the child?")
        print("Options: ")
        print("A: Approach, B: Leave")
        Answer2 = (input("Options: A or B: "))
        if (Answer2 == "A") | (Answer1 == "B"):
            answer2true = True
        else:
            answer2true = False
            while answer2true == False:
                Answer2 = (input("Answer must be A or B, try again: "))
                if (Answer2 == "A") | (Answer2 == "B"):
                    answer2true = True
        if Answer2 == "A":
            print("You approach the girl, and she immediately hugs you. She is clearly distraught. She then follows you around, with you being unable to get rid of her. You now have a traveling companion")
            companion = True
        else:
            print("You Continue on, leaving the lone girl to fend for herself.")
            companion = False
    if Answer3 == "C":    
        print("You Continue on. Leaving the child in peril...")
elif Answer1 == "B":
    print("You approach the girl and find that there was an ambush waiting, and you are shot from an unknown origin. You are killed")
    sys.exit("You Die. GAME OVER")
    companion = True
elif Answer1 == "C":
    print("You continue on...")
    companion = False
    

time.sleep(10)
# Ubuntu version 10.10
os.system('clear')

supplies()

print()
if companion == True:
    print("You have traveled with the girl and become quite attached to her. She has become almost like a daughter to you.")
print("After about 2 weeks of travel, you see a small settlement. It appears to be a bastion of hope in these darker times. You see about 20 people moving around farming, ranching, etc.")
print("Do You Approach?")
Answer1 = (input("Optiosn:\nA: Approach\nB: Evade\n"))
if (Answer1 == "A") | (Answer1 == "B"):
    answertrue = True
else:
    answertrue = False
    while answertrue == False:
        Answer1 = (input("Answer must be A or B, try again: "))
        if (Answer1 == "A") | (Answer1 == "B"):
            answertrue = True
            
if Answer1 == "A": 
    print("You Enter. The people are oddly kind. It is a welcome contrast to your experiences so far.")
    print("You spend about a week there. You find that this life is nice. You consider staying there.")
    print("You now come to a major crossroads. You can choose to leave, or you can choose to stay there")
    if companion == True:
        print("You also must consider the child. Will you take responsibility for her, or go out alone and leave her.")
    FinalAnswer = (input("Options:\nA: Leave\nB: Stay\n"))
    if (FinalAnswer == "A") | (FinalAnswer == "B"):
        answerftrue = True
    else:
        answerftrue = False
        while answerftrue == False:
            FinalAnswer = (input("Answer must be A or B, try again: "))
            if (FinalAnswer == "A") | (FinalAnswer == "B"):
                answerftrue = True
    if FinalAnswer == "A":
        if companion == True:
            print("Now you must decide whether to leave the girl or bring her with you")
            Answer2 = (input("Options:\nA: Bring Her\nB:Leave Her\n"))
            if (Answer2 == "A") | (Answer2 == "B"):
                answer2true = True
            else:
                answer2true = False
                while answer2true == False:
                    Answer2 = (input("Answer must be A or B, try again: "))
                    if (Answer2 == "A") | (Answer2 == "B"):
                        answer2true = True
            if Answer2 == "A":
                print("ENDING: You take the girl with you. You live out your lives as a parent/daughter pair")
                print("You live approximately 15 years, with the girl growing up the two of you traveling across North America.")
                print("However, you are mortally wounded in a conflict with a group of savages. You die peacefully with her at your side")
                sys.exit("You Win. Now try again to see what other endings you can come up with")
            if Answer2 == "B": 
                print("ENDING: You go out alone, living out you life as a loan wanderer, never finding a place to settle down")
                print("You grow senile being alone for so long and you die 5 years later in in a minor scuffle with a settlement.")
                sys.exit("You Win. Now try again to see what other endings you can come up with")
        else:
            print("ENDING: You go out alone, living out you life as a loan wanderer, never finding a place to settle down")
            print("You grow senile being alone for so long and you die 5 years later in in a minor scuffle with a settlement.")
            sys.exit("You Win. Now try again to see what other endings you can come up with")
    if FinalAnswer == "B":
        if companion == True:
            print("ENDING: Safety was key for you. You and you companion live together in the village for the rest of your lives")
            print("You live out your life and don't finally perish until 45 years later. You die peacefully with you great companion at your side when it happens from natural causes.")
            sys.exit("You Win. This was the best possible ending. Congratulations.")
        else:
            print("ENDING: Safety was key for you. You live happily in the village, eventually settling down and making a family")
            print("You ultimately die 40 years after your journey began. You die peacefully in bed with your family surrounding you. You lived a happy life")
            sys.exit("You Win. Now try again to see what other endings you can come up with")
else:
    if companion == True:
        print("You avoid the settlement live out your lives as a parent/daughter pair")
        print("You live approximately 15 years, with the girl growing up the two of you traveling across North America. You live your life as a father figure to the child, wandering from place to place across North America")
        print("However, you are mortally wounded in a conflict with a group of savages. You die peacefully with her at your side")
        sys.exit("You Win. Now try again to see what other endings you can come up with")
    else:
        print("ENDING: You continue on alone, living out you life as a loan wanderer, never finding a place to settle down")
        print("You grow senile being alone for so long and you die 5 years later in in a minor scuffle with a settlement.")
        sys.exit("You Win. Now try again to see what other endings you can come up with")
'''  
     else:
         Answer1 = (input("You Have 3 options:\nA: Charge and take them on\nB: Run Away\nC: Hide in a Tree\nD: Fight them from a tree\n"))
         if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C") | (Answer1 == "D"):
             answertrue = True
         else:
             answertrue = False
             while answertrue == False:
                 Answer1 = (input("Answer must be A or B, try again: "))
                 if (Answer1 == "A") | (Answer1 == "B") | (Answer1 == "C") | (Answer1 == "D"):
                     answertrue = True                
         if Answer1 == "A":
             print("You fool! You are totally wiped out by the wolves with little effort at all")
             sys.exit("You Die. GAME OVER")
         elif Answer1 == "B":
             print("The wolves catch you with ease. Fighting them on foot is a totaly failure")
             sys.exit("You Die. GAME OVER")
         elif Answer1 == "C":
             print("You manage to hide, and the horse escapes. However, the wolves find you in a tree. With them being unable to reach you, you gun them down from the tree and kill them all. You use ten bullets. You recover the horse")
             ammo = ammo - 10
         elif Answer1 == "D":
             print("From the tree you are able to shoot a couple and scare the pack. They run away at the unseen threat")
             ammo = ammo - 2
 wolves = False
'''

      
      
      
        
