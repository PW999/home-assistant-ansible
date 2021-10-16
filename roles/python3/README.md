# Ansible Role: hass-srv-dir

Installs python3 and pip3

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
        - role: hass-srv-dir
```

