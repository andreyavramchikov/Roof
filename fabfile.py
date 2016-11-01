from fabric.api import env, run
from fabric.operations import sudo

env.user = 'ubuntu'
env.hosts = [
    'ec2-54-237-251-218.compute-1.amazonaws.com'
]


env.key_filename = '/home/andrey/Roof.pem'

env.project_name = 'Roof'
env.path = '/home/ubuntu/projects/%(project_name)s' % env
env.env_path = '%(path)s/env' % env
env.repo_path = '%(path)s/repository' % env

# ssh -i ~/Roof.pem ubuntu@ec2-54-237-251-218.compute-1.amazonaws.com


def setup():
    # STILL NEED TO INSTALL MANUALLY MYSQL AND PYTHON-MYSQL ETC
    sudo('apt-get -y update')
    sudo('apt-get -y upgrade')
    sudo('apt-get -y install python-dev')
    sudo('apt-get -y install python-virtualenv')
    sudo('apt-get -y install libmysqlclient-dev')
    # sudo('pip install virtualenvwrapper')  # must update .bashrc still manually
    sudo('apt-get install -y mysql-server')
    create_database('roof')
    sudo('apt-get install -y git')
    sudo('apt-get install -y nginx')


def create_database(name):
    run('mysqladmin -u %s -p%s create %s' % ('root', 'pass', name))


def restart_nginx():
    sudo('/etc/init.d/nginx restart')


# deploy site with nginx-uwsgi conjunction
def deploy():
    sudo('rm -rf projects')
    sudo('rm -rf /etc/nginx/sites-enabled/mysite_nginx.conf')
    setup_directories()
    setup_virtualenv()
    clone_repo()
    install_requirements()
    sudo(
        'ln -s /home/ubuntu/projects/Roof/repository/mysite_nginx.conf /etc/nginx/sites-enabled/')
    sudo('/etc/init.d/nginx restart')
    # run(
    #     'cp -r /home/ubuntu/projects/Playtogether/repository/event/static/ /home/ubuntu/projects/Playtogether/repository/')
    run('source %(env_path)s/bin/activate; %(env_path)s/bin/python %(repo_path)s/manage.py migrate' % env)
    # run('source %(env_path)s/bin/activate; %(env_path)s/bin/python %(repo_path)s/manage.py collectstatic' % env)
    run('source %(env_path)s/bin/activate; pip install uwsgi' % env)
    run('source %(env_path)s/bin/activate; uwsgi --ini %(repo_path)s/mysite_uwsgi.ini' % env)


def install_requirements():
    """
    Install the required packages using pip.
    """
    run('source %(env_path)s/bin/activate; pip install -r %(repo_path)s/requirements.txt' % env)


def clone_repo():
    """
    Do initial clone of the git repository.
    """
    run('git clone https://github.com/andreyavramchikov/%(project_name)s.git %(repo_path)s' % env)


def setup_directories():
    """
    Create directories necessary for deployment.
    """
    run('mkdir -p %(path)s' % env)
    run('mkdir -p %(env_path)s' % env)


def activate_virtualenv():
    run('source %(env_path)s/bin/activate;' % env)


def setup_virtualenv():
    """
    Setup a fresh virtualenv.
    """
    run('virtualenv %(env_path)s --no-site-packages;' % env)
    run('source %(env_path)s/bin/activate;' % env)