#!/usr/bin/env python3
# coding=utf-8
# shadowsocks start | stop script
#

import os
import json
import sys
import time
from subprocess import Popen, PIPE

SSHome = '/usr/local/shadowsocks'
LogFile = os.path.join(SSHome, 'logs/access.log')
PidFile = os.path.join(SSHome, 'logs/shadowsocks.pid')
Prog = os.path.join(SSHome, 'sslocal.py')
ConfigDir = os.path.join(SSHome, 'config')
ConfigFile = os.path.join(SSHome, 'config.json')


def start():
    print('Starting Shadowsocks ...\t\t', end="")
    child = Popen('/usr/local/bin/python3 {0} -c {3} -d start --pid-file={1} --log-file={2}'.format(
                  Prog, PidFile, LogFile, ConfigFile), stderr=PIPE, shell=True, stdout=PIPE)
    data = child.communicate()[1].decode()
    if child.poll() != 0:
        print('[ \033[31mFailed\033[0m ]')
        print(data)
    else:
        print('[ \033[32mOK\033[0m ]')


def stop():
    print('Stopping Shadowsocks ...\t\t', end="")
    child = Popen('/usr/local/bin/python3 {0} -d stop --pid-file={1}'.format(Prog, PidFile),
                  stderr=PIPE, stdout=PIPE, shell=True)
    data = child.communicate()[1].decode()
    if child.poll() != 0:
        print('[ \033[31mFailed\033[0m ]')
        print(data)
    else:
        print('[ \033[32moK\033[0m ]')


def restart():
    stop()
    time.sleep(1)
    start()

def list_link():
    links = {} 
    current_conf = os.readlink(ConfigFile)
    dirpath, dirname, filenames = next(os.walk(ConfigDir))
    for index, filename in enumerate(filenames):
        filepath = os.path.join(dirpath, filename)
        is_current = False

        with open(filepath, 'r') as f:
            if current_conf == filepath:
                is_current = True

            config = json.load(f)
            links[filepath] = (index, config['server'], config['server_port'], is_current)
    return links 


def change(links, num):
    for filepath, server in links.items():
        if num == server[0]:
            os.popen('/bin/ln -sf {0} {1}'.format(filepath, ConfigFile))
            break

def usage():
    print('Usage: ./shadowsocks.py  {start | stop | restart | list | change [num]}')
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        start()
        sys.exit(0)
   
    if sys.argv[1] == 'start':
        start()
    elif sys.argv[1] == 'stop':
        stop()
    elif sys.argv[1] == 'restart':
        restart()
    elif sys.argv[1] == 'list':
        links = list_link()
        print('%-15s %-15s %-6s %s' % ('链路号', '链路', '链路端口', '当前链路'))
        for i in sorted(links.values(), key=lambda x: x[0]):
            if i[3]:
                print('  \033[35m%-10s %-24s %-12s %s\033[0m' % (i[0], i[1], i[2], '*'))
            else:
                print('  %-10s %-24s %-12s' % (i[0], i[1], i[2]))
    elif sys.argv[1] == 'change':
        try:
            num = int(sys.argv[2])
        except Exception:
            num = 0
        links = list_link()
        change(links, num)
        restart()
    else:
        usage()
    
