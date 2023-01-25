import requests
import asyncio
import threading
import os
from playwright.async_api import async_playwright


async def isRunViewBot(target):

    os.system("cls")

    check = isCheckUser(target)


    if target in check:
        print(check)
        async with async_playwright() as go:
            browser = await go.firefox.launch(headless=False)
            while True:
                try:
                    page = await browser.new_page()
                    await page.goto(f"https://toss.me/{target}")
                    await page.reload()
                except Exception as e:
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
    threading.Thread(target=asyncio.run,args=(isRunViewBot(target),)).start()
    
if __name__ == "__main__":
    main()