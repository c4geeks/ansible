# Add Grafana data sources with Ansible

Companion code for [Add Grafana Data Sources with Ansible: Prometheus and InfluxDB](https://computingforgeeks.com/how-to-add-grafana-data-source-using-ansible/).

Provisions Grafana data sources with the `community.grafana` collection, authenticated by a Grafana **service account token** (not the admin password). Tested in June 2026 against **Grafana 13** with `community.grafana` 2.3.0, driven from an Ansible control node.

## Layout

```
ansible.cfg
inventory/hosts.ini                       # localhost (the module is an API client)
group_vars/all.yml                        # grafana_url, token, the data-source list
grafana-datasources.yml                   # main playbook
roles/grafana_datasources/                # the reusable role
delete-datasource.yml                     # day-2: state: absent
rotate-token.yml                          # enforce_secure_data (push a rotated secret)
provisioning/                             # file-based alternative (Git/GitOps)
  deploy-provisioning.yml
  templates/datasources.yaml.j2
```

## Use

Install the collection, store your token with Ansible Vault, then run:

```bash
ansible-galaxy collection install community.grafana
ansible-playbook grafana-datasources.yml --ask-vault-pass
```

Run it again; it reports `changed=0`. Edit `group_vars/all.yml` to point at your
own Grafana, Prometheus, and InfluxDB, and to add more backends to the list.

## The secret gotcha

Grafana stores tokens write-only, so the module cannot detect a rotated secret
and leaves secure fields alone by default. Set `enforce_secure_data: true`
(see `rotate-token.yml`) to push a new token. That task then always reports
`changed`, so use it only while rotating.

## Two ways to provision

- **Module (`grafana-datasources.yml`)**: API-driven, data sources stay editable in the UI.
- **Files (`provisioning/deploy-provisioning.yml`)**: templates Grafana's own
  provisioning YAML and restarts it; data sources are read-only in the UI, Git-friendly.
