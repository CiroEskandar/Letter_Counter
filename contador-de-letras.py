
# todo: hacer que en el programa permita admitir los carácteres de cualquier idioma 

# todo: make the program support characters of any language


lista0 = list(input("ingresa el texto que desea analizar: "))

print()


#* esta es una tabla que muestra todas las letras y la cantidad de letra que hay de esa letra dentro del texto introducido

#* this is a table that shows all the letters and the amount of that letter within the text you enter


print("{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}".format("a: ",lista0.count("a"),"f: ",lista0.count("f"),"k: ",lista0.count("k"),"o: ",lista0.count("o"),"t: ",lista0.count("t"),"y: ",lista0.count("y")))

print("{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}".format("b: ",lista0.count("b"),"g: ",lista0.count("g"),"l: ",lista0.count("l"),"p: ",lista0.count("p"),"u: ",lista0.count("u"),"z: ",lista0.count("z")))

print("{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}".format("c: ",lista0.count("c"),"h: ",lista0.count("h"),"m: ",lista0.count("m"),"q: ",lista0.count("q"),"v: ",lista0.count("v"),"",""))

print("{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}".format("d: ",lista0.count("d"),"i: ",lista0.count("i"),"n: ",lista0.count("n"),"r: ",lista0.count("r"),"w: ",lista0.count("w"),"",""))

print("{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}|{:^5}{:^5}".format("e: ",lista0.count("e"),"j: ",lista0.count("j"),"ñ: ",lista0.count("ñ"),"s: ",lista0.count("s"),"x: ",lista0.count("x"),"",""))

print()


#* se crean variables relacionadas a los carácteres y a su cantidad dentro del texto

#* variables are created related to the characters and their number within the text


a = [lista0.count("a"),"a"]
b = [lista0.count("b"),"b"]
c = [lista0.count("c"),"c"]
d = [lista0.count("d"),"d"]
e = [lista0.count("e"),"e"]
f = [lista0.count("f"),"f"]

g = [lista0.count("g"),"g"]
h = [lista0.count("h"),"h"]
i = [lista0.count("i"),"i"]
j = [lista0.count("j"),"j"]
k = [lista0.count("k"),"k"]
l = [lista0.count("l"),"l"]

m = [lista0.count("m"),"m"]
n = [lista0.count("n"),"n"]
ñ = [lista0.count("ñ"),"ñ"]
o = [lista0.count("o"),"o"]
p = [lista0.count("p"),"p"]

q = [lista0.count("q"),"q"]
r = [lista0.count("r"),"r"]
s = [lista0.count("s"),"s"]
t = [lista0.count("t"),"t"]
u = [lista0.count("u"),"u"]

v = [lista0.count("v"),"v"]
w = [lista0.count("w"),"w"]
x = [lista0.count("x"),"x"]
y = [lista0.count("y"),"y"]
z = [lista0.count("z"),"z"]


#* Se crea una lista macro que incluye a todas las variables anteriormente creadas, se ordenan de menor a mayor, y se crean dos listas adicionales, 
#* una solo compuesta de letras que no están en el texto (cuya cantidad es igual a cero) y otra que no incluye la anterior.

#* A macro list is created that includes all the previously created variables, they are sorted from smallest to largest, and two additional lists are created, 
#* one only composed of letters that are not in the text (whose quantity is equal to zero) and another one that does not include the previous one.


listalarga = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z]

listalarga.sort(reverse=True)

ceros = [x for x in listalarga if x[0] < 1]

menores = [x for x in listalarga if x[0] >= 1]


#* se toman las 5 variables que más se repiten, se reordenan internamente, se guardan en una nueva variable en forma de str y se imprime por pantalla

#* the 5 most repeated variables are taken, reordered internally and stored in a new variable in the form of str and printed on the screen


listalarga[0].append(str(listalarga[0].pop(0)))
uno = " = ".join(listalarga[0])

listalarga[1].append(str(listalarga[1].pop(0)))
dos = " = ".join(listalarga[1])

listalarga[2].append(str(listalarga[2].pop(0)))
tres = " = ".join(listalarga[2])

listalarga[3].append(str(listalarga[3].pop(0)))
cuatro = " = ".join(listalarga[3])

listalarga[4].append(str(listalarga[4].pop(0)))
cinco = " = ".join(listalarga[4])

print("las letras que más se repiten son: ",uno,",",dos,",",tres,",",cuatro,"y",cinco)

print()


#* se toman las 5 variables que menos se repiten, se reordenan internamente, se guardan en una nueva variable en forma de str y se imprime por pantalla

#* the 5 least repeated variables are taken, reordered internally and stored in a new variable in the form of a string and printed on the screen.


menores[-1].append(str(menores[-1].pop(0)))
ult = " = ".join(menores[-1])

menores[-2].append(str(menores[-2].pop(0)))
pult = " = ".join(menores[-2])

menores[-3].append(str(menores[-3].pop(0)))
apult = " = ".join(menores[-3])

menores[-4].append(str(menores[-4].pop(0)))
aapult = " = ".join(menores[-4])

menores[-5].append(str(menores[-5].pop(0)))
aaapult = " = ".join(menores[-5])

print("las letras que menos se repiten son: ",ult,",",pult,",",apult,",",aapult,"y",aaapult)

print()


#* Se hace una lista con las letras que no están en el texto, se reordenan internamente, se guardan en una nueva variable en forma de str y se imprime por pantalla

#* A list is made of the letters that are not in the text, reordered internally, stored in a new variable in the form of str and printed on the screen.


[x.append(x.pop(0)) for x in ceros]

new_ceros = [x[0] for x in ceros]

no_estan = ", ".join(new_ceros)

print("las letras",no_estan,"no están presentes en el texto analizado")

print()