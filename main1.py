import random
import sys
import time
from playsound import playsound
import cv2
from PIL import Image



def User_move():
    usermove1=input("Pls enter your move: STONE(s)  PAPER(p)  SCISSORS(c)\nElse Press Q to quit\n")
    usermove=usermove1.lower()
    if usermove=="q":
        print("Thankyou for playing. Have a great Day!")
        exit()
    if (usermove=="s"):
        print(f"Your Move = STONE")
    if (usermove=="p"):
        print(f"Your Move = PAPER")
    if (usermove=="c"):
        print(f"Your Move = SCISSORS")
    return usermove

def Computers_move():
    a=["s", "p", "c"]
    b=["STONE", "PAPER", "SCISSORS"]
    d=random.randint(0,2)
    computersmove=a[d]
    print(f"COMPUTER'S MOVE: {b[d]}")
    return computersmove

def playvideo(video, val):

    vid = cv2.VideoCapture(video)

    while (vid.isOpened()):

        ret, frame = vid.read()
        if ret==True:

            cv2.imshow('frame',frame)

            if cv2.waitKey(val) & 0xFF == ord('q'):
                break
        else:
            break

    vid.release()
    cv2.destroyAllWindows()
    time.sleep(3)
    return "DONE"

def tie():
    img = cv2.imread("TIE.jpg")
 
    while True:
        cv2.imshow("ITS A TIE", img)
        if cv2.waitKey(2000):
              break
        # sys.exit() # to exit from all the processes
    cv2.destroyAllWindows()


def Check_condition(usermove, computersmove):

    if usermove!="s" and usermove!="p" and usermove!="c":
        print("Invalid character entered, You can only enter s or p or c ")
        usermove=input("Pls enter your move: STONE(s)  PAPER(p)  SCISSORS(c) \n")
    if usermove==computersmove:
            print("\n=====DRAW=====\n")
            tie()
            time.sleep(4)
            exit()
    elif usermove=="s" and computersmove=="c":
            playvideo("Rock and Scissors.mp4", 30)
            return 1
    elif usermove=="p" and computersmove=="s":
            playvideo("Rock and Paper.mp4", 30)
            return 1
    elif usermove=="c" and computersmove=="p":
            playvideo("Scissor and Paper.mp4", 30)
            return 1
    elif computersmove=="s" and usermove=="c":
            playvideo("Rock and Scissors.mp4", 30)
            return 0
    elif computersmove=="p" and usermove=="s":
            playvideo("Rock and Paper.mp4", 30)
            return 0
    elif computersmove=="c" and usermove=="p":
            playvideo("Scissor and Paper.mp4", 30)
            return 0


while(True):   

    if (Check_condition(User_move(),Computers_move()))==0:
            print("\n======DEFEAT!======\n")
            playsound("C:\\Users\\adity\\Downloads\\DEFEAT.mp3")
            

    else:
            print("\n=====YOU WIN!=====\n")
            playsound("C:\\Users\\adity\\Downloads\\WIN.mp3")
            

