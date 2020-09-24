import json
import requests
automate_url = "https://automate.panerabread.com/api/v1/cfgmgmt/nodes/b2aae1cf-0716-49e9-ac82-b4e50bde8180/attribute"
payload = {}
headers = {
    'api-token': 'h9QeCIOta9nHXzd7irW4tznHdN4='
}
response = requests.request("GET", automate_url, headers=headers, data=payload)
# print(response.text.encode('utf8'))
# print(json.dumps(response.json(), indent=4))
default_data = response.json().get('default')
app_versions = json.loads(default_data).get('app_versions')
def find_mismatch_versions(hab_versions, automate_versions):
    for app, ver in automate_versions.items():
        print('{} : {}'.format(app, ver))
        if hab_versions.get(app) != ver:
            print('VERSION MISMATCH: {} Hab version {} Automate Version: {}'.format(app, hab_versions.get(app), ver))
print('APP VERSIONS: {}'.format(app_versions))
mocked_hab_app_versions = {'cookbook_version': {'45.0.0': True}, 'icafe-data-proxy': '1.40.0-3',
                    'icafe-feed-watcher': '1.10.0-1',
                    'icafe-icafe-service': '3.3.0-6', 'icafe-iris-interface': '1.61.0-1', 'icafe-office-ui': '1.15.0-3',
                    'icafe-order-service': '1.43.0-6', 'icafe-posui': '1.62.0-48', 'icafe-publisher': '1.6.0-2',
                    'icafe-user-service': '4.3.0-2', 'idataload': '3.8.0-4', 'proxy-ssl': '1.62.0-48',
                    'release_name': {'Quasimodo': True}, 'sqitch_migration_target': 'release-1.26.0',
                    'sqitch_migrations': '2020.02.18.160044'}
find_mismatch_versions(hab_versions=mocked_hab_app_versions, automate_versions=app_versions)