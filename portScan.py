
import socket
import colorama
from colorama import Fore
from concurrent.futures import ThreadPoolExecutor
import threading
import sys
from datetime import datetime

colorama.init(autoreset=True)

g_silent = False
g_verbose = False
g_portlist = []
console_lock = threading.Lock()


def setArgs(args: list):
    global g_silent
    global g_verbose
    for arg in args:
        if arg == "-s":
            g_silent = True
        elif arg == "-v":
            g_verbose = True


def scan_port(ip: str, port: int, timeout: int):
    global g_portlist
    formatted_time = datetime.now().strftime("[%Y-%m-%d/%H:%M]") 
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((ip, port))
        with console_lock:
            if not g_silent:
                print(f"{formatted_time} {Fore.GREEN}Port {port} is reachable")
        s.close()
        g_portlist.append((port, "reachable", datetime.now().timestamp()))  # Add reachable port to the list
    except socket.timeout:
        with console_lock:
            g_portlist.append((port, "timeout", datetime.now().timestamp()))
            if not g_silent:
                print(f"{formatted_time} {Fore.RED}Port {port} is not reachable")
    except Exception as e:
        with console_lock:
            if g_verbose:
                g_portlist.append((port, f"exception: {e}", datetime.now().timestamp()))
            else:
                g_portlist.append((port, "exception", datetime.now().timestamp()))
            if g_verbose and not g_silent:
                print(f"{formatted_time} {Fore.RED}Port {port} exception: {e}")
            elif not g_silent:
                print(f"{formatted_time} {Fore.RED}Port {port} is not reachable")


def portScanThreads(ip: str, port_range: list, timeout: int, args: list, thread_count: int) -> list:
    setArgs(args)
    global g_portlist

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        futures = []
        for port in range(port_range[0], port_range[1] + 1):
            futures.append(executor.submit(scan_port, ip, port, timeout))

        # Wait for all threads to finish
        for future in futures:
            future.result()

    return g_portlist
