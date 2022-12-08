from Crypto.Cipher import DES # please install Pycrypto lib first
import binascii

def add_padding(str, blocksize=8):
    pad_len = blocksize - (len(str) % blocksize)
    padding = char_padding * pad_len
    return str + padding

def remove_padding(str, blocksize=8):
    pad_len = 0
    
    for char in str[::-1]:
        if char == char_padding:
            pad_len += 1
        else:
            break
            
    if(pad_len != 0):
        str = str[:-pad_len]
        
    return str

def DES_encrypt(plaintext, key, blocksize=8):
    
    if(len(plaintext) % blocksize != 0):
        plaintext = add_padding(plaintext)
        
    des = DES.new(key, mode)
    encryption = des.encrypt(plaintext)
    return encryption