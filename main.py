from entres import *
from calcul import *
from historique import *

save_calcul = []

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
    
    save_print = str(num_1_ok) + " " + " " + operator_ok + " " + str(num_2_ok) + " = " + str(calcul_made) 

    save_calcul.append(save_print)

    historique(save_calcul)
