import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hass_running(host):
    assert host.socket("tcp://8123").is_listening, "Home assistant should be running and listening on port 8123"


def test_fetch_hass_homepage(host):
    result = host.check_output('curl -s http://localhost:8123/onboarding.html -v 2>&1')
    assert 'HTTP/1.1 200' in result
    # it can take a loooooong time before HASS is actually initialized, so this is the best we can do
    assert '<title>Home Assistant</title>' in result
