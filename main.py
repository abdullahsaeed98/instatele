# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import json
import random
import os.path
import urllib.request
from telegram import (Bot, Update, ChatAction, TelegramError, User, InlineKeyboardMarkup,
                      InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent,
                      ShippingOption, LabeledPrice, ChatPermissions, Poll, BotCommand,
                      InlineQueryResultDocument)
from telegram.error import BadRequest, InvalidToken, NetworkError, RetryAfter
from telegram.utils.helpers import from_timestamp, escape_markdown
# from telebot import apihelper
import configparser
import time


def get_avatar_user():
    while True:
        u=users.split(",")
        for i in u:
            username=i
            # users=
            inst_url = "https://www.instagram.com/"
            # username="abdullah.saeed98"
            print("Targeting user :",i)
            fill=inst_url+i
            url=fill+"/?__a=1"
            # print(url)

            # response = requests.get(f"{inst_url}/{inst_username}/")
            response=requests.get(url)
        # while True:
            if response.ok:
                html = response.text
                bs_html = bs(html, 'html.parser')
                bs_html = bs_html.text
                # index = bs_html.find('display_url') + 21
                index = bs_html.find('display_url')
                try:
                    cap=bs_html.find('edge_media_to_caption')
                except:
                    pass
                print(cap)
                # exit(1)
                remaining_text = bs_html[index:]
                cap_remaining_text = bs_html[cap:]
                # print(cap_remaining_text)
                
                # exit(1)
                remaining_text_index = cap_remaining_text.find('requested_by_viewer') - 3
                # print("Rrr",remaining_text)
                # print("Rrr",remaining_text_index)
                cap_remaining_text_index = remaining_text.find('requested_by_viewer') - 3
                # print("ccc",cap_remaining_text)
                # print("ccc",cap_remaining_text_index)
                # print("ccc",cap_remaining_text)
                # exit(1)
                string_url = remaining_text[:remaining_text_index]
                cap_string_url =cap_remaining_text
                # print("aaa",string_url)

                # a=string_url.split(",")
                
                #caption
                y=cap_string_url.split(",")
                # q="https"+z[2]
                # print("q",y[0])
                k=y[0].split(":")
                m=k[-1]
                fcap=m[:-4]
                # print(fcap)
                # exit(1)
                #link
                a=string_url.split(",")
                # print("a",)
                b=a[0].split(":")
                # print("b",b)
                c="https"+b[2]
                # print("C",c)
                v=c.replace('"'," ")
                link=v[:5] + ':' + v[5:]
                # print("link,",link)
                # exit(1)
                vv=[]
                path = os.path.dirname(os.path.abspath(__file__))+'\\'+'cc.txt'
                with open(path,"r") as myfile:
                        aaa=myfile.readlines()
                        for i in aaa:
                            vv.append(i[:-1])
                        # print("read",vv)
                if link in vv:
                    print("already sent")
                    time.sleep(5)
                    # username=i
                    # print("u",username)
                    continue                
                # id=telegram_id_chanel
                id="806357535"
                # username=i
                # print("u",username)
                sendposttotelegram(id,link,fcap,username) 
                
            # urllib.request.urlretrieve(d, "local-filename.jpg")
            # exit(1)
        
        
def sendposttotelegram(id,link,fcap,username):
        
    # apihelper.proxy = proxy
        # bot = telebot.TeleBot(telegram_token)
        # path="./service_images"
        # test = os.listdir(path)
        # with open("cc.txt", 'r') as myfile:
        #     fstr = myfile.read()
        #     print(fstr)
        #     exit(1)
        # path = os.path.dirname(os.path.abspath(__file__))+'\\'+'help.jpeg'
        u=username
        # print("s",u)
        bot.send_message(chat_id=id, text="New Post By "+u)
        dd=bot.send_photo(chat_id=id, photo=link,caption=fcap)
        if dd:
            print("image sent")
            # bot.send_message(chat_id=id, text="I'm sorry Dave I'm afraid I can't do that.")
            path = os.path.dirname(os.path.abspath(__file__))+'\\'+'cc.txt'
            with open(path,"a") as myfile:
                myfile.write(link+"\n")
    # print('Posted image: '+imgname)

    # while True:
    #     filename = 'av_' + inst_username + '.jpg'
    #     file_exists = os.path.isfile(filename)

    #     if not file_exists:
    #         with open(filename, 'wb+') as handle:
    #             response = requests.get(string_url, stream=True)
    #             if not response.ok:
    #                 print(response)
    #             for block in response.iter_content(1024):
    #                 if not block:
    #                     break
    #                 handle.write(block)
    #     else:
    #         print("file already exist\ndone")
    #         break


# def get_post_from_url(inst_post_url):
    # response = requests.get(f"{inst_post_url}")

    # if response.ok:
    #     html = response.text
    #     bs_html = bs(html, 'html.parser')
    #     bs_html = bs_html.text
    #     index = bs_html.find('KL4Bh')
    #     remaining_text = bs_html[index:]
    #     remaining_text_index = remaining_text.find('s1080x1080') - 3
    #     string_url = remaining_text[:remaining_text_index]

    #     print(string_url, "\ndone")
    # while True:
    #     filename = 'post_1.jpg'
    #     file_exists = os.path.isfile(filename)

    #     if not file_exists:
    #         with open(filename, 'wb+') as handle:
    #             response = requests.get(string_url, stream=True)
    #             if not response.ok:
    #                 print(response)
    #             for block in response.iter_content(1024):
    #                 if not block:
    #                     break
    #                 handle.write(block)
    #     else:
    #         print("file already exist\ndone")
    #         break
def crudConfig(path):
    config = configparser.ConfigParser()
    config.read(path)

    url = config.get("SETTINGS", "url")
    print('Parse url: '+url)

    # global proxy
    global dropbox_token
    global telegram_token
    global telegram_id_chanel
    global users
    
    # proxy = {}
    # proxy['https'] = config.get("SETTINGS", "httpsproxy")
    # print(proxy)

    dropbox_token = config.get("SETTINGS", "dropbox_token")
    telegram_token = config.get("SETTINGS", "telegram_token")
    telegram_id_chanel = config.get("SETTINGS", "telegram_id_chanel")
    users=config.get("SETTINGS", "users")
    # print(users.split(","))
    folder_name = config.get("SETTINGS", "folder_name")

    if os.path.exists(folder_name):
        print('Folder to save: '+folder_name)
    else:
        print('Сreate folder')
        os.mkdir(str(folder_name))
    os.chdir(str(folder_name))

    # main(url)

path = os.path.dirname(os.path.abspath(__file__))+'\\'+'config.ini'
print('Config file: '+path)
crudConfig(path)



bot =Bot(telegram_token)
print(bot.get_me())
# exit(1)
# username = input('enter username: ')
get_avatar_user()
# get_post_from_url("https://www.instagram.com/p/B5PhreSgx-P/")
