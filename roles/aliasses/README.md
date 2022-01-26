# Ansible Role: aliasses

Configures aliasses for a list of users. The list of aliasses can be found and configured in [files/bash_alias](files/bash_alias)

## Requirements

This role assumes that every user also has a group with the same name as the user.

This role assumes that the user's home directory is /home/\<username\>

This role does not work for the root user.

## Role Variables

* `aliasses_users`: a list of users for which the aliases should be created

## Dependencies

None

## Usage Examples

### Example Playbooks

```yaml
- hosts: localhost
    vars:
        - aliasses_users:
            - phillip
    roles:
        - role: aliasses
```
