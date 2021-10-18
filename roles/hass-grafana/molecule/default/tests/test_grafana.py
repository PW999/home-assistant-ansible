import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_grafana_container(host):
    influx = host.docker('grafana')
    assert influx.is_running, 'The grafana container should be running'


def test_grafan_listening(host):
    socket = host.socket('tcp://0.0.0.0:3000')
    assert socket.is_listening, 'Influx should be listening on port 3000'


def test_grafana_config(host):
    root = "/srv/grafana/etc/provisioning/datasources/influx.yaml"
    assert host.file(f'{root}').contains('user: molecule_ro_user')
    assert host.file(f'{root}').contains('password: molecule_ro_pass')
    assert host.file(f'{root}').contains('database: molecule_db')
