<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>Login</title>
		<link rel="stylesheet" type="text/css" href="style/codigocss.css" />
	</head>
	<body>

		<form method="POST" action="/salida">
				<b><h5>Direccion del correo de salida</h5></b><br>
				<input name="origen"     type="text" /><br>
				<b><h5>Password</h5></b><br>
				<input name="password" type="password" /><br>
				<b><h5>Correo electronico de destino</h5></b><br>
				<input name="destino"     type="text" /><br>
				<b><h5>Redactar correo:</h5></b><br>
				<textarea name="texto" rows=20 cols=100></textarea><br>

				<input type="submit" />


              </form>
              <li id="nav_estrenos"><a href="{{enlaceOauth}}">Pulsa aquí si no quieres enviar un correo y solo quieres ver tus labels usando Oauth</a></li>
		
		<!--<img SRC=""> </img>-->
	</body>
</html>

