# Ansible Role: aliasses

Configures aliasses for a list of users

## Requirements

This role assumes that every user also has a group with the same name as the user.

This role assumse that the user's home directory is /home/<username>

This role does not work for the root user.

## Role Variables

* alias_user_list: a list of users for which the aliases should be created

## Dependencies

None

## Usage Examples

### Example Playbooks

```yaml
- hosts: localhost
    roles:
        - role: aliasses
```

