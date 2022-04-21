def print_grid(grid):
    print("     0)  1)  2)")
    print("   -------------")
    print("0)", end='')
    for i in range(3):
        print(" | "+str(grid[i]), end='')
    print(" |")
    print("   -------------")
    print("1)", end='')
    for i in range(3):
        print(" | "+str(grid[i+3]), end='')
    print(" |")
    print("   -------------")
    print("2)", end='')
    for i in range(3):
        print(" | "+str(grid[i+6]), end='')
    print(" |")
    print("   -------------")
 
 
def tour(grid, joueur):
    print("C'est le tour du joueur "+str(joueur))
    colonne=input("Entrez le numero de la colonne : ")
    ligne=input("Entrez le numero de la ligne : ")
    print("Vous avez joué la case ("+colonne+","+ligne+")")
    while grid[int(colonne)+int(ligne)*3]!=" ":
        print_grid(grid)
        print("Cette case est deja jouée ! Saisissez une autre case svp !")
        colonne=input("Entrez le numero de la colonne : ")
        ligne=input("Entrez le numero de la ligne : ")
        print("Vous avez joué la case ("+colonne+","+ligne+")")
 
    if joueur==1 :
        grid[int(colonne)+int(ligne)*3]="X"
    if joueur==2 :
        grid[int(colonne)+int(ligne)*3]="O"
    print_grid(grid)
 
def check_win(grid):
    if (grid[0]==grid[1]) and (grid[0]==grid[2]) and (grid[0]!=" "):
        return 1
    if (grid[3]==grid[4]) and (grid[3]==grid[5]) and (grid[3]!=" "):
        return 1
    if (grid[6]==grid[7]) and (grid[6]==grid[8]) and (grid[6]!=" "):
        return 1
    if (grid[0]==grid[3]) and (grid[0]==grid[6]) and (grid[0]!=" "):
        return 1
    if (grid[1]==grid[4]) and (grid[1]==grid[7]) and (grid[1]!=" "):
        return 1
    if (grid[2]==grid[5]) and (grid[2]==grid[8]) and (grid[2]!=" "):
        return 1
    if (grid[0]==grid[4]) and (grid[0]==grid[8]) and (grid[0]!=" "):
        return 1
    if (grid[2]==grid[4]) and (grid[2]==grid[6]) and (grid[2]!=" "):
        return 1
 
 
def equality(grid):
    for i in range(9):
        if grid[i]==" ":
            return 0
    return 1

def main(): 
        player=1
        print("Le joueur 1 possède les X. Le joueur 2 possède les O")
        grid=[" "," "," "," "," "," "," "," "," "]
        print_grid(grid)
        win=0
        while win==0:
            tour(grid, player)
            if check_win(grid):
                print("Le joueur "+str(player)+" remporte la partie")
                win=1
            else:
                if equality(grid):
                    print("Plus de place ! Match nul !")
                    win=1
            if player==1:
                player=2
            else:
                player=1
main()
