# Freterapido-api

##### Criar uma api qual receba um CNPJ e faça consulta na [RECEITAWS](https://receitaws.com.br/api) dando um retorno para o usuário. Assim como receber um JSON e fazer uma cotação fictícia na rota do [FRETERAPIDO](https://freterapido.com/sandbox/api/external/embarcador/v1/quote-simulator) 


Esta api foi feita utilizando as tecnologias Python, Flask, Bootstrap e Docker, portanto para executar este código será necessário no mínimo que você tenha Python e Docker instalados no seu computador, caso não os tenha ainda aqui estão alguns links úteis:

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

Ao executar este código aparecerá na sua tela 2 comandos que eu deixei pré-gravados no Makefile, um deles chamado 'make build' e outro chamado 'make run', os comandos anteriormente mencionados foram gravados nestes atalhos respectivamente para facilitar o uso.

## Utilização da API

Esta API têm duas rotas, uma delas é:


```
http:0.0.0.0:8000/cnpj/{number}
```

Onde aceita apenas métodos GET e será necessário passar no lugar de '{number}' um número de CNPJ que você queira como parametro, conforme exemplo em request feito pelo terminal abaixo:

![all text](https://i.imgur.com/i8qn5TN.png)

É claro, você é livre para usar o método de request que quiser, este foi só um exemplo, seguindo a segunda e última rota é:

```
http:0.0.0.0:8000/quote
```

Nesta serão aceitos requests apenas no método POST, enviando um JSON com as informações necessárias aparecerá o retorno desejado.

####Como uma nota: 

Notei dois pontos durante este desafio, o primeiro é que na [documentação](https://dev.freterapido.com/api-ecommerce.html#!#content_simulacao) mostra claramente que no destinatário se o 'tipo_pessoa' for 2, então é pessoa jurídica e serão obrigatórios outros 2 campos, mas ao testar colocando tipo 1 e ainda assim os campos de cnpj e inscrição estadual (que são obrigatórios apenas para pessoa jurídica) a API não retorna erro, deixa acontecer. O campo cpf_cnpj era pra ser obrigatório nos 2 casos, mas como na documentação diz que só é obrigatório no caso de 'tipo_pessoa' = 2, deixei sem tratativa pra isto, mas na minha visão seria bom dar uma olhada nisto.

O segundo ponto, no PDF, onde consta o link da URL para requisição do POST, se você clicar coloca um '/sandbox/' no meio da URL depois de '.com' e antes de '/api/' quando a URL que está escrita não tem sandbox, seria bom consertar o link no PDF para futuros desafios. 