from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from validate_docbr import CNPJ

from project.api import receitaws_api
from project.api import freterapido_api

app = Flask(__name__)


@app.route('/')
def home():
    """
    Home page from the app, root URL.
    :return:
    """
    return render_template('home.html')

@app.route('/cnpj', methods=['POST',])
def search():
    """
    Search method caller, querying in twitter api to fetch data.
    Only POST method allowed.
    :return:
    """
    inputed_data = request.form.get('cnpj')
    if not inputed_data:
        return redirect('/')
    is_cnpj = CNPJ().validate(inputed_data)
    if is_cnpj:
        ## Continuo ganhando erros de 'token inválido' e outros
        # conforme testo esta integração com a API do freterapido,
        # creio que esteja colocando algum dado inválido nesta
        test_json = '{"destinatario":{"tipo_pessoa":2,' \
                    '"cnpj_cpf":"17184406000174",' \
                    '"inscricao_estadual":"082917671",' \
                    '"endereco":{"cep":"29730000"}},' \
                    '"volumes":[{"tipo":7,"sku":"abc-teste-123",' \
                    '"descricao":"abc","quantidade":1,"altura":0.2,' \
                    '"largura":0.2,"comprimento":0.2,"peso":5,"valor":0.00,' \
                    '"volumes_produto":0,"consolidar":false,' \
                    '"sobreposto":false,"tombar":false},' \
                    '{"tipo":0,"sku":"a","descricao":"abc","quantidade":0,' \
                    '"altura":0.00,"largura":0.00,"comprimento":0.00,' \
                    '"peso":0.00,"valor":0.00,"volumes_produto":0,' \
                    '"consolidar":false,"sobreposto":false,"tombar":false}],' \
                    '"filtro":0,"canal":"aaa","limite":0,' \
                    '"codigo_plataforma":"588604ab3","cotacao_plataforma":0,' \
                    '"token":"c8359377969ded682c3dba5cb967c07b",' \
                    '"retornar_consolidacao":true}'
        get_cnpj = receitaws_api(inputed_data)
        return render_template('cnpj_screen.html',
                           hashtag=inputed_data,
                           result=get_cnpj.json(),
                           test_json=test_json)
    else:
        return render_template('home.html', message='Please, give a valid CNPJ')

@app.route('/quote', methods=['POST',])
def approve():
    """
    This method calls freterapido api to give an fiction quote
    with non real values and shows in screen the answer
    :return:
    """
    data = request.form.get('cnpj_json')
    try:
        response = freterapido_api(data)
    except Exception as err:
        return render_template('quote_screen.html',
                           status_code='500',
                           response_reason='Internal Error',
                           response='Please, verify if you gave the right '
                                    'parameters, the request to freterapido '
                                    'api crashed.')
    return render_template('quote_screen.html',
                           status_code=response.status_code,
                           response_reason=response.reason,
                           response=response.json())


if __name__ == '__main__':
    app.run(debug=True)
