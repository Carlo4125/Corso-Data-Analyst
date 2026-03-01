from math import sqrt,pi,pow
import random as rn
import string

#Calcolo della media aritmetica degli elementi all'interno di una lista di numeri
def media(lista1):
    somma=0
    for numero in lista1:
        somma=somma+numero
    if len(lista1)==0:
        media=None
    else:
        media=somma/len(lista1)
    return media


#Ordinamento decrescente di una lista
def reverse_ord(lista2):
    lista2.sort(reverse=True)
    return lista2


#Controllo se una lista contiene ripetizioni
def check_rep(lista3):
    checkset1=set(lista3)
    return len(checkset1)!=len(lista3)


#Calcolo dell'area di un cerchio dato il raggio
def area_cerchio (raggio):
    return pi*pow(raggio,2)


#Calcolo dell'ipotenusa in un triangolo rettangolo dati i due cateti
def ipotenusa(cat1,cat2):
    return sqrt(pow(cat1,2)+pow(cat2,2))


#Calclo dell'area di una sfera dato il raggio
def area_sfera(raggio):
    return 4*pi*pow(raggio,2)


#Calcolo del volume di una sfera dato il raggio
def volume_sfera(raggio):
    return 4*pi*pow(raggio,3)/3


#Generazione casuale di una lista, i numeri sono generati in un intervallo delimitato dai parametri min e max, e la dimensione
#della lista sarà data dal parametro quantità (nel caso in cui venisse omesso la dimensione di default è 10)
def gen_lista(min,max,quantità=10):
    return rn.choices(range(min,max), k=quantità)


#Generazione di un dizionario in cui le chiavi sono gli elementi unici all'interno di una lista e il valore di ogni chiave
#rapprenta il numero di ripetizioni di tale elemento
def count_rep(lista4):
    listrep=[]
    checkset2=set(lista4)
    for elemento in checkset2:
        listrep.append(lista4.count(elemento))
    dictrep=dict(zip(checkset2,listrep))
    return dictrep


#Generazione di una lista che contiene tutti gli indici in cui un dato elemento compare all'interno della data lista
def indici (lista5,elemento):
    listaind=[]
    for i in range(len(lista5)):
        if lista5[i]==elemento:
            listaind.append(i)
    return listaind


#Controllo se una lista è ordinata
def check_ord(lista6):
    lista7=sorted(lista6)
    return lista7==lista6


#Generazione di una lista contenente l'elemento o gli elementi che compaiono più volte all'interno di una data lista
def elem_piu (lista8):
    elem=count_rep(lista8)
    listelem=[]
    M=max(elem.values())
    for k,v in elem.items():
        if v==M:
            listelem.append(k)
    return listelem


#Rimozione dei duplicati e ordinamento di una data lista
def remove_dupord (lista9):
    setdup=set(lista9)
    return list(setdup)


#Controllo se due liste sono uguali (hanno gli stessi elementi amche se in posizioni diverse)
def check_equal (lista10,lista11):
    lista12=sorted(lista10)
    lista13=sorted(lista11)
    return lista12==lista13


#Rimozione degli elementi duplicati all'interno di una data lista mantenendo l'ordine originale della lista
def remove_dup(lista14):
    listadup=[]
    for elemento in lista14:
        if elemento not in listadup:
            listadup.append(elemento)
    return listadup


#Inserimento ordinato di un dato elemento in una data lista già ordinata
def insert_ord(lista15,elem):
    posizione=None
    for i in range(len(lista15)):
        if elem<=lista15[i]:
            posizione=i
            break
    if posizione!=None:
        lista15.insert(posizione,elem)
    else:
        lista15.append(elem)
    return lista15
    

#Generazione di una lista che corrisponde alla sequenza di fibonacci, il numero di passaggi deriva dal numero dato
def seq_fib(numero):
    lista16=[]
    if numero==1:
        lista16.append(1)
    elif numero==2:
        lista16.extend([1,1])
    else:
        lista16=[1,1]
    for i in range(2,numero):
        lista16.append(lista16[i-1]+lista16[i-2])
    return lista16


