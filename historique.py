def historique(save_calcul):
    autorised_char =["o", "n"]
    continue_break = input("Voulez-vous faire un autre calcul ? (o/n): ")
    if continue_break not in autorised_char:
        continue_break = input("Entrée non autorisé. Voulez-vous faire un autre calcul ? (o/n): ")
    elif continue_break == "n":
        histo = input("Voulez-vous afficher l'historique ? (o/n): ")
        if histo not in autorised_char:
            histo = input("Entrée non autorisé. Voulez-vous faire un autre calcul ? (o/n): ")
        elif histo == "o":
            print("Calculs effectués :")
            for calc in save_calcul:
                print(calc)
            supprimer = input("Voulez vous supprimer l'historique? (o/n) :")
            if supprimer not in autorised_char:
                supprimer = input("Entrée non autorisé. Voulez-vous faire un autre calcul ? (o/n): ")
            elif supprimer == "o":
                save_calcul.clear()