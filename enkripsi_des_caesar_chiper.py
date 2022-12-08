import streamlit as st
from Crypto.Cipher import DES # please install Pycrypto lib first
import binascii

if "section2" not in st.session_state:
    st.session_state.section2 = False

key = bytes([0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88]) # key in hex
mode = DES.MODE_ECB
char_padding = 'Z'
hasil_des=''

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
    encryption = des.encrypt(plaintext.encode('utf-8'))
    return encryption

def encrypt_char(char, key):
    x=None
    if (ord(char)+key != 127):
        x = (ord(char)+key)%127
    else:
        x = 127

    return str(chr(x)+" ")

def encrypt_message(message, key):
    cipher = ''
    for char in message:
        if char not in ' ,.':
            cipher += encrypt_char(char, key)
        else:
            cipher += char
    return cipher

st.header("Rekayasa Ide Keamanan Informasi Menggunakan Kriptografi Algoritma DES dan Caesar Chiper")

with st.form("s"):
    x = st.text_input('Masukkan Plain Teks Maks 8 Karakter')
    if st.form_submit_button("Enkripsi dengan Algoritma DES"):
        st.session_state.section2 = True
        
        plaintext = x[0:7]
        encrypt = DES_encrypt(plaintext, key)
        st.session_state.des = binascii.hexlify(encrypt).decode('utf-8')
        

if st.session_state.section2 :
    st.markdown('''**Hasil Enkripsi DES**''')
    st.code(st.session_state.des)
    
    if st.button("Enkripsi dengan Algoritma DES"):

        cc = encrypt_message(st.session_state.des,100)
        st.markdown('''**Hasil Enkripsi DES**''')
        st.code(cc)
        st.balloons()



