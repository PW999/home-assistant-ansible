# Ansible Role: Grafana

This role will setup a supervised Home Assistant using the convenience script provided by Home Assistant.
To installation directory for hass is defined in the hass-srv-dir role.

## Requirements

Python3

## Role Variables

* machine_type: see the list at [Home Assistant](https://github.com/home-assistant/supervised-installer)

## Dependencies

It needs following roles:

* hass-srv-dir
* docker
* hass

## Usage Examples

### Example Playbooks

```yaml
- hosts: localhost
    roles:
        - role: hass-srv-dir
        - role: docker
        - role: hass
```

