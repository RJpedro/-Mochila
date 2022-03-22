<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Problema Mochila</title>
</head>

<style>
    body{
        background-color: rgb(15,176,248,1);
    }

    button{
        display: flex; 
        position: relative; 
        align-items: center;
        justify-content: center; 
        bottom: 10%; 
        border-radius: 10px; 
        height: 70px; 
        width: 150px; 
        text-transform: uppercase; 
        border: none; 
        cursor: pointer; 
        outline: none; 
        background: rgba(15,176,248,1);
     
    }

    button::hover{
        background: rgba(15,176,248,1);
        color: #111;
        box-shadow:  0 0 50px rgba(15,176,248,1);
        transition-delay: 0.5s;
    }

    button::before{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 30px;
        height: 30px;
        border-top: 2px solid rgba(15,176,248,1);
        border-left: 2px solid rgba(15,176,248,1);
        transition: 0.5s;
        transition-delay: 0.5s;
    }

    button:hover::before{
        width: 100%;
        height: 100%;
        transition-delay: 0s;
    }

    button::after{
        content: '';
        position: absolute;
        bottom: 0;
        right: 0;
        width: 30px;
        height: 30px;
        border-bottom: 2px solid rgba(15,176,248,1);
        border-right: 2px solid rgba(15,176,248,1);
        transition: 0.5s;
        transition-delay: 0.5s;
    }

    button:hover::after{
        width: 100%;
        height: 100%;
        transition-delay: 0s;
    }

    .body-tamanho-problema{
        width: 100%; 
        height: 20vh; 
        position: relative; 
        display: flex; 
        justify-content: center; 
        align-items: center; 
        flex-direction: row;
    }

    .body-soluIncial{
        margin-top: 2.5%;
        margin-left: 6.5%;
        width: 40%; 
        height: 70vh; 
        background-color: rgb(255,255,255,0.1); 
        position: relative; 
        display: flex;  
        align-items: center; 
        flex-direction: column; 
        border-radius: 20px; 
        justify-content: space-between;
    }

    .body-resultado{
        margin-top: 2.5%;
        margin-left: 5%;
        width: 40%; 
        height: 70vh; 
        background-color: rgb(255,255,255,0.1); 
        position: relative; 
        display: flex;  
        align-items: center; 
        flex-direction: column; 
        border-radius: 20px;
    }

    input{
        outline: none;
        border-radius: 8px;
        height: 20px;   
    }

    label{
        font-size: 20px;
        color: black; 
        padding: 16px;
    }

</style>

<body style="margin: 0; padding: 0; display: flex; flex-wrap: wrap;">
    <div class="body-tamanho-problema">
        <form action="../luis.py">
            <!-- <label for="txtCapacidade">Capacidade: </label>
            <input type="number" id="txtCapacidade" name="txtCapacidade"></input>
         -->
            </div>
            <div class="body-soluIncial">
                <label>Solução Inicial </label>
            
                <button type="submit" id="btn_Exec" name="btn_Exec">Voltar</button>
            </div>
            <div class="body-resultado">
                <label>Ambiente: </label>
                {{ participantes }}
                <label>Candidatos Escolhidos: </label>
                {{ candidatos }}
                <label>Média das Notas dos Candidatos escolhidos: </label>
                {{ avalia }}
            </div>
        </form>
</body>
</html>