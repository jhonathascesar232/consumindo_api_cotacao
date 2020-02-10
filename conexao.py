import socket
   
confiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']

def check_host():
    global confiaveis
    for host in confiaveis:
        a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a.settimeout(.5)
        try:
            b=a.connect_ex((host, 80))
            if b==0: #ok, conectado
                return True
        except:
            pass
        a.close()
    return False

print(f'** Conexão {check_host()}')