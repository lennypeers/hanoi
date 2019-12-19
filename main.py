import copy
from turtle import *
import pickle
import time
import os.path

############################# PARTIE A ###############################
############################# PARTIE A ###############################
############################# PARTIE A ###############################
############################# PARTIE A ###############################
############################# PARTIE A ###############################
############################# PARTIE A ###############################

# initialisation du palteau de depart
# retourne un plateau avec n disques dans la premiere tour
def init(n):
    plateauini=[[],[],[]]
    tour1=[]
    for var in range(n,0,-1):
        tour1.append(var)
    plateauini[0]=tour1
    return plateauini

#renvoie le nb de disque sur une des tours
def nombre_disques(plateau,numtour):
    return len(plateau[numtour])

#renvoie le num du disque superieur sur une tour donnee
def disque_superieur(plateau,numtour):
    if nombre_disques(plateau,numtour)!=0:
        tour=plateau[numtour]
        return tour[-1]
    else:
        return -1

#donne le numero de la tour ou se trouve le disque cherche
def position_disque(plateau,numdisque):
    for var in range(len(plateau)):
        for var2 in plateau[var]:
            if numdisque==var2:
                return var

#verifie si le deplacement est correct
def verifier_deplacement(plateau,nt1,nt2):
    if (disque_superieur(plateau,nt1)<disque_superieur(plateau,nt2) or disque_superieur(plateau,nt2)==-1) and disque_superieur(plateau,nt1)!=-1:
        return True
    else:
        return False

#verifie si le joueur a gagne
def verifier_victoire(plateau,n):
    if len(plateau[-1])==n:
        return True
    else:
        return False

############################# PARTIE B ###############################
############################# PARTIE B ###############################
############################# PARTIE B ###############################
############################# PARTIE B ###############################
############################# PARTIE B ###############################
############################# PARTIE B ###############################

# permet de se deplacer les disques (qui sont des tortues) sans tracer
def goto_inv(x,y,npen):
    pen[npen].up()
    pen[npen].goto(x,y)
    pen[npen].down()

# dessine un rectangle avec le curseur 0 (curseur dedie au dessin du socle)
def rectangle(base,hauteur):
    pen[0].lt(90)
    pen[0].begin_fill()
    for i in range(4):
        if i%2==0:
            pen[0].fd(hauteur)
        else:
            pen[0].fd(base)
        pen[0].rt(90)
    pen[0].rt(90)
    pen[0].end_fill()

def creerturtle(n):
    # global pour acceder aux curseurs dans tout le programme
    global pen
    pen=[]
    tracer(0)
    # premier curseur sert a dessiner les tours et le socle:
    pen.append(Turtle())
    pen[0].ht()
    #autres curseurs seront les disques eux memes (forme de disque)
    for var in range(1,n+2):
        # on cree n disques
        pen.append(Turtle())
        # on midifie la taille du disque en fonction de son numero
        pen[var].shapesize(height_disk/20,(top_disk_len + (var-1)*2*gap_bw_2disks)/20 ,1)
        # on leve le curseur pour que le disque ne dessine pas
        pen[var].pu()
        # on utilise la forme carre pour le disque
        pen[var].shape("square")
        pen[var].speed(5)
    # fonction auxiliaire permettant de retrouver la couleur de la tourtue
        couleur(var)
    # la tortue n+1 sert a ecrire le nombre de coup actuel
    pen[n+1].ht()
    pen[n+1].color("Black")
    pen[n+1].goto(-width_window/2 +55 , + 160)

def impression_coup(num_coup): #affiche sur l'ecran le nombre de coups
    pen[n+1].clear()
    pen[n+1].write("coup(s): "+str(num_coup), move=False, align="center", font=("Arial", 16, "normal"))

# design: les disques (ou curseurs) pairs et impairs ont deux couleurs distinctes
def couleur(num_tortue):
    if num_tortue%2==0:
        pen[num_tortue].color("#CED640","yellow")
    else:
        pen[num_tortue].color("black","black")

