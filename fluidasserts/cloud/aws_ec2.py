# -*- coding: utf-8 -*-

"""
AWS cloud checks (EC2).

The checks are based on CIS AWS Foundations Benchmark.
"""

# standard imports
# None

# 3rd party imports
# None

# local imports
from fluidasserts import show_close
from fluidasserts import show_open
from fluidasserts import show_unknown
from fluidasserts.utils.decorators import track, level
from fluidasserts.helper import aws_helper


@level('low')
@track
def seggroup_allows_anyone_to_ssh(key_id: str, secret: str) -> bool:
    """
    Check if security groups allows connection from anyone to SSH service.

    :param key_id: AWS Key Id
    :param secret: AWS Key Secret
    """
    try:
        sec_groups = aws_helper.list_security_groups(key_id, secret)
    except aws_helper.ConnError as exc:
        show_unknown('Could not connect',
                     details=dict(error=str(exc).replace(':', '')))
        return False
    except aws_helper.ClientErr as exc:
        show_unknown('Error retrieving info. Check credentials.',
                     details=dict(error=str(exc).replace(':', '')))
        return False
    if not sec_groups:
        show_close('Not security groups were found')
        return False

    result = False
    for group in sec_groups:
        for ip_perm in group['IpPermissions']:
            try:
                vuln = [ip_perm for x in ip_perm['IpRanges']
                        if x['CidrIp'] == '0.0.0.0/0'and
                        ip_perm['FromPort'] <= 22 >= ip_perm['ToPort']]
            except KeyError:
                pass
        if vuln:
            show_open('Security group allows connection \
from anyone to port 22',
                      details=dict(group=group['Description'],
                                   ip_ranges=vuln))
            result = True
        else:
            show_close('Security group not allows connection \
from anyone to port 22',
                       details=dict(group=group['Description']))
    return result
