#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re


def lrc_parser(lines):
    my_regex = re.compile(r'\[(\S+?):(\S+?)\](.*)')
    # lrc_dict = {'head': {}, 'body': {}}
    lrc_dict = dict(head={}, body={})
    for line in lines.split('\n'):
        result = my_regex.match(line)
        if result:
            minute, second = result.group(1), result.group(2)
            # [by:阿卡琳]
            # [offset:500]
            if not minute.isdigit():
                lrc_dict['head'][minute] = second
            # [xx:xx.xxx]xxxxx
            else:
                lrc_dict['body'][int(minute) * 60000 + int(float(second) * 1000)] = result.group(3)

    return lrc_dict


def __time_wrapper(number):
    minute = number // 60000
    second = ((number - minute * 60000) % 1000)/1000.0
    return '[%02d:%06.3f]' % (minute, second)


def lrc_wrapper(lrc_dict):
    lrc_lines = ""
    if lrc_dict['head']:
        for (key, value) in lrc_dict['head'].iteritems():
            lrc_lines += '[%s:%s]\n' % (key, value)
    if lrc_dict['body']:
        for (key, value) in sorted(lrc_dict['body'].items()):
            lrc_lines += '%s%s\n' % (__time_wrapper(key), value)

    return lrc_lines
