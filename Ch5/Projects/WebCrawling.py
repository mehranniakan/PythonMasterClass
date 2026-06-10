import os
import time
from urllib.parse import urljoin

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://farsnews.ir/world/showcase"
news = []


def web_crawler_selenium():
    global news
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)

    container = driver.find_element(By.CSS_SELECTOR, ".flex.flex-col")
    items = container.find_elements(By.CSS_SELECTOR, ".pt-6")

    base_url = "https://farsnews.ir"

    for item in items:
        content = item.find_element(By.CSS_SELECTOR, ".grow.ms-10px.min-w-0.flex.flex-col")

        link = content.find_element(By.TAG_NAME, "a").get_attribute("href")
        title = content.find_element(By.TAG_NAME, "span").text

        link = urljoin(base_url, link)

        news.append({"title": title, "link": link})

    df = pd.DataFrame(news)
    file_name = 'news.csv'
    file_path = os.path.join(os.getcwd(), file_name)
    news = df.to_csv(file_path, index=False, encoding='utf-8')


def web_crawler_bs4():
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    container = soup.select_one(".flex.flex-col")

    items = container.select(".pt-6")

    base_url = "https://farsnews.ir"

    for item in items:
        content = item.select_one(".grow.ms-10px.min-w-0.flex.flex-col")

        a = content.select_one("a")
        span = content.select_one("span").get_text(strip=True)

        href = a.get("href")

        link = urljoin(base_url, href)

        news.append({
            "title": span,
            "link": link
        })

    df = pd.DataFrame(news)

    file_name = "news.csv"
    file_path = os.path.join(os.getcwd(), file_name)

    df.to_csv(file_path, index=False, encoding="utf-8")


web_crawler_selenium()
web_crawler_bs4()