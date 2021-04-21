from __future__ import annotations


class Facade:
    """
    The Facade class provides a simple interface to the complex logic of one or
    several subsystems. The Facade delegates the client requests to the
    appropriate objects within the subsystem. The Facade is also responsible for
    managing their lifecycle. All of this shields the client from the undesired
    complexity of the subsystem.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
        Depending on your application's needs, you can provide the Facade with
        existing subsystem objects or force the Facade to create them on its
        own.
        """

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
        The Facade's methods are convenient shortcuts to the sophisticated
        functionality of the subsystems. However, clients get only to a fraction
        of a subsystem's capabilities.
        """

        results = []
        results.append("FACHADA MOSTRANDO RESULTADO ")
        print("INICIALIZANDO FACHADA")
        if (self._subsystem1.operation1()) == "laboratorio":
            results.append(self._subsystem1.operation2())
            results.append(self._subsystem2.operation3())  
        else:
            results.append(self._subsystem1.operation2())
            results.append(self._subsystem2.operation4()) 
         
        return "\n".join(results)



class Subsystem1:
    """
    The Subsystem can accept requests either from the facade or client directly.
    In any case, to the Subsystem, the Facade is yet another client, and it's
    not a part of the Subsystem.
    """

   
    def operation1(self) -> str:
       print("ingrese el tipo de materia a evaluar laboratorio o teorico")
       dato = input()
       if dato == "laboratorio":
        return "laboratorio"
       else:
           return "teoricas"
    def operation2(self) -> str:
         print ("ingrese el nombre del estudiante")
         nombre = input()
         return nombre




class Subsystem2:
    """
    Some facades can work with multiple subsystems at the same time.
    """

    def operation3(self) -> str:
        nl = int(input("ingrese el numero de laboratorios a evaluar "))
        nl2 = int(input("ingrese por cuanta nota se evaluara los laboratorio "))
        t= int(nl2*nl)
        total = int (0) 
        for i in range(0,nl):
            nt= int(input("ingrese nota del laboratorio obtenida por el estudiante :  "))
            total = total + nt
        print("nota final")
        print(total)
        if total > t/2:
           return "aprobado"
        else:
           return "reprobado"

    def operation4(self) -> str:
        nl = int(input("Ingrese el numero de examnes que tomara"))
        print("ingrese por cuanta nota elvaluara cada examen")
        t = 0
        for j in range (0,nl):
           nl2 = int(input("por cuanta nota evaluara este examen "))
           t += nl2
        total = int (0) 
        for i in range(0,nl):
            nt= int(input("ingrese nota obtenida por el estudiante  :  "))
            total = total + nt
        print("nota final")
        print(total)
        if total > t/2:
           return "aprobado"
        else:
           return "reprobado"


def client_code(facade: Facade) -> None:
    """
    The client code works with complex subsystems through a simple interface
    provided by the Facade. When a facade manages the lifecycle of the
    subsystem, the client might not even know about the existence of the
    subsystem. This approach lets you keep the complexity under control.
    """

    print(facade.operation(), end="")


if __name__ == "__main__":
    # The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances.
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)