import java.util.Scanner;

public class teorico {
Scanner gabo = new Scanner(System.in);
	public void teorico() {
		System.out.println("ingrese nombre del estudiante");
		String nom = gabo.nextLine();
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
           System.out.println("alumno aprobo");
       else
           System.out.println("alumno reprobo");

	}

}
