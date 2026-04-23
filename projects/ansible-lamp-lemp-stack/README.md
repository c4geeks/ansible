# Deploy WordPress on LAMP/LEMP with Ansible (article #41)

Companion code for the ComputingForGeeks article
[Deploy WordPress on Rocky 10 with Ansible (LAMP/LEMP Role)](https://computingforgeeks.com/ansible-lamp-lemp-stack/).

## What's here

```
projects/ansible-lamp-lemp-stack/
├── inventory.ini                       # [lamp] and [lemp] groups under [web]
├── deploy_wordpress.yml                # one-liner play that calls the role
└── roles/cfg_webstack/
    ├── defaults/main.yml               # site_domain, db creds, wp admin
    ├── handlers/main.yml               # Reload httpd / nginx / web (alias)
    ├── meta/main.yml                   # galaxy metadata
    ├── tasks/
    │   ├── main.yml                    # OS-family dispatcher
    │   ├── install_lamp.yml            # Rocky 10 packages
    │   ├── install_lemp.yml            # Ubuntu packages + apt cache
    │   ├── db.yml                      # MariaDB root + WP db + WP user
    │   ├── web_lamp.yml                # Apache vhost + SELinux context
    │   ├── web_lemp.yml                # Nginx vhost + sites-enabled
    │   └── wordpress.yml               # tarball + extract + wp-config + install
    └── templates/
        ├── site_apache.conf.j2
        ├── site_nginx.conf.j2
        └── wp-config.php.j2
```

## Quick start

```bash
git clone https://github.com/c4geeks/ansible.git c4geeks-ansible
cd c4geeks-ansible/projects/ansible-lamp-lemp-stack

# Edit inventory.ini with your real LAMP and/or LEMP hosts
vim inventory.ini

# Install deps on the controller
ansible-galaxy collection install community.mysql ansible.posix

# LAMP only
ANSIBLE_ROLES_PATH=$PWD/roles ansible-playbook -i inventory.ini --limit lamp deploy_wordpress.yml

# LEMP only
ANSIBLE_ROLES_PATH=$PWD/roles ansible-playbook -i inventory.ini --limit lemp deploy_wordpress.yml

# Both stacks in one shot
ANSIBLE_ROLES_PATH=$PWD/roles ansible-playbook -i inventory.ini deploy_wordpress.yml
```

## Production notes

- Rotate `db_root_password`, `db_password`, and `wp_admin_password` away from the
  defaults in `roles/cfg_webstack/defaults/main.yml`. Store them in
  [Ansible Vault](https://computingforgeeks.com/ansible-vault-tutorial/) instead.
- `pw_weak: "1"` in the WordPress install bypasses the strength check during
  bootstrap. Change the admin password to a strong one immediately afterward.
- The role runs `chcon -R -t httpd_sys_rw_content_t` for SELinux. For relabel
  durability, swap to `community.general.sefcontext` + `restorecon -R`.
- Override `siteurl` and `home` in `wp_options` if you are testing on an IP
  that does not match `site_domain`.

## Related articles

- [Test Ansible Roles with Molecule](https://computingforgeeks.com/ansible-molecule-testing/)
- [Harden Rocky Linux 10 with Ansible (CIS L1)](https://computingforgeeks.com/ansible-server-hardening/)
- [Use Ansible Handlers: notify, listen, force_handlers](https://computingforgeeks.com/ansible-handlers-tutorial/)
- [Debug Ansible Playbooks](https://computingforgeeks.com/ansible-debugging/)
- [Ansible Automation Guide (pillar)](https://computingforgeeks.com/ansible-automation-guide/)
