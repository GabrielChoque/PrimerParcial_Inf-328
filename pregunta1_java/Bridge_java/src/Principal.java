import java.util.Scanner;


public class Principal {

	public static void main(String[] args) {
		Scanner gabo = new Scanner(System.in);
		System.out.println("Bridge iniciado");
		System.out.println("ingrese el tipo de materia a calificar  laboratorio o teorico");
        String mat = gabo.nextLine();
        if (mat.equals("laboratorio")) {
        	AbsLyT bridge = new AbsRefinada(new laboratorio());
			bridge.laboratorio();
        	
        }else {
        	
        }
		

	}

}
