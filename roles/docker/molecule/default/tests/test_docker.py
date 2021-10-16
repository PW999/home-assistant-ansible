import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_service(host):
    print('Check if the docker service is running and enabled')
    docker = host.service('docker')
    assert docker.is_running, 'Docker service should be running inside docker'
    assert docker.is_enabled, 'Docker should be enabled'


def test_docker_command(host):
    print('Check if the docker ps command works')
    host.run_expect([0], 'docker ps')
