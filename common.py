import requests
from config.config import *

def send_message(msg):
    return requests.get(f'{BASE}{TOKEN}{SEND_MSG_API}?chat_id={CHAN_ID}&text={msg}').json()

def send_message_formatted(msg):
    return requests.get(f'{BASE}{TOKEN}{SEND_MSG_API}?chat_id={CHAN_ID}&text={msg}&parse_mode=MarkdownV2').json()

def reply_message(id, msg):
    return requests.get(f'{BASE}{TOKEN}{SEND_MSG_API}?chat_id={CHAN_ID}&text={msg}&reply_to_message_id={id}&parse_mode=MarkdownV2').json()

def send_photo(img_url):
    return requests.get(f'{BASE}{TOKEN}{SEND_PHOTO_API}?chat_id={CHAN_ID}&photo={img_url}').json()

def escape(msg):
    for symbol in MD_ESCAPES:
        msg = msg.replace(symbol, "\\"+symbol)
    return msg