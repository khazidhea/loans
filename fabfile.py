import os

from fabric import task


PROJ_DIR = '/srv/loans'
host = os.environ['host']
username = os.environ['username']
hosts = ['{}@{}'.format(username, host)]


@task(hosts=hosts)
def deploy(c):
    c.put(
        'docker/docker-compose.yml',
        '{}/docker-compose.yml'.format(PROJ_DIR)
    )
    c.put(
        'docker/nginx.conf',
        '{}/nginx.conf'.format(PROJ_DIR)
    )
    c.put(
        'docker/gunicorn.conf',
        '{}/gunicorn.conf'.format(PROJ_DIR)
    )
    c.run(
        'cd {}; docker-compose pull && docker-compose down && docker-compose up -d'.format(PROJ_DIR)
    )
