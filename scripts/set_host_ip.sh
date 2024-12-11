#!/bin/bash

HOST_IP=$(hostname -I | awk '{print $1}')

echo "HOST_IP=${HOST_IP}" > .env
echo "HOST_IP является ${HOST_IP}"

docker-compose up --build
