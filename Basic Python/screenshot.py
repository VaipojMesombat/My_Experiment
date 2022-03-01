'''
# Capture Screenshot

captures screenshot at regular interval of time.

## Dependencies

```bash
pip install -r requirements.txt
```

## Usage

```bash
python screenshot.py                          # takes screenshot at interval of 1 hour
python screenshot.py -t m -f 5                # takes 5 screenshots in 1 minute 
python screenshot.py -p path_to_directory     # screenshots will be saved to path_to_directory
```
'''
import os
import argparse
import pyautogui
import time

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", help="absolute path to store screenshot.", default=r"./images")
parser.add_argument("-t", "--type", help="h (in hour) or m (in minutes) or s (in seconds)", default='h')
parser.add_argument("-f", "--frequency", help="frequency for taking screenshot per h/m/s.", default=1, type=int)

args = parser.parse_args()


sec = 0.

if args.type == 'h':
    sec = 60 * 60 / args.frequency
elif args.type == 'm':
    sec = 60 / args.frequency

if sec < 1.:
    sec = 1.
    

if os.path.isdir(args.path) != True:
    os.mkdir(args.path)


try:
    while True:
        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)
        file = current_time + ".jpg"
        image = pyautogui.screenshot(os.path.join(args.path,file))
        print(f"{file} saved successfully.\n")
        time.sleep(sec)
        
except KeyboardInterrupt:
    print("End of script by user interrupt")

    





