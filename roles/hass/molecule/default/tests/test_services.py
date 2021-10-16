import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('service', [
  'NetworkManager',
  'hassio-supervisor'   # installed by the convenience script
])
def test_service_running(host, service):
    print(f'Checking if {service} is running and enabled')
    service = host.service(service)
    assert service.is_running, f'The service {service} should be running'
    assert service.is_enabled, f'The service {service} should be enabled'


def test_service_not_running(host):
    service = host.service('ModemManager')
    assert not service.is_running, f'The service {service} should not be running'
    assert not service.is_enabled, f'The service {service} should not be enabled'
