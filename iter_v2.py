#!/usr/bin/env python3

# dependence: pip3 install pandas3 tabulate

import io
import os
import sys
import json
import base64
import subprocess
import pandas as pd
import glob
import urllib

PORT_IN_BASE=10900


def ignore_filter_pass(k):
    ignore_key_columns = ['ip', 'bilibili', 'iqiyi', 'youtube' ]
    for w in ignore_key_columns:
        if w in k:
            return False
    return True

def check_ip_and_parse_result(index, addr, remark):
    # check_ip
    ret_check_bin = subprocess.check_output(['./check_ip.sh', '{}'.format(PORT_IN_BASE+index)])
    str_id = ret_check_bin.find(b'{')
    ret_check = ret_check_bin[str_id:]
    try:
        result = json.loads(ret_check.decode('utf-8'))
    except json.decoder.JSONDecodeError as e:
        print('parse error')
        return

    # parse ok
    r = {}
    r['id'] = f'[{index}](config/{index}.json)'
    r['addr'] = addr
    r['ip'] = result['ip']
    k_sorted = sorted(result.keys())
    for k in k_sorted:
        if ignore_filter_pass(k):
            r[k] = result[k] if len(result[k]) < 17 else result[k][:17] + '...'

    # if no ip detected, ignore result and return False
    if len(r['ip']):
        final_tab.append(r)
        return True

    return False

def dump_and_check_ss(index, line):
    '''
    ss://YWVzLTI1Ni1nY206a0RXdlhZWm9UQmNHa0M0@85.208.108.60:8881#github.com/freefq%20-%20%E6%B2%99%E7%89%B9%E9%98%BF%E6%8B%89%E4%BC%AFArabic%20Computer%20System%20Co.%2023
        |aes-256-gcm:kDWvXYZoTBcGkC4         |addr:port         |remark ...|

    '''
    encoded_config, server_info  = line.split("://")[1].split('@')
    try:
        security, password = base64.b64decode(encoded_config).decode("utf-8").split(":")
    except Exception as e:
        line_exception.append(line)
        return
    server_address, server_port = server_info.split("#")[0].split(":")
    remark = urllib.parse.unquote(server_info.split("#")[1])

    if False:
        print(f'encoded_config:[{encoded_config}], server_info:[{server_info}]')
        print(f'server_address:[{server_address}] server_port:[{server_port}]')
        print(f'security      :[{security}] password:[{password}]')

    with open('template/ss.json') as ss:
        template = json.loads(ss.read())
        template['outbounds'][0]['settings']['servers'][0]['address'] = server_address
        template['outbounds'][0]['settings']['servers'][0]['port'] = int(server_port)
        template['outbounds'][0]['settings']['servers'][0]['method'] = security
        template['outbounds'][0]['settings']['servers'][0]['password'] = password
        template['inbounds'][0]['port'] = PORT_IN_BASE + index
        # for check ip
        with open(f'v2ray/config.json', 'w') as cfg:
            json.dump(template, cfg, indent=2)

        # check ip, parse result
        if check_ip_and_parse_result(index, server_address, remark):
            # record valid
            line_valid.append(line)

            # for final user
            with open(f'config/{index}.json', 'w') as cfg:
                json.dump(template, cfg, indent=2)
        else:
            # record invalid
            line_invalid.append(line)

def dump_and_check_vmess(index, line):
    try:
        v2_data = base64.urlsafe_b64decode(line.split("://")[1] + '==').decode("utf-8")
    except Exception as e:
        line_exception.append(line)
        return

    config = json.loads(v2_data)

    if False:
        k_sorted = sorted(config.keys())
        for k in k_sorted:
            v = config[k]
            print(f'{k}: {v}')
        print('______________________________')

    # load template and update by line
    with open('template/vmess.json') as vmess:
        template = json.loads(vmess.read())
        template['outbounds'][0]['settings']['vnext'][0]['address'] = config['add']
        template['outbounds'][0]['settings']['vnext'][0]['port'] = int(config['port'])
        template['outbounds'][0]['settings']['vnext'][0]['users'][0]['id'] = config['id']
        template['outbounds'][0]['settings']['vnext'][0]['users'][0]['alterId'] = int(config['aid'])
        if 'security' in config:
            template['outbounds'][0]['settings']['vnext'][0]['users'][0]['security'] = config['security']
        template['inbounds'][0]['port'] = PORT_IN_BASE + index

        # for check ip
        with open(f'v2ray/config.json', 'w') as cfg:
            json.dump(template, cfg, indent=2)

        # check ip, parse result
        if check_ip_and_parse_result(index, config['add'] if 'add' in config else '',
                config['ps'] if 'ps' in config else ''):

            # record valid
            line_valid.append(line)

            # for final user
            with open(f'config/{index}.json', 'w') as cfg:
                json.dump(template, cfg, indent=2)
        else:
            # record invalid
            line_invalid.append(line)


def dump_line(index, line):

    # ignore first line
    if 0 == index:
        return

    if line.startswith('ss://'):
        dump_and_check_ss(index, line)
    elif line.startswith('vmess://'):
        dump_and_check_vmess(index, line)
    # TODO for other protocol
    else:
        line_todo.append(line)

def record_line(file, title, lines):
    if len(lines) > 0:
        # title
        file.write(f'## {title}\n')

        # m+
        file.write(
'''```
'''
        )

        # lines
        for line in lines:
            file.write(line)

        # m-
        file.write(
'''```

'''
        )

def iter_v2_check():
    '''
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)
    
    '''
    global final_tab
    global line_valid
    global line_invalid
    global line_todo
    global line_exception

    final_tab = []
    line_valid = []
    line_invalid = []
    line_todo = []
    line_exception = []

    if len(sys.argv) > 1 and os.access(sys.argv[1], os.R_OK):

        # remove already generated '*.json' in 'config/'
        for f in glob.glob(os.path.join('config', '*.json')):
            os.remove(f)

        # equivalent shell command 'cat free/v2 | base64 -d | less'
        with open(sys.argv[1], 'r') as file:
            encoded_data = file.read()

            # decode base64 encoded file
            try:
                decoded_data = base64.b64decode(encoded_data)
            except Exception as e:
                sys.exit(False)

            # save into buffer
            buffer = io.StringIO(decoded_data.decode())

            # iter every line
            for index, line in enumerate(buffer):
                dump_line(index, line)

        table = pd.json_normalize(final_tab).to_markdown()

        with open('README.md', 'w') as file:
            file.write(iter_v2_check.__doc__)
            file.write('\n')
            file.write(table)
            file.write('\n\n')
            record_line(file, 'Valid', line_valid)
            record_line(file, 'Invalid', line_invalid)
            record_line(file, 'Exception', line_exception)
            record_line(file, 'Todo', line_todo)

if __name__ == '__main__':
    iter_v2_check()
