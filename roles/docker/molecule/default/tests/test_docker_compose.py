import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_compose_command(host):
    print('Check if the docker-compose command works')
    host.run_expect([0], 'docker-compose --version')
