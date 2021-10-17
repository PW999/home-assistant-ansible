import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_influx_container(host):
    samba = host.docker('samba')
    assert samba.is_running, 'The samba container'


@pytest.mark.parametrize('port', [
  139, 445
])
def test_tcp_port(host, port):
    socket = host.socket(f'tcp://0.0.0.0:{port}')
    assert socket.is_listening, f'Samba should be listening on TCP port {port}'


@pytest.mark.parametrize('port', [
  137, 138
])
def test_udp_port(host, port):
    socket = host.socket(f'udp://0.0.0.0:{port}')
    assert socket.is_listening, f'Samba should be listening on UDP port {port}'


def test_mount(host):
    # 32 => resoure is busy, in case of re-running tests with molecule verify
    host.run_expect([0, 32], 'mount -t cifs -o rw,vers=3.0,credentials=/root/.smbcredentials \
                            //127.0.0.1/data /mnt/data')
    assert host.file('/mnt/data/samba/docker-compose.yaml').exists
