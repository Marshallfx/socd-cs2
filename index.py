import keyboard
import time

a_pressed = False
d_pressed = False
a_released = False
d_released = False

def on_key_event(event):
    global a_pressed, d_pressed, a_released, d_released

    if event.name == 'a':
        if event.event_type == 'down':
            a_pressed = True
            a_released = False
        elif event.event_type == 'up':
            a_pressed = False
            a_released = True
    elif event.name == 'd':
        if event.event_type == 'down':
            d_pressed = True
            d_released = False
        elif event.event_type == 'up':
            d_pressed = False
            d_released = True

keyboard.hook(on_key_event)

print("marshall - start")

while True:
    if a_released and not d_pressed:
        time.sleep(0.01)
        keyboard.press_and_release('d')
        a_released = False

    if d_released and not a_pressed:
        time.sleep(0.01)
        keyboard.press_and_release('a')
        d_released = False

    time.sleep(0.01)  
