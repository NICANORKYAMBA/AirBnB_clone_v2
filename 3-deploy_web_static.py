#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your
web servers, using the function do_pack and do_deploy
"""
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists
import os

env.hosts = ['35.168.1.74', '54.90.54.132']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


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


def do_deploy(archive_path):
    """
    Distribute an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        """Get filename from archive_path"""
        filename = os.path.basename(archive_path)

        """Upload archive to /tmp/ directory on web servers"""
        put(archive_path, "/tmp/{}".format(filename))

        """
        Create the directory where the content will be unpacked
        on web servers
        """
        run("mkdir -p /data/web_static/releases/{}".format(
            filename[:-4]))

        """
        Unpack the content from the archive into the new directory
        """
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, filename[:-4]))

        """
        Delete the uploaded archive from /tmp/ directory on
        web servers
        """
        run("rm /tmp/{}".format(filename))

        """
        Move the content from the new directory to its
        final location
        """
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(
                filename[:-4], filename[:-4]))

        """
        Remove the now-empty web_static directory
        """
        run("rm -rf /data/web_static/releases/{}/web_static".format(
                filename[:-4]))

        """
        Delete the symbolic link from the web server's document root
        """
        run("rm -rf /data/web_static/current")

        """
        Create a new symbolic link pointing to the new version
        of the web site
        """
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(filename[:-4]))

        return True
    except (FileNotFoundError, NetworkError, CommandTimeout) as e:
        print("Error: {}".format(str(e)))
        return False


def deploy():
    """
    Deploy function to call do_pack and do_deploy
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
