import numpy as np

def jacobiMetoda(A, b, pocetIteracii, x):
    # vytvorenie matice D, v ktorej sa uloží diagonála matice A
    # teda z prvej rovnice to bude A1, z druhej A2 a z tretej A3
    D = np.diag(A)
    
    # odčítanie diagonálnych hodnôt od matice A
    R = A - np.diagflat(D)
   
    for i in range(pocetIteracii):
        x = (b - np.dot(R, x)) / D
        print(f"Po {i+1}. iterácií sú hodnoty x: x1 = {round(x[0,],5)}, "
              + f"x2 = {round(x[1,],5)}, x3 = {round(x[2,],5)}")
        
    return x
  
# definovanie vstupných premenných A, b, x, maxIt      
A = np.array([[7.0, -5.0, 2.0], 
              [1.0, 8.0, 2.0], 
              [-3.0, 1.0, 9.0]])
b = np.array([13.0, 5.0, 7.0])
zacX = np.array([0.0, 0.0, 0.0])
maxIt = 15
# zavolanie funkcie pre výpočet so zadanými vstupnými parametrami
# výstup sa uloží do premennej
vysledneX = jacobiMetoda(A,b,maxIt,zacX)

#výpis výsledných 
print(f"Výsledné hodnoty po {maxIt} iteráciach sú: x1 = {vysledneX[0,]}," 
      + f"x2 = {vysledneX[1,]}, x3 = {vysledneX[2,]}")


