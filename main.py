import requests
import time
import subprocess
import socket
import threading
import os

website = "https://www.bodin2.ac.th/test_24/data/files.json" #REPLACE THIS WITH API THAT GIVES DIFFRENT RESPOND WHEN THE EXAM RESULT IS OUT


kc = "import socket;socket.create_connection(('127.0.0.1',7000)).close()" #memory leak fix  #3
old = open("oldfile.txt", "r").read()
notify_halt = ["termux-notification", "--title", "IT HAS BEEN DONE", "--content", "The notification has stoped", "--priority", "max", "--sound"]
notify_score = ["termux-notification",  "--title", "TEST SCORE IS OUT", "--content", "TEST SCORE IS OUT", "--priority", "max", "--sound", "--action", f'python3 -c "{kc}"']
notify_start = ["termux-notification",  "--title", "the operation has started", "--content", "if you wish to stop click this notification", "--priority", "max", "--sound", "--action", f'python3 -c "{kc}"']


def listen_for_halt():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp 
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #android problem idk
    server.bind(("127.0.0.1", 7000))
    server.listen()

    con, adr = server.accept() #wait until someone connects
    #someone connected
    con.close()
    subprocess.run(notify_halt)
    os._exit(0) #stop the main process

def debug(status, time):
    return ["termux-notification", "--title", str(status), "--content", time, "--priority", "max", "--sound"]

# oporation starts here

threading.Thread(target=listen_for_halt, daemon=True).start()
subprocess.Popen(notify_start)


while True: # main loop
    try: # 104 connection reset by peer (7/20/26)
        answer = requests.get(website)
        if answer.status_code == 200:
            if old == answer.content.decode("utf-8"):
                print("OK: " + time.ctime())
            else:
                print(time.ctime() + " found it\n" + answer.content.decode("utf-8"))
                open("oldfile.txt", "w").write(answer.content.decode("utf-8"))
                d = 0
                while d <= 10:
                    d += 1
                    subprocess.Popen(notify_score)
                    subprocess.Popen(["termux-vibrate", "-d", "1000"])
                    time.sleep(5)
                break
        else:
            open("error_log.txt", "a").write(f"[{time.ctime()}] | {answer.status_code} | {answer.content.decode('utf-8')}\n\n")
            subprocess.Popen(debug(answer.status_code, time.ctime()))
            time.sleep(300)
    except Exception as e:
        open("error_log.txt", "a").write(f"[{time.ctime()}]: {e}\n\n")
        subprocess.Popen(debug(999, time.ctime()))
        time.sleep(300)

    time.sleep(60)
