from flask import Flask,jsonify,request,abort, make_response
from werkzeug.exceptions import HTTPException
import json
from nornir import InitNornir

app = Flask(__name__)

#files
from services.devices import get_inventory,add_device,get_device_by_name,delete_device,get_device_interfaces,get_device_interfaces_ip


"""
    - routes goes here - 
"""

@app.route("/")
def endpoint():
    return jsonify(
        env="DEV",
        name="fastprod_backend",
        version="1.0d"
    )


@app.route("/devices", methods=['GET', 'POST'])
def devices():
    if request.method == 'GET':
        devices = get_inventory()
        return jsonify(devices=devices, total_count=len(devices))
    if request.method == 'POST':
        data = request.get_json()
        new_device = add_device(data)
        init_nornir() # -- refresh nornir --
        return jsonify(device=new_device)


@app.route("/devices/<device_name>", methods=['GET', 'DELETE'])
def device_by_name(device_name):
    if request.method == 'GET':
        device = get_device_by_name(device_name)
        return jsonify(device=device)
    
    if request.method == 'DELETE':
        device = get_device_by_name(device_name)
        delete_device(device)
        init_nornir() # -- refresh nornir --
        return jsonify(message="Device deleted")

@app.route("/devices/<device_name>/interfaces", methods=['GET'])
def get_interfaces(device_name):
    interfaces = get_device_interfaces(device_name)
    return jsonify(interfaces=interfaces)

@app.route("/devices/<device_name>/interfaces/ip", methods=['GET'])
def get_interfaces_ip(device_name):
    if request.method == 'GET':
        device = get_device_by_name(device_name)
        interfaces_ip = get_device_interfaces_ip(device)
    return jsonify(interfaces_ip=interfaces_ip)
"""
    - Error handler -
"""
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
        })
    response.content_type = "application/json"
    return response




def init_nornir():
    app.config['nr'] = InitNornir(config_file="fastprod/inventory/config.yaml")



init_nornir()


"""
15.a.x)
Effectivement apres avoir ajouté notre device il n'apparait pas dans la requete GET.
Du fait qu'on ne refresh pas nornir. Pour ce faire, on ajoute init_nornir() apres chaque ajout/modification d'un des fichiers. (ici hosts.yaml)

"""
