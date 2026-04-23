# c4geeks/ansible

Companion playbooks, roles, and inventory examples for the **ComputingForGeeks Ansible series**.

Every folder in this repo maps to a published article at [computingforgeeks.com](https://computingforgeeks.com/). Clone it, open the subdirectory that matches the article you're reading, and run the example.

```bash
git clone https://github.com/c4geeks/ansible.git c4geeks-ansible
cd c4geeks-ansible
```

---

## Series index

### Pillar + reference
- **Ansible Automation Guide** — [article](https://computingforgeeks.com/ansible-automation-guide/) · `pillar/`
- **Ansible Cheat Sheet** — [article](https://computingforgeeks.com/ansible-cheat-sheet/) · `cheatsheet/`

### Beginner
| Article | Folder |
|---|---|
| [Install Ansible on Rocky Linux 10 & Ubuntu 24.04](https://computingforgeeks.com/install-ansible-rocky-linux-ubuntu/) | `beginner/install-ansible-rocky-linux-ubuntu/` |
| [Ansible Ad-Hoc Commands](https://computingforgeeks.com/ansible-ad-hoc-commands/) | `beginner/ansible-ad-hoc-commands/` |
| [Ansible Inventory Management](https://computingforgeeks.com/ansible-inventory-management/) | `beginner/ansible-inventory-management/` |
| [Your First Ansible Playbook](https://computingforgeeks.com/ansible-playbook-tutorial/) | `beginner/ansible-playbook-tutorial/` |
| [Ansible Variables](https://computingforgeeks.com/ansible-variables-tutorial/) | `beginner/ansible-variables-tutorial/` |
| [Ansible Conditionals and Loops](https://computingforgeeks.com/ansible-conditionals-loops-tutorial/) | `beginner/ansible-conditionals-loops-tutorial/` |
| [Ansible Jinja2 Templates](https://computingforgeeks.com/ansible-jinja2-templates-tutorial/) | `beginner/ansible-jinja2-templates-tutorial/` |
| [Ansible Roles Tutorial](https://computingforgeeks.com/ansible-roles-tutorial/) | `beginner/ansible-roles-tutorial/` |
| [Debug Ansible Playbooks: 10 Tools and Patterns](https://computingforgeeks.com/ansible-debugging/) | `beginner/ansible-debugging/` |

### Intermediate
| Article | Folder |
|---|---|
| [Ansible Vault](https://computingforgeeks.com/ansible-vault-tutorial/) | `intermediate/ansible-vault-tutorial/` |
| [Ansible Dynamic Inventory](https://computingforgeeks.com/ansible-dynamic-inventory-tutorial/) | `intermediate/ansible-dynamic-inventory-tutorial/` |
| [Test Ansible Roles with Molecule](https://computingforgeeks.com/ansible-molecule-testing/) | `intermediate/ansible-molecule-testing/` |

### Advanced
| Article | Folder |
|---|---|
| [Event-Driven Ansible (EDA)](https://computingforgeeks.com/event-driven-ansible-eda-tutorial/) | `advanced/event-driven-ansible-eda-tutorial/` |

### Integrations
| Article | Folder |
|---|---|
| [Terraform + Ansible](https://computingforgeeks.com/terraform-ansible-tutorial/) | `integrations/terraform-ansible-tutorial/` |
| [Ansible + Proxmox](https://computingforgeeks.com/ansible-proxmox-tutorial/) | `integrations/ansible-proxmox-tutorial/` |
| [Ansible for Windows Server](https://computingforgeeks.com/ansible-windows-server-tutorial/) | `integrations/ansible-windows-server-tutorial/` |

### Projects / Comparisons
| Article | Folder |
|---|---|
| [Harden Rocky Linux 10 with Ansible (CIS L1)](https://computingforgeeks.com/ansible-server-hardening/) | `projects/ansible-server-hardening/` |
| [Ansible vs Chef vs Puppet vs Salt](https://computingforgeeks.com/ansible-vs-chef-puppet-salt/) | `projects/ansible-vs-chef-puppet-salt/` |

### Planned (not yet published)
See the full 45-article plan at [computingforgeeks.com/ansible-automation-guide/](https://computingforgeeks.com/ansible-automation-guide/). Folders appear here as each article ships.

---

## Layout

```
pillar/             Code referenced by the pillar article
cheatsheet/         Snippets from the cheat sheet
beginner/           Playbooks for articles 1-10
intermediate/       Playbooks for articles 11-20
advanced/           Playbooks for articles 21-30
integrations/       Terraform, Proxmox, Cloudflare, Vault, GitLab CI, K8s, etc.
projects/           LAMP, hardening, user mgmt, backup, comparisons
ansible.cfg         Shared config used across examples
```

Per-article folders are named by the article's URL slug so you can jump from article to folder in one hop.

## How to use an example

```bash
cd beginner/ansible-playbook-tutorial/
# Read the folder's README for what's inside and how to run it
ansible-playbook -i inventory site.yml
```

Every folder with code has its own README explaining inventory expectations, required collections, and run commands.

## Requirements

- Ansible 2.16+ (`ansible-core` 2.16+)
- Python 3.10+
- `ansible-galaxy collection install -r requirements.yml` in folders that declare one

## Contributing

Issues and PRs welcome. If you spot a bug in an example referenced by a published article, open an issue linking the article URL and the folder. Fixes land in the repo first, then in the article.

## License

MIT — see [LICENSE](./LICENSE).

## Related c4geeks repos

- **k3s-ansible** — K3s cluster deploy role (pending absorption into `integrations/`)
- **ocp4_ansible** — OpenShift 4 automation (pending absorption into `integrations/`)
- **tomcat-ansible** — Tomcat role (pending absorption into `projects/`)
