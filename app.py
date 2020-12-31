import json

from flask import Flask
from flask import jsonify
from flask import request
from validate_docbr import CNPJ

from project.api import receitaws_api
from project.api import freterapido_api

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def home():
    """
    Home page from the app, root URL.
    :return:
    """
    return 'Welcome to freterapido API. Access README to more information about this API.'


@app.route('/cnpj/<int:cnpj>', methods=['GET',])
def search(cnpj):
    """
    Search method caller, querying in twitter api to fetch data.
    Only POST method allowed.
    :return:
    """
    try:
        is_cnpj = CNPJ().validate(str(cnpj))
        if is_cnpj:
            get_cnpj = receitaws_api(cnpj)
            response = formatted_receitaws(json.loads(get_cnpj.text))
            return jsonify(response), 200
        else:
            return jsonify({'Invalid_cnpj': 'Please, give a valid CNPJ'}), 404
    except Exception as err:
        return jsonify({'Unexpected Error:': err}), 500


@app.route('/quote', methods=['POST',])
def approve():
    """
    This method calls freterapido api to give an fiction quote
    with non real values and shows in screen the answer
    :return:
    """
    try:
        data = json.loads(request.data)
        errors = validate_data(data)
        if errors:
            return jsonify(errors), 403
        response = freterapido_api(data)
        formated_response = formatted_data(json.loads(response.text))
        return jsonify(formated_response), 200
    except Exception as err:
        return jsonify({'Unexpected error': err}), 500


def formatted_receitaws(data):
    """
    This method only use is to format the receitaws API response to the pattern
    that is asked in freterapido challenge, made in a way that it gets the value
    or fill it with an empty string
    :param data:
    :return:
    """
    formatted_data = {
        "empresa": {
            "cnpj": data.get('cnpj', ''),
            "ultima_atualizacao": data.get('ultima_atualizacao', ''),
            "abertura": data.get('abertura', ''),
            "nome": data.get('nome', ''),
            "fantasia": data.get('fantasia', ''),
            "status": data.get('status', ''),
            "tipo": data.get('tipo', ''),
            "situacao": data.get('situacao', ''),
            "capital_social": data.get('capital_social', ''),
            "endereco": {
                "bairro": data.get('bairro', ''),
                "logradouro": data.get('logradouro', ''),
                "numero": data.get('numero', ''),
                "cep": data.get('cep', ''),
                "municipio": data.get('municipio', ''),
                "uf": data.get('uf', ''),
                "complemento": data.get('complemento', '')
            },
            "contato": {
                "telefone": data.get('telefone', ''),
                "email": data.get('email', '')
            },
            "atividade_principal": [
                {
                    "text":
                        data.get('atividade_principal', [{'a': '', 'b': ''}])[
                            0].get('text', ''),
                    "code":
                        data.get('atividade_principal', [{'a': '', 'b': ''}])[
                            0].get('code', '')
                }
            ]
        }
    }
    return formatted_data


def validate_data(data):
    """
    This method checks if the json data inputed by the user is valid,
    accordingly with the documentation found in
    https://dev.freterapido.com/api-ecommerce.html#!#content_simulacao
    If the documentation at any time, is updated, this code's gonna need
    to be revisited
    :param data:
    :return:
    """
    errors = list()
    required_fields = {'remetente': 'cnpj',
                       'destinatario': ['tipo_pessoa', 'endereco'],
                       'volumes': ['tipo', 'quantidade', 'altura', 'largura',
                                  'comprimento', 'peso', 'valor'],
                       'params': ['codigo_plataforma', 'token']}
    for key, value in required_fields.items():
        key_exists = data.get(key or errors.append(
            f'Field required {key} is missing.')) if key != 'params' else None
        if not isinstance(key_exists,
                          dict) and key != 'volumes' and key != 'params':
            errors.append(f'Field {key} is not a dictionary.')
            continue
        elif key == 'volumes' and not isinstance(key_exists, list):
            errors.append(f'Field {key} is not a list.')
            continue
        elif key == 'params':
            for val in value:
                secret = data.get(
                    val or errors.append(f'Field required {val} is missing.'))
                if val == 'codigo_plataforma' and secret != '588604ab3':
                    errors.append('Field codigo_plataforma is wrong.')
                elif val == 'token' and secret != 'c8359377969ded682c3dba5cb967c07b':
                    errors.append('Field token is wrong.')
        if key_exists:
            if key == 'remetente':
                value_exists = data.get(key).get(value or errors.append(
                    f'Field required {value} is missing.'))
                if not isinstance(value_exists, str) and len(value_exists)!=14:
                    errors.append(
                        f'{value} field needs to be numeric str and 14 characters long.')
            elif key == 'destinatario':
                for val in value:
                    val_exists = data.get(key).get(val or errors.append(
                        f'Field required {val} is missing.'))
                    if val == 'tipo_pessoa':
                        if not isinstance(val_exists, int) and len(
                                val_exists) > 1:
                            errors.append(
                                f'{val} field needs to be an int between 1 and 2.')
                        if val_exists == 2:
                            # These fields are only mandatory if
                            # tipo_pessoa = 2
                            # (That means its 'pessoa juridica')
                            cnpj_cpf = data.get(key).get(
                                'cnpj_cpf' or errors.append(
                                    'Field required cnpj_cpf is missing.'))
                            if not isinstance(cnpj_cpf, str) and len(
                                    cnpj_cpf) > 10 and len(cnpj_cpf) < 15:
                                errors.append(
                                    'Field cnpj_cpf needs to be a numeric string and be between 11-14 characters long.')
                            insc_est = data.get(key).get(
                                'inscricao_estadual' or errors.append(
                                    'Field required inscricao_estadual is missing.'))
                            if not isinstance(insc_est, str):
                                errors.append('Field inscricao_estadual needs to be a string.')
                    elif val == 'endereco':
                        endereco = data.get(key).get(val or errors.append(
                            f'Field required {val} is missing.'))
                        if not isinstance(endereco, dict):
                            errors.append('Required field endereco needs to be a dict.')
                        elif endereco:
                            cep = endereco.get('cep' or errors.append(
                                'Fiel required cep is missing.'))
                            if not isinstance(cep, str) and len(cep) > 8:
                                errors.append(
                                    'Field cep needs to be a string with 8 characters long.')
            elif key == 'volumes':
                for volume in key_exists:
                    if not isinstance(volume, dict):
                        errors.append(
                            'Required field inside volume needs to be a dict.')
                        continue
                    for vol_k, vol_v in volume.items():
                        if vol_k in value:
                            number = volume.get(vol_k or errors.append(
                                f'Field required {vol_k} is missing.'))
                            comparer = int if vol_k in ['quantidade',
                                                      'tipo'] else float
                            if not isinstance(number, comparer):
                                errors.append(
                                    f'Required field {vol_k} needs to be {"an integer" if comparer == int else "a float"} number and not {number}.')
    return errors


def formatted_data(data):
    """
    This method only exists to format the freterapido API answer
    so the requirement from this challenge can be met.
    :param data:
    :return:
    """
    new_response = {'transportadoras': []}
    for result in data.get('transportadoras'):
        new_response['transportadoras'].append({
            'nome': result.get('nome'),
            'servico': result.get('servico'),
            'prazo_entrega': result.get('prazo_entrega'),
            'preco_frete': result.get('preco_frete')
        })
    return new_response


if __name__ == '__main__':
    app.run(debug=True)
