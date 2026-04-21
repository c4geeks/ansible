# Test Ansible Roles with Molecule (article #14)

Companion code for the ComputingForGeeks article
[Test Ansible Roles with Molecule: Real Pitfalls and Fixes](https://computingforgeeks.com/ansible-molecule-testing/).

## What's here

```
intermediate/ansible-molecule-testing/
└── roles/
    └── cfg_nginx_site/                # the role being tested
        ├── defaults/                  # tunable variables
        ├── handlers/                  # nginx reload
        ├── meta/                      # galaxy metadata
        ├── tasks/                     # main + OS-family installers
        ├── templates/                 # vhost + index page
        └── molecule/
            ├── default/               # full lifecycle on Rocky 10
            ├── ci/                    # leaner CI scenario
            └── multi-os/              # Rocky 10 + Ubuntu 24.04 in parallel
```

## Quick start

```bash
git clone https://github.com/c4geeks/ansible.git c4geeks-ansible
cd c4geeks-ansible/intermediate/ansible-molecule-testing/roles/cfg_nginx_site

# One-time toolchain setup
python3 -m venv .venv && source .venv/bin/activate
pip install ansible-core==2.18.* molecule molecule-plugins[podman] ansible-lint

# Run the full lifecycle on Rocky 10
molecule test -s default

# Or test against Rocky 10 + Ubuntu 24.04 in parallel
molecule test -s multi-os
```

## Scenarios

| Scenario | Hosts | Purpose |
|---|---|---|
| `default` | Rocky Linux 10 | Full lifecycle: dependency, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy |
| `ci` | Rocky Linux 10 | Lean cycle for CI: dependency, syntax, create, prepare, converge, verify, destroy |
| `multi-os` | Rocky Linux 10 + Ubuntu 24.04 | Parallel run proving the role works on both RHEL and Debian families |

## CI

A GitHub Actions matrix at `.github/workflows/molecule.yml` runs both `default`
and `multi-os` on every push.

## Related articles

- [Ansible Roles Tutorial](https://computingforgeeks.com/ansible-roles-tutorial/)
- [Ansible Vault](https://computingforgeeks.com/ansible-vault-tutorial/)
- [Ansible Dynamic Inventory](https://computingforgeeks.com/ansible-dynamic-inventory-tutorial/)
- [Ansible Automation Guide (pillar)](https://computingforgeeks.com/ansible-automation-guide/)
