# Ansible + Docker Lab

Companion repo folder for the article
[Manage Docker Containers with Ansible on Rocky Linux and Ubuntu](https://computingforgeeks.com/how-to-manage-docker-containers-with-ansible/).

One Ansible role plus seven playbooks. Installs Docker on Rocky 10 and Ubuntu 24.04
managed hosts, runs containers, deploys a docker compose observability stack,
ships rolling updates with `serial: 1`, backs up named volumes, and tears the
whole lab down on demand.

## Layout

```
ansible-docker/
├── ansible.cfg                # callbacks, ssh pipelining, fact caching
├── inventory.ini              # 3-host lab (control + 2 managed)
├── inventory-solo.ini         # single-host (ansible_connection=local)
├── group_vars/                # registry, stack root, observability ports
├── roles/docker/              # OS-dispatching install role
├── playbooks/
│   ├── 00-ping.yml            # preflight reachability
│   ├── 01-install-docker.yml  # the install role
│   ├── 02-run-container.yml   # single Uptime Kuma container
│   ├── 03-build-and-push.yml  # build sample image, push to GHCR
│   ├── 04-compose-stack.yml   # Uptime Kuma + cadvisor + Watchtower
│   ├── 05-rolling-update.yml  # serial: 1 with healthcheck wait
│   ├── 06-backup-volumes.yml  # tarball every named volume
│   └── 07-uninstall.yml       # tear down lab (optional engine remove)
├── templates/observability/   # compose.yml.j2 for the stack
├── collections/requirements.yml
└── vault/registry.yml.example # template for ansible-vault encrypt
```

## Quick start

```bash
git clone https://github.com/c4geeks/ansible.git
cd ansible/intermediate/ansible-docker

ansible-galaxy collection install -r collections/requirements.yml

# Edit inventory.ini with your real host IPs.
ansible -i inventory.ini docker_hosts -m ping

ansible-playbook -i inventory.ini playbooks/01-install-docker.yml -K
ansible-playbook -i inventory.ini playbooks/02-run-container.yml
ansible-playbook -i inventory.ini playbooks/04-compose-stack.yml
ansible-playbook -i inventory.ini playbooks/05-rolling-update.yml
```

## Solo mode (1 host)

```bash
ansible-playbook -i inventory-solo.ini playbooks/01-install-docker.yml -K
```

## Image push (GHCR)

```bash
cp vault/registry.yml.example vault/registry.yml
# edit, then encrypt:
ansible-vault encrypt vault/registry.yml

ansible-playbook -i inventory.ini playbooks/03-build-and-push.yml \
  -e @vault/registry.yml --ask-vault-pass
```

## Tear down

```bash
ansible-playbook -i inventory.ini playbooks/07-uninstall.yml
# or, to also remove Docker Engine:
ansible-playbook -i inventory.ini playbooks/07-uninstall.yml -e remove_docker_engine=true -K
```

## Tested on

- Control: Rocky Linux 10.1, ansible-core 2.16.x
- Managed: Rocky Linux 10.1 + Ubuntu 24.04 LTS
- Docker Engine: current stable (docker-ce repo)
- community.docker collection: 4.x

## License

MIT (see repo root).
