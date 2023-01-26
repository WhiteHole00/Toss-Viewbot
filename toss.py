import requests
import asyncio
import threading
import os
from playwright.async_api import async_playwright
import re


async def isRunViewBot(target):

    os.system("cls")

    check = isCheckUser(target)

    cnt = 0
    if target in check:
        print(check)
        async with async_playwright() as go:
            browser = await go.firefox.launch(headless=True)
            page = await browser.new_page()
            while True:
                try:
                    await page.goto(f"https://toss.me/{target}")
                    await page.reload()
                    cnt += 1
                    print("[SUCCESS] : "+ str(cnt) + "명")
                except Exception as e:
                    print(e)
                    return input("Unknown Error!")
    else:           
        print("{}는 없는 계정 입니다.".format(target))


def isCheckUser(target):
    from bs4 import BeautifulSoup

    r = requests.get(f"https://toss.me/{target}")

    ch = BeautifulSoup(r.content,'html.parser')

    g = ch.find('span','text adaptive-grey800-text text--word-break typography-st5 text--font-weight-bold text--display-inline-block')
    view = ch.find('span','css-a774xx')
    try:
        name = g.string
        v = view.text
        result = f"Hi, {name}({v})"
        
        if name:
            return result 
    except Exception as e:
        return "없는유저"

    


def main():
    target = input("TOSS ID > ")

    if re.compile(r'[a-zA-Z]').match(target):
            threading.Thread(target=asyncio.run,args=(isRunViewBot(target),)).start()
    else:
        return input("토스 아이디는 영어로만 이루어져 있습니다.")
    
if __name__ == "__main__":
    main()