# fonction d'accueil
def launching():
    global width_window,height_window,n
    width_window = 1200
    height_window = 400
    setup( width_window , height_window )
    title("Les tours de Hanoi")
    bgcolor("#fabe0b")
    bgpic("bg.gif")
    n=int(numinput("Nombre de disques", "Avec combien de disques voulez vous jouer?", 10, minval=1, maxval=10000))
    values_texture(n)

# creation des boutons : ce sont des tourtues
def ajoute_boutons():
    global bouton_annuler,bouton_solution,bouton_abandon
    bouton_annuler=Turtle()
    bouton_solution=Turtle()
    bouton_abandon=Turtle()
# on leve les curseurs pour ne rien tracer
    bouton_abandon.up()
    bouton_solution.up()
    bouton_annuler.up()
# on met on place la forme des bouton_solution
    register_shape("abandon.gif")
    register_shape("solution.gif")
    register_shape("annuler.gif")
    bouton_abandon.shape('abandon.gif')
    bouton_solution.shape('solution.gif')
    bouton_annuler.shape('annuler.gif')
# on place les boutons
    bouton_annuler.goto(-width_window/2 + 40 , + 80)
    bouton_abandon.goto(-width_window/2 + 40 ,0)
    bouton_solution.goto(-width_window/2 + 40 , - 80)

#dessine le plateau initial
def dessine_plateau(n):
    #on cree nos n curseurs (ou nos n disques)
    creerturtle(n)
    ajoute_boutons()
    #on dessine le socle
    goto_inv(-width_window*0.5, - height_window*0.5,0)
    pen[0].color("grey")
    rectangle(turtle_width +50 ,height_disk )
    # on dessine les 3 tours
    for i in range(3):
        goto_inv( -turtle_width*0.5 + borders*(1+i) + len_tower/2 -rayon_barre +len_tower*(i)  , -height_window*0.5 + height_disk,0)
        rectangle(diametre_barre,height_disk*(n+1))

def dessine_disque (nd, plateau, n):
    #on cherche les coordonnees du disques
    position_disk_tour = position_disque(plateau,nd)
    temp = plateau[position_disk_tour]
    for i in range(len(temp)):
        if nd==temp[i]:
            position_disk_hauteur=i
    positions=pen[nd].pos()
    #on deplace le curseur du disque suivant le chemin des tours
    goto_inv(positions[0],-height_window*0.5 + height_disk *(n+2),nd)
    goto_inv( -turtle_width*0.5 +borders*(1+position_disk_tour) +len_tower*position_disk_tour +gap_bw_2disks*(n-nd) +(top_disk_len + (nd-1)*2*gap_bw_2disks)/2 , -height_window*0.5 + height_disk *(n+2),nd)
    goto_inv( -turtle_width*0.5 +borders*(1+position_disk_tour) +len_tower*position_disk_tour +gap_bw_2disks*(n-nd) +(top_disk_len + (nd-1)*2*gap_bw_2disks)/2 ,  -height_window*0.5 + height_disk * (1+position_disk_hauteur+0.5) , nd )

def dessine_config(plateau, n):
    #on dessine chaque disque
    tracer(0)
    for e in plateau:
        for i in e:
            dessine_disque(i,plateau,n)
    #on active tracer afin de voir les animations
    impression_coup(num_coup)
    tracer(1.75)

def efface_tout():
    # pour tout effacer il suffit de cacher les tortues
    for var in range(1,n+1):
        pen[var].ht()

