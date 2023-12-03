import json
import os

def save(save_calcul, filename):
    with open(filename, 'w') as json_file:
        json.dump(save_calcul, json_file)
        json_file.write('\n')
        print(f"L'historique a été ajouté au fichier {filename}.")

def afficher_historique(filename):
    try:
        with open(filename, 'r') as json_file:
            historique_data = json.load(json_file)
            print("Historique des calculs :")
            for entry in historique_data:
                print(entry)
    except FileNotFoundError:
        print(f"Le fichier {filename} n'existe pas.")
    except json.JSONDecodeError:
        print(f"Erreur lors de la lecture du fichier {filename}. Le fichier JSON est mal formé.")

def supprimer_historique(filename):
    try:
        os.remove(filename)
        print(f"L'historique dans le fichier {filename} a été supprimé.")
    except FileNotFoundError:
        print(f"Le fichier {filename} n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la suppression de l'historique : {e}")