# -*- coding: utf-8 -*-

"""Servidor HTTP basado en Flask para exponer los mock HTTP.

Este modulo necesita un serio refactoring para reutilizar una logica
mas simple y menos repetitiva donde puede operar sobre una estructura
de datos que defina por cada header:

1. Nombre del header en el protocolo,
2. Valor satisfactorio del header,
3. Valor no satisfactorio del header,
4. URL base (opcional puede ser generada por la función a partir de 1,2 y 3)
5. Cuerpo de respuesta (opcional, ver razon de 4).

El metodo opera sobre esta estructura y a partir de los datos anteriores
y un formato definido de url:

http://xxx/header/ok -> responde con 2
http://xxx/header/fail -> responde con 3

Genera la respuesta correspondiente, tanto en el body, como en los headers

El refactoring sera adecuado cuando se añadan a la estructura de datos
nuevos headers y funcione para más casos de prueba.
"""

# standard imports
# none

# 3rd party imports
from flask import Flask, Response

# local imports
# none


APP = Flask(__name__)


@APP.route('/')
def home():
    """Respuesta a directorio raiz."""
    return 'Mock HTTP Server'


@APP.route('/http/headers/access_control_allow_origin/ok')
def access_control_allow_origin_ok():
    """Header AC Allow Origin bien establecido."""
    resp = Response('Access-Control-Allow-Origin OK')
    resp.headers['Access-Control-Allow-Origin'] = 'https://fluid.la'
    return resp


@APP.route('/http/headers/access_control_allow_origin/fail')
def access_control_allow_origin_fail():
    """Header AC Allow Origin mal establecido."""
    resp = Response('Access-Control-Allow-Origin FAIL')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@APP.route('/http/headers/cache_control/ok')
def cache_control_ok():
    """Header para Control de Cache bien establecido."""
    resp = Response('Cache-Control OK')
    resp.headers[
        'Cache-Control'] = ('private, no-cache, no-store, max-age=0, '
                            'no-transform')
    return resp


@APP.route('/http/headers/cache_control/fail')
def cache_control_fail():
    """Header para Control de Cache mal establecido."""
    resp = Response('Cache-Control FAIL')
    resp.headers['Cache-Control'] = 'Fail'
    return resp


@APP.route('/http/headers/content_security_policy/ok')
def content_security_policy_ok():
    """Header para politica de contenido bien establecida."""
    resp = Response('content-security-policy OK')
    resp.headers[
        'content-security-policy'] = ('private, no-cache, no-store, '
                                      'max-age=0, no-transform')
    return resp


@APP.route('/http/headers/content_security_policy/ok')
def content_security_policy_fail():
    """Header para politica de contenido mal establecida."""
    resp = Response('Content-Security-Policy FAIL')
    resp.headers['Content-Security-Policy'] = 'Fail'
    return resp


@APP.route('/http/headers/content_type/ok')
def content_type_ok():
    """Header que define bien el tipo de contenido."""
    resp = Response('Content-Type OK')
    resp.headers['Content-Type'] = 'APPlication/json'
    return resp


@APP.route('/http/headers/content_type/fail')
def content_type_fail():
    """Header que define mal el tipo de contenido."""
    resp = Response('Content-Type FAIL')
    resp.headers['Content-Type'] = 'Fail'
    return resp


@APP.route('/http/headers/expires/ok')
def expires_ok():
    """Header que define bien la expiración de la página en cache."""
    resp = Response('Expires OK')
    resp.headers['Expires'] = '0'
    return resp


@APP.route('/http/headers/expires/fail')
def expires_fail():
    """Header que define mal la expiración de la página en cache."""
    resp = Response('Expires FAIL')
    resp.headers['Expires'] = 'Fail'
    return resp


def start():
    """Inicia el servidor de pruebas."""
    APP.run()