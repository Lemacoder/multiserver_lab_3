import socket 
import json
import pickle

def saving():
    
    with open('pr_inf.json', 'w', encoding = "UTF-8") as file:
        json.dump(pickle.loads(data, encoding="utf-8"), file, indent=4, ensure_ascii=False)
        file.close()
        print("File was saved")
host = 'localhost'
port = 9090
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host, port)) 
flag = True
while True:
    m = input("Please, input your command ")
    if m == 'close':
        s.send(m.encode())
        flag = False
        break
    elif m == 'update':
        s.send(m.encode())
        p_l = int(s.recv(1024))
        byt = 0
        data = b''

        while byt <p_l:
            ch = s.recv(min(p_l-byt, 2048))
            byt = byt + len(ch)
            data += ch
        saving()
        print("Success!!!")
s.close()