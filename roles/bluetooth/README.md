# Ansible Role: bluetooth

Installs bluez and ensures that bluetooth services is running

## Requirements

A bluetooth adapter is needed, because of this, the automated testing of this role is pretty limited

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
        - role: bluetooth
```

