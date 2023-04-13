def read_list(ips_file_path):
    print(f'Reading ips from file {ips_file_path}')
    # each line should be an ipv4
    custom_ips_file = open(ips_file_path, 'r')
    custom_ips = [ip.replace('\n', '') for ip in custom_ips_file.readlines()]
    custom_ips_file.close()

    print(f'Reading ips from file completed')

    return custom_ips

def write_list(output_file, ips):
    print(f'Writing ips into file {output_file}')

    with open(output_file, 'w') as file:
        file.write('\n'.join(ips))

    print(f'Writing ips completed')
