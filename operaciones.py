
import math
import sympy as sy
from matplotlib import pyplot as plt


def resolverTeoremaResiduo(singularidad, orden, m, n, a, b, c) :
    
    z = sy.symbols('z')
    
    #parte1 = 1/(m-1)!
    #parte2 = diferencial
    
    parte1 = 1 / math.factorial(orden - 1);
    
    parte2 = sy.diff(((z - singularidad)**orden) * ((z**n) / (((z - (a * complex(0,1)))**m) * (z-b) * ((z+ (c*complex(0, 1)))**4))), z, orden - 1).evalf(subs = {z:singularidad})
    
    resultado = parte1 * parte2;
    
    return resultado

def resolverIntegralTeoremaResiduo (m, n, a, b, c, radio):
    
    residuos = [];
    residuos.append(0);
    residuos.append(0);
    residuos.append(0);
    
    z0 = complex(0, a) 
    z1 = complex(b, 0)
    z2 = complex(0, -c)
    
    print("\nSingularidades encontradas: ")
    print("\nSingularidad z0: ", z0)
    print("Singularidad z1: ", z1)
    print("Singularidad z2: ", z2)
    
    graficarCirculo(0 , 0, radio, z0, z1, z2)
    
    if (radio == a or radio == b or radio == -c or -radio == a or -radio == b or -radio == -c) :
        print ("\n\nEl resultado es INDEFINIDO, porque un zi toca la curva")
        exit();
    
    if (-radio < a < radio ) :
        residuos[0] = resolverTeoremaResiduo(z0, m, m, n, a, b, c)
        print("\nResiduo [f(z), " + "z0 = " + str(z0) + ", orden = " + str(m) + "] = " , residuos[0])
    else: 
       print("\nLa singularidad z0 no se encuentra dentro del radio") 
        
    if (-radio < b < radio) :
        residuos[1] = resolverTeoremaResiduo(z1, 1, m, n, a, b, c)
        print("Residuo [f(z), " + "z1 = " + str(z1) + ", orden = " + str(1) + "] = " , residuos[1])
    else: 
        print("La singularidad z1 no se encuentra dentro del radio") 
    
    if (-radio < -c < radio) :   
        residuos[2] = resolverTeoremaResiduo(z2, 4, m, n, a, b, c)
        print("Residuo [f(z), " + "z2 = " + str(z2) + ", orden = " + str(4) + "] = " , residuos[2]) 
    else: 
        print("La singularidad z2 no se encuentra dentro del radio")
        
    
    sumaResiduos = 0  
    
    print("\nSumando residuos...")
    for i in range(3):
        sumaResiduos += residuos[i]
    
    print("\nResultado expresado:  2πi * ( " + str(sumaResiduos) + " )");
    
    return complex(2) * complex(math.pi) * complex(0,1) * complex(sumaResiduos);

def graficarCirculo(h, k, radio, z0, z1, z2):
    axes = plt.subplots()[1]
    draw_circle = plt.Circle((h, k), radio, color = "g", fill=False)

    x_min = h - radio # datosCirculo[0] = h
    x_max = h + radio # datosCirculo[1] = k
    y_min = k - radio # datosCirculo[2] = r
    y_max = k + radio

    plt.title('GRAFICA GENERAL')
    plt.axis([x_min - 1, x_max + 1, y_min - 1, y_max + 1])
    plt.scatter(h, k, color="red")

    axes.set_xlabel("Reales")
    axes.set_ylabel("Imaginarios")

    axes.set_aspect(1)
    axes.add_artist(draw_circle)

    plt.axhline(0, color="black")
    plt.axvline(0, color="black")

    plt.scatter(z0.real, z0.imag, color="blue")
    plt.scatter(z1.real, z1.imag, color="orange")
    plt.scatter(z2.real, z2.imag, color="black")
    
    plt.grid()
    plt.show()
    
    

    
    