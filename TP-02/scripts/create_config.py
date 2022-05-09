
import json
from jinja2 import Template, Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader("templates"))


def load_json_data_from_file(file_path):
    try:
        with open(file_path) as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"ERREUR | Le fichier {file_path} n'existe pas.")
        raise(FileNotFoundError)
    return data

def render_network_config(template_name, data):
    """
    Param:
        tempalte_name
        data
    """
    # recupère les informations du tempalte.
    template = env.get_template(template_name)
    # render le template avec la data.
    return template.render(data)
    

def save_built_config(file_name, data):
    with open(file_name,"w") as file:
        file.write(data)
        return True
    exit("Erreur ?")


def create_vlan_config_cpe_marseille():
    data = load_json_data_from_file(f"./data/vlan_R2.json")
    a = render_network_config(f"./vlan_router.j2",data)
    data = load_json_data_from_file(f"./data/vlan_ESW2.json")
    b = render_network_config(f"./vlan_switch.j2",data)
    return a,b

def create_vlan_config_cpe_paris():
    """template = []
    equipments = ["router",""]
    equipement = {
        "R3":{
            "type":"router"
        },
        "ESW3":{
            "type":"switch"
        }
    }
    for equipment in equipments:    
        data = load_json_data_from_file(f"./data/{equipment}.json")
        template.append(render_network_config(f"./{equipment}.j2",data))
        
    return template"""
    data = load_json_data_from_file(f"./data/vlan_R3.json")
    a = render_network_config(f"./vlan_router.j2",data)
    data = load_json_data_from_file(f"./data/vlan_ESW3.json")
    b = render_network_config(f"./vlan_switch.j2",data)
    return a,b

def create_config_ospf():
    for el in ["R1","R2","R3"]:
        print(el)
        data = load_json_data_from_file(f"./data/vlan_{el}.json")
        a = render_network_config(f"./template_ospf.j2",data)
        save_built_config(f'config/ospf_{el}.conf', a)

    return 0


def create_file_config():
    r02_config, esw2_config = create_vlan_config_cpe_marseille()
    save_built_config('config/vlan_R02.conf', r02_config)
    save_built_config('config/vlan_ESW2.conf', esw2_config)

    r03_config, esw4_config = create_vlan_config_cpe_paris()
    save_built_config('config/vlan_R03.conf', r03_config)
    save_built_config('config/vlan_ESW3.conf', esw4_config)


if __name__ == "__main__":
    """
        process question 1 to 5:
    """
    create_file_config()
    create_config_ospf()