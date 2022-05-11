from re import template
from jinja2 import Template, Environment, FileSystemLoader
import json

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

def create_config_cpe_lyon_batA():
    """
    gen config for bat A
    """
    conf_to_gen = [f"./data/R1-CPE-BAT-A.json",f"./data/R2-CPE-BAT-A.json",f"./data/ESW1-CPE-BAT-A.json"]
    type_template = [f"./vlan_router.j2",f"./vlan_router.j2",f"./vlan_switch.j2"]
    config_gen = []

    if len(conf_to_gen) == len(type_template):
        for i in range(len(conf_to_gen)):
            data = load_json_data_from_file(conf_to_gen[i])
            
            render = render_network_config(type_template[i],data)
            if type_template[i] == "./vlan_router.j2":
                render += "\n"+render_network_config("./vrrp_router.j2",data)

            config_gen.append(render)
    
    return config_gen


def create_config_cpe_lyon_batB():
    """
    gen config for bat B
    """
    conf_to_gen = [f"./data/R1-CPE-BAT-B.json",f"./data/R2-CPE-BAT-B.json",f"./data/ESW1-CPE-BAT-B.json"]
    type_template = [f"./vlan_router.j2",f"./vlan_router.j2",f"./vlan_switch.j2"]
    config_gen = []

    if len(conf_to_gen) == len(type_template):
        for i in range(len(conf_to_gen)):
            data = load_json_data_from_file(conf_to_gen[i])
            
            render = render_network_config(type_template[i],data)
            if type_template[i] == "./vlan_router.j2":
                render += "\n"+render_network_config("./vrrp_router.j2",data)

            config_gen.append(render)
    
    return config_gen
    
if __name__ == "__main__":
    """
        process question 3 to 5:
    """
    confs = create_config_cpe_lyon_batA()
    names = ['config/R1-BAT-A.txt','config/R2-BAT-A.txt','config/ESW1-BAT-A.txt']
    for i in range(len(confs)):
        save_built_config(names[i],confs[i])

    confs = create_config_cpe_lyon_batB()
    names = ['config/R1-BAT-B.txt','config/R2-BAT-B.txt','config/ESW1-BAT-B.txt']
    for i in range(len(confs)):
        save_built_config(names[i],confs[i])
    
    print("Configuration généré")

    #question 3:
    #config = create_config_cpe_lyon_batA()

    #question 4:
    #save_built_config('config/R1_CPE_LYON_BAT_A.conf', config.get('r1'))
    #save_built_config('config/R2_CPE_LYON_BAT_A.conf', config.get('r2'))
    #save_built_config('config/ESW1_CPE_LYON_BAT_A.conf', config.get('esw1'))


    #question 5:
    #config = create_config_cpe_lyon_batB()
    #save_built_config('config/R1_CPE_LYON_BAT_B.conf', config.get('r1'))
    #save_built_config('config/R2_CPE_LYON_BAT_B.conf', config.get('r2'))
    #save_built_config('config/ESW1_CPE_LYON_BAT_B.conf', config.get('esw1'))
    pass