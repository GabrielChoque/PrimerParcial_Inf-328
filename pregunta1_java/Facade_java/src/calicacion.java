import java.util.Scanner;

public class calicacion {
	Scanner gabo = new Scanner(System.in);
		public boolean calificacion(String dato) {
			
			if (dato.equals("laboratorio")) {
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
		                return true;
		            else
		               return false;
		        }
			else {
				System.out.println("Ingrese el numero de examnes que tomara : \n");
		         int nl = gabo.nextInt();
		         System.out.println("ingrese por cuanta nota elvaluara cada examen ");
		        int t = 0;
		        int nl2 = 0;
		        for (int i =1 ; i<= nl ; i++){
		            System.out.println("por cuanta nota evaluara este examen : \n");
		            nl2 = gabo.nextInt();
		             t += nl2;
		        }
		          
		        int total =0;
		        int nt = 0;
		        for(int i = 1 ; i<= nl; i++){
		            System.out.println("ingrese nota obtenida por el estudiante  :  \n");
		            nt = gabo.nextInt();
		            total = total + nt;
		        }
		            
		        System.out.println("nota final : \n");
		        System.out.println(total);
		        if (total > t / 2)
		            return true;
		        else
		            return false;

				
			}
				
			
		}
		public String materia() {
			System.out.println("ingrese el tipo de materia a calificar laboratorio o teorica");
			String materia = gabo.nextLine();
			return materia;
		}
		public String nombre() {
			System.out.println("el nombre del estudiante a calificar");
			String nombre = gabo.nextLine();
			return nombre;
		}
		

}
