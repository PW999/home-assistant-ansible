import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_alias(host):
    host.run_expect([0], 'sudo -u molecule /bin/bash -vilc ll')
