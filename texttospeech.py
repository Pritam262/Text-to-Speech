
#import the pyttsx3 module inside program
import pyttsx3

#initializing the module

engine = pyttsx3.init()
  # .say() funtion is used to spak the text which you are written

engine.say("He, What is your name?")

#this is used to process and run the program

engine.runAndWait()
