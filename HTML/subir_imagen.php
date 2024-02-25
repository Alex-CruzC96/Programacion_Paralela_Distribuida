<?php
$connection=new mysqli("localhost", "root", "10022004AlexCruz9669", "optilent");
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

if(isset($_FILES["foto"]) && !move_uploaded_file($_FILES["foto"]["tmp_name"], $archivo)){
    switch ($_FILES['foto']['error']) {
        case UPLOAD_ERR_INI_SIZE:
            $message = "El archivo cargado excede el tamaño máximo permitido.";
            break;
        case UPLOAD_ERR_FORM_SIZE:
            $message = "El archivo cargado excede el tamaño máximo permitido por el formulario.";
            break;
        case UPLOAD_ERR_PARTIAL:
            $message = "El archivo fue sólo parcialmente cargado.";
            break;
        case UPLOAD_ERR_NO_FILE:
            $message = "No se cargó ningún archivo.";
            break;
        case UPLOAD_ERR_NO_TMP_DIR:
            $message = "Falta la carpeta temporal.";
            break;
        case UPLOAD_ERR_CANT_WRITE:
            $message = "Falló al escribir el archivo en el disco.";
            break;
        case UPLOAD_ERR_EXTENSION:
            $message = "Una extensión de PHP detuvo la carga del archivo.";
            break;

        default:
            $message = "Error desconocido.";
            break;
    }
    echo $message;
}
header('Location: index.html');
exit;

