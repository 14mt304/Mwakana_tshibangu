from netmiko import ConnectHandler

# Détails de connexion au routeur Cisco NX-OS
cisco1 = {
    "device_type": "cisco_nxos",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
}

# Fonction pour se connecter au routeur, exécuter une commande et afficher le résultat
def execute_command(device, command):
    try:
        # Connexion SSH au routeur
        net_connect = ConnectHandler(**device)
        
        # Exécution de la commande et récupération de la sortie
        output = net_connect.send_command(command)
        
        # Affichage de la sortie de la commande
        print(f"Résultat de la commande '{command}':")
        print(output)

    except Exception as e:
        print(f"Erreur lors de la connexion ou de l'exécution de la commande : {e}")

    finally:
        # Déconnexion propre du routeur
        net_connect.disconnect()

# Liste des commandes à exécuter
commands = [
    "show version",
    "show ip interface brief",
    "show ip route"
]

# Exécution des commandes et affichage des résultats
for command in commands:
    execute_command(cisco1, command)
