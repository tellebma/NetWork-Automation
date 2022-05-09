import json
import yaml
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


def load_yaml_data_from_file(file_path):
    try:
        with open(file_path) as file:
            data = yaml.safe_load(file)
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


if __name__ == "__main__":
    
    equipments = ["R2","ESW2"]
    use_json = False
    use_yaml = True
    for equipment in equipments:    
        if use_json:
            # JSON
            data = load_json_data_from_file(f"./data/{equipment}.json")
        elif use_yaml:
            # YAML
            data = load_yaml_data_from_file(f"./data/{equipment}.yaml")
        
        template = render_network_config(f"./{equipment}.j2",data)
        
        save_built_config(f"./config/config_{equipment}.conf",template)
        print(template)
    
