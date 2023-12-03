from entres import *
from calcul import *
from historique import *

autorised_char =["o", "n"]
filename = 'historique.json'
save_print = []

while True:
    entre = entres_utilisateur()
    num_1 = entre[0]
    operator = entre[1]
    num_2 = entre[2]

    test = test_entres(num_1, operator, num_2)
    num_1_ok = test[0]
    operator_ok = test[1]
    num_2_ok = test[2]

    calcul_made = calcul(num_1_ok, operator_ok, num_2_ok)
    print(f"Le résultat est {calcul_made}")
    
    save_print = save_print + [f"Le resultat de {str(num_1_ok)} {operator_ok} {str(num_2_ok)} est {str(calcul_made)}"]
    save(save_print, filename)

    histo = input("Voulez-vous afficher l'historique ? (o/n): ")
    if histo not in autorised_char:
        histo = input("Entrée non autorisé. Voulez-vous faire un autre calcul ? (o/n): ")
    if histo == "o":
        afficher_historique(filename)
    del_histo = input("Voulez vous supprimer l'historique ? (o/n): ")
    if del_histo not in autorised_char:
        del_histo = input("Entrée non autorisé. Voulez-vous faire un autre calcul ? (o/n): ")
    if del_histo == 'o':    
        supprimer_historique(filename)
        
