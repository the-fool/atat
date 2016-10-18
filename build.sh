set -e

docker run --rm -e STATIC_ASSET_PREFIX='/nginx-static/' -v $(pwd):/usr/src/app -w /usr/src/app node:6 /bin/bash -c "npm install && npm run build:prod"
cp dist/psppi.html atat/templates/
docker-compose build
docker-compose run --rm django python manage.py migrate
docker-compose run --rm django make datasets