from nornir import InitNornir
from create_config import save_built_config

nr = InitNornir(config_file="inventory/config.yaml")

def question_13(nr):
    print("="*20+"\nQuestion 13")
    print(nr.__dict__)
    print(nr.inventory)
    """
    {'data': <nornir.core.state.GlobalState object at 0x7f8076fbae50>,
    'inventory': <nornir.core.inventory.Inventory object at 0x7f8073586a00>,
    'config': <nornir.core.configuration.Config object at 0x7f80735e5ea0>,
    'processors': [],
    'runner': <nornir.plugins.runners.ThreadedRunner object at 0x7f8073509ca0>}
    
    a) Les attribus sont : data,inventory,config,processors,runner
    b) Le format de la donnée retourné est un json/dictionnaire Python
    c) La méthode inventory nous permet d'acceder a notre inventaire


    """

def question_14(nr):
    print("="*20+"\nQuestion 14")
    h = nr.inventory.hosts
    print(h)
    print(type(h))
    exit
    """
    Depuis la méthode inventory on peut appeler la fct/variable hosts
    Le format retourné est du yaml (?)
    Les données retourné sont les noms (key) de chaque objet

    Returns set of hosts that belongs to a group including those that belong indirectly via inheritance
    https://nornir.readthedocs.io/en/latest/api/nornir/core/inventory.html?highlight=hosts
    """
    return h

def question_15(nr=False,hosts=False):
    print("="*20+"\nQuestion 15")
    i = hosts['R1-CPE-BAT-A']
    print(i)
    print(type(i))
    """
    La valur retourné est un objet 
    """
    return i

def question_16(nr=False,i=False):
    print("="*20+"\nQuestion 16")
    """
    d = dir(i)
    for d_bis in d:
        print("*"*5)
        print(d_bis)
    """
    # LoL
    print(i.get_connection_parameters().dict())

    # donne l'IP
    print(i.hostname)
    """
    l'adresse IP peut se trouver dans hostname. Cette valeurest tiré du fichier hosts.yaml.
    """

    print(i.username)
    print(i.password)
    """
    Username et password proviennent du fichier defaults.yaml.
    """

    """
    Les infos viennent du block R1-CPE-BAT-A du fichier hosts.yaml.
    """

def question_17(nr=False,i=False):
    print("="*20+"\nQuestion 17")
    k = i.keys()
    print(k)
    """
    dict_keys(['device_name', 'device_type', 'device_model', 'locality', 'building', 'vendor'])
    Ces informations proviennent du fichier hosts.yaml de la catégorie 
        --data-- 
    On retrouve dans cet objet :    
        device_name: R1-CPE-BAT-A
        device_type: router
        device_model: C7200
        locality: lyon
        building: A
    
    Apres avoir rajouté room :
        room: 001
    
    dict_keys(['device_name', 'device_type', 'device_model', 'locality', 'building', 'room', 'vendor'])
    """
def question_18(nr=False,i=False):
    print("="*20+"\nQuestion 18")
    print(i['room'])


def question_19(nr):
    print("="*20+"\nQuestion 19")
    print(nr.inventory.groups)

def question_20(nr):
    print("="*20+"\nQuestion 20")
    g = nr.inventory.hosts.get('R1-CPE-BAT-A').groups
    print(g)

def question_21(nr):
    print("="*20+"\nQuestion 21")

    k = nr.inventory.hosts.get('R1-CPE-BAT-A').groups[0].keys()
    print(k)

def question_22(nr):
    print("="*20+"\nQuestion 22")

    #q21
    q21 = nr.inventory.hosts.get('R1-CPE-BAT-A').groups[0]
    print(q21['vendor'])
    


def question_23(nr):
    print("="*20+"\nQuestion 23")
    a = nr.inventory.hosts
    hosts = list(a.keys())
    #print(a)
    for host in hosts:
        print(host+" - "+nr.inventory.hosts.get(host).hostname)

def question_24(nr):
    print("="*20+"\nQuestion 24")

    t = nr.filter(device_type="router").inventory.hosts.keys()
    print(t)

def question_25(nr):
    print("="*20+"\nQuestion 25")

    t = nr.filter(device_type="router_switch").inventory.hosts.keys()
    print(t)


def question_26(nr):
    print("="*20+"\nQuestion 26")

    result = nr.run(task=hello_world)
    print(result)
    return result

def question_27(result):
    print(type(result))
    """
    Agregated result.
    """

def question_28(result):
    print_result(result)

def question_30(nr):
    print("="*20+"\nQuestion 30")

    result = nr.filter(device_type="router_switch").run(task=hello_world)
    print_result(result)
    return result

def question_32(nr):
    print("="*20+"\nQuestion 32")
    results = nr.filter(device_type="router").run(task=napalm_cli, commands=["show ip int brief"])
    print_result(results)

def question_33(nr):
    print("="*20+"\nQuestion 33")
    results = nr.filter(device_type="router_switch").run(task=napalm_get, getters=["get_arp_table"])
    print_result(results)

def question_34(nr):
    print("="*20+"\nQuestion 34")
    commandes = ["interface lo1","ip add 1.1.1.1 255.255.255.255"]
    result = nr.filter(hostname="172.16.100.125").run(task=napalm_configure, configuration="\n".join(commandes))
    print_result(result)
    
    commandes = ["interface lo1","ip add 2.2.2.2 255.255.255.255"]
    result = nr.filter(hostname="172.16.100.126").run(task=napalm_configure, configuration="\n".join(commandes))
    print_result(result)

def question_35(nr):
    print("="*20+"\nQuestion 35")

    results = nr.filter(device_type="router").run(task=napalm_get, getters=["get_config"])
    #print_result(results)
    
    #print(results)#['get_config']['running']
    for host in list(results.keys()):
        a = (results[host][0].result)['get_config']['running']
        save_built_config(f"./config/backup_{host}.bak",a)
    #TODO faire une boucle.

def question_36(nr):
    pass

def question_37(nr):
    pass

def question_38(nr):
    pass

def question_39(nr):
    pass
    
def question_40(nr):
    pass


def question_41(nr):
    pass

if __name__ == "__main__":
    
    #hosts
    question_13(nr)
    h = question_14(nr)
    i = question_15(nr,h)
    question_16(nr,i)
    question_17(nr,i)
    question_18(nr,i)

    #groups
    question_19(nr)
    question_20(nr)
    question_21(nr)
    question_22(nr)
    question_23(nr)

    #Filter
    question_24(nr)
    question_25(nr)


    from nornir.core.task import Task, Result
    def hello_world(task: Task) -> Result:
        return Result(
            host=task.host,
            result=f"{task.host.name} says hello world!"
        )

    result = question_26(nr)
    #question_27(result)


    from nornir_utils.plugins.functions import print_result

    #question_28(result)   
    
    # Q 29 :
    """
    La task va executer sur tous les hosts notre task ici "host says Hello World!"
    
    """
    #question_30(nr)

    from nornir_napalm.plugins.tasks import napalm_get,napalm_configure, napalm_cli
    from nornir_netmiko.tasks import netmiko_send_config,netmiko_send_command, netmiko_save_config, netmiko_commit
    #question_32(nr)
    
    #question_33(nr)
    #question_34(nr)
    question_35(nr)
    question_36(nr)
    question_37(nr)
    question_38(nr)
    question_39(nr)

    question_40(nr)
    question_41(nr)