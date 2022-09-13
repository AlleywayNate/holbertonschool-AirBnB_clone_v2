#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers """
from fabric.contrib import files
from fabric.api import env, put, run
import os

env.hosts = ['54.172.111.74', '3.85.212.121']


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
