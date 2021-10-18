import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_influx_container(host):
    influx = host.docker('influx')
    assert influx.is_running, 'The influx container should be running'


def test_influx_listening(host):
    socket = host.socket('tcp://0.0.0.0:8086')
    assert socket.is_listening, 'Influx should be listening on port 8086'


def test_hass_config(host):
    root = "/srv/homeassistant/homeassistant"
    assert host.file(f'{root}/secrets.yaml').contains('influx_user: molecule_user')
    assert host.file(f'{root}/secrets.yaml').contains('influx_pass: molecule_pass')
    assert host.file(f'{root}/configuration.yaml').contains('username: !secret influx_user')
    assert host.file(f'{root}/configuration.yaml').contains('password: !secret influx_pass')
