<html>
	<head>
		<title>Login</title>
	</head>
	<body>
		<link rel="stylesheet" type="text/css" href="codigocss2.css" />
  
			<b><h4>Dirección del correo de salida</h4></b>
			<b><h5>{{CorreoOrigen}}</h5></b><br><br>
			<br>
			<b><h4>Direccion de correo destino</h4></b>
			<b><h5>{{CorreoDestino}}</h5></b><br><br>

			<b><h4>Correo enviado</h4></b>
			<b><h5>{{contenido}}</h5></b><br><br>
			<ul>
			%for label in labels:
			<li>{{label}}</li>
			%end
			</ul>


		
		<!--<img SRC=""> </img>-->
	</body>
</html>
