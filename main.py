
import operaciones as operacion
import sympy as sy


if __name__ == "__main__":
    
    opc = 's';
    
    while (opc == 's' or opc == 'S') :
    
        print("\n-----BIENVENIDO A CALCULADORA DE INTEGRALES POR EL TEOREMA DEL RESIDUO------")
        
        print("\tz^n / (z-ai)^m (z-b) (z+ci)^4")
        
        n = int(input("\nn:"))
        m = int(input("m:"))
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        r = float(input("r:"))
        
        z = sy.symbols('z')
        
        resultadoFinal = operacion.resolverIntegralTeoremaResiduo(m, n, a, b, c, r)
        
        print("El resultado final es: ", resultadoFinal)
        
        opc = input("\n\nDeseas resolver otro caso? s/n \nRespuesta: ")
        
        
            


        
        
    
