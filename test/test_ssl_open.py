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

#
# Open tests
#


@pytest.mark.parametrize('run_mock',
                         [('ssl:weak', {'443/tcp': SSL_PORT})],
                         indirect=True)
def test_pfs_enabled_open(run_mock):
    """PFS habilitado en sitio?."""
    assert ssl.is_pfs_disabled(run_mock)


def test_sslv3_enabled_open(run_mock):
    """SSLv3 habilitado en sitio?."""
    assert ssl.is_sslv3_enabled(run_mock)


def test_tlsv1_enabled_open(run_mock):
    """TLSv1 habilitado en sitio?."""
    assert ssl.is_tlsv1_enabled(run_mock)


def test_has_poodle_sslv3_open(run_mock):
    """Sitio vulnerable a POODLE?."""
    assert ssl.has_poodle_sslv3(run_mock)


def test_has_beast_open(run_mock):
    """Sitio vulnerable a BEAST?."""
    assert ssl.has_beast(run_mock)


def test_allows_weak_alg_open(run_mock):
    """Sitio permite algoritmos debiles?."""
    assert ssl.allows_weak_ciphers(run_mock)


def test_allows_anon_alg_open(run_mock):
    """Sitio permite algoritmos anonimos?."""
    assert ssl.allows_anon_ciphers(run_mock)
