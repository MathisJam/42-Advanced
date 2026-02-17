#!/bin/bash
set -e

curl -sfL https://get.k3s.io | \
  INSTALL_K3S_EXEC="--node-ip=192.168.56.110 --write-kubeconfig-mode=644" sh -

# attendre que le kubeconfig existe
while [ ! -f /etc/rancher/k3s/k3s.yaml ]; do
  sleep 1
done

# corriger l'IP dans le kubeconfig
sudo sed "s/127.0.0.1/192.168.56.110/g" /etc/rancher/k3s/k3s.yaml > /vagrant/kubeconfig

# exporter le token
sudo cat /var/lib/rancher/k3s/server/node-token > /vagrant/node-token

echo "K3S Server Installé"
