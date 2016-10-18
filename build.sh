set -e

docker run --rm --env-file .env -v $(pwd):/usr/src/app -w /usr/src/app node:6 npm install && run build:prod
docker-compose build
docker-compose run --rm django python manage.py migrate
docker-compose run --rm django make datasets