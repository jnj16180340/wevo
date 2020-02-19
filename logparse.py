#!/usr/bin/env python

from pathlib import Path
from re import compile
from operator import add
from functools import reduce
import json

LOG_PATH = 'info/logs'

line_parser = compile(r'^(?P<date>\d{2}-\d{2})\s(?P<time>\d\d:\d{2}:\d{2}.\d{3})\s(?P<pid1>\d+)\s(?P<pid2>\d+)\s(?P<tag>[\s\w]+):\s(?P<msg>.*)$')

#log_files = Path(LOG_PATH).glob('COMMAND_LOG_*')
log_files = Path(LOG_PATH).glob('COMMAND_LOG_3')

#log_file = log_files.__next__()
for log_file in log_files:

    parsed_lines = []

    with open(log_file, 'r') as fh:
        for line in fh:
            matched_line = line_parser.match(line)
            if matched_line:
                parsed_line = matched_line.groupdict()
                parsed_lines.append(parsed_line)

    # There is chunking:
    # 'msg': 'Start chunked log'
    # 'End chunked log'

    smoothed_lines = []
    chunks = []
    _state = 'single'
    for line in parsed_lines:
        if 'msg' in line and line['msg'] == 'Start chunked log':
            _state = 'chunk'
            chunks = []
            continue
        if 'msg' in line and line['msg'] == 'End chunked log':
            if _state=='single':
                chunks = []
                continue
            _state = 'single'
            smoothed_lines.append({**chunks[0],**{'msg':reduce(add, [l['msg'] for l in chunks])}})
            continue
        if _state == 'single':
            smoothed_lines.append(line)
            continue
        if _state == 'chunk':
            chunks.append(line)
            continue

    #msg_parser = compile(r'(?P<comment>.*:\[.*\])\s(?P<json>{.*})')
    #msg_parser = compile(r'^(?P<json>\{.*\}$)')
    #msg_parser = compile(r'SENT COMMAND:\[set_crop\] (?P<json>\{.*})$')
    msg_parser = compile(r'(?P<json>\{.*\}$)')

    json_logs = []
    bad_messages = []
    n_err = 0
    for l in smoothed_lines:
        if 'msg' in l:
            m = msg_parser.search(l['msg']) #.match(l['msg'])
            if m:
                try:
                    json_logs.append(json.loads(m.groupdict()['json']))
                except Exception as e:
                    print(f'{e}: Message {l["msg"]}')
                    #print(m.groupdict()['json'])
                    n_err+=1
            else:
                bad_messages.append(l['msg'])
                print(l['msg'])
                print(m)
                pass

    with open(f'{log_file}-parsed.json', 'w') as fh:
        json.dump(json_logs, fh, indent=2)
