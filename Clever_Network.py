import ipaddress
import math
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

def decouper_reseau(cidr, nb_sous_reseaux=None, nb_hotes=None):
    try:
        reseau = ipaddress.ip_network(cidr, strict=False)
        print(f"\n Découpage du réseau {reseau} :\n")

        if nb_sous_reseaux:
            nouveaux_sous_reseaux = list(reseau.subnets(prefixlen_diff=math.ceil(math.log2(nb_sous_reseaux))))
            for i, sr in enumerate(nouveaux_sous_reseaux[:nb_sous_reseaux]):
                print(f"Sous-réseau {i+1}: {sr}")

        elif nb_hotes:
            bits_hotes = math.ceil(math.log2(nb_hotes + 2))
            prefix = 32 - bits_hotes
            if prefix < reseau.prefixlen:
                print(" Impossible d’avoir autant d’hôtes dans ce réseau.")
                return
            sous_reseaux = list(reseau.subnets(new_prefix=prefix))
            for i, sr in enumerate(sous_reseaux):
                print(f"Sous-réseau {i+1}: {sr} ({sr.num_addresses - 2} hôtes valides)")

        else:
            print(" Spécifie soit le nombre de sous-réseaux, soit le nombre d’hôtes.")

    except ValueError:
        print(" Erreur : Le format CIDR est invalide. Exemple attendu : 192.168.1.0/24")
    except Exception as e:
        print(f" Erreur inconnue : {e}")

def menu():
    while True:
        print("\n=====================================")
        print("   OUTIL RÉSEAU - CLEVER_NETWORK")
        print("=====================================")
        print("1. Analyser une adresse IP")
        print("2. Découper en sous-réseaux")
        print("3. Quitter")
        choix = input("\n Choix : ").strip()

        if choix == "1":
            cidr = input(" Entrez une adresse IP au format CIDR (ex: 192.168.1.0/24) : ").strip()
            analyser_adresse_ip(cidr)

        elif choix == "2":
            cidr = input(" Entrez une adresse IP au format CIDR (ex: 192.168.1.0/24) : ").strip()
            mode = input(" Découper par (1) nombre de sous-réseaux ou (2) nombre d’hôtes ? : ").strip()

            if mode == "1":
                try:
                    n = int(input(" Nombre de sous-réseaux souhaités : ").strip())
                    if n > 0:
                        decouper_reseau(cidr, nb_sous_reseaux=n)
                    else:
                        print(" Le nombre doit être supérieur à 0.")
                except ValueError:
                    print(" Entrée invalide. Veuillez entrer un nombre entier.")

            elif mode == "2":
                try:
                    h = int(input(" Nombre d’hôtes souhaités par sous-réseau : ").strip())
                    if h > 0:
                        decouper_reseau(cidr, nb_hotes=h)
                    else:
                        print(" Le nombre doit être supérieur à 0.")
                except ValueError:
                    print(" Entrée invalide. Veuillez entrer un nombre entier.")
            else:
                print(" Option invalide. Choisis 1 ou 2.")

        elif choix == "3":
            print("\n Merci d’avoir utilisé l’outil CLEVER.Network. À bientôt et reste connecté 💻 !")
            break

        else:
            print(" Choix invalide. Réessaie avec 1, 2 ou 3.")


if __name__ == "__main__":
    menu()
