#! /usr/bin/env python3
"""Pandoc filter that replaces labels of format {#?:???}, where ? is a
single lower case character defining the type and ??? is an alphanumeric
label, with numbers. Different types are counted separately.

"""

from pandocfilters import toJSONFilter, Str
import re

REF_PAT = re.compile('\{#([a-z]):(\w*)\}')
FORM = '{{#{}:{}}}'

known = {}

def figref(key, val, fmt, meta):

    new_val = val

    if key == 'Str' and REF_PAT.search(val):
        all_tags = REF_PAT.findall(val)
        for kind, label in all_tags:
            
            if kind in known:
                if label not in known[kind]:
                    known[kind][label] = str(len(known[kind]) + 1)
            else:
                known[kind] = {}
                known[kind][label] = "1"

            new_val = new_val.replace(FORM.format(kind,label), 
                                      known[kind][label])

        return [Str(new_val)]

if __name__ == '__main__':
    toJSONFilter(figref)