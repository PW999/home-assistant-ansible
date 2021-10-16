import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('container', [
  'hassio_supervisor',
  'hassio_dns',
  'hassio_audio',
  'hassio_cli',
  'hassio_observer',
  'hassio_multicast',
  'homeassistant'
])
def test_docker_container_present(host, container):
    print(f'Checking if {container} is present')
    containers = host.docker(container)
    assert containers.is_running, f'The container {container} should be running'
