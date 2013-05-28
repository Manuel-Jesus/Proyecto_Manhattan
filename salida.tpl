<html>
  <head>
		<title>Login</title>
	</head>
	<body>
  
			<b>Dirección del correo de salida</b><br>	
			<b>{{CorreoOrigen}}</b><br><br>
			<br>
			<b>Direccion de correo destino</b><br>
			<b>{{CorreoDestino}}</b><br><br>

			<b>Correo enviado</b><br>
			<b>{{contenido}}</b><br><br>
		
			<ul>
			%for label in labels:
			<li>{{label}}</li>
			%end
			</ul>


		
		<!--<img SRC=""> </img>-->
	</body>
</html>
