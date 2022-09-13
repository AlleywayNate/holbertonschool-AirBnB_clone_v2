#!/usr/bin/python3
""" Fabric script that creates and distributes
an archive to your web servers """
from fabric.contrib import files
from fabric.api import env, put, run, local
import os
import time

env.hosts = ['54.172.111.74', '3.85.212.121']


def do_pack():
    """ Generate .tgz file """
    timest = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(timest))
        return ("versions/web_static_{:s}.tgz".format(timest))
    except Exception:
        return None


def do_deploy(archive_path):
    """ Distribute file to server """
    if not os.path.exists(archive_path):
        return False

    data_path = '/data/web_static/releases/'
    temp = archive_path.split('.')[0]
    name = temp.split('/')[1]
    dest = data_path + name

    try:
        put(archive_path, '/temp')
        run('sudo mkdir -p {}'.format(dest))
        run('sudo tar -xzf /temp/{}.tgz -C {}'.format(name, dest))
        run('sudo rm -f /temp/{}.tgz'.format(name))
        run('sudo mv {}/web_static/* {}/'.format(dest, dest))
        run('sudo rm -rf {}/web_static'.format(dest))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(dest))
        return True
    except Exception:
        return False


def deploy():
    """ Creates and distributes an archive """
    path = do_pack()
    print(path)
    if path:
        do_deploy(path)
    else:
        return False
