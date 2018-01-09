# -*- coding: utf-8 -*-

"""Modulo para pruebas de SMB.

Este modulo contiene las funciones necesarias para probar si el modulo de
SMB se encuentra adecuadamente implementado.
"""

# standard imports
from __future__ import print_function

# 3rd party imports
import pytest

# local imports
from fluidasserts.service import smb

# Constants
CONTAINER_IP = '172.30.216.101'
SMB_PORT = 445


@pytest.mark.parametrize('run_mock',
                         [('smb:hard', {'445/tcp': SMB_PORT})],
                         indirect=True)
# pylint: disable=unused-argument
def test_is_anonymous_enabled_close(run_mock):
    """Conexion anonima habilitada?"""
    assert not smb.is_anonymous_enabled(CONTAINER_IP)