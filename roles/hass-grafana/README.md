# Ansible Role: Grafana

This role will setup a grafana server using docker-compose.

It will also provision a connection to the hass-influx database.

## Requirements

Python3

## Role Variables

* grafana_version: The version of grafana to install, the docker image should exist on hub.docker.com, defaults to 7.5.6

## Dependencies

It needs following roles:

* hass-srv-dir
* docker
* hass
* hass-influx

## Usage Examples

### Example Playbooks

```yaml
- hosts: localhost
    roles:
        - role: hass-srv-dir
        - role: docker
        - role: hass
```

