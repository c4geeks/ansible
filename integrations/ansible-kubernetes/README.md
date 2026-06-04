# Ansible with Kubernetes: Deploy and Manage a Cluster

Companion code for the ComputingForGeeks guide
[Ansible with Kubernetes: Deploy and Manage a Cluster](https://computingforgeeks.com/ansible-kubernetes-cluster/).

Two jobs, one toolchain:

1. **Provision** a kubeadm cluster (containerd + Calico) with Ansible roles.
2. **Manage** workloads on it with the `kubernetes.core` collection.

Tested June 2026 on Ubuntu 24.04 with Kubernetes 1.36, kubernetes.core 6.4.0,
Calico 3.32 and Helm 3.21.

## Layout

```
ansible.cfg
inventory/hosts.ini           # control plane + workers
group_vars/all.yml            # k8s version, pod CIDR, pause image
bootstrap.yml                 # common -> control plane -> workers
roles/
  common/                     # swap, modules, sysctl, containerd, kube* packages
  control_plane/              # kubeadm init, Calico, join command
  worker/                     # kubeadm join
manage/
  01-deploy-app.yml           # namespace + ConfigMap + Secret + Deployment + Service
  02-helm-metrics-server.yml  # Helm install via Ansible
  03-day2-operations.yml      # drain / uncordon / rolling restart
```

## Controller setup

```bash
pipx install --include-deps ansible
pipx inject ansible kubernetes
ansible-galaxy collection install kubernetes.core
curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

## Run

```bash
# stand up the cluster
ansible-playbook bootstrap.yml

# manage workloads (uses the admin.conf fetched by bootstrap.yml)
ansible-playbook manage/01-deploy-app.yml
ansible-playbook manage/02-helm-metrics-server.yml
ansible-playbook manage/03-day2-operations.yml
```

Add a worker by appending it to `inventory/hosts.ini` under `[workers]` and
re-running `ansible-playbook bootstrap.yml`. The play is idempotent, so existing
nodes report `changed=0` and only the new node joins.

> The pod network CIDR in `group_vars/all.yml` is `10.244.0.0/16`. Keep it off
> your node/LAN subnet, or pod routing will collide with your network.
