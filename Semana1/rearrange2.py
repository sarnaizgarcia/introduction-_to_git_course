#!/usr/bin/env python3

import re


def arrange_name(name):
    result = re.search(r'^([\w .-]*), ([\w .-]*)$', name)
    if result == None:
        return result
    return f'{result[2]} {result[1]}'
