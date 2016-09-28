# -*- coding: utf-8 -*-

"""Modulo para pruebas de HTTP.

Este modulo contiene las funciones necesarias para probar si el modulo de
HTTP se encuentra adecuadamente implementado.
"""

# standard imports
import time
from multiprocessing import Process

# 3rd party imports
import pytest

# local imports
from fluidasserts import http
from test.mock import httpserver


#
# Constants
#


BASE_URL = 'http://localhost:5000/http/headers'


#
# Fixtures
#


@pytest.fixture(scope='module')
def mock_http(request):
    """Inicia y detiene el servidor HTTP antes de ejecutar una prueba."""
    # Inicia el servidor HTTP en background
    prcs = Process(target=httpserver.start, name='MockHTTPServer')
    prcs.daemon = True
    prcs.start()

    # Espera que inicie servidor antes de recibir conexiones
    time.sleep(0.1)

    def teardown():
        """Detiene servidor HTTP al finalizar las pruebas."""
        prcs.terminate()

    request.addfinalizer(teardown)


#
# Open tests
#


@pytest.mark.usefixtures('mock_http')
def test_access_control_allow_origin_open():
    """Header Access-Control-Allow-Origin no establecido?"""
    assert http.has_header_access_control_allow_origin(
        '%s/access_control_allow_origin/fail' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_cache_control_open():
    """Header Cache-Control no establecido?"""
    assert http.has_header_cache_control(
        '%s/cache_control/fail' % (BASE_URL))

#
# Close tests
#

@pytest.mark.usefixtures('mock_http')
def test_access_control_allow_origin_close():
    """Header Access-Control-Allow-Origin establecido?"""
    assert not http.has_header_access_control_allow_origin(
        '%s/access_control_allow_origin/ok' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_cache_control_close():
    """Header Cache-Control establecido?"""
    assert not http.has_header_cache_control(
        '%s/cache_control/ok' % (BASE_URL))


#
# TODO(glopez) Functions in HTTP library
#
# http.has_header_x_xxs_protection('%s/access_control_allow_origin/fail'
#   % (BASE_URL))
# http.has_header_x_xxs_protection("http://challengeland.co/")
# http.has_header_x_frame_options("http://localhost/cursos")
# http.has_header_x_frame_options("http://challengeland.co/")
# http.has_header_x_permitted_cross_domain_policies("http://localhost/cursos")
# http.has_header_x_permitted_cross_domain_policies("http://challengeland.co/")
# http.has_header_x_content_type_options("http://localhost/cursos")
# http.has_header_x_content_type_options("http://challengeland.co")
# http.has_header_pragma("http://localhost/cursos")
# http.has_header_pragma("http://challengeland.co")
# http.has_header_expires("http://localhost/cursos")
# http.has_header_expires("http://challengeland.co")
# http.has_header_pragma("http://localhost/cursos")
# http.has_header_content_type("http://challengeland.co")
# http.has_header_content_security_policy("http://challengeland.co")
# http.has_header_content_security_policy("http://localhost/cursos")
# cookie.has_http_only("http://challengeland.co","ci_session")
# http.basic_auth("http://localhost/fluidopens/BasicAuth/","root","1234")
# http.basic_auth("http://localhost/fluidopens/BasicAuth/","Admin","1234")
# Asymetric testing
# http.response_is_stable(seconds, URL, repeat)