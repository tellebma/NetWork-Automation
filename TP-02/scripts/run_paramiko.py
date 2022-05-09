import time,paramiko,re

import warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

devices = {
    "R1":{
        "ip":"172.16.100.126",
        "username":"cisco",
        "password":"cisco"
    },
    "R2":{
        "ip":"172.16.100.190",
        "username":"cisco",
        "password":"cisco"
    },
    "R3":{
        "ip":"172.16.100.254",
        "username":"cisco",
        "password":"cisco"
    }
}

def initSSH(device):
    ssh = paramiko.SSHClient() #initialization of SSHClient class
    #Set policy to use when connecting to servers without a known host key
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #init connection with the remote device
    ssh.connect(device['ip'],
        username=device['username'],
        password=device['password'],
        look_for_keys=False, allow_agent=False,
        timeout=5)
    
    #get the remote shell
    remote_conn = ssh.invoke_shell()
    return ssh, remote_conn


def commande(device,commande_to_send,sshAlreadyStarted=False):
    nbytes=65535
    if isinstance(commande_to_send,list):
        if not sshAlreadyStarted:
            ssh, remote_conn = initSSH(device)
        else:
            ssh, remote_conn = sshAlreadyStarted
        res = []
        for commande_i in commande_to_send:
            res.append(commande(device,commande_i,(ssh,remote_conn)))
        ssh.close()
        return res
    if not sshAlreadyStarted:
        ssh, remote_conn = initSSH(device)
    else:
        ssh, remote_conn = sshAlreadyStarted

    commande_to_send+="\n"
    
    duration = 0.5
    if commande_to_send[0:2] == "sh":
        duration = 2
    
    remote_conn.send(commande_to_send)
    time.sleep(duration)
    output = remote_conn.recv(nbytes).decode('utf-8') #Get output data from the channel
  
    if not sshAlreadyStarted:
        ssh.close()
    
    return output


def save_built_config(file_name, data):
    with open(file_name,"w") as file:
        file.write(data)
        

def save_config(devices_to_save=[]):
    """
    devices_to_save = ["R1","R2"]
    on peut passer soit:
    une liste soit un device précis.
    """
    if isinstance(devices_to_save,list):
        for device in devices_to_save:
            save_config(device)
        return True
    equipement = devices[devices_to_save]
    # permet d'afficher tout le res dan le terminal.
    
    save_built_config(f"./config/backup/backup_{devices_to_save}.conf",commande(equipement,["terminal length 0","sh run"])[1])
        




if __name__ == "__main__":
    #res = commande(["sh run","sh ip int brief"])
    
    """
    q14 - le resultat est tronqué.
    
    """
    
    """
    q15 - 
    """
    """
    res = commande(["conf t",
                    "int lo1",
                    "ip add 192.168.1.1 255.255.255.255",
                    "desc loopback interface from paramiko (incroyable.)"])

    for r in res:
        print("============================")
        print(r)
    """
    
    
    """
    q16:
    """
    """for device in devices:
        show_lo1 = commande(devices[device],"sh ip int lo1")
        print(show_lo1)"""
    """
    q17:
    """
    """
    for device in devices:
        res = commande(devices[device],["conf t ","int G0/0.99","desc desc incroyable non c'est faux."])
        for r in res:
            print(r)
    """
    """
    q18:
    """
    save_config(["R1","R2","R3"])
