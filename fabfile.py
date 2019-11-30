import os

from fabric import task


PROJ_DIR = '/srv/loans'
VIRTUALENV_CMD = '/srv/.virtualenvs/loans/bin/activate'
host = os.environ['host']
username = os.environ['username']
hosts = ['{}@{}'.format(username, host)]


@task(hosts=hosts)
def deploy(c):
    c.run('cd {}; git pull'.format(PROJ_DIR))
    c.run(
        'cd {}; source {}; pip install -r requirements.txt'.format(
            PROJ_DIR, VIRTUALENV_CMD
        )
    )
    c.run(
        'cd {}; source {}; python manage.py collectstatic --noinput'.format(
            PROJ_DIR, VIRTUALENV_CMD
        )
    )
    c.run('sudo supervisorctl restart all', pty=True)

