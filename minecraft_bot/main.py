import pyautogui as pt
from time import sleep


# x = attack
def mine_block(seconds):
    pt.keyDown('m')
    sleep(seconds)
    pt.keyUp('m')


pickaxes = 9

sleep(3)

for i in range(1, pickaxes + 1):
    pt.press(str(i))
    mine_block(190)
    print(f'pickaxe #{i} has been used. ')
