# Globo-Desafio

#### Desafio:
  **Criar uma aplicação controle que receba tweets de determinada hashtag configurável e moderar-los**


Este desafio foi feito utilizando as tecnologias Python, Flask, Bootstrap e Docker, portanto para executar este código será necessário no mínimo que você tenha Python e Docker instalados no seu computador, caso não os tenha ainda aqui estão alguns links úteis:

* **[Documentação oficial do Docker](https://docs.docker.com/get-docker/)**
* **[Site oficial do Python](https://python.org.br/)**


Feito estes dois passos seu sistema operacional está pronto para rodar esta aplicação, como qualquer repositório público do Github você têm total acesso a esta aplicação e inclusive pode criar pull requests para esta branch com melhorias caso queira contribuir com a comunidade. 

Ao clonar este repositório para o seu local você estará apto a rodar a aplicação, basta buildar a imagem do container como exemplo de código abaixo:

```
docker build -t flask-app:latest .
```
E logo após poderá rodar-lo com o código a seguir:

```
docker run -p 8000:8000 flask-app
```

Com este comando você fará seu docker rodar a aplicação na porta 8000, em questão de segundos aparecerá no seu terminal uma mensagem do tipo 

>* Running on **[http://0.0.0.0:8000/](http://0.0.0.0:8000/)**

Pronto, sua aplicação está rodando e pronta para ser usada, basta clicar no link fornecido pelo seu terminal ou abrir um navegador, não se preocupe em gravar estes códigos mencionados acima, basta gravar um bem simples, este:

```
make
```

Ao executar este código aparecerá na sua tela 2 comandos que eu deixei pré-gravados no Makefile, um deles chamado 'make build' e outro chamado 'make run', os comandos anteriormente mencionados foram gravados nestes atalhos respectivamente para facilitar o uso, espero que tenha sido útil de alguma forma.