# Home Assistant Supervised Playbook

This playbook installs the latest Home Assistant Supervised on Debian/Raspbian/Ubuntu.

More information about the Home Assistant supervised installer can be found in [the official supervised repo](https://github.com/home-assistant/supervised-installer)

## Project Description

This ansible playbook creates a complete Home Assistant environment from scratch. I originally started working on this playbook because I wanted to have a fast way of restoring and re-installing Home Assistant in case something would happen to my current installation (because no Home Assistant means no lights).
The playbook can also install extra services like Influx and Grafana without relying on the Home Assistant Supervisor, this is mainly because I prefer to have an easy way to migrate such services to another instance. 
The playbook as it comes will reflect my personal setup, but I'll try to make it as configurable as possible for easy re-use.

Once installed you can update Home Assistant through it's supervisor, this playbook won't re-install Docker or Home Assistant once it's installed. Updating the OS and it's dependencies can be done using the playbook.

## Compatibility

The official Home Assistant documentation only mentions Debian 10 as supported host operating system, so the focus of this playbook lies on supporting that OS. Most roles are also tested against Ubuntu 20 and Ubuntu 21 in case you really want to run Home Assistant on another Debian based OS. Non-debian based OS'es are not (yet) supported by this playbook.

Keep in mind that the default outcome of this playbook does not meet the following of Home Assistant's criterias for having a "supported" setup: _"The operating system is dedicated to running Home Assistant Supervised."_ and _"No additional software, outside of the Home Assistant ecosystem, is installed."_. Skipping roles tagged with the 'extra' tag will bring you closest to a supported environment (see Advanced Installation) .

As I'm still working out all the details and I have not yet tested it on an actual Raspberry Pi. So far it's been tested using Molecule and on a Vagrant managed VirtualBox. As such, this playbook and it's variables might change and breaking changes between commits are possible.

## Prerequisites & Dependencies
Please read [Home Assistant 0014](https://github.com/home-assistant/architecture/blob/master/adr/0014-home-assistant-supervised.md) first. The playbook will handle most dependencies, just make sure to run it on Debian 10 or Raspbian 10.

In order to run the playbook you'll need

* Unlimited internet access
* Root access
* Python 3.7+
* Ansible 2.10+

If you are using a Raspberry Pi then it's strongly advised to boot it from an HDD/SSD. Home Asssitant isn't optimized for use on SD-cards and neither is InfluxDB (read: you **will** wreck your SD-card and loose everything on it).

# How to run the playbook
Assuming you'll be running Ansible directly on the target system, you can install everything with the following script.
```bash
sudo apt-get update -y
sudo apt-get install python3-pip git --no-install-recommends -y
pip3 install ansible

git clone https://github.com/PW999/home-assistant-ansible.git
cd home-assistant-ansible
ansible-galaxy install -r requirements.yaml

# Have a look at group_vars/all and update the variables to your needs
# You must do this because there's some passwords to update
# Using Ansible Vault for passwords would of course be the better solution
# So consider this a quick-and-dirty install
ansible-playbook playbook.yml -i hosts
```

The playbook _should_ automatically restart the system after everything is installed. If something goes wrong while runnig the playbook it's possible that the system won't restart so it's advised to reboot the system at least once after running it.

## Advanced installation
When configured correctly, the whole playbook will do the following:

* Install basic tools and utilities like htop, vim, ...
* Configure the hostname
* Create a swap file
* Configure your keyboard layout
* Configure OpenSSH
* Configure so handy aliasses
* Configure git username and e-mail
* Configure tune2fs
* Cleanup journalctl
* Create and configure linux users
* Install blueZ for bluetooth support
* Install Docker
* Install Home Assistant Supervised
* Create a backup script using rsync to a remote location
* Create an InfluxDB container
* Create a Grafana container
* Create a Samba container
* Configure the firewall

These different roles can be skipped either by skipping the associated tag or by not configuring the variables which are needed for that role.

### Tags
The different roles in the playbook are tagged to allow skipping certain parts of the playbook. By default, all roles are executed (if the variables are configured correctly).
| Tag         | Description                                                                           | Mandatory |
|-------------|---------------------------------------------------------------------------------------|-----------|
| core        | Configures the basics of the system and installs some basic utilities                 | Yes       |
| ha          | Installs docker and home assistant.                                                   | Yes       |
| maintenance | Some tasks to make sure the system remains healthy (e.g. tune2fs)                     | No        |
| bluetooth   | Installs bluetooth dependencies and starts the bluetooth service.                     | No        |
| backup      | Configures an rsync backup to a remote server.                                        | No        |
| history     | Installs an influx db and grafana server and updates the Home Assistant config files. | No        |
| samba       | Installs a Samba container.                                                           | No        |
| extra       | Everything 'extra' (backup, history, samba)                                           | No        |

You can skip any of the above tags by passing e.g. `--skip-tags "samba,history"` to the ansible playbook command. For an exact list of which roles are executed, please have a look at `playbook.yml`.

### Variables
Some roles are only executed if a certain variable has been defined.
Below is a list of the variables and what they trigger:

* `hostname`: the hostname will be set to this value, the system will reboot if the hostname was changed
* `swap_files`: a swapfile will be created and enabled
* `git_username` + `git_user_email` + `git_user_name`: git's `user.name` and `user.email` property will be set for the Linux user `git_username`
* `hass_backup_ssh_key` + `hass_backup_rsync_destination`: create the rsync back-up script
* `influxdb_admin_password` + `influxdb_read_user_password` + `influxdb_user_password`: Creates an InfluxDB and Grafana container and configure Home Assistant to connect and log to it
* `samba_password`: Creates a Samba container to share the installation dir
* `keyboard_layout` + `keyboard_model`: configures the keyboard layout if set
* `common_nameservers`: allows override the default DNS server configuration
* `tune2fs_settings`: set the maximum number of reboots before the filesystem is checked
* `unattended_package_blacklist`: setup unattended upgrades, I strongly encourage to blacklist docker and container.d to prevent sudden restarts of docker
* `openssh_permit_root_login`: configures openSSH, but the defaults allow root login so I strongly encourage to disable it
* `users_user_list`: creates or modifies the users in the list
* `aliasses_users`: adds some handy aliasses to the users in this list
* `maintenance_journalctl_vacuum`: cleans the journalctl logs which are older this the set value

# Available variables
There are a *ton* of variables to configure, please have a look at group_vars/all for an example.

Check the README's of the different roles in this repository to get a detailled overview of the hass's role's variables.

For the other roles, please have a look at these repo's README's
* [hostname](https://github.com/robertdebock/ansible-role-hostname)
* [git](https://github.com/robertdebock/ansible-role-git)
* [swap](https://github.com/robertdebock/ansible-role-swap)
* [sysctl](https://github.com/robertdebock/ansible-role-sysctl)
* [tune2fs](https://github.com/robertdebock/ansible-role-tune2fs)
* [maintenance](https://github.com/robertdebock/ansible-role-maintenance)
* [openssh](https://github.com/robertdebock/ansible-role-openssh)
* [users](https://github.com/robertdebock/ansible-role-users)
* [common](https://github.com/robertdebock/ansible-role-common)
* [keyboard](https://github.com/gantsign/ansible-role-keyboard)
* [unattended-upgrades](https://github.com/jnv/ansible-role-unattended-upgrades)

# Testing
All the included roles in this playbook are tested using Molecule using the Docker driver and the testinfra verifier. The containers are custom built to include systemd for supporting docker running inside docker independently from the host's docker installation. Even though nowadays you can run systemd inside Docker without a privileged containers, to get docker in docker working with systemd you still need a privileged container. Without this hacky setup, individual test runs could be impacted because of leftovers on the host system.

Since Home Assistant requires Docker to use the overlay2 driver, /var/lib/docker/overlay2 needs to be mounted to something outside the molecule test container so that docker (in docker) can write it's overlay2 data on a "normal" non-overlay2 filesystem, (overlay2 on overlay2 doesn't work). Because of the massive amounts of data which needs to be written to the overlay2 filesystem, mount it to a tmpfs is not possible because the default 1.5GB of RAM that's assigned to it is too small. Because of this, the molecule containers will mount /var/lib/docker/overlay2 somewhere in `/tmp`. This only works if `/tmp` isn't mounted as tmpfs in your host system.

Finally, to be able to run these tests you'll need a recent version of systemd on your host system. Systemd v148 (and higher?) is not supported though, it seems to break the systemd in docker support.

The assertions in the tests are usually very basic but should cover the correct functioning of the role. 
To prepare your environment for running tests:
```bash
sudo apt-get install python3 python3-pip
pip3 install pytest ansible molecule molecule[ansible,docker,lint] flake8 ansible-lint yamlllint pytest-testinfra
docker run -d --restart=always --cap-drop=all --name apt-cacher-ng -p 3142:3142 konstruktoid/apt-cacher-ng VerboseLog=1 Debug=7 ForeGround=1 PassThroughPattern=.*
```
The apt-cacher-ng docker container might speed up the molecule tests as it will cache all apt packages (the hit ratio on a good evening is 80%, which saved 1GB of data transfers).

There's a bash script in the roles folder which will execute `molecule test` for all roles. I don't have the fastest setup ever (Manjaro, 3rd gen i3 running on a 10 years old HDD) but I can easily go have diner while all tests are running. To upside to the slowness is that I can optimize the playbook for running on even slower hardware. To run the molecule tests you need to specify three environment variables:
* `MOLECULE_NAME`: an arbitrary name which will be used as the name for the container and the overlay2 folder in ` /tmp`
* `MOLECULE_DISTRO`: the distribution to use, either debian or ubuntu
* `MOLECULE_DISTRO_VERSION`: the version of the distro's docker image to use (e.g. `10.10` for Debian)
The above environment variables can be set using the `setenv.sh` script.
