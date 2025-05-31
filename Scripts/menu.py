from .analyse import analyser_adresse_ip
from .decoupage import decouper_reseau

def lancer_menu():
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
