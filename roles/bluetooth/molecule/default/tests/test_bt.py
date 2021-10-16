import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('package_name', [
  'bluez'
])
def test_package(host, package_name):
    package = host.package(package_name)
    assert package.is_installed, f'{package_name} should be present'


def test_service_exists(host):
    print('Checking if bluetooth exists')
    host.service('bluetooth')
