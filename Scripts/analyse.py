## Fichier: clever_network/analyse_ip.py
import ipaddress

def analyser_adresse_ip(cidr):
    try:
        reseau = ipaddress.ip_network(cidr, strict=False)
        premiere_octet = int(str(reseau.network_address).split('.')[0])

        if 1 <= premiere_octet <= 126:
            classe = 'A'
        elif 128 <= premiere_octet <= 191:
            classe = 'B'
        elif 192 <= premiere_octet <= 223:
            classe = 'C'
        elif 224 <= premiere_octet <= 239:
            classe = 'D (Multicast)'
        elif 240 <= premiere_octet <= 254:
            classe = 'E (Expérimental)'
        else:
            classe = 'Inconnue'

        infos = {
            "Adresse IP CIDR": cidr,
            "Adresse réseau": str(reseau.network_address),
            "Masque de sous-réseau": str(reseau.netmask),
            "CIDR": f"/{reseau.prefixlen}",
            "Adresse de broadcast": str(reseau.broadcast_address),
            "Nombre total d'adresses": reseau.num_addresses,
            "Nombre d'hôtes valides": reseau.num_addresses - 2 if reseau.num_addresses > 2 else 0,
            "Plage d'hôtes": f"{list(reseau.hosts())[0]} - {list(reseau.hosts())[-1]}" if reseau.num_addresses > 2 else "N/A",
            "IP privée ?": "Oui" if reseau.is_private else "Non",
            "Classe IP": classe
        }

        print("\n Résultat de l’analyse IP :\n")
        for k, v in infos.items():
            print(f"{k:<30} {v}")
        print()

    except ValueError:
        print(" Erreur : Le format CIDR est invalide. Exemple attendu : 192.168.1.0/24")
    except Exception as e:
        print(f" Erreur inconnue : {e}")

