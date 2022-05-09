
from asyncio import transports
import re,json

from netmiko import ConnectHandler
from scripts import create_config

r01 = {
    'device_type': 'cisco_ios',
    'host': '172.16.100.126',
    'username': 'cisco',
    'password': 'cisco'
}


def question_25(net_connect):
    return net_connect.send_command("sh ip int brief")


def question_26(net_connect):
    return net_connect.send_command("sh ip int brief", use_textfsm=True)



def question_27(net_connect):
    return net_connect.send_command("sh ip route", use_textfsm=True)


def question_28(net_connect):
    print("Etat Interfaces :")
    interfaces = question_26(net_connect)
    for interface in interfaces:
        print("--------------------------------------------")
        print(f"{interface['intf']} --> {interface['status']}")
        print(net_connect.send_command(f"show run | section interface {interface['intf']}"))
        
    return 0


def question_29(net_connect):
    commandes = ["int lo3","ip add 192.168.1.5 255.255.255.255","desc loopback interface from netmiko"]
    output = net_connect.send_config_set(commandes)
    
    #print(output)
    print(net_connect.send_command(f"show run | section interface Loopback3"))
    net_connect.save_config()


def question_30(net_connect,interface="lo1"):
    return net_connect.send_config_set(f"no int {interface}")


def question_31(net_connect,file="./config/loopback_R01.conf"):
    res = net_connect.send_config_from_file(file)
    net_connect.save_config()
    return res
    
def question_31_b(net_config):
    with open("./config/loopback_R01.conf") as file:
        data = file.readlines()
    res = net_connect.send_config_set(data)
    net_connect.save_config()
    return res
    
    
        

def question_32(net_connect):
    interfaces = question_26(net_connect)
    int_remove = []
    for interface in interfaces:
        if interface['intf'][0:8] == "Loopback":
            question_30(net_connect,interface=interface['intf'])
            int_remove.append(interface['intf'])
    return int_remove
    


def get_inventory():
    try:
        with open('./inventory/hosts.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"ERREUR | Le fichier './inventory/hosts.json' n'existe pas.")
        raise(FileNotFoundError)
    return data


def question_35(liste_equipement_all):
    for eq in liste_equipement_all:
        if eq[0] == "R":
            print(eq+"---")
            net_connect = ConnectHandler(**liste_equipement_all[eq])
            print(net_connect.send_command(f"show run | section interface GigabitEthernet0/0.99"))
    return 0

def connectDevice(device):
    inv = get_inventory()
    for eq in inv:
        if eq == device:
            return ConnectHandler(**inv[eq])
    exit("Device non trouvé.")
    return False        
    

def question_36():
    
    files = {
        "ESW2":"vlan_ESW2.conf",
        "ESW3":"vlan_ESW3.conf",
        "R2":"vlan_R02.conf",
        "R3":"vlan_R03.conf"
    }
    for device,file in files.items():
        try:
            print(f"{device} => {file}")
            net_connect=connectDevice(device)
            question_31(net_connect,f"./config/{file}")
            print("   Config Pushed")
        except Exception:
            print("   Erreur lors de la config.")


    return 0
      

if __name__ == "__main__":    
    create_config.create_file_config()
    



    #23
    net_connect = ConnectHandler(**r01)
    #24
    #print(net_connect.__dict__)
    
    #25
    #print(question_25(net_connect))

    #26
    #    print(question_26(net_connect))
    # 27
    #   print(question_27(net_connect))
    #28
    #question_28(net_connect)
    #29
    #print(question_29(net_connect))
    #30
    #print(question_30(net_connect))
    #VErifier :
    #question_28(net_connect)
    #31
    # => send_config_from_file
    #print(question_31(net_connect))
    # parse file by lines
    #print(question_31_b(net_connect))
    #32
    # print(question_32(net_connect))
    # vEerifier
    # question_28(net_connect)
    
    #34
    #liste_equipement = get_inventory()
    
    
    #35 
    #print(question_35(liste_equipement))

    #36
    question_36()