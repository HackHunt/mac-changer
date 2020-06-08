#! usr/bin/env python3

import subprocess
import argparse
import re
import random
import sys
from termcolor import colored

def mac_change(interface, mac):
    print(colored("[+] Changing interface (" + interface + ") to down state", 'yellow'))
    subprocess.call(["ifconfig", interface, "down"])

    print(colored("[+] Changing MAC Address for " + interface + " to " + colored(mac, 'white'), 'yellow'))
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])

    print(colored("[+] Changing interface (" + interface + ") to up state\n", 'yellow'))
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    result = subprocess.check_output(["ifconfig", interface])
    mac_add = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))

    if mac_add:
        return mac_add[0]
    else:
        return -1


def check_mac(ori_mac, cur_mac):
    print(colored("[+/-] Checking current MAC Address...\n", 'yellow'))

    if ori_mac != cur_mac:
        print(colored("[+] MAC Address changed successfully.\n", 'green'))
    else:
        print(colored("[-] MAC Address is not changed. Please try again.\n", 'red'))


def generate_random_mac():
    print(colored("[+/-] Generating Random MAC Address...\n", 'yellow'))
    mac = ""
    possible_value = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                      'a','b','c', 'd', 'e']
    value_second_place = ['2', '4', '6', '8', 'a', 'c', 'e']

    for i in range(1, 13):
        if i == 2:
            value = random.choice(value_second_place)
        else:
            value = random.choice(possible_value)
        mac += value
        if i % 2 == 0 and i != 12:
            mac += ':'

    print(colored("[+] Random MAC Address generated successfully.\n", 'green'))
    return mac


def get_cmd_line_arguments():
    parser = argparse.ArgumentParser(prog="MAC Changer",
                                     usage="%(prog)s [options]\n\t[-i | --interface] interface_name\n\t[-m | --mac] mac_address",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=""">>> | MAC Changer v1.0 by Hack Hunt | <<<
    ---------------------------------""",
                                     epilog="*** If -m or --mac is not specified MAC will be generated randomly")


    parser._optionals.title = "Optional Argument"
    parser.add_argument('-m', '--mac',
                        dest='mac',
                        metavar="",
                        help='Specify new MAC address.')

    required_arguments = parser.add_argument_group("Required Argument")
    required_arguments.add_argument('-i','--interface',
                                    dest='interface',
                                    metavar="",
                                    help='Specify interface to change its MAC Address.',
                                    required=True)
    return parser.parse_args()


def main():

    args = get_cmd_line_arguments()
    interface = args.interface
    mac = args.mac

    try:
        subprocess.check_call(['ifconfig', interface], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print(colored("\n[-] Error! Interface (" + interface + ") not found!\n", 'red'))
        sys.exit()

    original_mac = get_current_mac(interface)
    if original_mac != -1:
        if not mac:
            mac_change(interface, generate_random_mac())
            current_mac = get_current_mac(interface)
            check_mac(original_mac, current_mac)
        elif mac[1].lower() in ['a', 'c', 'e', '2', '4', '6', '8']:
            mac_change(interface, args.mac)
            current_mac = get_current_mac(interface)
            check_mac(original_mac, current_mac)
        else:
            print(colored("\n[-] Please enter a valid MAC Address\n", 'red'))
    else:
        print(original_mac)


main()