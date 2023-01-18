from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests


def find_gifs():
    figs = browser.find_elements(By.CLASS_NAME, "GifListItem")
    gifs = {}
    for fig in figs:
        try:
            idx = fig.get_attribute("data-index")
            gif = fig.find_element(By.TAG_NAME, "img")
            url = gif.get_attribute("src")
            gifs[idx] = url
        except:
            pass
    return gifs


def save_gif(idx, url):
    if not os.path.isdir("tenor"):
        os.mkdir("tenor")

    with open(f"./tenor/{idx}.gif", "wb") as file:
        res = requests.get(url, stream=True)
        for block in res.iter_content(1024):
            if not block:
                break
            file.write(block)


def diff_gifs(prev, curr):
    to_save = {idx: curr[idx] for idx in curr if not prev.get(idx)}
    return to_save


if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser.get("https://tenor.com")

    while True:
        prev = {}
        curr = find_gifs()
        saved = []

        if prev != curr:
            prev = curr

            for idx, url in prev.items():
                if not idx in saved:
                    save_gif(idx, url)
                    saved.append(idx)

        browser.execute_script("window.scrollBy(0, 150)")