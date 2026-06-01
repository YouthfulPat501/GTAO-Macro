import pydirectinput
import time

pydirectinput.PAUSE = 0.05

def sendInput(path):
    with open(path, "r") as file:
        for line in file:
            line = line.strip().lower()
            #print(f"LINE: {line}")
            if not line:
                continue
            elif line.startswith("delay"):
                time.sleep(float(line.split()[1]))
            elif len(line) >= 2 and len(set(line)) == 1:
                key = line[0]
                hold_duration = len(line) * 0.25
                #print(f"HOLD: '{key}' for {hold_duration}s")
                pydirectinput.keyDown(key)
                time.sleep(hold_duration)
                pydirectinput.keyUp(key)
                time.sleep(0.02)
            else:
                #print(f"PRESS: '{line}'")
                pydirectinput.press(line)