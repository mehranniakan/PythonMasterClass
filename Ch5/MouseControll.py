from pynput import mouse
from pynput.mouse import Button, Controller
import time

# def on_move(x, y):
#     print(f'Pointer moved to ({x}, {y})')
#
#
# def on_click(x, y, button, pressed):
#     print(f'{"Pressed" if pressed else "Released"} at ({x}, {y}) with {button}')
#
#     # وقتی دکمه رها شود، لیسنر متوقف می‌شود
#     if not pressed:
#         return False
#
#
# def on_scroll(x, y, dx, dy):
#     direction = "down" if dy < 0 else "up"
#     print(f'Scrolled {direction} at ({x}, {y})')
#
#
#
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()
#
# listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# listener.start()

#####################################################

mouse = Controller()

mouse.position = (1920, -1)
time.sleep(0.3)
mouse.click(Button.left, 1)

mouse.position = (900, 455)
time.sleep(0.3)
mouse.click(Button.left, 1)