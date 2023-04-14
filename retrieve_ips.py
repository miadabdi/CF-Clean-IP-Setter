from resolve_domains import resolve_domains
from vahid_pub_ips import get_list_ips, get_domains
import ipv4_list_file

def retrieve_ips(config):
    # it will contain all ips which would be tested
    all_ips = []

    if config['include_list_ips']:
        # getting ips available in github.com/vfarid/cf-clean-ips
        vahid_ips = get_list_ips(config['operator'])
        all_ips.extend(vahid_ips)

    if config['include_list_domains']:
        # resolvig domains to ips
        domains_to_resolve = []

        vahid_domains = get_domains(config['operator'])
        domains_to_resolve.extend(vahid_domains)
        domains_to_resolve.extend(config['additional_domains'])

        public_ips = resolve_domains(domains_to_resolve)
        all_ips.extend(public_ips)

    # reading ips from a local file
    if config['include_custom_ips']:
        custom_ips = ipv4_list_file.read_list(config['custom_ips_file_path'])
        all_ips.extend(custom_ips)


    # delete duplicate ips
    all_ips = list(set(all_ips))

    print(f"Found {len(all_ips)} IPs")

    # writing final ips into a file
    ipv4_list_file.write_list(config['output_file'], all_ips)
