print("Welcome to my Quiz contest")
import pyttsx3
engine= pyttsx3.init()
voice = engine.getProperty('voices')
voicerate = engine.setProperty("rate",178)
engine.setProperty('voice', voice[1].id)

engine.say("Welcome to my Quiz contest")
engine.runAndWait()
engine.stop()
engine.say("Do you want to play?")
engine.runAndWait()
engine.stop()

playing= input("Do you want to play?")


if playing != "yes":
    quit()
engine.say("Okay! let's play")
engine.runAndWait()
engine.stop()

print("Okay! let's play")

engine.say("Who is the principal of Our college UIT burdwan?")
engine.runAndWait()
engine.stop()

answer = input("Who is the principal of Our college UIT burdwan?")

if answer == "AMIT":
    print("correct")    
    engine.say("correct,You are The real student of UIT burdwan and you got 1 lac rupees")
    engine.runAndWait()
    engine.stop()

elif answer == "amit":
    print("correct")    
    engine.say("correct,You are The real student of UIT burdwan and you got 1 lac rupees")
    engine.runAndWait()
    engine.stop()

else:
    print("incorrect!")    
    engine.say("incorrent!")
    engine.runAndWait()
    engine.stop() 


print("How many Brunches are in our college")
engine.say("How many Brunches are in our college")
engine.runAndWait()
engine.stop()
answer = input("Enter -> ")

if answer == "5":
    print("Correct!")
    engine.say("Correct, you got 2 thousands rupees")
    engine.runAndWait()
    engine.stop()    


else:
    print("Incorrect!")    
    engine.say("so sad you don't know,there is 5 brunches in our college like CSE,IT,ECE,EE,AEIE")
    engine.runAndWait()
    engine.stop()    
  
engine.say("How many hostel in our college?")
engine.runAndWait()
engine.stop()
answer = input("How many hostel in our college?")
if answer =="4":
    print("correct")
    engine.say("noise viru,you have a great memories")
    engine.runAndWait()
    engine.stop()
elif answer == "2":
    engine.say("but you forget APC Banabas!")
    engine.runAndWait()
    engine.stop()

else:
    print("incorrect")
    engine.say("A vi pata nahi")
    engine.runAndWait()
    engine.stop()    
pass