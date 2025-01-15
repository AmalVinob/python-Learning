'''
9-5pm
water - water.mp3 - (3.5l)  - drank - logout of file 9 -5 = 15m -110 ml
eyes - eyes.mp3 - exercice bw 30 mini - done
phycical activity - phsical.mp3 - every 45 minitues - exdone

rule
mp3 - pygame to play audio
from pygame import mixer

mixer.init()
mixer.music.load()
mixer.music.set_volume(0.9)
mixer.music.play()
mixer.music.stop()
time.sleep(2)
'''


from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def my_logs(msg):
    with open("logs.txt","a") as f:
        f.write(f"{msg} {datetime.now()} \n")

if __name__ == '__main__':
    # musiconloop("Queen.mp3", "stop")
    inti_water = time()
    inti_eye = time()
    inti_exercise = time()
    water_sec = 40*60
    eye_sec = 30*60
    exe_sec =15*60

    while True:
        if time() - inti_water > water_sec:
            print("water drinker time . \n enter 'drank' to stop the alarm :")
            musiconloop("Queen.mp3","drank")
            inti_water = time()
            my_logs("drank water at")

        if time() - inti_eye > eye_sec:
            print("eye exercise. \n enter 'done' to stop the alarm :")
            musiconloop("Queen.mp3","done")
            inti_eye = time()
            my_logs("eye exercise done at")


        if time() - inti_exercise > exe_sec:
            print("work out done  . \n enter 'yeah done' to stop the alarm :")
            musiconloop("Queen.mp3","yeah done")
            inti_exercise = time()
            my_logs("workout water at")

