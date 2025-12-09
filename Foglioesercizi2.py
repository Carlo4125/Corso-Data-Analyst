#Esercizio 1

'''
numero=int(input("Inserisci un numero: "))
if numero>0 :
    print("Il numero è positivo")
elif numero<0 :
    print("Il numero è negativo")
else :
    print("Il numero è zero")
    
'''

#Esercizio 2

'''
numero=int(input("Inserisci un numero: "))
if numero%2==0 :
    print("Il numero è pari")
else :
    print("Il numero è dispari")
    
'''

#Esercizio 3

'''
numero=int(input("Inserisci la tua età: "))
if numero>=18 :
    print("Sei maggiorenne")
else :
    print("Sei minorenne")
    
'''

#Esercizio 4

'''
numero=int(input("Inserisci un numero: "))
if numero>0 :
    print("Positivo")
elif numero<0 :
    print("Negativo")
else :
    print("Zero")
    
'''

#Esercizio 5

'''
numero1=int(input("Inserisci il primo numero: "))
numero2=int(input("Inserisci il secondo numero: "))
if numero1>numero2 :
    print(f"Il numero {numero1} è il più grande")
elif numero1<numero2 :
    print(f"Il numero {numero2} è il più grande")
else :
    print("I numeri inseriti sono uguali")

'''

#Esercizio 6

'''
numero1=int(input("Inserisci il primo numero: "))
numero2=int(input("Inserisci il secondo numero: "))
numero3=int(input("Inserisci il terzo numero: "))
if numero1>numero2 :
    if numero1>numero3:
        print(f"Il numero più grande è {numero1}")
    elif numero3>numero1:
        print(f"Il numero più grande è {numero3}")
    else :
        print(f"I numeri più grandi sono {numero1} inseriti due volte")
elif numero2>numero1:
    if numero2>numero3:
        print(f"Il numero più grande è {numero2}")
    elif numero3>numero2:
        print(f"Il numero più grande è {numero3}")
    else :
        print(f"I numeri più grandi sono {numero2} inseriti due volte")    
elif numero3>numero1:
    print(f"Il numero più grande è {numero3}")
elif numero1>numero3:
    print(f"Il numero più grande è {numero1} inserito due volte")
else :
    print(f"Tutti i numeri inseriti sono uguali, ossia {numero1}")

'''

#Esercizio 7

'''
lettera=str(input("Inserisci una lettera: "))
if lettera=='a' or lettera=='e' or lettera=='i' or lettera=='o' or lettera=='u' :
    print("La lettera inserita è una vocale")
else:
    print("La lettera inserita è una consonante")

'''

#Esercizio 8

'''
numero=int(input("Inserisci un numero: "))
if numero%3==0 and numero%5==0 :
    print("Il numero è divisibile sia per 3 che per 5")
else :
    print("Il numero non è divisibile sia per 3 che per 5")

'''

#Esercizio 9

'''
voto=int(input("Inserisci il voto: "))
if voto<6:
    print("Insufficiente")
elif voto<8:
    print("Sufficiente")
elif voto<10:
    print("Buono")
else :
    print("Ottimo")

'''

#Esercizio 10

'''
numero=int(input("Inserisci un numero: "))
if numero>=1 and numero<=100:
    print("Il numero appartiene all'intervallo tra 1 e 100 estremi compresi")
else :
    print("Il numero inserito non è compreso tra 1 e 100")

'''

#Esercizio  11

'''
eta=int(input("Inserisci l'età: "))
if eta<14 :
    print("La persona è un bambino")
elif eta <25 :
    print("La persona è un adolescente")
elif eta<60 :
    print("La persona è un adulto")
else :
    print("La persona è un anziano")

'''

#Esercizio 12

'''
anno=int(input("Inserisci l'anno: "))
if anno%4==0 :
    if anno%100==0:
        if anno%400==0:
            print("L'anno è bisestile")
        else :
            print("L'anno non è bisestile")
    else :
        print("L'anno è bisestile")
else :
    print("L'anno non è bisestile")

'''
    
#Esercizio 13

'''
password=str(input("Inserisci la tua password: "))
controllo=str(input("Conferma che la password inserita sia corretta: "))
if password==controllo :
    print("Controllo confermato la password inserita è corretta.")
else:
    print("Riprova, le password non corrispondono.")

'''

#Esercizio 14

'''
numero=int(input("Inserisci un numero: "))
if numero%2==0 or numero%3==0 :
    print("Il numero inserito è multiplo di 2 o di 3")
else:
    print("Il numero inserito non è nè multipo di 2 nè multiplo di 3")

'''

#Esercizio 15

'''
giorno=int(input("Inserisci il giorno della settimana numericamente: "))
if giorno==1 :
    print("Il giorno della settimana è lunedi")
elif giorno==2 :
    print("Il giorno della settimana è martedi")
elif giorno==3 :
    print("Il giorno della settimana è mercoledi")
elif giorno==4 :
    print("Il giorno della settimana è giovedi")
elif giorno==5 :
    print("Il giorno della settimana è venerdi")
elif giorno==6 :
    print("Il giorno della settimana è sabato")
elif giorno==7 :
    print("Il giorno della settimana è domenica")
else:
    print("Il numero inserito è sbagliato")

'''

#Esercizio 16

'''
numero1=int(input("Inserisci il primo numero: "))
numero2=int(input("Inserisci il secondo numero: "))
if numero1==numero2:
    print("I numeri inseriti sono uguali")
else:
    print("I numeri inseriti sono diversi")

'''

#Esercizio 17

'''
eta=int(input("Inserisci la tua età: "))
documento=bool(input("Scrivi True se possiedi il documento, False in caso contrario: "))
if eta>=18 and documento==True:
    print("Puoi entrare nel locale")
else:
    print("Non puoi entrare nel locale")

'''

#Esercizio 18

'''
temperatura=int(input("Inserisci la temperatura: "))
if temperatura<10:
    print("Freddo")
elif temperatura<25:
    print("Tiepido")
else:
    print("Caldo")

'''

#Esercizio 19

'''
estr1=int(input("Inserisci il primo estremo: "))
estr2=int(input("Inserisci il secondo estremo: "))
numero=int(input("Inserisci un numero: "))
if estr1>estr2:
    if numero>=estr2 and numero<=estr1:
        print("Il numero inserito è compreso tra i due estremi")
    else:
        print("Il numero inserito non è compreso tra i due estremi")
elif estr2>estr1:
    if numero>=estr1 and numero<=estr2:
        print("Il numero inserito è compreso tra i due estremi")
    else:
        print("Il numero inserito non è compreso tra i due estremi")    
else:
    if numero==estr1:
        print("Il numero inserito è uguale ai due estremi a loro volta uguali tra loro")
    else:
        print("Il numero non è uguale ai due estremi che sono uguali tra loro")

'''

#Esercizio 20

'''
numero=int(input("Inserisci un numero: "))
if numero>0:
    if numero%2==0:
        print("Positivo e pari")
    else:
        print("Positivo e dispari")
elif numero<0:
    print("Negativo")
else:
    print("Zero")

'''
