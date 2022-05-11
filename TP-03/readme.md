# TP 3

Creation de Fichier data json => parse Dans nos templates Jinja. Comme dans les précedents TPs.

Mise en situation cas réél (simulation GNS3)

### <a href="./scripts/run_nornir.py">Nornir</a>
Nornir est un outil très très puissant.(comme python lol)

Avec une simple configuration <a href="./inventory">celle-ci</a> il est possible de configurer et de naviguer dans les equipements. Toutes les configuration sont faites en yaml (pas mon fav...) 

Ex configuration router:  
```yaml
R1-CPE-BAT-A:
  hostname: 172.16.100.125
  port: 22
  groups:
    - ios
  data: # Anything under this key is custom data
    device_name: R1-CPE-BAT-A
    device_type: router
    device_model: C7200
    locality: lyon
    building: A
    room: 54001
```

L'initialisation de nornir permet d'acceder à toutes les info possible, identifiant de connexion aux routers, mdp, ip etc.   
La commande pour effectuer des tâche est la suivante:  ```python nr.filter(device_type="router_switch").run(task=hello_world) ```  
Dans le cas ou l'on souhaite faire des tâches plus complexe, on couple nornir avec les différents outils utilisé dans le <a href="../TP-02">TP-02</a>
Avec Napalm cela donne:  
```python  nr.filter(device_type="router").run(task=napalm_cli, commands=["show ip int brief"])```   
On peut aussi utiliser des fonction simplifier pour avoir les différentes info que l'on souhaite,  
pour les utiliser => <a href="https://nornir.readthedocs.io/en/latest/api/index.html" >Documentation</a>  
ex:    
Done les information sur la Table ARP :  
```python run(task=napalm_get, getters=["get_arp_table"])```   
      
Pour filtrer les équipements sur lesquel nous faisons des action On utiliser la foncton `filter`  
```python nr.filter(device_type="router").filter(building="A"). ```   ou   ```python nr.filter(device_type="router",building="A"). ```  
     
Nous avons donc avec nornir push les confguration Txt créé. (routage, switch et vrrp)   

@Maxime BELLET
@Jeremy METRA

09/05/2022
