import random
import hashlib
import math
from tkinter import*
from tkinter import ttk
import sympy as sy
import re
import Crypto
from Crypto.Util.number import *
import libnum
from random import randint
from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
import cv2
from numpy import random
from tkinter import filedialog

ventana = Tk()
ventana.title('CRIPTOMATIC')
ventana.geometry("600x650")
ingreso=StringVar()
ingreso1=StringVar()
ingreso2=StringVar()
ingreso3=StringVar()
#---------menu------------
notebook=ttk.Notebook(ventana)
notebook.pack(fill='both',expand='yes')
pes0=ttk.Frame(notebook)
pes1=ttk.Frame(notebook)
pes2=ttk.Frame(notebook)
pes3=ttk.Frame(notebook)
pes4=ttk.Frame(notebook)
pes5=ttk.Frame(notebook)
pes6=ttk.Frame(notebook)
notebook.add(pes0,text='RSA')
notebook.add(pes1,text='Elgamal')
notebook.add(pes2,text='Rabin')
notebook.add(pes3,text='Menezes')
notebook.add(pes4,text='Firma RSA')
notebook.add(pes5,text='Firma Elgamal')
notebook.add(pes6,text='Criptografia visual')
#-------pestaña RSA-------
Label(pes0, text = "Algoritmo RSA").place(x=10,y=10)
Label(pes0, text = "Primo1: ").place(x=10,y=40)
caja1=Entry(pes0, font='arial 8',width=13)
caja1.place(x=10, y=60)
Label(pes0, text = "Primo2: ").place(x=105,y=40)
caja2=Entry(pes0, font='arial 8',width=13)
caja2.place(x=105, y=60)
Label(pes0, text = "Clave publica e: ").place(x=200,y=40)
caja3=Entry(pes0, font='arial 8',width=13)
caja3.place(x=200, y=60)
Label(pes0, text = "Clave privada d: ").place(x=295,y=40)
caja4=Entry(pes0, font='arial 8',width=13)
caja4.place(x=295, y=60)
Label(pes0, text = "Mensaje: ").place(x=190,y=130)
caja5=Entry(pes0, font='arial 8',width=66)
caja5.place(x=10, y=165)
Label(pes0, text = "Mensaje encriptado: ").place(x=150,y=230)
caja6=Text(pes0, width=50, height=7)
caja6.place(x=10, y=260)
Label(pes0, text = "Mensaje desencriptado: ").place(x=140,y=390)
caja7=Text(pes0, width=50, height=7)
caja7.place(x=10, y=420)
def primos():
    global p,q,fi,e,d
    numeros = [53, 113, 107, 89, 73, 139, 107, 109, 89, 67, 131, 103, 139, 73, 131, 107, 59, 149, 101]
    p=random.choice(numeros) 
    q=random.choice(numeros) 
    fi=(p-1)*(q-1)
    for i in range(8,random.randint(21, 30)):
        if math.gcd(i,fi)==1:
            e=i
    k=1
    tope=0
    while tope == 0:
        if (k*e)%fi==1:
            tope=1  
        else:
            k = k + 1
        d = k 
    def llenar():
        if p!=q:
            caja1.insert(INSERT,p)
            caja2.insert(INSERT,q)
        caja3.insert(INSERT,e)
        caja4.insert(INSERT,d)
    llenar()
def getmsj():
    obtener3 = caja5.get()    
    def encriptar():
        p=int(caja1.get())
        q=int(caja2.get())
        e=int(caja3.get())
        if sy.isprime(p) is False or sy.isprime(q) is False:
            aviso = Label(pes0, text = 'ERROR PRIMOS')
            aviso.place(x=390,y=40)
        else:
            aviso = Label(pes0, text = '                             ')
            aviso.place(x=390,y=40)
        global listentnew
        binario=bin(int.from_bytes(obtener3.encode(), 'big'))
        binent=int(binario, base=2)
        charbinent=str(binent)
        listent = []
        for letra in charbinent:
            ent1 = int(letra)
            cifrado = (ent1**e)%(p*q)
            listent.append(cifrado)
        listentnew = [str(a) for a in listent]
    encriptar()
    caja6.insert(INSERT,listentnew)
