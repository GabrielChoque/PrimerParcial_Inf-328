<title></title>
<h2>datos</h2>
<form method="GET" action="http://localhost:15349/WebApplication1/NewServlet">
	Nombre: <input type="text" name="nombre"/><br/><br/>
	Apellido: <input type="text" name="apellido"/><br/><br/>
	<input type="submit" name="Enviar"/>
	<br/> <br/> <br/>
	<input type="hidden" name="tiempo_php">
</form>
<script type="text/javascript">
	var d = new Date().toLocaleDateString().concat(" ", new Date().getHours(), ":", new Date().getMinutes(), ":", new Date().getSeconds());
	document.write(d);
	document.forms[0].elements[3].value=d;
</script>