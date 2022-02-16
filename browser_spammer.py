"""
-------------------------------------------------------
[Simple Browser Spammer]
-------------------------------------------------------
Author:  Luka Senfner
ID:      210729560
Email:   senfl5620@gmail.com
__updated__ = "2022-02-15"
-------------------------------------------------------
"""
# Imports
import webbrowser
from time import sleep
from platform import system


def getos():
    os_type = system()
    browser(os_type)


def browser(os_type):
    if os_type == 'Windows':
        os_default = 'windows-default'
    elif os_type == 'Darwin':
        os_default = 'macosx'
    URL = str(input("Paste the URL of the website you want to go to: "))
    num_times_open = int(
        input("How many times do you want the link to open in a new tab?: "))

    if num_times_open > 0:
        webbrowser.get(os_default).open_new(URL)
    else:
        print("You broke me!  Try again")
    if num_times_open > 1:
        for i in range(num_times_open - 1):
            webbrowser.get(os_default).open_new_tab(URL)
            sleep(.15)


getos()
