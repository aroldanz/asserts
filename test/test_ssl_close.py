# -*- coding: utf-8 -*-

"""Modulo para pruebas de SSL.

Este modulo contiene las funciones necesarias para probar si el modulo de
SSL se encuentra adecuadamente implementado.
"""

# standard imports
from __future__ import print_function

# 3rd party imports
import pytest

# local imports
from fluidasserts.proto import ssl


# Constants

SSL_PORT = 443
NON_EXISTANT = '0.0.0.0'

#
# Closing tests
#


@pytest.mark.parametrize('run_mock',
                         [('ssl:hard', {'443/tcp': SSL_PORT})],
                         indirect=True)
def test_pfs_enabled_close(run_mock):
    """PFS habilitado en sitio?."""
    assert not ssl.is_pfs_disabled(run_mock)
    assert not ssl.is_pfs_disabled(NON_EXISTANT)


def test_sslv3_enabled_close(run_mock):
    """SSLv3 habilitado en sitio?."""
    assert not ssl.is_sslv3_enabled(run_mock)
    assert not ssl.is_sslv3_enabled(NON_EXISTANT)


def test_tlsv1_enabled_close(run_mock):
    """TLSv1 habilitado en sitio?."""
    assert not ssl.is_tlsv1_enabled(run_mock)
    assert not ssl.is_tlsv1_enabled(NON_EXISTANT)


def test_has_poodle_sslv3_close(run_mock):
    """Sitio vulnerable a POODLE?."""
    assert not ssl.has_poodle_sslv3(run_mock)
    assert not ssl.has_poodle_sslv3(NON_EXISTANT)


def test_has_poodle_tls_close(run_mock):
    """Sitio vulnerable a POODLE?."""
    assert not ssl.has_poodle_tls(run_mock)
    assert not ssl.has_poodle_tls(NON_EXISTANT)


def test_has_beast_close(run_mock):
    """Sitio vulnerable a BEAST?."""
    assert not ssl.has_beast(run_mock)
    assert not ssl.has_beast(NON_EXISTANT)


def test_allows_weak_alg_close(run_mock):
    """Sitio permite algoritmos debiles?."""
    assert not ssl.allows_weak_ciphers(run_mock)
    assert not ssl.allows_weak_ciphers(NON_EXISTANT)


def test_allows_anon_alg_close(run_mock):
    """Sitio permite algoritmos anonimos?."""
    assert not ssl.allows_anon_ciphers(run_mock)
    assert not ssl.allows_anon_ciphers(NON_EXISTANT)


def test_has_breach_close(run_mock):
    """Presencia de la vulnerabilidad Breach?."""
    assert not ssl.has_breach(run_mock, SSL_PORT)
    assert not ssl.has_breach(NON_EXISTANT, SSL_PORT)


def test_has_heartbleed_close(run_mock):
    """Presencia de la vulnerabilidad Heartbleed?."""
    assert not ssl.has_heartbleed(run_mock, SSL_PORT)
    assert not ssl.has_heartbleed(NON_EXISTANT, SSL_PORT)