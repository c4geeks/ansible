# Ansible Handlers Tutorial (article #7)

Companion code for the ComputingForGeeks article
[Use Ansible Handlers: notify, listen, force_handlers](https://computingforgeeks.com/ansible-handlers-tutorial/).

## Files

| File | Demonstrates |
|---|---|
| `inventory.ini` | One-host inventory pointing at a Rocky 10 managed node |
| `nginx_with_handlers.yml` | `notify`, `listen`, `meta: flush_handlers` in one play |
| `force_handlers.yml` | `force_handlers: true` runs handlers even after a task failure |
| `broken_notify.yml` | A handler-name mismatch and the runtime error it produces |

## Quick start

```bash
git clone https://github.com/c4geeks/ansible.git c4geeks-ansible
cd c4geeks-ansible/beginner/ansible-handlers-tutorial

# Edit inventory.ini to point at your own managed node (Rocky 10 with nginx-friendly setup)
vim inventory.ini

# The full demo (notify + listen + flush)
ansible-playbook -i inventory.ini nginx_with_handlers.yml

# Force handlers to run even after a failure
ansible-playbook -i inventory.ini force_handlers.yml

# Watch the runtime error from a name mismatch
ansible-playbook -i inventory.ini broken_notify.yml
```

## Related articles

- [Test Ansible Roles with Molecule](https://computingforgeeks.com/ansible-molecule-testing/)
- [Debug Ansible Playbooks: 10 Tools and Patterns](https://computingforgeeks.com/ansible-debugging/)
- [Ansible Roles Tutorial](https://computingforgeeks.com/ansible-roles-tutorial/)
- [Ansible Automation Guide (pillar)](https://computingforgeeks.com/ansible-automation-guide/)
