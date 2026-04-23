# Debugging Ansible Playbooks (article #10)

Companion code for the ComputingForGeeks article
[Debug Ansible Playbooks: 10 Tools and Patterns That Actually Work](https://computingforgeeks.com/ansible-debugging/).

## Files

| File | Purpose |
|---|---|
| `inventory.ini` | One-host inventory pointing at a Rocky 10 managed node |
| `deploy_app.yml` | Clean working playbook: tiny systemd-managed http.server demo |
| `broken_v1.yml` | Same playbook with a deliberate undefined-variable typo |
| `debug_with_assert.yml` | Defensive variant with `debug` + `assert` pre-flight checks |

## Quick start

```bash
git clone https://github.com/c4geeks/ansible.git c4geeks-ansible
cd c4geeks-ansible/beginner/ansible-debugging

# Edit inventory.ini to point at your own managed host
vim inventory.ini

# Working flow
ansible-playbook -i inventory.ini deploy_app.yml

# Failing flow (deliberate typo)
ansible-playbook -i inventory.ini broken_v1.yml

# Defensive variant (fails fast with assert)
ansible-playbook -i inventory.ini debug_with_assert.yml
ansible-playbook -i inventory.ini debug_with_assert.yml -e 'app_message=Hello'
```

## Diagnostic flags reference

```bash
# Inventory introspection
ansible-inventory -i inventory.ini --graph
ansible-inventory -i inventory.ini --host web1
ansible all -i inventory.ini -m ping

# Pre-flight
ansible-playbook -i inventory.ini --syntax-check deploy_app.yml
ansible-playbook -i inventory.ini deploy_app.yml --list-tasks
ansible-playbook -i inventory.ini --check --diff deploy_app.yml

# Run with logging
ANSIBLE_LOG_PATH=/tmp/ansible.log \
  ansible-playbook -i inventory.ini deploy_app.yml -vv

# The deepest dial — only when nothing else explains the issue
ANSIBLE_DEBUG=1 ANSIBLE_LOG_PATH=/tmp/ansible-deep.log \
  ansible-playbook -i inventory.ini deploy_app.yml
```

## Related articles

- [Test Ansible Roles with Molecule](https://computingforgeeks.com/ansible-molecule-testing/)
- [Ansible Roles Tutorial](https://computingforgeeks.com/ansible-roles-tutorial/)
- [Ansible Vault](https://computingforgeeks.com/ansible-vault-tutorial/)
- [Ansible Automation Guide (pillar)](https://computingforgeeks.com/ansible-automation-guide/)
