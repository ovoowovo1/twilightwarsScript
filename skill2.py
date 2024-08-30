from pynput.keyboard import Key, Controller, Listener
import time
import random
import json

keyboard = Controller()

# Load configuration
with open('./Config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

# Extract configuration
combos = {combo['trigger_key']: combo for combo in config['combos']}
min_delay = config['delay']['min']
max_delay = config['delay']['max']

# Record currently pressed keys
currently_pressed_keys = set()

def process_key_sequence(key, combo):
    print(f"{key} pressed! Executing {combo['name']}...")
    for k in combo['sequence']:
        keyboard.press(k)
        time.sleep(random.uniform(min_delay, max_delay))  # Random delay
        keyboard.release(k)

def on_press(key):
    try:
        # When a specified key is pressed
        if key.char in combos:
            if key.char not in currently_pressed_keys:
                currently_pressed_keys.add(key.char)
                process_key_sequence(key.char, combos[key.char])
        else:
            # Other key operations
            pass
    except AttributeError:
        pass

def on_release(key):
    try:
        if key.char in combos:
            currently_pressed_keys.discard(key.char)  # Reset key when released
    except AttributeError:
        pass

# Start listening to the keyboard
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()