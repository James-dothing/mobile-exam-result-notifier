import requests
import time
import subprocess
import random
import socket
import threading
import os

old = open("oldfile.txt", "r").read()
notify_score = ["termux-notification",  "--title", "TEST SCORE IS OUT", "--content", "TEST SCORE IS OUT", "--priority", "max", "--sound", "--action", "nc 127.0.0.1 7000"]
notify_halt = ["termux-notification", "--title", "IT HAS BEEN DONE", "--content", "IT HAS BEEN DONE", "--priority", "max", "--sound"]
def listen_for_halt():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp 
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #android problem idk
    server.bind(("127.0.0.1", 7000))
    server.listen()

    con, adr = server.accept() #wait until someone connects
    con.close() #someone connected
    subprocess.run(notify_halt)
    os._exit(0) #stop the main process

def rand():
    return random.randint(45,90) #shhh shhh don't ask
def debug(status, time):
    return ["termux-notification", "--title", str(status), "--content", time, "--priority", "max", "--sound"]

while True:
    website = "https://www.bodin2.ac.th/test_24/data/files.json"
    answer = requests.get(website)
    if answer.status_code == 200:
        if old == answer.content.decode("utf-8"):
            print("OK: " + time.ctime())
        else:
            print(time.ctime() + " found it\n" + answer.content.decode("utf-8"))
            open("oldfile.txt", "w").write(answer.content.decode("utf-8"))
            threading.Thread(target=listen_for_halt, daemon=True).start()
            d = 0
            while d <= 50:
                d += 1
                subprocess.Popen(notify_score)
                subprocess.Popen(["termux-vibrate", "-d", "1000"])
                time.sleep(5)
    else:
        open("error_log.txt", "a").write(f"[{time.ctime()}] | {answer.status_code} | {answer.content.decode('utf-8')}\n")
        subprocess.Popen(debug(answer.status_code, time.ctime()))
    time.sleep(min(rand(), rand(), rand())) #low bias shenanigan
