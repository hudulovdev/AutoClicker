import pyautogui

x=input("Enter X cordinate: ")
y=input("Enter Y cordinate: ")
choose=input("Select (L)eft or (R)ight")
i=input("How many do you want repeat click? :")
a=0

if choose=="L":
    choose="left"
else:
    choose="right"

pyautogui.moveTo(x, y, duration=0.1)

while a<i+1:
    pyautogui.click(button=choose)