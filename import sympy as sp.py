<?php
$directorio = "uploads/";
if (!file_exists($directorio)) {
    mkdir($directorio, 0777, true);
}

if (isset($_FILES["archivo"]) && $_FILES["archivo"]["error"] == 0) {
    $titulo = htmlspecialchars($_POST["titulo"]);
    $nombreArchivo = basename($_FILES["archivo"]["name"]);
    $rutaDestino = $directorio . $nombreArchivo;

    $tipo = strtolower(pathinfo($rutaDestino, PATHINFO_EXTENSION));

    // Validar tipo de archivo
    if ($tipo != "pdf" && $tipo != "txt") {
        die("❌ Solo se permiten archivos PDF o TXT.");
    }

    if (move_uploaded_file($_FILES["archivo"]["tmp_name"], $rutaDestino)) {
        echo "<h2>✅ Archivo subido correctamente</h2>";
        echo "<p><strong>Título:</strong> $titulo</p>";
        echo "<p><strong>Archivo guardado en:</strong> <a href='$rutaDestino' target='_blank'>$nombreArchivo</a></p>";
        echo "<p><a href='index.html'>⬅️ Volver al inicio</a></p>";
    } else {
        echo "❌ Error al subir el archivo.";
    }
} else {
    echo "⚠️ No se recibió ningún archivo.";
}
?>
