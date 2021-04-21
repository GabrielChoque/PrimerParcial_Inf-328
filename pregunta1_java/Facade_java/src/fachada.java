

public class fachada {
   private calicacion materia = new calicacion();
   private calicacion nombre = new calicacion();
   private calicacion calificacion = new calicacion();
	public void fachada() {
		String nom = materia.nombre();
	
		String mat= materia.materia();
		
		if (calificacion.calificacion(mat)) {
			System.out.println(nom);
			System.out.println("APROBO");
		}else {
			System.out.println(nom);
			System.out.println("REPROBO");
		} 
		
	}

}
