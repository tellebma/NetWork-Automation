# TP 2

- Base Jinja2 - <a href="./scripts/create_config.py">createconfig.py</a>  

Creation de fichier data (yaml et json).  
Puis passage dans un render de template et écriture de la configuration dans un fichier txt.  

Mise en situation cas réél (simulation GNS3)

### <a href="./scripts/run_paramiko.py">Paramiko</a>
Fonctionnement assez basic  
- Connexion avec l'equipement  
- envoi de commande.  
- Sauvegarde de la configuration de l'équipement  
  <b>NB:</b>  
Pas de gestion de l'environnement invité de commande (conf t, etc)  

### <a href="./scripts/run_netmiko.py">Netmiko  </a>
Netmiko est assez pratique, simple a utiliser, mais assez basic.
- Envoi de commande en # et en Conf T. (send_command, send_config_set)
- Envoie de fichier de configuration (send_config_from_file)  

###  <a href="./scripts/run_napalm.py">Napalm </a>
Napalm est l'outil le plus complet sur lequel nous avons travaillé.
- Connexion à l'équipement
- Envoi de commande cli et configuration
- Pour les configuration, Il est possible de discard ou de commit les modifications (très pratique) (verifyConf())
- Creation de toutes les backup pour tous les équipements


@Maxime BELLET
@Jeremy METRA

26/04/2022
