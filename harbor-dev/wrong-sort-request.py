import requests
import json

def get_sorted_values(key):
    j = requests.get(f"http://127.0.0.1:80/api/v2.0/projects?page=1&page_size=100&sort={key}&with_detail=true").json()
    print(f"j: {json.dumps(j, indent=4)}")
    return [x[key] for x in j]

keys = ['repo_count','owner_name','creation_time','name','owner_id','project_id','update_time']

for key in keys:
    print(key, get_sorted_values(key))

# repo_count [1, 0, 0, 3, 3, 1, 1]
# owner_name ['admin', 'gxr', 'admin', 'srini', 'srini', 'hoachvbnd', 'admin']
# chart_count [0, 0, 0, 0, 0, 0, 0]
# creation_time ['2023-03-09T05:00:36.132Z', '2023-03-09T06:03:49.190Z', '2023-03-09T07:24:36.972Z', '2023-03-09T08:06:22.627Z', '2023-03-09T13:57:47.875Z', '2023-03-09T14:50:57.258Z', '2023-03-09T15:42:38.237Z']
# name ['demo', 'gxr', 'library', 'operator12', 'operator7', 'test_harhor', 'zk-test']
# owner_id [1, 1, 1, 3, 3, 5, 14]
# project_id [1, 3, 7, 8, 12, 13, 14]
# update_time ['2023-03-09T05:00:36.132Z', '2023-03-09T06:03:49.190Z', '2023-03-09T07:24:36.972Z', '2023-03-09T08:06:22.627Z', '2023-03-09T13:57:47.875Z', '2023-03-09T14:50:57.258Z', '2023-03-09T15:42:38.237Z']