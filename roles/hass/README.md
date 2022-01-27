# Ansible Role: Grafana

This role will setup a supervised Home Assistant using packages provided by Home Assistant.
To installation directory for hass is defined in the hass-srv-dir role.

## Requirements

Python3
Docker

## Role Variables

* machine_type: see the list at [Home Assistant](https://github.com/home-assistant/supervised-installer)

## Dependencies

It needs following roles:

* robertdebock.update_package_cache
* hass-srv-dir
* docker

## Usage Examples

### Example Playbooks

```yaml
- hosts: localhost
    roles:
        - role: hass-srv-dir
        - role: docker
        - role: hass
```
