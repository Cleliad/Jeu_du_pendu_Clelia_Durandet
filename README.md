Ce programme vous permet de jouer au "jeu du pendu" avec des mots écrits en français, en lettres minuscules et sans caractères spéciaux.

# BUT DU JEU: 
Trouver le mot en testant des lettres à chaque manche. 
Quand vous lancez le script, un mot sera choisi au hasard parmi la liste des mots donnés.
Une liste des lettres contenues dans ce mot sera créée puis mise à jour pour remplacer les caractères spéciaux par leur équivalents afin de simplifier le jeu.
Le joueur aura accès à chaque manche au mot écrit sous forme de '_' qui seront remplacés au fur et à mesure qu'il trouve les lettres. 

# ATTENTION:
Pour plus de lisibilité dans la console, j'utilise le package colorama qui permet d'écrire les messages/commentaires de la console en couleur.
Voici la démarche pour l'installer avant de lancer le programme:
- clique sur Files => Settings
- Dans le menu déroulant à gauche, clique sur le projet ou tu enregistres le code, puis sur 'Python interpreter'
- dans le tableau avec les packages, clique sur la croix en haut à gauche
- dans la barre de recherche tape colorama et clique sur le package nommé "colorama" puis sur 'Install Package'
  
# Programme: 
Le script est composé de 6 fonctions annexes qui sont toutes utilisées dans une fonction principale (jouer) qui permet de lancer le jeu. 

Ces fonctions sont les suivantes:
- choisir_mot: pour choisir un mot au hasard dans la liste des mots donnée, l'utilisateur peut fournir sa propre liste de mots ou bien utilisées celle par défault.
  Si l'utilisateur fournit son fichier, il doit indiquer le chemin complet pour y accéder et mettre des doubles \\\ (ex: C:\\\Users\\\Dossier\\\nom_fichier.txt)
- liste_lettres_mot: pour créer une liste contenant toutes les lettres du mot dans le bon ordre
- ecrire_equivalence: pour créer la liste des lettres du mot sans les caractères spéciaux pour faciliter le jeu
- tester_lettres: pour tester si la lettre est présente dans le mot à trouver et l'écrire à la place du '_'
- jouer_a_nouveau: pour relancer une partie du jeu si le joueur le souhaite
- donner_indice: pour donner un indice si c'est la dernière chance du joueur: renvoit une lettre qui n'est pas présente dans le mot

Déroulement du jeu (fonction jouer()): 
Il y a 6 chances au départ. 
Tant que les lettres entrées par l'utilisateur sont dans le mot à deviner, le nombre de chance reste intact. 
En revanche, si la lettre n'est pas dans le mot, le nombre de chance diminue de 1. 
Les lettres présentes plusieurs fois dans le même mot seront toutes ajoutées en une seule fois. 
A chaque manche, le joueur a accès à une liste des lettres qu'il a déjà testées afin de ne pas se répéter. 
Lorsqu'il ne reste qu'une seule chance au joueur, le programme lui demande s'il veut un indice. 
L'indice proposé sera une lettre qui n'est pas contenue dans le mot. L'utilisateur peut refuser cet indice. 
L'indice ne pourra être donné qu'une seule fois dans la partie lorsqu'il ne reste qu'une seule chance. La lettre donnée en indice s'ajoute à la liste des lettres testées. 
Le joueur gagne s'il trouve le mot complet avant que le nombre de chance soit nul. 
A la fin de la partie le joueur peut soit rejouer soit quitter le jeu.

  
