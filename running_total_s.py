#somma i numeri di una lista. La lista e' formata da user inputs. L'utente puo' dare input al massimo 9 volte.
#algoritmo: 
# 1. definisci una lista; 
# 2. inizializza il limite entro cui continuare a sommare i numeri (i.e. dopo il nono numero chiesto, smetti di sommare); 
# 3. definisci il running total (r_total)
# 4. fino a che i numeri della lista sono meno del limite:
#	a. chiedi un numero
#	b. aggiungi il numero agli elementi della lista 
#		b2. questo dovrebbe aggiornare anche il limite
#	c. somma il nuovo elemento 

numbers = [] #definisce una lista chiamata numbers
limit = len(numbers) #conta gli element nella lista numbers
print(f"Limite {limit}") #stampa il numero di elementi nella lista
r_total=0 #definisce il running total
while limit <= 9: #fino a che gli elementi della lista sono meno di 9:
	x = (input("NOW Add your number: ")) #chiedi un numero
	numbers.append(x) #metti il numero nella lista
	print(f"limite {limit}") #stampa il n. di elementi nella lista
	print(f"numeri {numbers}") #stampa gli elementi della lista




