<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Login</title>
		<link rel="stylesheet" type="text/css" href="style/codigocss2.css" />
	</head>
	<body>
		
			<img style="float:right;" src="/style/logo.png" alt="logotipo" />
			<b><h4>Dirección del correo de salida</h4></b>
			<b><h5>{{CorreoOrigen}}</h5></b><br><br>
			<br>
			<b><h4>Direccion de correo destino</h4></b>
			<b><h5>{{CorreoDestino}}</h5></b><br><br>

			<b><h4>Correo enviado</h4></b>
			<b><h5>{{contenido}}</h5></b><br><br>
			<br><br><br>
			<b><h4>Labels</h4></b>
			<ul>
			%for label in labels:
			<li><h5>{{label}}</h5></li>
			%end
			</ul>


		
		<!--<img SRC=""> </img>-->
	</body>
</html>
