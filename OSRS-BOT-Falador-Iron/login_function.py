import pyautogui as py
import time

class login:

    def login_time(self):
        password = "deadhead11"

        if py.locateOnScreen('dc_screen.png', confidence=0.90) !=None:
            ok_location = py.locateOnScreen("dc_ok.png", confidence=0.90)
            ok_location = py.moveTo(ok_location)
            py.click(ok_location)
            py.moveTo(py.locateCenterOnScreen("login_screen.png", confidence = 0.80))
            time.sleep(1)


        if py.locateOnScreen("existing_user.png", confidence=0.95) != None:
            py.press("enter")
            time.sleep(0.5)
            py.moveTo()
            py.typewrite(password, interval=0.1)
            py.press("enter")
            py.moveTo(py.locateCenterOnScreen("login_screen.png", confidence = 0.80))
            time.sleep(12)
        
        if py.locateCenterOnScreen("click_here.png", confidence = 0.60) !=None:

            py.moveTo(py.locateCenterOnScreen("click_here.png", confidence = 0.60))
            py.click()
            time.sleep(5)

        if py.locateOnScreen("error_wrong.png", confidence=0.95) !=None:
                exit

        if py.locateOnScreen("already_logged.png", confidence=0.9) !=None: 
                time.sleep(700)
                py.press("enter")
                time.sleep(10)
                


            














