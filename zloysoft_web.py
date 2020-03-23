from splinter import Browser
import keyboard
from bs4 import BeautifulSoup
from main import parse_solition
from re import findall
from main import baza_load

def init_driver():
    browser = Browser()
    browser.visit('https://192.168.115.98')

    return browser

def remove_character(string):
    reg = findall(r"[a-z_\[\]\=\ \;0-9$\*\^&=()><A-zА-я]+",string)
    new_str = "".join(reg)
    return new_str


def lookup(driver):
    soup = BeautifulSoup(driver.html)
    divs = soup.find_all('div', id="cell-text-task")
    text = divs[1].contents[7].contents[0]

    sols = parse_solition(text)
    all_sols = ""
    for sol in sols[0]:
        all_sols += (remove_character(sol.split('\r')[0]) + '\\\\')


    driver.execute_script(("alert(\'{}\')").format(all_sols))


def ebatel():
    browser = init_driver()
    baza_load("PHP")
    while(1 != 2):
        keyboard.wait('ctrl+alt+shift')
        try:
            lookup(browser)
        except:
            browser.execute_script(("alert(\'{}\')").format('Задача не найдена'))

if __name__ == "__main__":
    ebatel()


