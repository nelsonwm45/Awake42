from pynput.mouse import Controller
from time import sleep
import logging
import os

# Set up logging
logging.basicConfig(filename='awake.log', level=logging.INFO, format='%(asctime)s - %(message)s')

mouse = Controller()

logging.info("Awake script started.")

# Save the PID to a file
with open('awake.pid', 'w') as f:
    f.write(str(os.getpid()))

# Main loop
while True:
    sleep(60)         # Wait for 1 minute
    mouse.move(1, 0)  # Move the mouse slightly
    mouse.move(-1, 0)
    logging.info("Mouse moved.")
