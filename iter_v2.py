#!/usr/bin/env python3

# dependence: pip3 install pandas3 tabulate PySocks

import io
import os
import sys
import json
import base64
import subprocess
import pandas as pd
import glob
import urllib
import requests

import socks
import socket

PORT_IN_BASE=10900


def ignore_filter_pass(k):
    ignore_key_columns = ['ip', 'bilibili', 'iqiyi', 'youtube', 'netflix', 'tiktok' ]
    for w in ignore_key_columns:
        if w in k:
            return False
    return True

def set_socks(port):
    proxy_host = '127.0.0.1'
    proxy_port = port

    # 设置代理类型为 SOCKS5
    socks.set_default_proxy(socks.SOCKS5, proxy_host, proxy_port)
    socket.socket = socks.socksocket


def check_ip_and_parse_result(index, line, template, addr, remark):
    # check_ip
    ret_check_bin = subprocess.check_output(['./check_ip.sh', '{}'.format(PORT_IN_BASE+index)])
    str_id = ret_check_bin.find(b'{')
    ret_check = ret_check_bin[str_id:]
    r = {}

    parse_ok = True

    try:
        result = json.loads(ret_check.decode('utf-8'))
    except json.decoder.JSONDecodeError as e:
        parse_ok = False
        return

    if parse_ok and len(result['ip']):

        line_valid.append(line)
        # for final user
        with open(f'config/{index}.json', 'w') as cfg:
            json.dump(template, cfg, indent=2)

        r['id'] = f'[{index}](config/{index}.json)'
        r['addr'] = addr

        # ip/cc/cn/isp by https://ipapi.co/json/ by proxy
        set_socks(PORT_IN_BASE + index)
        response = requests.get('https://ipapi.co/json/')
        ip_info = response.json()
        r['cn'] = ip_info.get('country_name', '')
        r['cc'] = ip_info.get('country_code', '')
        r['isp'] = ip_info.get('org', '')

        # copy result
        r['ip'] = result['ip']
        k_sorted = sorted(result.keys())
        for k in k_sorted:
            if ignore_filter_pass(k):
                r[k] = result[k] if len(result[k]) < 17 else result[k][:17] + '...'

        final_tab_valid.append(r)

    else:
        line_invalid.append(line)
        # for final user
        with open(f'config_invalid/{index}.json', 'w') as cfg:
            json.dump(template, cfg, indent=2)
        r['id'] = f'[{index}](config_invalid/{index}.json)'
        r['addr'] = addr
        final_tab_invalid.append(r)


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
        check_ip_and_parse_result(index, line, template, server_address, remark)

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
        if 'scy' in config:
            template['outbounds'][0]['settings']['vnext'][0]['users'][0]['security'] = config['scy']
        template['inbounds'][0]['port'] = PORT_IN_BASE + index

        if 'net' in config and 'tcp' == config['net']:
            template['outbounds'][0]['streamSettings']['network'] = 'tcp'
            template['outbounds'][0]['streamSettings']['wsSettings'] = None
        if 'net' in config and 'ws' == config['net']:
            template['outbounds'][0]['streamSettings']['network'] = 'ws'

            if 'tls' in config and len(config['tls']):
                template['outbounds'][0]['streamSettings']['security'] = config['tls']
                tls_settings = {}
                tls_settings['allowInsecure'] = False
                if 'host' in config:
                    tls_settings['serverName'] = config['host']
                template['outbounds'][0]['streamSettings']['tlsSettings'] = tls_settings

            ws_settings = {}
            ws_settings['connectionReuse'] = True
            if 'path' in config:
                ws_settings['path'] = config['path']
            if 'host' in config:
                headers = {}
                headers['Host'] = config['host']
                ws_settings['headers'] = headers
            template['outbounds'][0]['streamSettings']['wsSettings'] = ws_settings

        # for check ip
        with open(f'v2ray/config.json', 'w') as cfg:
            json.dump(template, cfg, indent=2)

        # check ip, parse result
        check_ip_and_parse_result(index, line,
            template,
            config['add'] if 'add' in config else '',
            config['ps'] if 'ps' in config else '')


def dump_line(index, line):

    # ignore first line
    if 0 == index:
        return
    print(f'[{index}] {line}')

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
    global final_tab_valid
    global final_tab_invalid
    global line_valid
    global line_invalid
    global line_todo
    global line_exception

    final_tab_valid = []
    final_tab_invalid = []
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

        table_valid = pd.json_normalize(final_tab_valid).to_markdown()
        table_invalid = pd.json_normalize(final_tab_invalid).to_markdown()

        with open('README.md', 'w') as file:
            file.write(iter_v2_check.__doc__)
            file.write('\n')
            file.write(table_valid)
            file.write('\n\n')
            record_line(file, 'Valid', line_valid)
            file.write(table_invalid)
            file.write('\n\n')
            record_line(file, 'Invalid', line_invalid)
            record_line(file, 'Exception', line_exception)
            record_line(file, 'Todo', line_todo)

if __name__ == '__main__':
    iter_v2_check()
