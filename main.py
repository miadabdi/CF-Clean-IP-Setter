from cf_api import CFApi
from scan import scan, find_last_result
from retrieve_ips import retrieve_ips
import json
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(dir_path, "config.json")
config = json.loads(open(env_path).read())

if config['use_provided_result'] == False:
    retrieve_ips(config)
    scan(config['output_file'], config['scan_concurrency'], config['upload_speed'], config['custom_config'])
    config['last_result_path'] = find_last_result()


cfApi = CFApi(config['email'], config['global_key'], config['zone_id'])
cfApi.replace_ips(config['last_result_path'], config['max_no_records'], config['sub_domain'])
