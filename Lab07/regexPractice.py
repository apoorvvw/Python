#!/usr/local/bin/python3.4

__author__ = 'ee364e10'

import re
import os

def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

if __name__ == "__main__":
    count = c = 0
    # a = "falks12.45dfkj @@eeeEE364. 1.45554886 EE364"
    a = "I like like like like like like like like like you you you"
    # ff = re.subn(r"(EE364)","(EE461)",a , count = 1)
    ff = re.search("(I){1}(like){10,}(you){1,2}" , a)
    #re.match("(.*)(is a)(.*)",a)
    #re.search("e",a,re.I)
    #re.findall(r"[0-2]?[0-9]?[0-9]+\.[0-2]?[0-9]?[0-9]+\.[0-2]?[0-9]?[0-9]+\.[0-2]?[0-9]?[0-9]+",a)
    #\.[0-255]{1,3}\.[0-255]{1,3}\.[0-255]{1,3}
    print(ff)
    # for i in ff:
    #     count += int(i)
    #     c += 1
    # print(count / c)
    # pass