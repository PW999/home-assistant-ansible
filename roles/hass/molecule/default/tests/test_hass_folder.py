import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hass_folder(host):
    hass_home = host.file('/srv/homeassistant')
    assert hass_home.exists, 'Home folder should exist'
    assert hass_home.is_directory, 'Home folder should be a folder'
    assert hass_home.user == 'root'
    assert hass_home.group == 'root'


@pytest.mark.parametrize('file', [
  'homeassistant.json',
  'updater.json'
])
def test_some_hass_files(host, file):   # these are created when HASS starts, it's a basic indication that HASS works
    print(f'Checking if {file} is present')
    hass_home = host.file(f'/srv/homeassistant/{file}')
    assert hass_home.exists, f'{file} should exist'
    assert hass_home.is_file, f'{file} should be a file'
