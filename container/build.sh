
SERVICE_NAME=$1

if [ -z "$SERVICE_NAME" ]
then
  docker-compose down && docker-compose up -d --build --force-recreate
else
  docker-compose up -d --build --force-recreate --no-deps $SERVICE_NAME
fi


