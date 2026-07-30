<?php

// Configurações do banco
$host    = "sql312.infinityfree.com";        // substituir
$usuario = "if0_42533317";        // substituir
$senha   = "jzUsfDJahNd";        // substituir
$banco   = "if0_42533317_newdent";        // substituir

// Conexão MySQLi
$conexao = mysqli_connect($host, $usuario, $senha, $banco);

if (!$conexao) {
    die("Erro na conexão: " . mysqli_connect_error());
}

echo "Conexão realizada com sucesso!";
?>