#m3u parse
from Playlist import *

plst = []
def m3u_parse(fname):
    words = ''
    l = []
    with open(fname, 'r') as f:
        data = f.readline()
       # while data:

        tmp = []

        while data:
            if '#EXTM3U' in data: 
                data = f.readline()
                continue
            if "#EXTINF:" not in data: 
                tmp.append(data)
                l.append(tmp)
                plst.append(Plist_item(data))

                tmp = [] 
            else:
                tmp.append(data)
            data = f.readline()     

    return plst
def m3u_parseb(fname):
    words = ''
    l = bytes()
    with open(fname, 'rb') as f:
        byte = f.read(1)
        b_len = 0
        while byte:
            try:
                if b'\n' == byte: n_str = " END_OF_REC " 
                else: n_str = byte.decode('Latin-1')
                print("STRING: ",n_str,)
                print(byte)
                l += byte
                b_len += 1
            except UnicodeEncodeError as US:
                print("?", end = "")
            byte = f.read(1)
    return l
test = m3u_parse('testplaylist.m3u')