# pour avoir la meilleur interface, on doit calculer chaque distance intervant
# dans le design du plateau en fonction du nombre de disque
def values_texture(n):
    #global nous permet d'acceder a toutes les valeurs des mesures dans tout le programme
    global turtle_width, turtle_height, height_disk, borders, len_tower, top_disk_len, gap_bw_2disks,diametre_barre, rayon_barre, num_coup , dico_plateau, couple_coup, plateau
    turtle_width  = width_window -20
    turtle_height = 5*height_window/6 -50
    # la hauteur d'un disque vaut la hauteur de la fenetre
    # divise par n+2 car il y a le socle et le bout supplementaire de la tour
    height_disk = turtle_height / (n+2)
    borders  =  turtle_width / 16
    len_tower = turtle_width / 4
    top_disk_len =  len_tower / n
    # on elimine le cas de division par 0 pour eviter les erreurs (quand n=1)
    if n!=1:
        gap_bw_2disks  =   (len_tower -  top_disk_len)/ (2*(n-1))
    else:
        gap_bw_2disks = 0
    diametre_barre =  top_disk_len / 6
    rayon_barre = diametre_barre / 2
    # initialisation des variables utiles:
    # num_coup note le nombre de coup effectue
    num_coup=0
    # dico_plateau note tous les plateaux en fonction des coups
    dico_plateau={}
    # on initialise le plateau au coup 0 (debut)
    dico_plateau[0]=init(n)
    # couple_coup est une variable globale notant les coup que l'utilisateur pense faire
    couple_coup=[]
    # on initialise le plateau
    plateau=init(n)

############################# NEW PARTIE C ###############################
############################# NEW PARTIE C ###############################
############################# NEW PARTIE C ###############################
############################# NEW PARTIE C ###############################
############################# NEW PARTIE C ###############################
############################# NEW PARTIE C ###############################

#verifie si le disque est deplacable inclu tour non vide //voir si possible d'utiliser verifier_deplacement
def disquesup_deplacable(plateau,numtour):
    if nombre_disques(plateau, numtour)==0:
        return False
    elif disque_superieur(plateau,numtour)>=disque_superieur(plateau,0):
        if disque_superieur(plateau,0)!=-1:
            if disque_superieur(plateau,numtour)>=disque_superieur(plateau,1) :
                if disque_superieur(plateau,1)!=-1:
                    if disque_superieur(plateau,numtour)>=disque_superieur(plateau,2) :
                        if disque_superieur(plateau,2)!=-1:
                            return False
    return True

def jouer_un_coup2(plateau,n,coord):
    disque=disque_superieur(plateau,coord[0])
    #on update la liste en fonction du deplacement
    for var in plateau:
        if disque in var:
            var.remove(disque)
    plateau[coord[1]].append(disque)
    #redessine le disque sur la nouvelle tour
    dessine_disque(disque, plateau, n)
    return plateau

# fonction qui renvoie le numero de la tour lors d'un click
def zoneclick(x,y):
    if y< abs(height_window-len_tower ) :
        if (-width_window/2 + borders +20) <x<(-width_window/2 + borders + len_tower):
            return 0
        elif x> (borders + len_tower/2):
            return 2
        elif x>(-width_window/2 + borders + len_tower):
            return 1
        else:
            return 5 # pour eviter les bugs quand on click dehors
    else:
        return 5 # pour eviter les bugs quand on click dehors

def click(x,y):
    n_tour=zoneclick(x,y) #on determine quelle tour a ete cliquee
    global couple_coup, num_coup, dico_plateau, plateau
    muet() # on coupe l'ecoute des clicks
    if 0<=n_tour<=2:
        # on ajoute la tour au couple de coup
        couple_coup.append(n_tour)
        if len(couple_coup)==1:
            # si la tour n'est pas valide, le couple est initialise a zero
            if not disquesup_deplacable(plateau,n_tour):
                couple_coup=[]
            else:
            # change la couleur du disque selectionne si le disque est deplacable
                pen[disque_superieur(plateau,couple_coup[0])].color("red")
        elif len(couple_coup)==2:
            if verifier_deplacement(plateau,couple_coup[0],couple_coup[1]):
            # on retablit la couleur du disque selectionne
                couleur(disque_superieur(plateau,couple_coup[0]))
                jouer_un_coup2(plateau,n,couple_coup)
                num_coup+=1
                dico_plateau[num_coup]=copy.deepcopy(plateau)
                impression_coup(num_coup)
            else:
                couleur(disque_superieur(plateau,couple_coup[0]))
            couple_coup=[]
    if verifier_victoire(plateau,n):
        nom_joueur=textinput("Victoire","Bravo! Vous avez gagne. Entrez votre nom pour le classement: ")
        saveJeu(nom_joueur, n, num_coup)
        finish() # le jeu est fini
    ecoute() # on retablit l'ecoute des clicks

