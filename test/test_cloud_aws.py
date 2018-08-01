# -*- coding: utf-8 -*-

"""Test methods of fluidasserts.cloud packages."""

# standard imports
import os

# 3rd party imports
# None

# local imports
from fluidasserts.cloud import aws


# Constants
AWS_ACCESS_KEY_ID="AKIAJ2C5RAAC554PAUOQ"
AWS_SECRET_ACCESS_KEY="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"
AWS_SECRET_ACCESS_KEY_BAD="bad"

#
# Open tests
#


def test_pass_len_unsafe_open():
    """Search IAM policy: Password length requirement."""
    assert aws.iam_min_password_len_unsafe(AWS_ACCESS_KEY_ID,
                                           AWS_SECRET_ACCESS_KEY)


def test_pass_reuse_unsafe_open():
    """Search IAM policy: Password reuse requirement."""
    assert aws.iam_password_reuse_unsafe(AWS_ACCESS_KEY_ID,
                                         AWS_SECRET_ACCESS_KEY)


def test_pass_expiration_unsafe_open():
    """Search IAM policy: Password expiration requirement."""
    assert aws.iam_password_expiration_unsafe(AWS_ACCESS_KEY_ID,
                                              AWS_SECRET_ACCESS_KEY)


def test_root_mfa_open():
    """Search IAM summary: MFA for root."""
    assert aws.iam_root_without_mfa(AWS_ACCESS_KEY_ID,
                                    AWS_SECRET_ACCESS_KEY)

#
# Closing tests
#

def test_has_mfa_disabled_close():
    """Search MFA on IAM users."""
    assert not aws.iam_has_mfa_disabled(AWS_ACCESS_KEY_ID,
                                        AWS_SECRET_ACCESS_KEY)
    assert not aws.iam_has_mfa_disabled(AWS_ACCESS_KEY_ID,
                                        AWS_SECRET_ACCESS_KEY_BAD)

    os.environ['http_proxy'] = 'https://0.0.0.0:8080'
    os.environ['https_proxy'] = 'https://0.0.0.0:8080'

    assert not aws.iam_has_mfa_disabled(AWS_ACCESS_KEY_ID,
                                        AWS_SECRET_ACCESS_KEY)
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)


def test_have_old_creds_enabled_close():
    """Search old unused passwords."""
    assert not aws.iam_have_old_creds_enabled(AWS_ACCESS_KEY_ID,
                                              AWS_SECRET_ACCESS_KEY)
    assert not aws.iam_have_old_creds_enabled(AWS_ACCESS_KEY_ID,
                                              AWS_SECRET_ACCESS_KEY_BAD)

    os.environ['http_proxy'] = 'https://0.0.0.0:8080'
    os.environ['https_proxy'] = 'https://0.0.0.0:8080'

    assert not aws.iam_have_old_creds_enabled(AWS_ACCESS_KEY_ID,
                                              AWS_SECRET_ACCESS_KEY)
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)


def test_have_old_access_keys_close():
    """Search old access keys."""
    assert not aws.iam_have_old_access_keys(AWS_ACCESS_KEY_ID,
                                            AWS_SECRET_ACCESS_KEY)
    assert not aws.iam_have_old_access_keys(AWS_ACCESS_KEY_ID,
                                            AWS_SECRET_ACCESS_KEY_BAD)

    os.environ['http_proxy'] = 'https://0.0.0.0:8080'
    os.environ['https_proxy'] = 'https://0.0.0.0:8080'

    assert not aws.iam_have_old_access_keys(AWS_ACCESS_KEY_ID,
                                            AWS_SECRET_ACCESS_KEY)
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)


def test_root_has_access_keys_close():
    """Search root access keys."""
    assert not aws.iam_root_has_access_keys(AWS_ACCESS_KEY_ID,
                                            AWS_SECRET_ACCESS_KEY)
    assert not aws.iam_root_has_access_keys(AWS_ACCESS_KEY_ID,
                                            AWS_SECRET_ACCESS_KEY_BAD)

    os.environ['http_proxy'] = 'https://0.0.0.0:8080'
    os.environ['https_proxy'] = 'https://0.0.0.0:8080'

    assert not aws.iam_root_has_access_keys(AWS_ACCESS_KEY_ID,
                                            AWS_SECRET_ACCESS_KEY)
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)


def test_not_requires_uppercase_close():
    """Search IAM policy: Uppercase letter requirement."""
    assert not aws.iam_not_requires_uppercase(AWS_ACCESS_KEY_ID,
                                              AWS_SECRET_ACCESS_KEY)
    assert not aws.iam_not_requires_uppercase(AWS_ACCESS_KEY_ID,
                                              AWS_SECRET_ACCESS_KEY_BAD)

    os.environ['http_proxy'] = 'https://0.0.0.0:8080'
    os.environ['https_proxy'] = 'https://0.0.0.0:8080'

    assert not aws.iam_not_requires_uppercase(AWS_ACCESS_KEY_ID,
                                              AWS_SECRET_ACCESS_KEY)
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)


