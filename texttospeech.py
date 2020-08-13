
#import the pyttsx3 module inside program
import pyttsx3

#initializing the module

engine = pyttsx3.init()
  # .say() funtion is used to spak the text which you are written

engine.say("NEW DELHI: IndusInd Bank on Tuesday said it has sold a portion of the invoked pledged shares of Eveready Industries and McLeod Russel India.")

#this is used to process and run the program

engine.runAndWait()