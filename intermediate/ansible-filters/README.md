# Ansible Filters: Transform Data in Playbooks (article #15)

Companion code for the ComputingForGeeks article
[Ansible Filters: Transform Data in Playbooks](https://computingforgeeks.com/ansible-filters/).

Every playbook here targets `localhost` and prints its result with `debug`, so
none of them need an inventory or a remote host. Run any one and read the
output. These are the exact playbooks used to capture the output in the article.

## What's here

```
intermediate/ansible-filters/
├── defaults.yml            # default, default(omit), ternary, mandatory
├── strings.yml             # trim/lower, replace, regex_replace, split/join, regex_search
├── lists.yml               # map, selectattr/rejectattr, unique/sort, set algebra, zip/flatten
├── dicts.yml               # dict2items/items2dict, combine (+recursive)
├── numbers.yml             # int/float, round, human_readable, human_to_bytes, int(base=)
├── encoding.yml            # b64encode, hash, password_hash, to_nice_json/yaml, from_json
├── collection-filters.yml  # json_query (community.general), ipaddr (ansible.utils)
├── chained-transform.yml   # one expression: fleet data -> load-balancer server lines
└── requirements.yml        # the two collections, pinned for ansible-core 2.16
```

## Quick start

```bash
git clone https://github.com/c4geeks/ansible.git c4geeks-ansible
cd c4geeks-ansible/intermediate/ansible-filters

# core-only playbooks need nothing extra
ansible-playbook lists.yml
ansible-playbook chained-transform.yml

# the collection-filters playbook needs two collections + two Python libs
ansible-galaxy collection install -r requirements.yml
pip3 install --user jmespath netaddr
ansible-playbook collection-filters.yml
```

## The escaping gotcha worth remembering

Filters run in Jinja2 on the control node. A regex inside a **double-quoted**
YAML value needs **doubled** backslashes, or YAML rejects it before Ansible
runs:

```yaml
# fails to load: "found unknown escape character"
msg: "{{ logline | regex_search('\d+\.\d+\.\d+\.\d+') }}"

# works (doubled backslashes in a double-quoted value)
msg: "{{ logline | regex_search('\\d+\\.\\d+\\.\\d+\\.\\d+') }}"

# also works (single-quoted value, single backslashes)
msg: '{{ logline | regex_search("\d+\.\d+\.\d+\.\d+") }}'
```

Tested June 2026 on a Rocky Linux 10 control node (ansible-core 2.16.16,
community.general 10.7.9, ansible.utils 5.1.2).
