# Install and Use Ansible Collections (article #13)

Companion code for the ComputingForGeeks article
[Ansible Collections: Install and Use Community Content](https://computingforgeeks.com/ansible-collections-tutorial/).

A collection is the unit Ansible ships modules, roles, and plugins in, and
`ansible-galaxy` is the tool that installs them. This folder is a minimal,
reproducible project: a pinned `requirements.yml`, an `ansible.cfg` that keeps
collections project-local, and a playbook that calls three collections by their
fully qualified name.

## What's here

```
intermediate/ansible-collections/
├── ansible.cfg        # collections_path = ./collections (project-local wins)
├── inventory.ini      # one Rocky 10 host, one Ubuntu 24.04 host
├── requirements.yml   # collections + a role, pinned for ansible-core 2.16
└── site.yml           # FQCN demo: firewalld (RHEL) / ufw (Debian) / crypto cert
```

## Quick start

```bash
git clone https://github.com/c4geeks/ansible.git c4geeks-ansible
cd c4geeks-ansible/intermediate/ansible-collections

# Edit inventory.ini with your two hosts, then install the pinned set
ansible-galaxy collection install -r requirements.yml

# See what landed and where
ansible-galaxy collection list

# Run the cross-platform playbook
ansible-playbook site.yml
```

## Why the versions are pinned

Rocky Linux 10 and Ubuntu 24.04 ship `ansible-core` 2.16. The newest
`community.general` (13.x) and `community.crypto` (3.x) target a newer core and
print `does not support Ansible version 2.16.x`. The ranges in
`requirements.yml` stay on the lines that support 2.16:

| Collection          | Pinned range          | Reason                          |
|---------------------|-----------------------|---------------------------------|
| `community.general` | `>=10.0.0,<11.0.0`    | 10.x line supports core 2.16    |
| `community.crypto`  | `>=2.20.0,<3.0.0`     | 2.x line supports core 2.16     |
| `ansible.posix`     | `>=2.0.0,<3.0.0`      | current line, core 2.16 friendly|

After you upgrade `ansible-core` (for example with
`python3 -m pip install --user --upgrade ansible-core`), bump these ranges to
pick up the newest collections.

## Verify before you trust

```bash
ansible-galaxy collection verify community.general
```

A clean install reports `Successfully verified ...`; a modified file is named in
the output. Wire this into CI next to the install step.

Tested June 2026 on a Rocky Linux 10 control node (ansible-core 2.16.16)
managing Rocky Linux 10 and Ubuntu 24.04 hosts.
