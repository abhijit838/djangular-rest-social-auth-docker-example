## ~ Django-Docker-Ansible Devops ~
## ~ Manual Dev Setup:
#### ~ Project Setup:
    git clone <Project URL>
    activate <venv name>
    pip install -r requirements.txt
    python manage.py migrate --settings=backend.settings.<local/dev/prod>
    OR
    python manage.py migrate --run-syncdb
    cp .env.example .env
    AND
    update social app key-secret

## ~ Automated Dev Setup:
    - Install docker
    - Install docker-compose
    - Run the command
        $ docker-compose -f docker/backend-dev.yml up --build
    - To stop containers run
        $ docker-compose -f docker/backend-dev.yml down

    Note: Source code directory is automatically synced with docker container, means any source code changes in host system reflected in container
        Start the dev containers once write code anytime.

Stay tuned for ansible integration.