#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives,
from webservers using the function do_clean
"""
from fabric.api import env, local, put, run
from os.path import exists
import os

env.hosts = ['35.168.1.74', '54.90.54.132']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """
    Deletes out-of-date archives from the web servers.
    """
    try:
        number = int(number)
    except ValueError:
        print("Error: invalid number argument")
        return False

    if number < 1:
        print("Error: number must be a positive integer")
        return False

    archives_to_keep = sorted(local(
            'ls -1t versions', capture=True).split())
    archives_to_delete = archives_to_keep[number:]

    for archive in archives_to_delete:
        archive_path = os.path.join('versions', archive)
        if os.path.exists(archive_path):
            local('rm -f {}'.format(archive_path))
