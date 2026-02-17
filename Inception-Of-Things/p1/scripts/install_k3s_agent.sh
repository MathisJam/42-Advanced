#!/bin/bash
set -e

# attendre que le server écoute
while ! nc -z 192.168.56.110 6443; do
  echo "Waiting for k3s server..."
  sleep 1
done

while [ ! -f /vagrant/node-token ]; do
  echo "Waiting for node-token..."
  sleep 1
done

TOKEN=$(cat /vagrant/node-token)

curl -sfL https://get.k3s.io | \
  K3S_URL="https://192.168.56.110:6443" K3S_TOKEN="$TOKEN" INSTALL_K3S_EXEC="--node-ip=192.168.56.111" sh -

echo "K3S Agent Installé"
