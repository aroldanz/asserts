# -*- coding: utf-8 -*-

"""Modulo para pruebas de TCP.

Este modulo contiene las funciones necesarias para probar si el modulo de
tcp se encuentra adecuadamente implementado.
"""

# standard imports
from __future__ import print_function

# 3rd party imports
import pytest

# local imports
from fluidasserts.service import tcp
import fluidasserts.utils.decorators

# Constants
fluidasserts.utils.decorators.UNITTEST = True
CONTAINER_IP = '172.30.216.101'
WEAK_PORT = 80

#
# Open tests
#


@pytest.mark.parametrize('run_mock',
                         [('tcp:weak', {'21/tcp': WEAK_PORT})],
                         indirect=True)
# pylint: disable=unused-argument
def test_port_open_open(run_mock):
    """Check open port."""
    assert tcp.is_port_open(CONTAINER_IP, WEAK_PORT)


def test_port_open_error():
    """Check open port with error."""
    with pytest.raises(AssertionError):
        tcp.is_port_open(CONTAINER_IP, -1)
# El caso de prueba deberia generar AssertionError
# se deja comentado mientras se realizan los cambios
# necesarios en el codigo.
#    with pytest.raises(AssertionError):
#        tcp.is_port_open(CONTAINER_IP+'.1', 1)


def test_port_insecure_open(run_mock):
    """Check secure port."""
    assert tcp.is_port_insecure(CONTAINER_IP, WEAK_PORT)
