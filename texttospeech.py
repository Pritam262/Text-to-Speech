# Python program to show
# how to convert text to speech
import pyttsx3

# Initialize the converter
converter = pyttsx3.init()

# Set properties before adding
# Things to say

# Sets speed percent
# Can be more than 100
converter.setProperty('rate', 140)
# Set volume 0-1
converter.setProperty('volume', 0.8)
voices = converter.getProperty('voices')
converter.setProperty('voice', voices[1].id) #changing index changes voices but ony 0 and 1 are working here

# Queue the entered text
# There will be a pause between
# each one like a pause in
# a sentence
converter.say('''Parliament’s IT committee drops 4G in J&K issue from meeting agenda.''')
# converter.say("I'm also a geek")

# Empties the say() queue
# Program will not continue
# until all speech is done talking
converter.runAndWait()