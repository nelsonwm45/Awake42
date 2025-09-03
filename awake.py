from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
from time import sleep
import logging
import os
import random

# Set up logging
logging.basicConfig(filename='awake.log', level=logging.INFO, format='%(asctime)s - %(message)s')

mouse = MouseController()
keyboard = KeyboardController()

logging.info("Awake script started.")

# Save the PID to a file
with open('awake.pid', 'w') as f:
    f.write(str(os.getpid()))

# Main loop
while True:
    sleep(10)
    
    # Mouse movement
    dx = random.randint(5, 20)
    dy = random.randint(5, 20)
    if random.choice([True, False]):
        dx = dx
    else:
        dx = -dx

    if random.choice([True, False]):
        dy = dy
    else:
        dy = -dy
    mouse.move(dx, dy)
    mouse.move(-dx, -dy)
    logging.info(f"Mouse moved by ({dx}, {dy}) and returned.")

    # Keyboard press
    # keyboard.press(Key.f15)
    # keyboard.release(Key.f15)
    # logging.info("Pressing f15 key!")
