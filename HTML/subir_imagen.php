<?php
$connection=new mysqli("localhost", "root", "10022004AlexCruz9669", "imagenes");
$carpeta = "Imagenes-pruebas/";
$archivo = $carpeta.basename($_FILES["foto"]["name"] ?? '');
$imageFileType=strtolower(pathinfo($archivo, PATHINFO_EXTENSION));

if(isset($_POST["submit"]) && isset($_FILES["foto"])){
    $check = getimagesize($_FILES["foto"]["tmp_name"]);
    if($check !== false){
        echo "El archivo es una imagen - ".$check["mime"].".";
    }else{
        echo "El archivo no es una imagen";
        exit;
    }
}

if(isset($_FILES["foto"]) && move_uploaded_file($_FILES["foto"]["tmp_name"], $archivo)){
    echo "El archivo ".htmlspecialchars(basename($_FILES["foto"]["name"]))."Ha sido subido.";
    $rutaFinal = $archivo; // Aquí se guarda la ruta final de la imagen
}else{
    echo "Error";
}

// Ahora puedes usar $rutaFinal para lo que necesites
// Por ejemplo, podrías insertarlo en tu base de datos
$sql= "INSERT INTO imagenes(Ruta_Imagen) VALUES('$rutaFinal')";
if ($connection->query($sql) === TRUE) {
    echo "Ruta de la imagen guardada con éxito!";
} else {
    echo "Error al guardar la ruta de la imagen: " . $connection->error;
}

header('Location: index.html');
exit;

