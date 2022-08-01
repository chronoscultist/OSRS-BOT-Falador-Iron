from login_function import login
import pyautogui as py
import time

time.sleep(3)
log = login()



# if it detects the osrs login screen image, it will initiate the re-logging process
if py.locateOnScreen("login_screen.png", confidence=0.85):
    print("Initiating login process")
    log.login_time()

time.sleep(2)

reset_mouse_pos = py.locateCenterOnScreen("reset_position_mouse.png", confidence=0.95)
#ini_time = time.time()

#def agi(i):
i=1
while True:

    print("ore "+str(i))
    full = py.locateCenterOnScreen("full.png", confidence=0.97)
    if full != None:
        bank = py.locateCenterOnScreen("bank.png", confidence=0.95)
        py.moveTo(bank)
        py.click(bank)
        time.sleep(7)

    deposite = py.locateCenterOnScreen("deposite.png", confidence=0.94)
    if deposite != None:
        py.moveTo(deposite)
        py.click(deposite)
        time.sleep(0.5)
        ore_start1 = py.locateCenterOnScreen("ore_start.png", confidence=0.96)
        py.moveTo(ore_start1)
        py.click(ore_start1)
        time.sleep(3)

    ore = py.locateCenterOnScreen("ore"+str(i)+".png", confidence=0.91)
    if ore !=None:
        py.moveTo(ore)
        py.click(ore)
        py.moveTo(reset_mouse_pos)
        py.moveTo(reset_mouse_pos)
        i=i+1
        if i==4:
            i=1
#fin_time = time.time()
#print(fin_time-ini_time)
#agi(1)