def getmsj2():
    obtener4 = caja6.get('1.0', END)
    def desencriptar():
        p=int(caja1.get())
        q=int(caja2.get())
        d=int(caja4.get())
        global char
        lista = (obtener4).split()
        lista2=[]
        for t in lista:
            ent2 = int(t)
            desencriptado = (ent2**d)%(p*q)
            lista2.append(desencriptado)
        listentnew2 = [str(a) for a in lista2]
        ent3 = int("" . join(listentnew2))
        char=ent3.to_bytes((ent3.bit_length() + 7) // 8, 'big').decode()
        caja7.insert(INSERT,char) 
    desencriptar()
def borrar():
    caja1.delete(0, 'end')
    caja2.delete(0, 'end')
    caja3.delete(0, 'end')
    caja4.delete(0, 'end')
def borrar1():
    caja5.delete(0, 'end')
def borrar2():
    ingreso2.set('')
    caja6.delete('1.0',END)
def borrar3():
    ingreso3.set('')
    caja7.delete('1.0',END)
boton1 = Button(pes0, text='Llenar campos', command = primos).place(x=80, y=90)
boton2 = Button(pes0, text='Borrar', command = borrar).place(x=240, y=90)
boton3 = Button(pes0, text='Borrar', command = borrar1).place(x=420, y=165)
boton4 = Button(pes0, text='Encriptar', command = getmsj).place(x=420, y=260)
boton5 = Button(pes0, text='Borrar', command = borrar2).place(x=420, y=300)
boton6 = Button(pes0, text='Desencriptar', command = getmsj2).place(x=420, y=420)
boton7 = Button(pes0, text='Borrar', command = borrar3).place(x=420, y=460)

#----------pestaña elgamal--------------
ingresoe=StringVar()
ingresoe1=StringVar()
ingresoe2=StringVar()
ingresoe3=StringVar()
Label(pes1, text = "Algoritmo Elgamal").place(x=10,y=10)
Label(pes1, text = "Nro primo: ").place(x=10,y=40)
cajae1=Entry(pes1, font='arial 8',width=13)
cajae1.place(x=10, y=60)
Label(pes1, text = "Clave publica: ").place(x=105,y=40)
cajae2=Entry(pes1, font='arial 8',width=13)
cajae2.place(x=105, y=60)
Label(pes1, text = "Raiz primitiva: ").place(x=200,y=40)
cajae3=Entry(pes1, font='arial 8',width=13)
cajae3.place(x=200, y=60)
Label(pes1, text = "Mensaje: ").place(x=190,y=130)
cajae5=Entry(pes1, font='arial 8',width=66)
cajae5.place(x=10, y=165)
Label(pes1, text = "Mensaje encriptado: ").place(x=150,y=230)
cajae6=Text(pes1, width=50, height=7)
cajae6.place(x=10, y=260)
Label(pes1, text = "Mensaje desencriptado: ").place(x=140,y=390)
cajae7=Text(pes1, width=50, height=7)
cajae7.place(x=10, y=420)

lamda=random.randint(10,100)
mu=random.randint(10,100)
def primo():    
    numerose = [1151, 6133, 9403, 2999, 5113, 2221, 5261, 8093, 1847, 5167, 1811, 4483, 9311, 8297, 7817, 2887, 9151, 5813, 1699, 8291, 3671, 1291, 8963, 6389, 2411, 9511, 1741, 5077, 8537, 4493, 8861, 3259, 5737, 1153, 5531]
    pe=random.choice(numerose)
    #genera raiz primitiva
    s = set(range(1, pe))
    for a in s:
        g = set()
        for x in s:
            g.add((a**x) % pe)
        if g == s:
            alfa=a
            break
    cpub=(alfa**lamda)%pe
    def llenare():
        cajae1.insert(INSERT,pe)
        cajae2.insert(INSERT,cpub)
        cajae3.insert(INSERT,alfa)
    llenare()
def getmsje():
    obtenere3 = cajae5.get()    
    def encriptare():
        pe=int(cajae1.get())
        s = set(range(1, pe))
        for a in s:
            g = set()
            for x in s:
                g.add((a**x) % pe)
            if g == s:
                alfa=a
                break
        cpub=(alfa**lamda)%pe
        if sy.isprime(pe) is False:
            avisoe = Label(pes1, text = 'ERROR PRIMO')
            avisoe.place(x=390,y=40)
        else:
            avisoe = Label(pes1, text = '                             ')
            avisoe.place(x=390,y=40)
        global listente1,n2,listente
        binarioe=bin(int.from_bytes(obtenere3.encode(), 'big'))
        binente=int(binarioe, base=2)
        charbinente=str(binente)
        listente = []
        listente1 = []
        for letrae in charbinente:
            ente1 = int(letrae)
            n1=(alfa**mu)%pe
            n2=(ente1*(cpub**mu))%pe
            listente.append(n1)
            listente1.append(n2)
    encriptare()
    cajae6.insert(INSERT,(listente,listente1))
def getmsje2():
    obtenere4 = cajae6.get('1.0', 'end-1c')
    string = re.sub("\{|\}","",obtenere4)
    listae=list(map(int,(string.split(' '))))
    tam=int(len(listae)/2)
    liste1=(listae[:tam])
    liste2=(listae[tam:])
    def desencriptare():
        pe=int(cajae1.get())
        listae2=[]
        c=0
        for te in liste1:
            n3 = (te**lamda)%pe
            #genera el inverso modular
            j=1
            tope=0
            while tope == 0:
                if (j*n3)%pe==1:
                    tope=1  
                else:
                    j = j + 1
                n4 = j
            n=((liste2[c])*n4)%pe
            c=c+1
            listae2.append(n)
        listentnewe2 = [str(a) for a in listae2]
        ente3 = int("" . join(listentnewe2))
        chare=ente3.to_bytes((ente3.bit_length() + 7) // 8, 'big').decode()
        cajae7.insert(INSERT,chare) 
    desencriptare()
def borrare():
    cajae1.delete(0, 'end')
    cajae2.delete(0, 'end')
    cajae3.delete(0, 'end')
def borrare1():
    cajae5.delete(0, 'end')
def borrare2():
    ingresoe2.set('')
    cajae6.delete('1.0',END)
def borrare3():
    ingresoe3.set('')
    cajae7.delete('1.0',END)
botone1 = Button(pes1, text='Llenar campos', command = primo).place(x=80, y=90)
botone2 = Button(pes1, text='Borrar', command = borrare).place(x=240, y=90)
botone3 = Button(pes1, text='Borrar', command = borrare1).place(x=420, y=165)
botone4 = Button(pes1, text='Encriptar', command = getmsje).place(x=420, y=260)
botone5 = Button(pes1, text='Borrar', command = borrare2).place(x=420, y=300)
botone6 = Button(pes1, text='Desencriptar', command = getmsje2).place(x=420, y=420)
botone7 = Button(pes1, text='Borrar', command = borrare3).place(x=420, y=460)

#-------pestaña Rabin-------

Label(pes2, text = "Algoritmo Rabin").place(x=10,y=10)
Label(pes2, text = "Primo1: ").place(x=10,y=40)
cajar1=Entry(pes2, font='arial 8',width=13)
cajar1.place(x=10, y=60)
Label(pes2, text = "Primo2: ").place(x=105,y=40)
cajar2=Entry(pes2, font='arial 8',width=13)
cajar2.place(x=105, y=60)
Label(pes2, text = "Clave privada: ").place(x=200,y=40)
cajar3=Entry(pes2, font='arial 8',width=13)
cajar3.place(x=200, y=60)
Label(pes2, text = "Mensaje: ").place(x=190,y=130)
cajar5=Entry(pes2, font='arial 8',width=66)
cajar5.place(x=10, y=165)
Label(pes2, text = "Mensaje encriptado: ").place(x=150,y=230)
cajar6=Text(pes2, width=50, height=7)
cajar6.place(x=10, y=260)
Label(pes2, text = "Mensaje desencriptado: ").place(x=140,y=390)
cajar7=Text(pes2, width=50, height=7)
cajar7.place(x=10, y=420)
def primosr():
    global pr,qr,nr
    numerosr = [907, 1439, 5903, 9227, 251, 2851, 8111, 3623, 1723, 6911, 5011, 5011, 6247, 6299, 3547, 9643, 5563]
    pr=random.choice(numerosr) 
    qr=random.choice(numerosr)
    nr=pr*qr
    def llenarr():
        if pr!=qr:
            cajar1.insert(INSERT,pr)
            cajar2.insert(INSERT,qr)
        cajar3.insert(INSERT,nr)
    llenarr()
def getmsjr():
    obtenerr3 = cajar5.get()
    listr=list(obtenerr3)
    def encriptarr():
        pr=int(cajar1.get())
        qr=int(cajar2.get())
        nr=int(cajar3.get())
        if (pr%4!=3) or (qr%4!=3):
            avisor = Label(pes2, text = 'PRIMOS NO CONGRUENTES')
            avisor.place(x=350,y=40)
        else:
            avisor = Label(pes2, text = '                                                                                   ')
            avisor.place(x=300,y=40)
        global listentr
        li=[]
        for h in listr:
            binarior=bin(int.from_bytes(h.encode(), 'big'))
            binentr=int(binarior, base=2)
            li.append(binentr)
        listentr = []
        for letrar in li:
            cifrador = (letrar**2)%(nr)
            listentr.append(cifrador)
    encriptarr()
    cajar6.insert(INSERT,listentr)
def getmsjr2():
    obtenerr4 = cajar6.get('1.0', END)
    def desencriptarr():
        pr=p1=int(cajar1.get())
        qr=q1=int(cajar2.get())
        nr=int(cajar3.get())
        a = 1
        u1 = 0
        b = 0
        v1 = 1
        while q1 != 0:    # este while halla los numeros de bezout para los primos escogidos
            q = p1//q1
            r = p1 - q1 * q
            u = a - q * u1
            v = b - q * v1
            p1 = q1
            q1 = r
            a = u1
            u1 = u
            b = v1
            v1 = v
        global charr
        listar = (obtenerr4).split()
        listar1=[]
        for tr in listar:
            entr2 = int(tr)
            s = (entr2**int((qr+1)/4)) % qr
            r = (entr2**int((pr+1)/4)) % pr
            r1 = (a*pr*s+b*qr*r) % nr
            r2 = (a*pr*s-b*qr*r) % nr
            r3 = nr - r1
            r4 = nr - r2
            if len(str(r1))<=3:
                listar1.append(chr(r1))
            elif len(str(r2))<=3:
                listar1.append(chr(r2))
            elif len(str(r3))<=3:
                listar1.append(chr(r3))
            elif len(str(r4))<=3:
                listar1.append(chr(r4))
        cajar7.insert(INSERT,listar1) 
    desencriptarr()
def borrarr():
    cajar1.delete(0, 'end')
    cajar2.delete(0, 'end')
    cajar3.delete(0, 'end')
def borrarr1():
    cajar5.delete(0, 'end')
def borrarr2():
    ingreso2.set('')
    cajar6.delete('1.0',END)
def borrarr3():
    ingreso3.set('')
    cajar7.delete('1.0',END)
botonr1 = Button(pes2, text='Llenar campos', command = primosr).place(x=80, y=90)
botonr2 = Button(pes2, text='Borrar', command = borrarr).place(x=240, y=90)
botonr3 = Button(pes2, text='Borrar', command = borrarr1).place(x=420, y=165)
botonr4 = Button(pes2, text='Encriptar', command = getmsjr).place(x=420, y=260)
botonr5 = Button(pes2, text='Borrar', command = borrarr2).place(x=420, y=300)
botonr6 = Button(pes2, text='Desencriptar', command = getmsjr2).place(x=420, y=420)
botonr7 = Button(pes2, text='Borrar', command = borrarr3).place(x=420, y=460)

#----------menezes vanstone--------------

Label(pes3, text = "Algoritmo Menezes-Vanstone").place(x=10,y=5)
Label(pes3, text = "Curva secp256k1").place(x=10,y=25)
Label(pes3, text = "Clave publica: ").place(x=10,y=50)
cajam1=Entry(pes3, font='arial 8',width=66)
cajam1.place(x=10, y=70)
Label(pes3, text = "Clave privada: ").place(x=10,y=90)
cajam2=Entry(pes3, font='arial 8',width=66)
cajam2.place(x=10, y=110)
Label(pes3, text = "Mensaje: ").place(x=190,y=140)
cajam5=Entry(pes3, font='arial 8',width=66)
cajam5.place(x=10, y=165)
Label(pes3, text = "Mensaje encriptado: ").place(x=150,y=230)
cajam6=Text(pes3, width=50, height=7)
cajam6.place(x=10, y=260)
Label(pes3, text = "Mensaje desencriptado: ").place(x=140,y=390)
cajam7=Text(pes3, width=50, height=7)
cajam7.place(x=10, y=420)
def llenarm():
    global pubKeyHex, privKey, privKeyHex
    privKey = generate_eth_key()
    privKeyHex = privKey.to_hex()
    pubKeyHex = privKey.public_key.to_hex()
    cajam1.insert(INSERT,pubKeyHex)
    cajam2.insert(INSERT,privKeyHex)
def encriptarm():
    global encrypted
    obtenerm = cajam5.get().encode()
    encrypted = encrypt(cajam1.get(), obtenerm)
    cajam6.insert(INSERT,encrypted)
def desencriptarm():
    obtenm = cajam6.get('0.1', 'end-1c').encode()
    decrypted = decrypt(cajam2.get(), encrypted)
    cajam7.insert(INSERT,decrypted)
def borrarm1():
    cajam1.delete(0, 'end')
    cajam2.delete(0, 'end')
def borrarm2():
    cajam5.delete(0, 'end')
def borrarm3():
    ingreso2.set('')
    cajam6.delete('1.0',END)
def borrarm4():
    ingreso3.set('')
    cajam7.delete('1.0',END)
    
botonm1 = Button(pes3, text='Llenar campos', command = llenarm).place(x=190, y=25)
botonm2 = Button(pes3, text='Borrar', command = borrarm1).place(x=350, y=25)
botonm3 = Button(pes3, text='Borrar', command = borrarm2).place(x=420, y=165)
botonm4 = Button(pes3, text='Encriptar', command = encriptarm).place(x=420, y=260)
botonm5 = Button(pes3, text='Borrar', command = borrarm3).place(x=420, y=300)
botonm6 = Button(pes3, text='Desencriptar', command = desencriptarm).place(x=420, y=420)
botonm7 = Button(pes3, text='Borrar', command = borrarm4).place(x=420, y=460)

#------------firmaRSA------------------

Label(pes4, text = "Firma RSA").place(x=10,y=10)
Label(pes4, text = "Primo1: ").place(x=10,y=40)
cajah1=Entry(pes4, font='arial 8',width=13)
cajah1.place(x=10, y=60)
Label(pes4, text = "Primo2: ").place(x=105,y=40)
cajah2=Entry(pes4, font='arial 8',width=13)
cajah2.place(x=105, y=60)
Label(pes4, text = "Clave publica e: ").place(x=200,y=40)
cajah3=Entry(pes4, font='arial 8',width=13)
cajah3.place(x=200, y=60)
Label(pes4, text = "Clave privada d: ").place(x=295,y=40)
cajah4=Entry(pes4, font='arial 8',width=13)
cajah4.place(x=295, y=60)
Label(pes4, text = "n:  ").place(x=390,y=40)
cajanh=Entry(pes4, font='arial 8',width=13)
cajanh.place(x=390, y=60)
Label(pes4, text = "Mensaje: ").place(x=190,y=130)
cajah5=Entry(pes4, font='arial 8',width=66)
cajah5.place(x=10, y=165)
Label(pes4, text = "Hash del mensaje: ").place(x=70,y=230)
cajah6=Text(pes4, width=24, height=7)
cajah6.place(x=10, y=260)
Label(pes4, text = "Firma: ").place(x=300,y=230)
cajahf=Text(pes4, width=24, height=7)
cajahf.place(x=220, y=260)
Label(pes4, text = "Mensaje Verificado: ").place(x=140,y=390)
cajah7=Text(pes4, width=50, height=7)
cajah7.place(x=10, y=420)
def primosh():
    global ph,qh,eh,dh,nh
    numerosh = [827, 997, 191, 863, 743, 941, 229, 739, 541, 727, 251, 179, 823, 337, 457, 163, 461, 601, 653, 739, 163, 953, 881, 593, 577, 167, 613, 419, 919, 937]
    ph=random.choice(numerosh) 
    qh=random.choice(numerosh) 
    fih=(ph-1)*(qh-1)
    for i in range(8,random.randint(21, 30)):
        if math.gcd(i,fih)==1:
            eh=i
    kh=1
    topeh=0
    while topeh == 0:
        if (kh*eh)%fih==1:
            topeh=1  
        else:
            kh = kh + 1
        dh = kh 
    nh=ph*qh
    def llenarh():
        if ph!=qh:
            cajah1.insert(INSERT,ph)
            cajah2.insert(INSERT,qh)
            cajanh.insert(INSERT,nh)
        cajah4.insert(INSERT,dh)
        cajah3.insert(INSERT,eh)
    llenarh()
def getmsjh():
    obtenerh3 = cajah5.get().encode(encoding="utf-8")  
    def firmar():
        global m,hexa,sh,msjhashint
        ph=int(cajah1.get())
        qh=int(cajah2.get())
        dh=int(cajah4.get())
        nh=int(cajanh.get())
        if sy.isprime(ph) is False or sy.isprime(qh) is False:
            aviso = Label(pes4, text = 'ERROR PRIMOS')
            aviso.place(x=390,y=10)
        else:
            aviso = Label(pes4, text = '                             ')
            aviso.place(x=390,y=10)
        m = hashlib.shake_256(obtenerh3)
        hexa=m.hexdigest(20)
        binhash=bin(int.from_bytes(hexa.encode(), 'big'))
        benthash=int(binhash, base=2)
        benthashstr=str(benthash)
        msjhashint=int(benthashstr[:5])
        sh = (msjhashint**dh)%nh
    firmar()
    cajah6.insert(INSERT,(hexa))
    cajahf.insert(INSERT,(sh))
def getmsjh2():
    obtenerh4f = cajahf.get('1.0', END)
    def verificar():
        global msjhashintf,m1f
        nhf=int(cajanh.get())
        ehf=int(cajah3.get())
        obtenerh3f = cajah6.get('1.0', 'end-1c')
        binhashf=bin(int.from_bytes(obtenerh3f.encode(), 'big'))
        benthashf=int(binhashf, base=2)
        benthashstrf=str(benthashf)
        msjhashintf=int(benthashstrf[:5])
        m1f = (int(obtenerh4f)**ehf)%nhf
    verificar()
    if msjhashintf==m1f:
        cajah7.insert(INSERT,str('Firma válida'))
    else:
        cajah7.insert(INSERT,str('Firma inválida'))
def borrarh():
    cajah1.delete(0, 'end')
    cajah2.delete(0, 'end')
    cajah3.delete(0, 'end')
    cajah4.delete(0, 'end')
    cajanh.delete(0, 'end')    
def borrarh1():
    cajah5.delete(0, 'end')
def borrarh2():
    ingreso2.set('')
    cajah6.delete('1.0',END)
    cajahf.delete('1.0',END)
def borrarh3():
    ingreso3.set('')
    cajah7.delete('1.0',END)
botonh1 = Button(pes4, text='Llenar campos', command = primosh).place(x=80, y=90)
botonh2 = Button(pes4, text='Borrar', command = borrarh).place(x=240, y=90)
botonh3 = Button(pes4, text='Borrar', command = borrarh1).place(x=420, y=165)
botonh4 = Button(pes4, text='Firmar', command = getmsjh).place(x=420, y=260)
botonh5 = Button(pes4, text='Borrar', command = borrarh2).place(x=420, y=300)
botonh6 = Button(pes4, text='verificar', command = getmsjh2).place(x=420, y=420)
botonh7 = Button(pes4, text='Borrar', command = borrarh3).place(x=420, y=460)

#firma elgamal------------------------------

Label(pes5, text = "Firma Elgamal").place(x=10,y=10)
Label(pes5, text = "P publico: ").place(x=10,y=40)
cajag1=Entry(pes5, font='arial 8',width=13)
cajag1.place(x=10, y=60)
Label(pes5, text = "G publico: ").place(x=105,y=40)
cajag2=Entry(pes5, font='arial 8',width=13)
cajag2.place(x=105, y=60)
Label(pes5, text = "Y publico: ").place(x=200,y=40)
cajag3=Entry(pes5, font='arial 8',width=13)
cajag3.place(x=200, y=60)
Label(pes5, text = "Clave privada: ").place(x=295,y=40)
cajag4=Entry(pes5, font='arial 8',width=13)
cajag4.place(x=295, y=60)
Label(pes5, text = "Mensaje: ").place(x=190,y=130)
cajag5=Entry(pes5, font='arial 8',width=66)
cajag5.place(x=10, y=165)
Label(pes5, text = "r: ").place(x=70,y=230)
cajag6=Text(pes5, width=24, height=7)
cajag6.place(x=10, y=260)
Label(pes5, text = "s: ").place(x=300,y=230)
cajagf=Text(pes5, width=24, height=7)
cajagf.place(x=220, y=260)
Label(pes5, text = "Mensaje Verificado: ").place(x=140,y=390)
cajag7=Text(pes5, width=50, height=7)
cajag7.place(x=10, y=420)
bits=60
def primosgg():
    global pg, gg, ag, yg
    pg =Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    gg=2
    ag= randint(0, pg-1)
    yg = pow(gg,ag,pg)
    def llenargg():
        cajag1.insert(INSERT,pg)
        cajag2.insert(INSERT,gg)
        cajag4.insert(INSERT,yg)
        cajag3.insert(INSERT,ag)
    llenargg()
def getmsjgg():
    obtenerg3 = cajag5.get()  
    def firmargg():
        global hm, rg, sg, pg, gg, ag
        pg=int(cajag1.get())
        gg=int(cajag2.get())
        ag=int(cajag3.get())
        kg=2
        while (libnum.gcd(kg,pg-1)!=1):
            kg= randint(0,pg-1)
        rg = (pow(gg,kg,pg))
        invk=(libnum.invmod(kg, pg-1))
        hm=int.from_bytes(hashlib.sha256(obtenerg3.encode()).digest(),byteorder='big' )
        sg=(invk*(hm-ag*rg))%(pg-1)
    firmargg()
    cajag6.insert(INSERT,rg)
    cajagf.insert(INSERT,sg)
def getmsjgg2():
    rg1 = int(cajag6.get('1.0', END))
    sg1 = int(cajagf.get('1.0', END))
    pg=int(cajag1.get())
    yg=int(cajag4.get())
    gg=int(cajag2.get())
    hm=int.from_bytes(hashlib.sha256(cajag5.get().encode()).digest(),byteorder='big' )
    def verificargg():
        global v1,v2
        v1=(pow(yg,rg1,pg)*pow(rg1,sg1,pg))%pg
        v2=pow(gg,hm,pg)
    verificargg()
    if (v1==v2):
        cajag7.insert(INSERT,'Firma valida')
    else:
        cajag7.insert(INSERT,'Firma invalida')
def borrargg():
    cajag1.delete(0, 'end')
    cajag2.delete(0, 'end')
    cajag3.delete(0, 'end')
    cajag4.delete(0, 'end')
    cajanh.delete(0, 'end')    
def borrargg1():
    cajag5.delete(0, 'end')
def borrargg2():
    ingreso2.set('')
    cajag6.delete('1.0',END)
    cajagf.delete('1.0',END)
def borrargg3():
    ingreso3.set('')
    cajag7.delete('1.0',END)
botong1 = Button(pes5, text='Llenar campos', command = primosgg).place(x=80, y=90)
botong2 = Button(pes5, text='Borrar', command = borrargg).place(x=240, y=90)
botong3 = Button(pes5, text='Borrar', command = borrargg1).place(x=420, y=165)
botong4 = Button(pes5, text='Firmar', command = getmsjgg).place(x=420, y=260)
botong5 = Button(pes5, text='Borrar', command = borrargg2).place(x=420, y=300)
botong6 = Button(pes5, text='verificar', command = getmsjgg2).place(x=420, y=420)
botong7 = Button(pes5, text='Borrar', command = borrargg3).place(x=420, y=460)

#-------pestaña criptografia visual-------

Label(pes6, text = "Crypto visual").place(x=10,y=10)
def seleccion():
    global archivo
    archivo=filedialog.askopenfilename(title='Seleccione archivo',initialdir='C:/desktop')
    Label(pes6, text = "Imagen cargada con exito!").place(x=150,y=35)
def encrimg():
    global enc, dec, encriptada, llaveimg, llave
    # Carga la imagen
    demo = cv2.imread(archivo)
    r, c, t = demo.shape
    # crea una llave aleatoria
    llave = random.randint(256, size = (demo.shape))
    enc = demo ^ llave  # encripta
    dec = enc ^ llave  # desencripta
    cv2.imwrite("resultados/encriptada.png", enc)
    cv2.imwrite("resultados/llave.png", llave)
    encriptada=PhotoImage(file="resultados/encriptada.png")
    Label(pes6, image=encriptada).place(x=10,y=100)
    llaveimg=PhotoImage(file="resultados/llave.png")
    Label(pes6, image=llaveimg).place(x=320,y=100)
def transparencia1():
    global transparencia_1, encriptada
    transparencia_1=filedialog.askopenfilename(title='Importar transparencia 1',initialdir='C:/desktop')
    encriptada=PhotoImage(file="resultados/encriptada.png")
    Label(pes6, image=encriptada).place(x=10,y=100)
def transparencia2():
    global transparencia_2, llaveimg
    transparencia_2=filedialog.askopenfilename(title='Importar transparencia 2',initialdir='C:/desktop')
    llaveimg=PhotoImage(file="resultados/llave.png")
    Label(pes6, image=llaveimg).place(x=320,y=100)
def desencrimg():
    global desencriptada
    try:
        v1 = cv2.imread(transparencia_1)
        v2 = cv2.imread(transparencia_2)
    except:
        v1 = cv2.imread('C:/Users/Kike/Desktop/project/resultados/encriptada.png')#
        v2 = cv2.imread('C:/Users/Kike/Desktop/project/resultados/llave.png')
    dst = cv2.addWeighted(v1, 1, v2, 1, 0)
    cv2.imwrite("resultados/desencriptada.png", dst)
    desencriptada=PhotoImage(file="resultados/desencriptada.png")
    Label(pes6, image=desencriptada).place(x=170,y=350)
def borrarv():
    encriptada=PhotoImage(file="resultados/encriptada.png")
    Label(pes6, image=encriptada).place(x=10,y=100)
    Label(pes6, image=encriptada).place(x=320,y=100)
    Label(pes6, image=encriptada).place(x=170,y=350)
    Label(pes6, text = "                                                                      ").place(x=150,y=35)
botonv0 = Button(pes6, text='Seleccionar imagen', command = seleccion).place(x=10, y=33)
botonv1 = Button(pes6, text='Generar tranasparencias', command = encrimg).place(x=10, y=60)
botonv2 = Button(pes6, text='Unir transparencias', command = desencrimg).place(x=10, y=410)
botonv3 = Button(pes6, text='Importar transparencia 1', command = transparencia1).place(x=10, y=350)
botonv4 = Button(pes6, text='Importar transparencia 2', command = transparencia2).place(x=10, y=380)
botonv5 = Button(pes6, text='Borrar todo', command = borrarv).place(x=10, y=440)
ventana.mainloop()