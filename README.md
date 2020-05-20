## Introduction
Have you ever regret that you have forgotten to punch out in Dingding before you leaved your office and you were beyond the valid geographical fence so that you had to go back to the office just to click the punch button in Dingding? So here comes the remedy. This project uses python script to control your extra phone to automatically punch in and out just in your office.

## How does it work
This project simply uses uiautomator and adb to control your Android phone through USB connection. It routinely wake the phone up and start Dingding app. When it is around the punch time and you have set quick punch in your attendence module in Dingding. Dingding will help you punch in or out.

## What you need
You have to own an extra Android phone in your office to punch in or out.

## Step by step
#### 1 install adb and python

#### 2 install uiautomator on your computer
```
pip install --pre -U uiautomator2
```

#### 3 install uiautomator app on your Android phone
```
python -m uiautomator2 init
```

#### 4 run python script
```
python main.py
```