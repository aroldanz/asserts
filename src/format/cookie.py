# -*- coding: utf-8 -*-

"""Modulo para verificaciones de Cookies HTTP.

Este modulo deberia considerarse su anexion al verificador de http.py pues como
tal las cookies son parte de dicho protocolo.
"""


# standard imports
from http.cookies import BaseCookie

# 3rd party imports
import logging
from termcolor import colored

# local imports
from fluidasserts.helper import http_helper

logger = logging.getLogger('FLUIDAsserts')


def has_not_http_only(url, cookie_name):
    """Verifica si la cookie tiene el atributo httponly."""
    http_req = http_helper.HTTPSession(url)
    cookielist = BaseCookie(http_req.headers['set-cookie'])
    result = colored('OPEN', 'red')
    if cookie_name in cookielist:
        if cookielist[cookie_name]['httponly']:
            result = colored('CLOSE', 'green')
        logger.info('%s HTTP cookie %s, Details=%s, %s',
                    cookie_name, url, cookielist[cookie_name], result)
    else:
        logger.info('%s HTTP cookie %s, Details=%s, %s',
                    cookie_name, url, 'Not Present', colored('OPEN', 'red'))
    return result == colored('OPEN', 'red')


def has_not_secure(url, cookie_name):
    """Verifica si la cookie tiene el atributo secure."""
    http_req = http_helper.HTTPSession(url)
    cookielist = BaseCookie(http_req.headers['set-cookie'])
    result = colored('OPEN', 'red')
    if cookie_name in cookielist:
        if cookielist[cookie_name]['secure']:
            result = colored('CLOSE', 'green')
        logger.info('%s HTTP cookie %s, Details=%s, %s',
                    cookie_name, url, cookielist[cookie_name], result)
    else:
        logger.info('%s HTTP cookie %s, Details=%s, %s',
                    cookie_name, url, 'Not Present', colored('OPEN', 'red'))
    return result == colored('OPEN', 'red')
