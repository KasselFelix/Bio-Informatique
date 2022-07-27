from itertools import product
import random
nuc = ('A', 'C', 'G', 'T')
k=7
reLow=5
def removeLowComplexePair(motifs):
    """
    Eleve les motifs peu complexe 
    entrée motifs: liste de motifs 
    sortie validMotif: liste de motifs filtré
    """
    validMotif = []
    for mo in motifs:
        k=0
        cpt=0
        for i in range(1,len (mo)-reLow+2):
            k=1
            cpt=1
            while( cpt/2<=2 and k<=reLow  ):
                if i+k-1<len(mo) and mo[i+k-2]==mo[i+k-1]:
                    k+=1
                elif i+cpt<len(mo) and mo[i+cpt-2]==mo[i+cpt]:
                    cpt+=1
                else:
                    break  
            if k>=reLow or cpt/2>=2:#repetition de lettres superieures a m
                break #motif suivant
        if k<reLow and cpt/2<2:#si aucune rep
            validMotif.append(mo) #add
            
    return validMotif


#Genere tous les K-mers de taille K ayant de AAA... à TTT...
allkmers = product(nuc, repeat=k)
kmers=["".join(k) for k in list(allkmers)]
print(len(kmers))


#Enlever les motifs peu complexe
kmersValid = removeLowComplexePair(kmers)
print (len(kmersValid))

print('####################################################')

k=7

n=80


def getRandomFixePositions(k, n):
    """
    Genere une projection de k vers n
    entrée k: nombre de positions du motif original
    entrée n: nombre de positions choisi pour la projection 
    sortie projection: liste de positions choisi aléatoirement
    """
    projection = []
    while len(projection) != n:
        print(projection)
        i = random.randint(0, k-1)
        if not i in projection:
            projection.append (i)
    projection.sort()
    return projection

lR = getRandomFixePositions(7, 4)
print (lR)


def generateKey(positions, motif):
    """
    extrait les caractères du motif et génère la cle de la projection
    entrée positions : liste de positions qui represent la projection
    entrée motif : motif de taille k
    sortie cle : cle de la projection
    """
    return "".join(motif[positions[i]] for i in range(len(positions) ))

print(generateKey(lR, "01234567"))