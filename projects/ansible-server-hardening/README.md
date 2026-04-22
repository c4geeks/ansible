# Ansible Server Hardening Playbook (article #42)

Companion code for the ComputingForGeeks article
[Harden Rocky Linux 10 with Ansible: CIS Level 1 Playbook](https://computingforgeeks.com/ansible-server-hardening/).

## Layout

```
projects/ansible-server-hardening/
├── inventory/
│   └── hosts.ini.example       # rename to hosts.ini and edit IPs
├── plays/
│   └── harden.yml              # one-liner play that applies the role
└── roles/
    └── cfg_hardening/
        ├── defaults/main.yml   # tunable knobs (SSH, sysctl, firewall, etc.)
        ├── handlers/main.yml   # restart sshd / fail2ban, reload auditd
        ├── tasks/
        │   ├── main.yml        # gated includes for each feature area
        │   ├── ssh.yml
        │   ├── sudoers.yml
        │   ├── sysctl.yml
        │   ├── firewall.yml
        │   ├── fail2ban.yml
        │   ├── auditd.yml
        │   ├── pam.yml
        │   └── banner.yml
        └── templates/
            ├── 99-cfg-hardening.conf.j2   # sshd_config drop-in
            └── jail.local.j2              # Fail2ban sshd jail
```

## Quick start

```bash
git clone https://github.com/c4geeks/ansible.git c4geeks-ansible
cd c4geeks-ansible/projects/ansible-server-hardening

cp inventory/hosts.ini.example inventory/hosts.ini
# edit inventory/hosts.ini with your real IP

ANSIBLE_ROLES_PATH=$PWD/roles \
  ansible-playbook -i inventory/hosts.ini plays/harden.yml
```

## Measuring the score

Run an OpenSCAP CIS Level 1 scan before and after the role to see the delta.
On a vanilla Rocky 10.1 the article measured **+9.63 percentage points**:

```bash
ssh root@TARGET "dnf -y install openscap-scanner scap-security-guide"
ssh root@TARGET "oscap xccdf eval \
  --profile xccdf_org.ssgproject.content_profile_cis_server_l1 \
  --results /root/scap-reports/baseline-results.xml \
  --report /root/scap-reports/baseline-report.html \
  /usr/share/xml/scap/ssg/content/ssg-rl10-ds.xml"
```

## Toggling features

Every section of the role is gated by a boolean default. Override in your
playbook or group_vars:

```yaml
hardening_apply_ssh:      true
hardening_apply_sudo:     true
hardening_apply_sysctl:   true
hardening_apply_firewall: true
hardening_apply_fail2ban: true
hardening_apply_auditd:   true
hardening_apply_pam:      true
hardening_apply_banner:   true
```

## Related articles

- [Test Ansible Roles with Molecule](https://computingforgeeks.com/ansible-molecule-testing/)
- [Ansible Vault](https://computingforgeeks.com/ansible-vault-tutorial/)
- [Ansible Automation Guide (pillar)](https://computingforgeeks.com/ansible-automation-guide/)
