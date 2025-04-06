import pyautogui
import random
import time
import threading
import keyboard

quotes = [
    "Back of the net!",
    "Aha!",
    "Dan! Dan! Dan! Dan! Dan!",
    "Smell my cheese, you mother!",
    "I’m not driving a Mini Metro.",
    "Kiss my face!",
    "That was textbook.",
    "Lovely stuff.",
    "I’m Alan Partridge and I drive a Lexus.",
    "Jurassic Park!",
    "Monkey tennis?",
    "This country is going to the dogs.",
    "I’m not a small man, but I know what I like.",
    "Cashback!",
    "No Lynn - these are sex people!",
    "I'm not a fan of the new Top Gear.",
    "Don't get Bond wrong!",
    "Stop getting Bond wrong!",
    "Do you want me to lap-dance for you?",
    "That’s liquid football!"
]

running = False

def toggle_script():
    global running
    running = not running
    print(f"Auto-Alan {'enabled' if running else 'paused'} (F8 to toggle)")

keyboard.add_hotkey("F8", toggle_script)

def chat_loop():
    global running
    print("Press F8 to start/stop, Ctrl+C to exit.")
    try:
        while True:
            if running:
                delay = random.randint(20, 180)
                print(f"Waiting {delay} seconds...")
                time.sleep(delay)
                message = random.choice(quotes)
                pyautogui.write(message, interval=0.05)
                pyautogui.press('enter')

                print(f"Sent: {message}")
            else:
                time.sleep(0.1)  # Don't hammer CPU while paused
    except KeyboardInterrupt:
        print("\nScript stopped by user.")

chat_loop()
