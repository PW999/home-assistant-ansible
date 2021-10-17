# Ansible Role: rsync backup

This role will setup an rsync cron job which creates a backup of the install and /etc directory.

This role assumes that you've setup a remote (SSH) location to which rsync can sync the files to.

Rsync will run as *root* since most of the files in the installation directory are owned by root and are not accissible by anyone other than root.

This role will also setup a logrotate configuration for the rsync log files.

## Requirements

Python3

## Role Variables

* hass_backup_log_dir: where the rsycn output is logged to, defaults to /var/log/backup
* hass_backup_ssh_key: the location of the private SSH key
* hass_backup_hour: at what time of day the cron job should run, defaults to 8 (and add 30 minutes for the /etc)
* hass_backup_rsync_destination: the remote location where the backups will be sync'ed to

## Dependencies

It needs following roles:

* robertdebock.update_package_cache
* hass-srv-dir
* nickhammond.logrotate

## Usage Examples

### Example Playbooks

```yaml
- hosts: localhost
  vars: 
    hass_backup_ssh_key: /home/me/install/hass-backup-key
    hass_backup_hour: 4
    hass_backup_rsync_destination: homeassistant@10.0.0.100::NetBackup/hass-backup/
  roles:
    - role: hass-rsync-backup
```

