import os
import keyboard
from sendInput import sendInput

actions = {
    "f4":        "Macros/Personal_Vehicle_Spawn.txt",
    "f5":        "Macros/Personal_Vehicle_Despawn.txt",
    "f6":        "Macros/Sparrow_Spawn.txt",
    "f7":        "Macros/Sparrow_Despawn.txt",
    "f8":        "Macros/BST.txt",
    "delete":    "Macros/Call_Lester.txt",
    "end":       "Macros/Call_Mechanic.txt",
    "page down": "Macros/Call_MMI.txt",
    "`":         "Macros/Brake.txt",
}

def on_key(event):
    if event.name in actions:
        #print(event.name)
        sendInput(actions[event.name])

keyboard.on_press(on_key)
keyboard.add_hotkey("ctrl+q", lambda: os._exit(0))

with open("Intro.txt", "r", encoding="utf-8") as intro:
    print(intro.read())

if input() == "!help":
    with open("Help.txt", "r", encoding="utf-8") as help:
        print(help.read())

keyboard.wait()
