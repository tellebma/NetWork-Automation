import napalm,json

r01 = {
'hostname':'172.16.100.126',
'username': 'cisco',
'password': 'cisco'
}


def get_inventory():
    try:
        with open('./inventory/hosts napalm.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"ERREUR | Le fichier './inventory/hosts napalm.json' n'existe pas.")
        raise(FileNotFoundError)
    return data

   

def save_built_config(file_name, data):
    with open(file_name,"w") as file:
        file.write(data)
        return True
    exit("Erreur ?")

def get_json_data_from_file(file):
    pass


def question_41(device,commande=["sh ip int brief"]):
    return device.cli(commande)


def question_42(r):
    return type(r)

def question_43(device):
    return 0

def question_45(device,file_or_conf=""):
    return device.load_merge_candidate(file_or_conf)

def question_46():
    devices = {
        "R1":{
            'hostname':'172.16.100.126',
            'username': 'cisco',
            'password': 'cisco'
            },
            "R2":{
            'hostname':'172.16.100.190',
            'username': 'cisco',
            'password': 'cisco'
            },"R3":{
            'hostname':'172.16.100.254',
            'username': 'cisco',
            'password': 'cisco'
            }
    }
    
    driver = napalm.get_network_driver('ios')
    
    #connect to device R01.
    device = driver(**r01)
    device.open() # open device.

    for device in devices:
        # device = R1
        # devices[device] = {..info..} 
        dev = driver(**devices[device])
        dev.open()
        question_45(dev,f"./config/ospf_{device}.conf")
        verifyConf(dev,hostname=device,overlaps=True,overlapsValue=False)
        # overlaps <=> doit ton courcircuité la demande a l'utilisateur. Si oui overlapsValue est utilisé pour save la config ou la discard.
    return 0





def verifyConf(device,hostname=False,overlaps=False,overlapsValue=False):
    if not overlaps and device:    
        print("================================")
        if hostname:
            print(f"\t---{hostname}---")
        print(device.compare_config())
        print("================================")

        if input("Are you satisfied ? (y,n)\t") == "y":
            device.commit_config()
            print("Config Pushed")
        else:
            device.discard_config()
            print("Config discarded.")
    if overlaps:
        if overlapsValue:
            device.commit_config()
        else:
            device.discard_config()
    return True

def createBackup():
    driver = napalm.get_network_driver('ios')
    host = get_inventory()
    for eq in host:
        print(f"Creating Backup for {eq}")
        device = driver(**host[eq])
        device.open() # open device.
        data = device.get_config("running")
        print(data)
        save_built_config(f"./config/backup/{eq}.bak",data['running'])


if __name__ == "__main__":
    # generate driver.
    driver = napalm.get_network_driver('ios')
    
    #connect to device R01.
    device = driver(**r01)
    device.open() # open device.
    
    commande_envoye = 'sh ip int brief'
    r =question_41(device,[commande_envoye])
    # print(r) # Le resultat est sous la forme d'un dict.
    
    type_r = question_42(r)
    # 42
    print(type_r)
    print(r[commande_envoye])
    
    # 43
    arp_config = device.get_arp_table()
    print(arp_config)

    # 44
    print(type(arp_config)) # liste 
    print(arp_config[0]) 
    print(type(arp_config[0])) # dict

    # 45
    file = "./config/loopback_R01_napalm.conf"
    res = question_45(device,file)
    verifyConf(device,overlaps=True,overlapsValue=False) # overlaps <=> doit ton courcircuité la demande a l'utilisateur. Si oui overlapsValue est utilisé pour save la config ou la discard.

    r =question_41(device,[commande_envoye])
    print(r[commande_envoye])


    """
    Q 45b :
    Loopback1                  192.168.1.1     YES TFTP   up                    up      
    Loopback2                  192.168.2.1     YES TFTP   up                    up      
    Loopback4                  192.168.4.1     YES NVRAM  up                    up

    Les loopback ont comme méthode "TFTP"
    Ce qui signifie que les interface on été créé depuis un server TFTP.
    Napalm utilise TFTP pour envoyer les configuration sur les équipement.
    """

    # 46
    question_46()



    createBackup()