# coding=utf-8
#

import re, os
import logging


class WhiteList:
    def __init__(self, config):
        sourcefile = os.path.abspath(config.get('whitelist', 'whitelist.txt'))
        self.pat = re.compile(r'[a-z]+', re.I)
        self.whitelist = self.gen_whitelist(sourcefile)

    def gen_whitelist(self, sourcefile):
        whitelist = {
            'domain': {},
            'shortkey': {},
            'longkey': {}
        }
        try:
            with open(sourcefile, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('#'): continue

                    # generate domain whitelist
                    if self.pat.search(line):
                        whitelist['domain']['.'.join(line.split('.')[-2:])] = 1
                        continue

                    # generate ip net whitelist
                    tempkey = [key for key in line.split('.') if key != '*']
                    key = '.'.join(tempkey)
                    if len(tempkey) <= 2:
                        whitelist['shortkey'][key] = 1
                    else:
                        whitelist['longkey'][key] = 1

        except Exception as e:
            logging.error('generate whitelist failed: {0}'.format(e))
        return whitelist


if __name__ == '__main__':
    import json
    config = os.path.abspath('../config.json')
    with open(config, 'r') as f:
        config = json.load(f)
    wt = WhiteList(config)
    # print(wt)
    print(wt.whitelist.get('192.168.1'))

