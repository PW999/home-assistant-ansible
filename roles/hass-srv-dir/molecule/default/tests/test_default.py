import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('path', [
  '/srv',
  '/srv/setup'
])
def test_server_path(host, path):
    server_path = host.file(path)
    assert server_path.user == 'root'
    assert server_path.group == 'root'
