#!/usr/bin/python3
import platform
import sys
import subprocess


def get_ttl_number(host):
    param = '-n' if platform.system().lower() == "windows" else '-c'
    command = [f"ping {param} 1 {host}"]
    _process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = _process.communicate()
    return int(output.split()[12].split(b'=')[1])


def get_os_name_from_ttl(ttl_number):
    if 0 <= ttl_number <= 64:
        return 'Linux'

    elif 65 <= ttl_number <= 128:
        return 'Windows'
    else:
        return 'Unknown'


if __name__ == '__main__':
    host_ip = sys.argv[1]
    ttl = get_ttl_number(host_ip)

    try:
        print(f"\n{host_ip} --> {get_os_name_from_ttl(ttl)}")
    except:
        pass
