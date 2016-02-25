#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib2


def get_lyric(music_id):
    url = "http://music.163.com/api/song/lyric?os=osx&id=" + str(music_id) + "&lv=-1&kv=-1&tv=-1"
    opener = urllib2.build_opener()
    opener.addheaders = [('Cookie', 'appver=1.5.2'), ('Referer', 'http://music.163.com/')]
    result = opener.open(url)
    return result.read()


if __name__ == '__main__':
    print(get_lyric(sys.argv[1]))
