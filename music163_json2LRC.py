#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import json
    import lrcutility
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1]) as jsonfile:
            jsonText = jsonfile.read()
    else:
        jsonText = raw_input()

    jsonOBJ = json.loads(jsonText)
    lrc_dict = lrcutility.lrc_parser(jsonOBJ['lrc']['lyric'])

    if jsonOBJ['tlyric']['lyric'] is not None:
        tlyric = lrcutility.lrc_parser(jsonOBJ['tlyric']['lyric'])
        for k, v in tlyric['body'].items():
            lrc_dict['body'][k] += ' %s' % v

    print(lrcutility.lrc_wrapper(lrc_dict))
