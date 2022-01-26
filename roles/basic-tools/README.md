# Ansible Role: basic-tools

A very basic role which installs some handy tools. Installs and updates following packages:

* vim-tiny (because vim pulls a load of dependencies and we want to keep it light)
* htop
* ca-certificates
* wget
* curl
* jq
* lsof

These tools are more a personal preference and are not needed for the actual installation of home assistant.

## Requirements

None

## Role Variables

None

## Dependencies

* robertdebock.update_package_cache: fetches updates for the package manager

## Usage Examples

### Example Playbooks

```yaml
- hosts: localhost
    roles:
        - role: robertdebock.update_package_cache
        - role: basic-tools
```
