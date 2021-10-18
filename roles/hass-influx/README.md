# Ansible Role: Influx

This role will setup an influx database server using docker-compose.

Additionally it will add the configuration to home-assistant's configuration.yaml and secrets.yaml (and restart HA).

## Requirements

Python3

## Role Variables

* influxdb_version: The version of influx to install, the docker image should exist on hub.docker.com, defaults to 1.8.5
* influxdb_user: the read/write user for home-assistant, defaults to hass_rw
* influxdb_user_password: the password for above user
* influxdb_read_user: a read-only user, defaults to hass_ro
* influxdb_read_user_password: the password for above user
* influxdb_db: the name of the database, defaults to homeassistant
* influxdb_http_auth_enabled: whether you want http authentication enabled (true is advised)
* influxdb_admin_user: the admin user, defaults to admin
* influxdb_admin_password: the password for above user

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

