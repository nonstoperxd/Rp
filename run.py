from urllib import response
import mechanize
import os
import datetime
import sys
from time import sleep

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def sp(stri):
    for letter in stri:
        print(letter, end="")
        sys.stdout.flush()
        sleep(0.03)

def login(email, password, two_factor_code):
    browser.open(url)
    browser.select_form(nr = 0)
    browser.form['email'] = USERNAME
    browser.form['pass'] = PASSWORD
    r = browser.submit()
    f = open("login.html", "wb")
    f.write(r.read())
    f.close()
    browser.select_form(nr = 0)
    print("\033[1;33;40m", end = "")
    sp("\n Your 2-Factor Authentication Code :\n")
    print("\033[1;37;40m")
    apr = str(input())
    try:
        browser.form['approvals_code'] = apr
    except mechanize._form_controls.ControlNotFoundError:
        print("Wrong password or some shit, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    browser.select_form(nr = 0)
    try:
        browser.form['name_action_selected'] = ['save_device']
    except mechanize._form_controls.ControlNotFoundError:
        print("Some shit gone down, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    f = open("full_login_" + str(USERNAME) + ".html", "wb")
    f.write(r.read())
    f.close()

def findtextchat(curl):
    r = browser.open(curl)
    x = browser.title()
    if x == "Review recent login":
        print("\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.")
        exit(1)
    if x == "Login approval needed":
        print("\nYour account is stuck on verification\nPlease do it and then re run the program.")
        exit(1)
    if x == "Epsilon":
        print("\nYour account got locked, recover it kindly and re run the script.")
        exit(1)

def sendtextconvo(comment):
    try:
        browser.select_form(nr = 1)
    except mechanize._mechanize.FormNotFoundError:
        print("Some error occured while finding text area, please check your account")
        exit(1)
    try:
        browser.form['body'] = comment
    except mechanize._form_controls.ControlNotFoundError:
        print("Some error occured while filling text, please check your account")
        exit(1)
    r = browser.submit()
    e = datetime.datetime.now()
    print("\033[1;32;40m", end = "")
    print (e.strftime("%d/%m/%Y   %I:%M:%S %p"))
    print(">>", line, "\n")

def read_input_from_file(file_name):
    with open(file_name, 'r') as f:
        return f.read().strip()

os.system('clear')
sys.stdout.flush()

print("\033[1;33;40m", end="")
print('===========================================================')
print("[-[ The Bunny Mer'Chant Inbox & Convo Creation ]-]")
print('===========================================================')
print("\033[1;37;40m")

# Read input from separate text files
USERNAME = read_input_from_file('email.txt')
PASSWORD = read_input_from_file('password.txt')
TWO_FACTOR_CODE = read_input_from_file('two_factor_code.txt')
CONVERSATION_ID = read_input_from_file('conversation_id.txt')
NOTEPAD_LINK = read_input_from_file('notepad_link.txt')
TIMER = int(read_input_from_file('timer.txt'))

login(USERNAME, PASSWORD, TWO_FACTOR_CODE)
curl = 'https://m.facebook.com/messages/t/' + CONVERSATION_ID

clear()

print("\033[1;33;40m", end="")
print('===========================================================')
print("[-[ The Bunny Mer'Chant Inbox & Convo Creation ]-]")
print('===========================================================')
print("\033[1;37;40m")

count = 0
with open(NOTEPAD_LINK, 'r') as f:
    lines = f.readlines()

while True:
    for line in lines:
        if len(line) > 3:
            if count != 0:
                sleep(TIMER)
            findtextchat(curl)
            sendtextconvo(line)
            count += 1
            if count % 10 == 0:
                sleep(1)
                clear()
                print("\033[0;37;41m\n")