#Generazione di una lista che contiene gli elementi in comune tra due date liste
def comm_elem(lista17,lista18):
    listcomm=[]
    if len(lista17)>=len(lista18):
        listmom=lista17
        for elem in lista18:
            if elem in listmom:
                listcomm.append(elem)
                listmom.remove(elem)
    else:
        listmom=lista18
        for elem in lista17:
            if elem in listmom:
                listcomm.append(elem)
                listmom.remove(elem)
    return listcomm        


#Divisione di una data lista in tante sottoliste di dimensione derivata dal parametro grandezza
def divis_lista(lista19,grandezza):
    listanuova=[]
    listaprova=[]
    for elem in lista19:
        if len(listaprova)!=grandezza:
            listaprova.append(elem)
        else:
            listanuova.extend([list(listaprova)])
            listaprova.clear()
            listaprova.append(elem)
    if len(listaprova)!=grandezza:
        listanuova.extend([list(listaprova)])
    return listanuova


#Calcolo del massimo comune divisore tra due dati numeri
def mcd(x,y):
    massimo=1
    if x<y:
        for numero in range(1,x+1):
            if x%numero==0 and y%numero==0 and numero>massimo:
                massimo=numero
    elif y>x:
        for numero in range(1,y+1):
            if x%numero==0 and y%numero==0 and numero>massimo:
                massimo=numero
    else:
        massimo=x
    return massimo


#Calcolo del minimo comune multiplo dati due numeri (non sfruttando la funzione precedente)
'''def mcm(x,y):
    minimo=1
    if x<y:
        for numero in range(y,x*y+1):
            if numero%x==0 and numero%y==0:
                minimo=numero
                break
    elif x>y:
        for numero in range(x,x*y+1):
            if numero%x==0 and numero%y==0:
                minimo=numero
                break
    else:
        minimo=x
    return minimo
'''


#Calcolo del minimo comune multiplo dati due numeri (sfruttando la funzione precedente)
def mcm(x,y):
    return floor(x*y/mcd(x,y))


#Verifica se un numero dato è primo
def primo(n):
    primo=True
    if n<2:
        primo=False
    else:
        for numero in range(2,ceil(n/2)+1):
            if n%numero==0:
                primo=False
    return primo


#Generazione di una lista che contiene i divisori di un dato numero
def divisori(n):
    divis=[]
    if n>0:
        for numero in range(1,n+1):
            if n%numero==0:
                divis.append(numero)
    return divis


#Generazione di un dizionario che contiene come chiavi i numeri e come valori i rispettivi esponenti che rappresentano la
#scomposizione in fattori primi di un dato numero
def scomposizione(n):
    listafatt=[]
    m=n
    if n<2:
        dictfatt={}
    else:
        for numero in range(2,m+1):
            while  m%numero==0:
                listafatt.append(numero)
                m=floor(m/numero)
    dictfatt=count_rep(listafatt)
    return dictfatt


#Generazione di una matrice casuale dato il numero di righe, di colonne e l'intervallo delimitato dai parametri min e max
def gen_matrix(righe,colonne, min, max):
    matrice=[]
    for numero in range(righe):
        riga=rn.choices(range(min,max), k=colonne)
        matrice.append(riga)
    return matrice


#Rimescolamento casuale di una data lista
def rand_mesc(lista20):
    listindex=rn.sample(range(0,len(lista20)), k=len(lista20))
    listanuova=[]
    for numero in listindex:
        listanuova.append(lista20[numero])
    return listanuova


#Generazione casuale di una stringa contenente le lettere dell'alfabeto in minuscolo e le cifre dallo 0 al 9, la lunghezza della
#stringa generata è data dal parametro lunghezza (nel caso in cui venisse omesso la dimensione di default è 10)
def gen_str(lunghezza=10):
    stringa = string.ascii_lowercase + string.digits
    return ''.join(rn.choice(stringa) for _ in range(lunghezza))


#Controllo se una data lista contiene solo numeri, interi o float
def num_list(lista21):
    solonumeri=True
    if len(lista21)==0:
        solonumeri=None
    else:
        for i in range(len(lista21)):
            if type(lista21[i])!=int and type(lista21[i])!=float:
                solonumeri=False
    return solonumeri


#Calcolo della distanza euclidea tra due punti bidimensionali
def distanza(A,B):
    risultato=None
    if len(A)==2 and len(B)==2:
        risultato=sqrt(pow(A[0]-B[0],2)+pow(A[1]-B[1],2))
    return risultato
