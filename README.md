# Globo-Desafio

#### Desafio:
  **Criar uma aplicação controle que receba tweets de determinada hashtag configurável e moderar-los**


Este desafio foi feito utilizando as tecnologias Python, Flask e Docker, portanto para executar este código será necessário no mínimo que você tenha Python e Docker instalados no seu computador, caso não os tenha ainda aqui estão alguns links úteis:

**[Documentação oficial do Docker](https://docs.docker.com/get-docker/)**:
Neste link do Docker você é levado direto para a página onde pode selecionar seu sistema operacional e fazer a instalação de acordo.


**[Site oficial do Python](https://python.org.br/)**:
No site do python você precisa clicar em "Inicie-se" no topo da página, aparecerá um dropdown com algumas opções, entre elas as de instalação da linguagem nos sistemas operacionais Windows, Mac e Linux (Se você utiliza Linux ou Mac é bem improvável que não tenha python instalado), basta selecionar o seu e seguir o tutorial.


Feito estes dois passos seu sistema operacional está pronto para rodar esta aplicação, como qualquer repositório público do Github você têm total acesso a esta aplicação e inclusive pode criar pull requests para esta branch com melhorias caso queira contribuir com a comunidade.

Nesta minha pagina do Github onde se encontra esta aplicação existe logo acima na direita um botão verde escrito "Clone or download", clicando nele terá uma URL com clipboard e um botão 'Download ZIP', pode clicar no clipboard que ficará gravado no seu 'colar' a URL necessária, agora, abrindo um terminal seu, vá para uma pasta sua de projetos ou uma pasta vazia e coloque o seguinte comando (usuários Windows têm opção extra de 'Clone in desktop')
```
git clone https://github.com/Pabl0Azeved0/Globo-Desafio.git
```

Apenas adicionei 'git clone' a URL copiada pelo Github, então pode digitar no terminal 'git clone' e logo após colar, executando este comando você irá clonar a pasta da aplicação pra sua pasta local pelo terminal, agora restam apenas mais dois passos para que você possa rodar e testar a aplicação, primeiro precisaremos criar uma imagem do docker

```
docker build -t flask-app:latest .
```

Caso de erro de permissão coloque um sudo na frente e a sua senha, irá levar alguns segundos para criar sua imagem do container, uma vez que tenha finalizado você notará que o terminal estará habilitado novamente e logo acima terá uma hash grande, é o ID do seu container, mas não se preocupe, não precisa gravar isto para o próximo passo, hora de rodar a aplicação

```
docker run -p 8000:8000 flask-app
```

Com este comando você fará seu docker rodar a aplicação na porta 8000, em questão de segundos aparecerá no seu terminal uma mensagem do tipo 
>* Running on **[http://0.0.0.0:8000/](http://0.0.0.0:8000/)**

Será um link clicável exatamente igual apareceu aqui pra você, com isto você terá a opção de clicar ali ou abrir um navegador você mesmo e digitar a URL mencionada, pronto, a aplicação estará aberta e pronta pra ser usada, creio eu que ela seja bem intuitiva então não se preocupe, você saberá o que fazer daqui pra frente, espero que goste!
