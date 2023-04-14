import requests
import re
import concurrent.futures
from os import listdir
from os.path import isfile, join

class CFApi:
    base_url = 'https://api.cloudflare.com/client/v4'
    
    def __init__(self, email, global_key, zone_id) -> None:
        self.email = email
        self.global_key = global_key
        self.zone_id = zone_id

    def call(self, method, trailing_url, data = {}):
        headers = {'X-Auth-Key': self.global_key, 'X-Auth-Email': self.email, 'Content-Type': 'application/json'}
        url = f'{self.base_url}/{trailing_url}'

        req = requests.request(method, url, headers=headers, json=data)

        return req.json()

    def get_all_records(self) -> list:
        trailing_url = f'zones/{self.zone_id}/dns_records'
        response = self.call('GET', trailing_url)
        return response['result']

    def list_records(self):
        records = []
        fetched_records = self.get_all_records()

        for record in fetched_records:
            sub = record['name'].replace(record['zone_name'], '') [0:-1]
            if sub == '':
                sub = '@'

            records.append({
                'id': record['id'],
                'type': record['type'],
                'content': record['content'],
                'name': record['name'],
                'zone_name': record['zone_name'],
                'sub': sub
            })

        return records


    def update_record(self, record_id, name, content, proxied, type):
        data = {
            'name': name,
            'content': content,
            'proxied': proxied,
            'type': type
        }
        trailing_url = f'zones/{self.zone_id}/dns_records/{record_id}'
        response = self.call('PUT', trailing_url, data)

        if response['success'] == False:
            raise Exception(f'updating record failed: {response}')

        return response['result']


    def create_record(self,name, content, proxied, type):
        data = {
            'name': name,
            'content': content,
            'proxied': proxied,
            'type': type
        }
        trailing_url = f'zones/{self.zone_id}/dns_records'
        response = self.call('POST', trailing_url, data)

        if response['success'] == False:
            raise Exception(f'creating record failed: {response}')

        return response['result']

    def delete_record(self,record_id):
        trailing_url = f'zones/{self.zone_id}/dns_records/{record_id}'
        response = self.call('DELETE', trailing_url)

        if response['success'] == False:
            raise Exception(f'deleting record failed: {response}')

        return response['result']

    def linux_scan_to_iplist_sorted(self, result_file_path):
        data = []
        with open(result_file_path, 'r') as f:
            data = f.readlines()
        ips = []
        for item in data:        # iterate over the list items
            result = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', item) # extract the IP using regular expression
            delay = re.search(r'(\d*),', item) # extract the delay using regular expression
            if result:          # check if IP is found and add to the list
                ips.append({ 'ip': result.group(0), 'delay': int(delay.group(1)) })

        return sorted(ips, key=lambda x: x['delay'], reverse=False)

    def replace_ips(self, result_file_path, max_no_records, target_sub):
        result_ips = self.linux_scan_to_iplist_sorted(result_file_path)

        if len(result_ips) == 0:
            raise Exception("No ips were found in result file")
        
        print("Healthy IPs: \n", '\n'.join([f'ip: {item["ip"]} delay: {item["delay"]}' for item in result_ips]))

        print('Fetching existing records')
        existing_records = self.list_records()

        ids_to_delete = []
        for record in existing_records:
            if (record['sub'] == target_sub):
                print(f'deleting {record["content"]} of {target_sub}')
                # delete_record(record['id'])
                ids_to_delete.append(record['id'])

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for id in ids_to_delete:
                futures.append(executor.submit(self.delete_record, record_id=id))
            for future in concurrent.futures.as_completed(futures):
                # print(future)
                # print(f'deleting {record["content"]} of {target_sub} DONE')
                print(f'Deleting Done, result: {future.result()}')


        print('starting to create domains')
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for item in result_ips[:max_no_records]:
                futures.append(executor.submit(self.create_record, name=target_sub, content=item['ip'], proxied=False, type='A'))
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                print(f'created record for {target_sub} content {result["content"]}')

        print('done creating domains')
