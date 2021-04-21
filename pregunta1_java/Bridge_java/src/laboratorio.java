import java.util.Scanner;

public class laboratorio {
Scanner gabo = new Scanner(System.in);
	public void laboratorio() {
		System.out.println("ingrese nombre del estudiante");
		String nom = gabo.nextLine();
		 System.out.println("ingrese numero de laboratorios a evaluar : \n");
         int nl = gabo.nextInt();
         System.out.println("ingrese por cuanta nota evaluara cada laboratorio  : \n");
         int nl2 = gabo.nextInt();
         int t= (nl2*nl);
         int total = 0;
         int nt = 0;
         for (int i = 1; i <= nl; i++)
         {
             System.out.println("ingresde nota del laboratorio obtenida por el estudiante : \n ");
              nt = gabo.nextInt();
             total = total + nt;
         }
             
         System.out.println("nota final: \n");
         System.out.println(total);
         if (total > t/2)
        	 
             System.out.println("alumno "+ nom +" aprobado ");
         else
            System.out.println("alumno "+ nom + " reprobado ");
	}

}
