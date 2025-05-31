## Fichier: clever_network/decoupage.py
import ipaddress
import math

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
