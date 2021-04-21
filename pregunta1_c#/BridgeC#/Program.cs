using System;

namespace RefactoringGuru.DesignPatterns.Bridge.Conceptual
{
    // The Abstraction defines the interface for the "control" part of the two
    // class hierarchies. It maintains a reference to an object of the
    // Implementation hierarchy and delegates all of the real work to this
    // object.
    class Abstraction
    {
        protected IImplementation _implementation;

        public Abstraction(IImplementation implementation)
        {
            this._implementation = implementation;
        }

        public virtual string Operation()
        {
            return "Abstraccion de los materia y nombre del estudiante \n" +
                _implementation.OperationImplementation();
        }
    }

    // You can extend the Abstraction without changing the Implementation
    // classes.
    class ExtendedAbstraction : Abstraction
    {
        public ExtendedAbstraction(IImplementation implementation)
            : base(implementation)
        {
        }

        public override string Operation()
        {
            return "Abstraccion de los materia y nombre del estudiante \n" +
                base._implementation.OperationImplementation();
        }
    }

    // The Implementation defines the interface for all implementation classes.
    // It doesn't have to match the Abstraction's interface. In fact, the two
    // interfaces can be entirely different. Typically the Implementation
    // interface provides only primitive operations, while the Abstraction
    // defines higher- level operations based on those primitives.
    public interface IImplementation
    {
        string OperationImplementation();
    }

    // Each Concrete Implementation corresponds to a specific platform and
    // implements the Implementation interface using that platform's API.
    class ConcreteImplementationA : IImplementation
    {
        public string OperationImplementation()
        {
            Console.WriteLine("ingrese nombre del estudiante : \n");
            String nombre = Console.ReadLine();
            Console.WriteLine("ingrese el numero de laboratorios a evaluar :  \n");
             int nl = Convert.ToInt32(Console.ReadLine());
             Console.WriteLine("ingrese por cuanta nota evaluara los laboratorios");
             int nl2 = Convert.ToInt32(Console.ReadLine());
             int t= nl2*nl;
             int total = 0; 
             for (int i = 0 ; i< nl ; i++){
                 Console.WriteLine("ingrese nota del laboratorio obtenida por el estudiante :  \n");
                 int nt= Convert.ToInt32(Console.ReadLine());
                 total = total + nt;
             }
           
        Console.WriteLine("nota final : \n");
        Console.WriteLine(total);
        if (total > t / 2)
            return "aprobado";
        else
            return "reprobado";
        
        }
    }

    class ConcreteImplementationB : IImplementation
    {
        public string OperationImplementation()
        {
        Console.WriteLine("Ingrese el numero de examnes que tomara : \n");
        int nl = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("ingrese por cuanta nota elvaluara cada examen : \n");
        int t = 0;
        for (int i = 0 ; i< nl ; i++){
            Console.WriteLine("por cuanta nota evaluara este examen : \n");
            int nl2 = Convert.ToInt32(Console.ReadLine());
            t += nl2;
        }
            
        int total = 0; 
       for (int i = 0 ; i< nl ; i++){
           Console.WriteLine("ingrese nota obtenida por el estudiante  :  \n");
            int nt= Convert.ToInt32(Console.ReadLine());
            total = total + nt;
       }
        Console.WriteLine("nota final : \n");
        Console.WriteLine(total);
        if (total > t/2)
                return "aprobado";
        else
                return "reprobado"; 

        }
    }

    class Client
    {
        // Except for the initialization phase, where an Abstraction object gets
        // linked with a specific Implementation object, the client code should
        // only depend on the Abstraction class. This way the client code can
        // support any abstraction-implementation combination.
        public void ClientCode(Abstraction abstraction)
        {
            Console.Write(abstraction.Operation());
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Client client = new Client();

           
            // The client code should be able to work with any pre-configured
            // abstraction-implementation combination.
            Console.WriteLine("ingrese el tipo de materia a revisar laboratorio o teorica");
            string materia = Console.ReadLine();
            Abstraction abstraction;
            if (materia == "laboratorio")
            {
                abstraction = new Abstraction(new ConcreteImplementationA());
                client.ClientCode(abstraction);
            }
            else {
                abstraction = new ExtendedAbstraction(new ConcreteImplementationB());
                client.ClientCode(abstraction);
            }
            

            Console.WriteLine();

            
            Console.ReadLine();
        }
    }
}