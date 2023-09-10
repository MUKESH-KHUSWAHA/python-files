#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      mukes
#
# Created:     04/09/2023
# Copyright:   (c) mukes 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pyttsx3
engine=pyttsx3.init()
name=["rahul","rohan", "karn"]
for i in name:
    engine.say(f"shoutout to {i}" )

engine.runAndWait()