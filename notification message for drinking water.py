#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mukesh
#
# Created:     06/09/2023
# Copyright:   (c) mukes 2023
# Licence:     <your licence>
#---------------------------------------------------------------------------
from win10toast import ToastNotifier
import time

def send_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)  # Toast will disappear after 10 seconds

def main():
    while True:
        # You can customize the title and message as per your needs
        send_notification("Hello!", "It's time for your drinking water.")

        # Sleep for an hour (3600 seconds)
        time.sleep(3600)

if __name__ == "__main__":
    main()
