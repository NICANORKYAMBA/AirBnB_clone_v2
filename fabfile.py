#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone
repo, using the function do_pack
"""
from fabric import local
from datetime import datetime


def do_pack():
    """
    Create a compressed archive of the web_static directory
    """
    try:
        archive_time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        archive_name = "versions/web_static_{}".format(archive_time)
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except:
        return None
