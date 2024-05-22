#====================================================================================
# Author : Clelia Durandet
# Date : 2024/05/22
# PROGRAMME: JEU DU PENDU
#====================================================================================
import random

# FONCTION 1 : Choix du mot au hasard dans la liste fournie
def choisir_mot():
    choix_fichier= input('Voulez-vous fournir votre propre fichier de mots: répondez oui ou non: ')
    if choix_fichier=='oui':
        chemin_choisi= input('Entrez le lien d''accès de votre fichier, attention il est possible que vous deviez mettre 2 anti slash à chaque slash du chemin pour que ça fonctionne : ')
        fichier_utilisateur= open(chemin_choisi, 'r', encoding='utf-8')
        texte = fichier_utilisateur.readlines()
    else:
        fichier_texte = open('mots_pendu.txt', 'r', encoding='utf-8')
        texte = fichier_texte.readlines()
    print(texte)
    mots = []
    for i in texte:
        mots.append(i[:-1]) # on enlève le \n qui sépare les mots
    return random.choice(mots) # renvoie un mot au hasard


mot_choisi=choisir_mot()

# FONCTION 2: Crée une liste avec les lettres du mot choisi dans l'ordre
def liste_lettres_mot(mot_choisi):
    lettres_du_mot=[]
    for l in mot_choisi:
        lettres_du_mot.append(l) # ajoute chaque lettre du mot dans l'ordre dans une liste
    #print(lettres_du_mot)
    return(lettres_du_mot)

print(liste_lettres_mot(mot_choisi))

lettres_du_mot= liste_lettres_mot(mot_choisi)

# FONCTION 3: Ecris la liste des lettres du mot sans les caractères spéciaux pour faciliter le jeu
def ecrire_equivalence (lettres_du_mot):
    lettres_du_mot_equivalence=[]
    caracteres_speciaux=['é','è','ê','ë','à','â','û','î','ô']
    equivalents=['e','e','e','e','a','a','u','i','o']
    for i in range(len(caracteres_speciaux)):
        for j in range(len(lettres_du_mot)): # parcourt chaque lettre du mot afin de remplacer celles qui ont des caractères spéciaux
            if lettres_du_mot[j]==caracteres_speciaux[i]:
                lettres_du_mot[j]=equivalents[i]
    lettres_du_mot_equivalence=lettres_du_mot
    return lettres_du_mot_equivalence

print(ecrire_equivalence(lettres_du_mot))