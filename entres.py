def entres_utilisateur() -> (int, str, int):
    entre_num_1 = input("Premier nomber: ")
    entre_operator = input("Opérateur: ")
    entre_num_2 = input("Deuxiement nombre: ")
    return (entre_num_1, entre_operator, entre_num_2)


def test_entres(num_1, operator, num_2):
    while True:
        if num_1.isdigit():
            num_1_ok = int(num_1)
        elif num_1.replace(".", "").isdigit():
            num_1_ok = float(num_1)
        else:
            num_1 = input("Votre premier nombre n'est pas une entrée valide : ")
            continue

        if (
            operator != "+"
            and operator != "-"
            and operator != "/"
            and operator != "*"
            and operator != "("
            and operator != ")"
        ):
            operator = input("Votre opérateur n'est pas une entrée valide :")
            continue
        else:
            operator_ok = operator
    
        if num_2.isnumeric():
            num_2_ok = int(num_2)
        elif num_2.replace(".", "").isdigit():
            num_2_ok = float(num_2)
        else:
            num_2 = input("Votre deuxième nombre n'est pas une entrée valide :")
            continue

        return (num_1_ok, operator_ok, num_2_ok)
    
# def full_calcul():
#     enter_autorised = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "/", "*", "(", ")", "%", " ", "."]

#     while True:
#         complete_calcul = input("Veuillez entrer votre calcul complet : ")

#         if all(char in enter_autorised for char in complete_calcul):
#             break 
#         else:
#             print("Caractères non autorisés. Veuillez entrer un calcul avec des caractères autorisés.")
#     return(complete_calcul)