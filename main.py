from logging import exception
from time import sleep
import requests
from bs4 import BeautifulSoup
from config.config import *
from common import *

class metal_injection_crawler:
    def __init__(self, bar):
        self.bar = bar

    def get_links(self):
        r = requests.get("https://metalinjection.net/category/reviews")
        if r.status_code != 200:
            raise exception(f"Error: get link failed, link: reviews page, code: {r.status_code}")
        soup = BeautifulSoup(r.content, 'html.parser')
        links = list(
            filter(lambda l: l.startswith("https://metalinjection.net/reviews/"),
                map(lambda l: l.get('href'), 
                    soup.find_all('a', {"rel": "bookmark"}))))
        verified = set()
        unique_list = list()
        for link in links:
            if link not in verified:
                unique_list.append(link)
                verified.add(link)
        return unique_list
    
    def crawl(self):
        links = self.get_links()
        for link in links:
            r = requests.get(link)
            if r.status_code != 200:
                raise exception(f"Error: get link failed, link: {link}, code: {r.status_code}")
            soup = BeautifulSoup(r.content, 'html.parser')
            score = float(soup.find('span', {"class": "rwp-overlall-score-value"}).getText())
            post_time = soup.find('time', {"class": "post-date"}).getText()
            if "hour" not in post_time:
                break
            if score < 9.0:
                continue
            msg_title = escape("Best Albums - Metal Injection")
            title = escape(soup.find('h1').getText())
            paragraph = escape(soup.find('div', {"class": "zox-post-body"}).getText()[:200].strip()+"...")
            full_msg = f"{msg_title}\n[{title}]({link})\n\n{paragraph}"
            res = send_message_formatted(full_msg)
            if not res['ok']:
                raise exception(f"Error: send message failed, {res}")
            sleep(10)

def main():
    metal_injection_crawler(9).crawl()

if __name__ == '__main__':
    main()