# fonction permettant d'abandonner
def abandon(x,y): # recoit x,y comme parametres car les onclicks les exigent
    muet() # on coupe l'ecoute des clicks
    reponse=textinput("Abandon", "Etes-vous sur d'abandonner? (oui/non)")
    if reponse=="oui":
        # on demande a l'utilisateur si veut voir la solution
        solution(x,y)
        finish()
    ecoute() # on retablit l'ecoute des clicks

# fonction jouant la solution optimale
def solution(x,y): # recoit x,y comme parametres car les onclicks les exigent
    muet()
    reponse=textinput("Solution", "Voulez-vous affichez la solution optimale? (oui/non)")
    if reponse=="oui":
        # on reinitialise toutes les variables pour jouer
        plateau=init(n)
        values_texture(n)
        # on stock les solutions dans la variable sol
        sol=hanoi(n,0,2,1)
        dessine_config(plateau,n)
        num_coup=0
        impression_coup(num_coup)
        # on joue les couples solution
        for solu in sol:
            jouer_un_coup2(plateau,n,solu)
            num_coup+=1
            impression_coup(num_coup)
        finish()
    else:
        ecoute()

# permet d'annuler un coup
def annulation(x,y): # recoit x,y comme parametres car les onclicks les exigent
    muet()
    global couple_coup, num_coup, dico_plateau, plateau
    if len(couple_coup)==1:
        couleur(disque_superieur(plateau,couple_coup[0]))
    if num_coup>0:
        plateau=annuler_dernier_coup(dico_plateau,num_coup)
        num_coup-=1
        impression_coup(num_coup)
    couple_coup=[]
    ecoute()

def finish(): # fonction appellee quand le jeu se termine
    muet()
    # on affiche le classement
    tableauBestScores("fichier_score",n)
    onscreenclick(replay) # on redemande si il veut rejouer
    mainloop()

def replay(x,y):
    reponse=textinput("Nouvelle partie","Voulez-vous rejouer? (oui/non)")
    if reponse=="oui":
        pen[n+1].clear()
        pen[0].clear()
        classement.ht()
        efface_tout()
        main()
    else:
        TurtleScreen._RUNNING=True
        bye()


def boucle_jeu(plateau,n):
    ecoute()
    listen()
    mainloop()

# pour eviter les bugs on doit couper l'ecoute des clicks quand une
# action est en train d'etre effectuee
def ecoute():
    onscreenclick(click)
    bouton_abandon.onclick(abandon)
    bouton_solution.onclick(solution)
    bouton_annuler.onclick(annulation)

def muet():
    onscreenclick(None)
    bouton_abandon.onclick(None)
    bouton_solution.onclick(None)
    bouton_annuler.onclick(None)

############################# PARTIE D ###############################
############################# PARTIE D ###############################
############################# PARTIE D ###############################
############################# PARTIE D ###############################
############################# PARTIE D ###############################
############################# PARTIE D ###############################

# renvoie le dernier coup joue sous la forme d'une paire(liste) a partir
# d'un numero de coup turn
def dernier_coup(dico_plateau,turn):
    der_coup_joue= [0,0]
    for v1 in range(len(dico_plateau[turn-1])) :
        if len(dico_plateau[turn-1][v1])>len(dico_plateau[turn][v1]):
            der_coup_joue[0]=v1
        elif len(dico_plateau[turn-1][v1])<len(dico_plateau[turn][v1]):
            der_coup_joue[-1]=v1
    return der_coup_joue

# annule le dernier coup n, update la fenetre graphique et return
# la config du plateau au coup n-1
def annuler_dernier_coup(dico_plateau,turn):
    #update graphisme
    der_coup=dernier_coup(dico_plateau,turn)
    plateau=copy.deepcopy(dico_plateau[turn-1])
    dessine_disque(disque_superieur(plateau,der_coup[0]), plateau, n)
    del dico_plateau[turn]
    return plateau

############################# PARTIE E ###############################
############################# PARTIE E ###############################
############################# PARTIE E ###############################
############################# PARTIE E ###############################
############################# PARTIE E ###############################
############################# PARTIE E ###############################

