# -*- coding: utf-8 -*-
"""
Modulo OS os_unix_generic
"""

# standard imports
import logging

# 3rd party imports
# None

# local imports
# None


def is_os_min_priv_enabled(server, username, password, ssh_config):
    """
    Checks if umask or similar is secure in os_unix_generic
    """
    pass


def is_os_sudo_enabled(server, username, password, ssh_config):
    """
    Checks if there's sudo or similar installed in os_unix_generic
    """
    pass


def is_os_compilers_installed(server, username, password, ssh_config):
    """
    Checks if there's any compiler installed in os_unix_generic
    """
    pass


def is_os_antimalware_installed(server, username, password, ssh_config):
    """
    Checks if there's any antimalware installed in os_unix_generic
    """
    pass


def is_os_remote_admin_enabled(server, username, password, ssh_config):
    """
    Checks if admins can remotely login in os_unix_generic
    """
    pass


def is_os_syncookies_enabled(server, username, password, ssh_config):
    """
    Checks if SynCookies or similar is enabled in os_unix_generic
    """
    pass