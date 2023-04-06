#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone
repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the timestamp
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")

    # Create the archive filename
    archive_name = "web_static_{}.tgz".format(current_time)

    # Create the command to generate the archive
    command = "tar -czvf versions/{} web_static".format(archive_name)

    # Run the command and capture the output
    result = local(command)

    # Check if the command was successful
    if result.failed:
        return None

    # Return the path to the archive file
    return "versions/{}".format(archive_name)