def saveJeu(nom_joueur, nb_disque, nb_coup):
    #cree le fichier score si pas sur l'ordi
    if not (os.path.exists("fichierscores")) :
        pickle.dump({},open('fichierscores','wb'))
    #recupere la date de la partie
    t = time.localtime()
    date = str(t[2])+"/"+str(t[1])+"/"+str(t[0])
    fichier_score=pickle.load(open('fichierscores','rb'))
    #fichier_score={nb_disque:{nom_joueur:[nb_coup,date]}}
    if nb_disque in fichier_score:
        if nom_joueur in fichier_score[nb_disque]:

            if nb_coup < fichier_score[nb_disque][nom_joueur][0]:
                fichier_score[nb_disque][nom_joueur]=[nb_coup,date]
        else :
            fichier_score[nb_disque][nom_joueur]=[nb_coup,date]
    else:
        fichier_score[nb_disque]={nom_joueur:[nb_coup,date]}
    pickle.dump(fichier_score,open('fichierscores','wb'))

def tableauBestScores(fichier_score,n):
    # classement est une tortue servant de decors
    global classement # on pourra cacher classement dans la partie suivante
    classement=Turtle()
    classement.pu()
    register_shape("leaderboard.gif")
    classement.shape("leaderboard.gif")
    # si le fichier score n'existe pas, on le cree
    if not (os.path.exists("fichierscores")) :
        pickle.dump({},open('fichierscores','wb'))
    fichier_score=pickle.load(open('fichierscores','rb'))
    # si aucun score n'existe pour la valeur n:
    if not n in fichier_score : # on utilisera la tortue n+1 pour ecrire
        pen[n+1].goto(0,0)
        pen[n+1].write("Classement vide", move=False, align="center", font=("Arial", 18, "normal"))
    else: # il faut classer les joueurs
        if n in fichier_score:
            list_score= fichier_score[n].items()
            list_score= sorted(list_score, key= lambda x :  x[1][0] )
            ligne=0
            for elements in list_score:
                #print(elements[0],elements[1][0],elements[1][1])
                nomjoueur=elements[0]
                nbcoup=elements[1][0]
                date=elements[1][1]
                pen[n+1].goto(-0,+90-25*ligne)
                pen[n+1].write("#"+str(ligne+1)+" "+nomjoueur+" avec "+str(nbcoup)+" coup(s) le "+date  ,move=False,align="center",font=("Arial",18,"normal"))
                ligne+=1


############################# PARTIE F ###############################
############################# PARTIE F ###############################
############################# PARTIE F ###############################
############################# PARTIE F ###############################
############################# PARTIE F ###############################
############################# PARTIE F ###############################

def cree_sol(n,a,c,b,solution):
    """ Cree la solution (stockee dans la liste solution) des couples de
mouvements, pour n disques allant de la tour a, pour  arriver a la tour c,
en utilisant la tour intermediaire b. """
    # dans le cas ou on a un seul disque a deplacer, on a deux coups:
    if n==1:
        solution.append([a,c])
    # deplacer n disques revient a deplacer n-1 disques vers la tour auxiliaire,
    # deplacer le disque de la base vers la tour finale et deplacer n-1 disques
    # vers la tour finale :
    else:
        # on appelle la fonction elle meme mais avec des les tours echanges:
        # ici: a est la tour de dep, b la finale et c la tour auxiliaire
        cree_sol(n-1,a,b,c,solution)
        solution.append([a,c])
        cree_sol(n-1,b,c,a,solution)

def hanoi(n,a="0",c="2",b="1"):
    # il faut une fonction externe pour stocker les solutions car la fonction
    # generatrice s'appelle elle meme
    liste_solution=[]
    cree_sol(n,a,c,b,liste_solution)
    return liste_solution

############################# TEST ###############################
############################# TEST ###############################
############################# TEST ###############################
############################# TEST ###############################
############################# TEST ###############################
############################# TEST ###############################
def main():
    launching()
    dessine_plateau(n)
    dessine_config(plateau,n)
    boucle_jeu(plateau,n)

if __name__ == '__main__':
    main()
