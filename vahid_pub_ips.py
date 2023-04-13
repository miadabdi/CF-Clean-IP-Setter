import requests
import re

vahid_list_ips = 'https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.json'
vahid_ips_url = 'https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.txt'
vahid_domains = 'https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/providers.json'

list_of_operators = ['MCI','MTN','MKH','RTL','HWB','AST','SHT','PRS','MBT','ASK','RSP','AFN','ZTL','PSM','ARX','SMT','FNV','DBN','APT']

def get_file_ips(operator):
    ips = []

    vahid_ips_page = requests.get(vahid_ips_url).text
    for line in vahid_ips_page.split('\n'):
        ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
        line_operator = 'unknown'
        for pvr in list_of_operators:
            if pvr in line:
                line_operator = pvr
        if (ip):
            ips.append({ 'ip':ip.group(0), 'operator': line_operator })

    print("Vahid IPs fetched")

    filtered_ips = [item['ip'] for item in ips if item['operator'] == operator or operator == 'ALL']

    return filtered_ips

def get_list_ips(filter_operator):
    ips = []

    list_ips = requests.get(vahid_list_ips).json()
    for ipv4 in list_ips['ipv4']:
        ip = ipv4['ip']
        operator = ipv4['operator']
        ips.append({ 'ip':ip, 'operator': operator })

    print("List of IPs fetched")

    filtered_ips = [item['ip'] for item in ips if (item['operator'] == filter_operator or filter_operator == 'ALL')]

    return filtered_ips

def get_domains(operator):
    domains_page = requests.get(vahid_domains)
    domains_json = domains_page.json()

    domains = []
    for domain, pvr in domains_json.items():
        if (pvr == operator or operator == 'ALL'):
            domains.append(domain)

    return domains
