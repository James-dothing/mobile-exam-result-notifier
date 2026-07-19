# exam-result-notifier
an exam result notifier (bodin2 school)

## **Features:**
- notify you when the exam result came out
  - constant vibrating
  - spam notification
  - all of those can be stop by tabbing on the notification
- everything runs on your phone (android only)


## **Requirements:**
- termux api —https://github.com/termux/termux-api/releases
  - open termux api app and then do all of the step it tells you
- termux — https://termux.dev/
  - inside termux download all of the packages :
  - ```bash
    pkg update -y && pkg upgrade -y && pkg install -y python netcat-openbsd termux-api
    ```
  - python library: **none!** your welcome
  - wake lock: enter this command in the terminal — `termux-wake-lock`
