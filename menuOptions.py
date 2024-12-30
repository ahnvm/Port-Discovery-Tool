import sys
import os
import colorama
from datetime import datetime
import portScan as ps

colorama.init(autoreset=True)


def clear():
    os.system("clear")

def set_ip() -> str:
    while True:
        try:
            ip = input(f"{colorama.Fore.CYAN}Enter IP Pattern (like 127.0.0): {colorama.Style.RESET_ALL}")
            ip_list = ip.split(".")
            if (os.system("ping -c 1 " + ip) == 0):
                clear()
                return ip
            ip_list = [int(i) for i in ip_list]
            if len(ip_list) == 4:
                if ip_list[0] < 0 or ip_list[0] > 255 or ip_list[1] < 0 or ip_list[1] > 255 or ip_list[2] < 0 or ip_list[2] > 255 or ip_list[3] < 0 or ip_list[3] > 255:
                    clear()
                    print(f"{colorama.Fore.RED}[Input Error] Invalid IP{colorama.Style.RESET_ALL}")
                else:
                    return ip
            else:
                clear()
                print(f"{colorama.Fore.RED}[Input Error] You must enter 4 IP addresses or valid host{colorama.Style.RESET_ALL}")
        except ValueError:
            clear()
            print(f"{colorama.Fore.RED}[Input Error] Invalid IP{colorama.Style.RESET_ALL}")
            continue
        except KeyboardInterrupt:
            print(f"\n{colorama.Fore.YELLOW}Exiting...{colorama.Style.RESET_ALL}")
            sys.exit(0)
        except EOFError:
            print(f"\n{colorama.Fore.YELLOW}Exiting...{colorama.Style.RESET_ALL}")
            sys.exit(0)

def set_port_range() -> list:
    while True:
        try:
            port_range = input(f"{colorama.Fore.CYAN}Enter Port Range (like 15 380): {colorama.Style.RESET_ALL}")
            port_range_list = port_range.split(" ")
            if len(port_range_list) == 2:
                try:
                    port_range_list = [int(i) for i in port_range_list]
                    if port_range_list[0] < 0 or port_range_list[0] > 65534 or port_range_list[1] < 0 or port_range_list[1] > 65535:
                        clear()
                        print(f"{colorama.Fore.RED}[Input Error] Invalid Port Range{colorama.Style.RESET_ALL}")
                    elif port_range_list[0] >= port_range_list[1]:
                        clear()
                        print(f"{colorama.Fore.RED}[Input Error] Invalid Port Range{colorama.Style.RESET_ALL}")
                    else:
                        return port_range_list
                except ValueError:
                    clear()
                    print(f"{colorama.Fore.RED}[Input Error] Invalid Port Range{colorama.Style.RESET_ALL}")
            else:
                clear()
                print(f"{colorama.Fore.RED}[Input Error] You must enter 2 Port addresses{colorama.Style.RESET_ALL}")
        except ValueError:
            clear()
            print(f"{colorama.Fore.RED}[Input Error] Invalid Port Range{colorama.Style.RESET_ALL}")
            continue
        except KeyboardInterrupt:
            clear()
            print(f"\n{colorama.Fore.YELLOW}Exiting...{colorama.Style.RESET_ALL}")
            sys.exit(0)
        except EOFError:
            clear()
            print(f"\n{colorama.Fore.YELLOW}Exiting...{colorama.Style.RESET_ALL}")
            sys.exit(0)

def save_results(outlist):
    if not outlist:
        print(f"{colorama.Fore.RED}No results to save{colorama.Style.RESET_ALL}")
        return

    try:
        sorted_portlist = sorted(outlist, key=lambda x: x[0])
    except ValueError as e:
        print(f"{colorama.Fore.RED}Error sorting ports: {e}{colorama.Style.RESET_ALL}")
        return

    with open("results.txt", "w") as f:
        for port, status, timestamp in sorted_portlist:
            formatted_time = datetime.fromtimestamp(timestamp).strftime("[%Y-%m-%d/%H:%M]")
            f.write(f"{formatted_time} {port} is {status}\n")

    print(f"{colorama.Fore.YELLOW}Results saved to results.txt{colorama.Style.RESET_ALL}")


def print_port_list(outlist):
    upcount = 0
    downcount = 0
    open_ports = []
    for port, status, timestamp in outlist:
        formatted_time = datetime.fromtimestamp(timestamp).strftime("[%Y-%m-%d/%H:%M]")
        if status == "reachable":
            print(f"{colorama.Fore.YELLOW}{formatted_time} {colorama.Fore.GREEN}Port {port} is {status}{colorama.Style.RESET_ALL}")
            upcount += 1
            open_ports.append(port)
        else:
            print(f"{colorama.Fore.YELLOW}{formatted_time} {colorama.Fore.RED}Port {port} is {status}{colorama.Style.RESET_ALL}")
            downcount += 1
    print(f"{colorama.Fore.YELLOW}Total Ports: {len(outlist)}{colorama.Style.RESET_ALL}")
    print(f"{colorama.Fore.GREEN}Open Ports: {upcount}{colorama.Style.RESET_ALL} {open_ports}")
    print(f"{colorama.Fore.RED}Closed Ports: {downcount}{colorama.Style.RESET_ALL}")
    try:
        input(f"{colorama.Fore.YELLOW}Press enter to continue...{colorama.Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"{colorama.Fore.YELLOW}Exiting...{colorama.Style.RESET_ALL}")
        sys.exit(0)
    except EOFError:
        print(f"{colorama.Fore.YELLOW}Exiting...{colorama.Style.RESET_ALL}")
        sys.exit(0)

def scanPorts(ip, port_range, timeout, args) -> list:
    return ps.portScanThreads(ip, port_range,timeout, args, 16)