import subprocess
import os


def scan(ips_file, threads, speed, custom_config):
    bashCommand = f"bash CFScanner/bash/cfScanner.sh -vpn YES --test-type UP --mode IP --thread {threads} --tryCount 1 --config {custom_config} --speed {speed} --file {ips_file}"

    print("Running Scanner")

    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) #, stdout=subprocess.PIPE)
    output, error = process.communicate()
        
    if error != None:
        raise Exception('error happaned during testing ips')

    print("Scanning done")

    print("removing redundant config files")
    filelist = os.listdir('./CFScanner/config')
    for f in filelist:
        os.remove(os.path.join('./CFScanner/config', f))

def find_last_result():
    onlyfiles = [f for f in os.listdir('./CFScanner/result') if os.path.isfile(os.path.join('./result', f))]
    last_created_result = onlyfiles[-1]
    last_created_result_path = f'./CFScanner/result/{last_created_result}'

    return last_created_result_path
