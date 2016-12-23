# -*- coding: utf-8 -*-

"""Modulo para pruebas de HTTP.

Este modulo contiene las funciones necesarias para probar si el modulo de
HTTP se encuentra adecuadamente implementado.
"""

# standard imports
from multiprocessing import Process
import time

# 3rd party imports
import pytest

# local imports
from fluidasserts.helper import http_helper
from fluidasserts.service import http
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
    assert http.is_header_access_control_allow_origin_missing(
        '%s/access_control_allow_origin/fail' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_cache_control_open():
    """Header Cache-Control no establecido?"""
    assert http.is_header_cache_control_missing(
        '%s/cache_control/fail' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_hsts_open():
    """Header Strict-Transport-Security no establecido?"""
    assert http.is_header_hsts_missing(
        '%s/hsts/fail' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_basic_open():
    """Auth BASIC habilitado?"""
    assert http.is_basic_auth_enabled(
        '%s/basic/fail' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_notfound_string():
    """Expected string not found?"""
    url = '%s/notfound' % (BASE_URL)
    expected = 'Expected string'
    assert http.generic_http_assert(url, expected)


@pytest.mark.usefixtures('mock_http')
def test_delete_open():
    """HTTP DELETE Allowed"""
    assert http.has_delete_method('%s/delete_open' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_put_open():
    """HTTP PUT Allowed"""
    assert http.has_put_method('%s/put_open' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_trace_open():
    """HTTP TRACE Allowed"""
    assert http.has_trace_method('%s/trace_open' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_version_open():
    """Header Server inseguro?"""
    assert http.is_header_server_insecure(
        '%s/version/fail' % (BASE_URL))


#
# Close tests
#


@pytest.mark.usefixtures('mock_http')
def test_access_control_allow_origin_close():
    """Header Access-Control-Allow-Origin establecido?"""
    assert not http.is_header_access_control_allow_origin_missing(
        '%s/access_control_allow_origin/ok' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_cache_control_close():
    """Header Cache-Control establecido?"""
    assert not http.is_header_cache_control_missing(
        '%s/cache_control/ok' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_hsts_close():
    """Header Strict-Transport-Security establecido?"""
    assert not http.is_header_hsts_missing(
        '%s/hsts/ok' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_basic_close():
    """Auth BASIC no habilitado?"""
    assert not http.is_basic_auth_enabled(
        '%s/basic/ok' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_put_close():
    """HTTP PUT Not Allowed"""
    assert not http.has_put_method('%s/put_close' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_trace_close():
    """HTTP TRACE Not Allowed"""
    assert not http.has_trace_method('%s/trace_close' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_delete_close():
    """HTTP DELETE Not Allowed"""
    assert not http.has_delete_method('%s/delete_close' % (BASE_URL))


@pytest.mark.usefixtures('mock_http')
def test_expected_string():
    """Expected string found?"""
    url = '%s/expected' % (BASE_URL)
    expected = 'Expected string'

    assert not http.generic_http_assert(url, expected)


@pytest.mark.usefixtures('mock_http')
def test_version_close():
    """Header Server inseguro?"""
    assert not http.is_header_server_insecure(
        '%s/version/ok' % (BASE_URL))


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
