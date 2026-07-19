# exam-result-notifier
an exam result notifier (bodin2 school) that works everywhere

## **Features:**
- **notify you when the exam result came out**
  - constant vibrating
  - spam notification
  - *(all of those can be stop by tabbing on the notification)*
- **everything runs on your phone 24/7** *(android only)*


## **Requirements:**
- termux api —https://github.com/termux/termux-api/releases
  - open termux api app and then do all of the step it tells you
- termux — https://termux.dev/
  - open termux download all of the packages :
  - ```bash
    pkg update -y && pkg upgrade -y && pkg install -y python netcat-openbsd termux-api
    ```
  - python library: **none!** your welcome
  - wake lock: enter this command in the terminal — `termux-wake-lock`
 

## **RUN:**
```bash
python3 main.py
```

## **Notes:**
- this only work once if you wish to get notify again, run the program again
- this project is made during exam so i've got a couple hour to do so sorry if this is janky
- licensing under MIT
