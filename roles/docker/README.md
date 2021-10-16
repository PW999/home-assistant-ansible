# Ansible Role: Docker

This script will install docker using the script from https://get.docker.com. 
The script is the preferred way of installing Docker on ARM and instead of 
replicating it's behaviour in Ansible (and needing to maintain it), the script 
will just be executed as-is (though we still install most dependencies using 
ansible).
Pip3 will be used to install docker-compose.

## Requirements

Python3

## Role Variables

None

## Dependencies

It needs following roles:

* robertdebock.update_package_cache
* basic-tools
* hass-srv-dir
* python3

## Usage Examples

### Example Playbooks

```yaml
- hosts: localhost
    roles:
        - role: robertdebock.update_package_cache
        - role: basic-tools
        - role: hass-srv-dir
        - role: python3
```

