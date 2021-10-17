# Ansible Role: rsync backup

This role will create a Samba docker container which exposes the install dir (/srv by default) as a Sambda share called "data".
Since a lot of files are owned by root by default (docker), the samba user is also root.

Make sure to use a strong password because this Samba share gives full read- and write access to the whole configuration (including sensitive data).

## Requirements

Python3

## Role Variables

* samba_version: The version of gists/samba-server to install
* samba_password: The password to use for the samba user
* samba_workgroup: Your networks workgroup

## Dependencies

It needs following roles:

* hass-srv-dir
* docker

## Usage Examples

### Example Playbooks

```yaml
- hosts: localhost
  vars: 
    samba_workgroup: MYCASA
    samba_version: 4.12.9
    samba_password: "M@k€_th1s_à-verry-Str0000ng-p@ssWooooord"
  roles:
    - role: hass-samba
```

