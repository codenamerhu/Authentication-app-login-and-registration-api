import os, time
from binascii import hexlify
                             
                             
def create_hash():
    return str(hexlify(os.urandom(16)), 'ascii')
                             
def time_stamp():
    return int(round(time.time()))

def create_private_key():
    
    _key = "privt_" + str(hexlify(os.urandom(16)), 'ascii')
    return _key

def create_public_key():
    
    _key = "pub_" + str(hexlify(os.urandom(16)), 'ascii')
    return _key


def peachLiveUrl():
    
    return ""

def peachSandboxUrl():
    return ""