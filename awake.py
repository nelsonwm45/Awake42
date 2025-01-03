from pynput.mouse import Controller
from time import sleep

mouse = Controller()

print("Press Ctrl+C to stop.")
while True:
    sleep(60)         # Wait for 1 minute
    mouse.move(1, 0)  # Move the mouse slightly
    mouse.move(-1, 0)
