# Ansible Role: hass-srv-dir

Creates the directory where everything will be installed in. 
This role will also set the installation path as a fact which 
can be re-used by other roles.

## Requirements

None

## Role Variables

* install_dir: defaults to /srv

## Dependencies

None

## Usage Examples

### Example Playbooks

```yaml
- hosts: localhost
    roles:
        - role: hass-srv-dir
```

