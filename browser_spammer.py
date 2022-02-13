"""
-------------------------------------------------------
[Simple Browser Spammer]
-------------------------------------------------------
Author:  Luka Senfner
ID:      210729560
Email:   senfl5620@gmail.com
__updated__ = "2022-02-12"
-------------------------------------------------------
"""
# Imports
import webbrowser


def browser():
    URL = str(input("Paste the URL of the website you want to go to: "))
    num_times_open = int(
        input("How many times do you want the link to open in a new tab?: "))
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    for i in range(num_times_open):
        webbrowser.get(chrome_path).open(URL)


browser()
