<h1 align="center"> <b> Portfolio </b> </h1>

<ul>
  <li> <b> Nome: </b> Gabriel da Cunha de Macedo
  <li> <b> Curso: </b> Desenvolvimento de Softwares Multiplataformas
</ul>
  
<h1 align="center"> <b> Pastas </b> </h1>
<ul>
  <li> <b> doc -> </b> Pasta contendo documentos, sendo ele exclusivamente o arquivo .pdf do Wireframe do portfolio para dispositivos Mobile
  <li> <b> src -> </b> Pasta com todo o código fonte 
    <ul> 
    <li> <b> templates -> </b> Pasta contendo todos os arquivos .html do portfolio
    <li> <b> static -> </b> Pasta contendo o .css
      <ul>
        <li> <b> image -> </b> Pasta contendo todas as imagens do portfolio.
      </ul>
    </ul>
</ul>
<h1 align="center"> <b> Executando local </b> </h1>
Depois de baixar o [Python](https://www.pyth.org/download/) e clonar o projeto:

``` powershell
# Acesse a pasta do projeto por meio do terminal
cd src

# Instale as dependências
pip install -r requirements.txt
      
# Configure a variável de ambiente FLASK_APP
set FLASK_APP=app.py

# Executar a aplicação
flask run

# O site estará disponível através do link: http://localhost:5000/ ou http://127.0.0.1:5000/

