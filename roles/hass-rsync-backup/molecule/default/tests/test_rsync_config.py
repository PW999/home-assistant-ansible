import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('package_name', [
  'cron',
  'rsync',
  'logrotate'
])
def test_package(host, package_name):
    package = host.package(package_name)
    assert package.is_installed, f'{package_name} should be present'


def test_cron(host):
    crontab = host.run('sudo crontab -l')
    assert '0 6 * * * echo rsync -av --delete -e "ssh -i /root/.ssh/homeassistant-rsync -p 22" ' \
        '/srv homeassistant@10.0.0.100::NetBackup/hass-backup/ 2>&1 >> /var/log/backup/rsync.log' in crontab.stdout
    assert '30 6 * * * echo rsync -av --delete -e "ssh -i /root/.ssh/homeassistant-rsync -p 22" ' \
        '/etc homeassistant@10.0.0.100::NetBackup/hass-backup/ 2>&1 >> /var/log/backup/rsync.log' in crontab.stdout


def test_private_key(host):
    key = host.file('/root/.ssh/homeassistant-rsync')
    assert key.exists, 'The private key should exist'
    assert key.user == 'root', 'The private key should be owned by root'
    assert key.group == 'root', 'The private key should be owned by root'
    assert key.mode == 0o400, 'The private key should only be read-able by the owner'


def test_logrotate_cron(host):
    assert host.file('/etc/cron.daily/logrotate').exists, 'Logrotate should run daily'
