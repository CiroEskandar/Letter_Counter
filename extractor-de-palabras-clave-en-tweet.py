# hola

print()
tweet = input("ingresa tu tweet: ")
print()


#? crit = input("introduce el criterio de busqueda: ")


#* código encargada de la indexación de las palabras clave relacionadas al "#"

#* code in charge of the indexing of the keywords related to the "#"


m1 = 0
bef_hast = []
after_hast = []


for x in tweet:

    if x == "#":            #? == crit:

        bef_hast.append(m1)
        after_hast.append(tweet.index(" ",m1))

    m1 += 1


#* código encargado de la extracción de las palabras clave y su posterior impresión por pantalla

#* code in charge of keyword extraction and subsequent screen printing

   
m2 = 0
key_words = []


for x in bef_hast:

    key_words.append(tweet[bef_hast[m2]:after_hast[m2]])
    
    m2 += 1

print("las palabras clave encontradas fueron: ",key_words)

print()