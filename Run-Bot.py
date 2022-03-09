from selenium import webdriver
import time
from os import name, system
import sys
from selenium import webdriver
import time
from colorama import init
import os, colorama
from colorama import Fore,Style,Back
colorama.init()

os.system("mode con: cols=120 lines=30")
def clear():
  
    # Para Windows
    if name == 'nt':
        _ = system('cls')
  
    # Para lo que no sea Windows(here, os.name es 'posix')
    else:
        _ = system('clear')
print(Fore.LIGHTBLACK_EX + """
                              ██▓ ███▄    █   ██████     ▄▄▄▄    ▒█████  ▄▄▄█████▓ 
                              ▓██▒ ██ ▀█   █ ▒██    ▒    ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
                              ▒██▒▓██  ▀█ ██▒░ ▓██▄      ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
                              ░██░▓██▒  ▐▌██▒  ▒   ██▒   ▒██░█▀  ▒██   ██░░ ▓██▓ ░  Ver 3.0
                              ░██░▒██░   ▓██░▒██████▒▒   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
                              ░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░  
                               ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░   ▒░▒   ░   ░ ▒ ▒░     ░    
                               ▒ ░   ░   ░ ░ ░  ░  ░      ░    ░ ░ ░ ░ ▒    ░    Bugs Fixeds! 
                                ░           ░       ░      ░          ░ ░           
                                 ░                              
""")
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
print_slow(Fore.LIGHTBLACK_EX + """[!] Script creado por SadicX - """)
print(Fore.RED + "[Github >] Github.com/SadicX")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
print_slow(Fore.LIGHTBLACK_EX + "[>] Este script esta protegido por:") 
print(Fore.RED + """ S4K T34M""")
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.060)
print_slow(Fore.LIGHTBLACK_EX + """[>] Lo que significa que esta totalmente prohibido modificar este archivo y subirlo a cualquier red social.""")
time.sleep(2)
os.system("cls")

print(Fore.LIGHTBLACK_EX + """
                              ██▓ ███▄    █   ██████     ▄▄▄▄    ▒█████  ▄▄▄█████▓ 
                              ▓██▒ ██ ▀█   █ ▒██    ▒    ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
                              ▒██▒▓██  ▀█ ██▒░ ▓██▄      ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
                              ░██░▓██▒  ▐▌██▒  ▒   ██▒   ▒██░█▀  ▒██   ██░░ ▓██▓ ░  Ver 3.0
                              ░██░▒██░   ▓██░▒██████▒▒   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
                              ░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░  
                               ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░   ▒░▒   ░   ░ ▒ ▒░     ░    
                               ▒ ░   ░   ░ ░ ░  ░  ░      ░    ░ ░ ░ ░ ▒    ░    Bugs Fixeds! 
                                ░           ░       ░      ░          ░ ░           
                                 ░                              
""")
                              
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
print_slow(Fore.LIGHTBLACK_EX + """[!] Abriendo servidor web en:
""")
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
print_slow(Fore.LIGHTBLACK_EX + """4
""")
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
print_slow(Fore.LIGHTBLACK_EX + """3
""")
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
print_slow(Fore.LIGHTBLACK_EX + """2
""")
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
print_slow(Fore.LIGHTBLACK_EX + """1
""")
print(Fore.LIGHTBLACK_EX + """.:--------------------------------- LOGS: -------------------------------------:.""")
time.sleep(1)

web = webdriver.Chrome()
web.get('http://instagram.com')
time.sleep(5)


def login():
    user = "dedillo.100"
    paswd = "faykan27099"
    acceptCookies = web.find_element_by_xpath("/html/body/div[4]/div/div/button[1]").click()
    time.sleep(5)
    inputUser = web.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    inputUser.send_keys(user)
    inputPass = web.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    inputPass.send_keys(paswd)
    loginButton = web.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()


def open_followers(account_instagram):
    web.get("https://www.instagram.com/" + account_instagram + "/followers/")
    time.sleep(5)
    web.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()


def scroll_followers(minutes):
    pop_up_window = web.find_element_by_xpath("/html/body/div[6]/div/div/div[2]")
    # HACE SCROLL HASTA LAS NUEVAS CUENTAS
    timeout = time.time() + 60 * minutes
    while True:
        if time.time() > timeout:
            break
        web.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
            pop_up_window)
        time.sleep(1)


def follow_followers():
    list_followers = web.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/ul")
    for child in list_followers.find_elements_by_css_selector("li"):
        user_name = child.find_element_by_css_selector(".notranslate").text
        follow_button = child.find_element_by_css_selector("button")
        print(user_name)
        print("> ------------------------------------- <")
        print(follow_button.text)
        if "Seguir" == follow_button.text:
            follow_button.click()
            print(user_name + "seguido")
        else:
            print("Ya lo sigues")
        time.sleep(1)


sources = ["galisteo_yt"]
login()
time.sleep(5)
for account in sources:
    open_followers(account)
    time.sleep(5)
    scroll_followers(2)
    follow_followers()