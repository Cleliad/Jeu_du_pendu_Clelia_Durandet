#====================================================================================
# Author : Clelia Durandet
# Date : 2024/05/23
# PROGRAMME: JEU DU PENDU
#====================================================================================
import random
import string


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
    mots = []
    for i in texte:
        mots.append(i[:-1])
    return random.choice(mots)

# FONCTION 2: Crée une liste avec les lettres du mot choisi dans l'ordre
def liste_lettres_mot(mot_choisi):
    lettres_du_mot=[]
    for l in mot_choisi:
        lettres_du_mot.append(l) # ajoute chaque lettre du mot dans l'ordre dans une liste
    #print(lettres_du_mot)
    return(lettres_du_mot)


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

# FONCTION 4: Teste si la lettre est présente dans le mot à trouver et l'écrit à la place du '_'
def tester_lettres(lettre, mot_instant, lettres_du_mot_equivalence):
    trouve = 0 # permet de boucler pour trouver les occurences (s'il y en a dans le mot)
    for i in range(len(mot_instant)):
        if lettres_du_mot_equivalence[i]==lettre:
            mot_instant[i] = lettre
            trouve +=1
    if trouve >0:
        return True
    else:
        return False

# FONCTION 5: Permet de relancer une partie du jeu si le joueur le souhaite
def jouer_a_nouveau():
    print('Veux-tu jouer à nouveau?')
    choix = input('Répondre: oui ou non ')
    if choix == 'oui':
        jouer()
        return True
    else:
        print('LE JEU EST FINI, A BIENTOT')
        return False

# FONCTION 6: Permet de donner un indice si c'est la dernière chance du joueur: renvoit une lettre qui n'est pas présente dans le mot
def donner_indice(liste_alphabet,lettres_du_mot_equivalence,liste_lettres_test):
    lettres_du_mot_equivalence.extend(liste_lettres_test) # on concatène les deux listes pour avoir toutes les lettres utilisées
    for i in range(len(lettres_du_mot_equivalence)):
        if lettres_du_mot_equivalence[i] in liste_alphabet:
            liste_alphabet.remove(lettres_du_mot_equivalence[i]) # on retranche les lettres utilisées à la liste alphabétique
            indice = random.choice(liste_alphabet)
            liste_lettres_test.append(indice) # on renvoit une lettre au hasard parmi celles qui ne sont pas dans le mot et qui n'ont pas été testées
            return (indice)


# FONCTION PRINCIPALE: JOUER
def jouer():

    # Initialisation des variables
    liste_alphabet = list(string.ascii_lowercase)  # Liste des lettres de l'alphabet en minuscules
    print('''Vous vous appretez à commencer une partie de pendu, vous avez 6 chances !''')
    print('Consignes: Vous n''avez pas besoin de préciser les accents et caractères spéciaux quand vous entrez les lettres (minuscules)')
    num_indice=0 # nombre d'indice donné (le jeu ne donne qu'un seul indice par partie quand il reste 1 chance)
    mot_choisi = choisir_mot() # mot à trouver
    lettres_du_mot = liste_lettres_mot(mot_choisi) # liste des lettres du mot à trouver
    longueur = len(lettres_du_mot) # nombre de lettre du mot à trouver
    lettres_du_mot_equivalence = ecrire_equivalence(lettres_du_mot) # liste des lettres du mot à trouver sans les caractères speciaux
    underscores = '_'
    mot_instant = [underscores for j in range(longueur)]  # initialisation du mot avec les tirets
    chance=6 # initialisation du nombre de chance
    compteur = mot_instant.count('_') # compte le nombre de lettre qu'il reste à trouver
    #print(mot_choisi)
    liste_lettres_test = [] # liste des lettres déjà testées par l'utilisateur
    while compteur!=0:

        # Initialisation du jeu
        print('Le mot à deviner est:', mot_instant) # affiche le mot à deviner avec les '_'
        print('Les lettres testées sont:', liste_lettres_test) # affiche la liste des lettres testées par le joueur
        lettre = str(input('Entrez une lettre: ')) # demande à l'utilisateur de renseigner une lettre
        print(lettre)

        # Teste si la lettre est dans le mot et actualise le compteur
        if tester_lettres(lettre, mot_instant, lettres_du_mot_equivalence):
            print('BIEN JOUÉ, LA LETTRE EST DANS LE MOT !')
            compteur=mot_instant.count('_')

        # Si la lettre n'est pas dans le mot, le nombre de chance diminue et la lettre est ajoutée à la liste des lettres testées
        else:
            chance -= 1
            print('Mince, essais à nouveau \nIL TE RESTE', chance, 'CHANCES')
            liste_lettres_test.append(lettre)

        # S'il ne reste qu'une chance au joueur et qu'il n'a pas encore trouvé le mot, il peut avoir l'indice (un seul par partie)
        if chance == 1 and num_indice == 0:
            print('Ceci est ta derniere tentavive ! \nVeux-tu un indice ?')
            reponse = input('Répondre: oui ou non :')

            # Le joueur accepte d'avoir l'indice
            if reponse == 'oui':
                num_indice+=1
                lettre_pas_dans_le_mot= donner_indice(liste_alphabet,lettres_du_mot_equivalence,liste_lettres_test)
                print('VOICI UN INDICE:', lettre_pas_dans_le_mot, "n'est pas dans le mot à trouver")

        # Le joueur n'a pas trouvé le mot, il perd la partie !
        elif chance == 0:
            compteur=0
            print('DOMMAGE TU AS PERDU, LE MOT ÉTAIT:', mot_choisi )
            jouer_a_nouveau()

    # Le joueur trouve le mot avec les 6 chances données, il gagne !
    if chance>0:
        print('BIEN JOUÉ TU AS GAGNÉ, LE MOT ÉTAIT:', mot_choisi)
        jouer_a_nouveau()

# APPEL DE LA FONCTION
jouer()