def test_not_requires_lowercase_close():
    """Search IAM policy: Lowercase letter requirement."""
    assert not aws.iam_not_requires_lowercase(AWS_ACCESS_KEY_ID,
                                              AWS_SECRET_ACCESS_KEY)
    assert not aws.iam_not_requires_lowercase(AWS_ACCESS_KEY_ID,
                                              AWS_SECRET_ACCESS_KEY_BAD)

    os.environ['http_proxy'] = 'https://0.0.0.0:8080'
    os.environ['https_proxy'] = 'https://0.0.0.0:8080'

    assert not aws.iam_not_requires_lowercase(AWS_ACCESS_KEY_ID,
                                              AWS_SECRET_ACCESS_KEY)
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)


def test_not_requires_symbols_close():
    """Search IAM policy: Symbols requirement."""
    assert not aws.iam_not_requires_symbols(AWS_ACCESS_KEY_ID,
                                            AWS_SECRET_ACCESS_KEY)
    assert not aws.iam_not_requires_symbols(AWS_ACCESS_KEY_ID,
                                            AWS_SECRET_ACCESS_KEY_BAD)

    os.environ['http_proxy'] = 'https://0.0.0.0:8080'
    os.environ['https_proxy'] = 'https://0.0.0.0:8080'

    assert not aws.iam_not_requires_symbols(AWS_ACCESS_KEY_ID,
                                            AWS_SECRET_ACCESS_KEY)
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)


def test_not_requires_numbers_close():
    """Search IAM policy: Numbers requirement."""
    assert not aws.iam_not_requires_numbers(AWS_ACCESS_KEY_ID,
                                            AWS_SECRET_ACCESS_KEY)
    assert not aws.iam_not_requires_numbers(AWS_ACCESS_KEY_ID,
                                            AWS_SECRET_ACCESS_KEY_BAD)

    os.environ['http_proxy'] = 'https://0.0.0.0:8080'
    os.environ['https_proxy'] = 'https://0.0.0.0:8080'

    assert not aws.iam_not_requires_numbers(AWS_ACCESS_KEY_ID,
                                            AWS_SECRET_ACCESS_KEY)
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)


def test_pass_len_unsafe_close():
    """Search IAM policy: Password length requirement."""
    assert not aws.iam_min_password_len_unsafe(AWS_ACCESS_KEY_ID,
                                               AWS_SECRET_ACCESS_KEY_BAD)

    os.environ['http_proxy'] = 'https://0.0.0.0:8080'
    os.environ['https_proxy'] = 'https://0.0.0.0:8080'

    assert not aws.iam_min_password_len_unsafe(AWS_ACCESS_KEY_ID,
                                               AWS_SECRET_ACCESS_KEY)
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)


def test_pass_reuse_unsafe_close():
    """Search IAM policy: Password reuse requirement."""
    assert not aws.iam_password_reuse_unsafe(AWS_ACCESS_KEY_ID,
                                             AWS_SECRET_ACCESS_KEY_BAD)

    os.environ['http_proxy'] = 'https://0.0.0.0:8080'
    os.environ['https_proxy'] = 'https://0.0.0.0:8080'

    assert not aws.iam_password_reuse_unsafe(AWS_ACCESS_KEY_ID,
                                             AWS_SECRET_ACCESS_KEY)
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)


def test_pass_expiration_unsafe_close():
    """Search IAM policy: Password expiration requirement."""
    assert not aws.iam_password_expiration_unsafe(AWS_ACCESS_KEY_ID,
                                                  AWS_SECRET_ACCESS_KEY_BAD)

    os.environ['http_proxy'] = 'https://0.0.0.0:8080'
    os.environ['https_proxy'] = 'https://0.0.0.0:8080'

    assert not aws.iam_password_expiration_unsafe(AWS_ACCESS_KEY_ID,
                                                  AWS_SECRET_ACCESS_KEY)
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)


def test_root_mfa_close():
    """Search IAM summary: MFA for root."""
    assert not aws.iam_root_without_mfa(AWS_ACCESS_KEY_ID,
                                        AWS_SECRET_ACCESS_KEY_BAD)

    os.environ['http_proxy'] = 'https://0.0.0.0:8080'
    os.environ['https_proxy'] = 'https://0.0.0.0:8080'

    assert not aws.iam_root_without_mfa(AWS_ACCESS_KEY_ID,
                                        AWS_SECRET_ACCESS_KEY)
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)


def test_policies_attached_close():
    """Search IAM policies: Policies attached directly to users."""
    assert not aws.iam_policies_attached_to_users(AWS_ACCESS_KEY_ID,
                                                  AWS_SECRET_ACCESS_KEY)
    assert not aws.iam_policies_attached_to_users(AWS_ACCESS_KEY_ID,
                                                  AWS_SECRET_ACCESS_KEY_BAD)

    os.environ['http_proxy'] = 'https://0.0.0.0:8080'
    os.environ['https_proxy'] = 'https://0.0.0.0:8080'

    assert not aws.iam_policies_attached_to_users(AWS_ACCESS_KEY_ID,
                                                  AWS_SECRET_ACCESS_KEY)
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)