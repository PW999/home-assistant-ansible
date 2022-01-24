import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('package_name', [
  'python3',
  'python3-pip',
  'python3-wheel',
  'python3-dev',
  'python3-setuptools',
  'python3-cryptography'
])
def test_package(host, package_name):
    package = host.package(package_name)
    assert package.is_installed, f'{package_name} should be present'


def test_python3(host):
    host.run_expect([0], 'python3 --version')


def test_pip3(host):
    host.run_expect([0], 'pip3 --version')
