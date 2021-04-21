from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
  

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraccion de materia, nombre y notas del estudiante : \n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    
    def operation(self) -> str:

        return (f"Abstraccion de materia, nombre y notas del estudiante : \n"
                f"{self.implementation.operation_implementation()}")
           
        


class Implementation(ABC):
  

    @abstractmethod
    def operation_implementation(self) -> str:
        pass




class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        nombre = input("ingrese nombre del estudiante \n")
        nl = int(input("ingrese el numero de laboratorios a evaluar \n"))
        nl2 = int(input("ingrese por cuanta nota se evaluara los laboratorio\n "))
        t= int(nl2*nl)
        total = int (0) 
        for i in range(0,nl):
            nt= int(input("ingrese nota del laboratorio obtenida por el estudiante :  \n"))
            total = total + nt
        print("nota final \n")
        print(total)
        if total > t/2:
            return "aprobado"
        else:
             return "reprobado"
        
            





class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:

        nl = int(input("Ingrese el numero de examnes que tomara"))
        print("ingrese por cuanta nota elvaluara cada examen \n")
        t = 0
        for j in range (0,nl):
            nl2 = int(input("por cuanta nota evaluara este examen \n"))
            t += nl2
        total = int (0) 
        for i in range(0,nl):
            nt= int(input("ingrese nota obtenida por el estudiante  :  \n"))
            total = total + nt
        print("nota final\n")
        print(total)
        if total > t/2:
                return "aprobado"
        else:
                return "reprobado"   



def client_code(abstraction: Abstraction) -> None:
  

    print(abstraction.operation(), end="")



if __name__ == "__main__":
   

    materia = input("ingrese materia a revisar laboratorio o teorica :  \n")
    if materia == "laboratorio":
          implementation = ConcreteImplementationA()
          abstraction = Abstraction(implementation)
          client_code(abstraction)
    else:
        implementation = ConcreteImplementationB()
        abstraction = ExtendedAbstraction(implementation)
        client_code(abstraction)



    