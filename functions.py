def croisement(ile1, ile2, ile3, ile4):
    """
    ile_x = (i_x, j_x) # couple
    cette fonction retourne Vrai si: Le Pont (ile1, ile2) se croise avec le Pont (ile3, ile4)
    """
    i1,j1 = ile1
    i2,j2 = ile2
    i3,j3 = ile3
    i4,j4 = ile4

    if ile1 == ile3 or ile1 == ile4 or ile2 == ile3 or ile2 == ile4:
        return False                      
    
    if i1 == i2 and j1 != j2: # (ile1, il2) est horizental et (ile3, ile4) est vertical
        if (j3 > j1 and j3 < j2) or (j3 > j2 and j3 < j1): 
            return True
        else:
            return False
        
    elif j1 == j2 and i1 != i2: # (ile1, il2) est vertical et (ile3, ile4) est horizental
        if (i3 > i1 and i3 < i2) or (i3 > i2 and i3 < i1):
            return True
        else: 
            return False
        
    else:
        return False
