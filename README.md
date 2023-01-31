<h1 align="center">Mercado Livre -> Melhor Anúncio</h1>

<br>

## :dart: Sobre ##

Os golpes onlines vem aumentando cada vez mais com isso o Mercado Livre é um alvo dos bandidos, para isso desenvolvi uma versão inicial de um programa capaz de analisar anúncios sobre um determinado produto e retornar então um item que seja confiável, retornando o título, valor e o link do produto. Foi utilizado Docker com objetivo de escalar o processo. Para transmissão de dados, criei um servidor UDP com multithreading, aumentando a performance do aplicativo. Contém alguns bugs, mas é um excelente protótipo. 

## :sparkles: Features ##

:heavy_check_mark: Selenium - Usado para fazer webscrappy da página\
:heavy_check_mark: UDP - Servidor UDP com multithreading\
:heavy_check_mark: Docker - Utilizado para escalar

## :rocket: Tecnologias ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Selenium 4](https://www.selenium.dev/)


## :checkered_flag: Iniciando ##

```bash
# Clone o repositório
$ git clone https://github.com/murilosimao/MLBestPrice.git

# Acesse a pasta
$ cd MLBestPrice

# Contrua a imagem Docker
$ docker build --tag bestprice:msimao .

# Rode o container
$ docker run -p 8080:8080/udp bestprice:msimao

# Rode o client.py
$ python client.py
```

## :memo:  ##

Made with :heart: by <a href="https://github.com/murilosimao" target="_blank">MuriloSimão</a>

&#xa0;

<a href="#top">Ir para o ínicio</a>
