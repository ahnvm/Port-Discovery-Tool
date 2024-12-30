import os
import colorama
import menuOptions
import sys

colorama.init(autoreset=True)

g_ip = "0.0.0"
g_port_range_list = [0, 65535]
g_timeout = 1
g_port_list = []
g_known_ports = [20, 21, 22, 23, 25, 53, 80, 110, 123, 135, 139, 143, 443, 445, 993, 995, 3306, 3389, 8080, 8443]


ascii_art = f"""
{colorama.Fore.CYAN}
           _    _ _   ___      ____  __   _______ ____   ____  _       _____ 
     /\   | |  | | \ | \ \    / /  \/  | |__   __/ __ \ / __ \| |     / ____|
    /  \  | |__| |  \| |\ \  / /| \  / |    | | | |  | | |  | | |    | (___  
   / /\ \ |  __  | . ` | \ \/ / | |\/| |    | | | |  | | |  | | |     \___ \ 
  / ____ \| |  | | |\  |  \  /  | |  | |    | | | |__| | |__| | |____ ____) |
 /_/    \_\_|  |_|_| \_|   \/   |_|  |_|    |_|  \____/ \____/|______|_____/ 
                                                                             
                                                {colorama.Fore.YELLOW}by https://github.com/ahnvm
{colorama.Style.RESET_ALL}
"""

def menuChoices(choice):
    global g_ip
    global g_port_range_list
    global g_timeout
    global g_port_list
    if choice == "1":
        g_port_list.clear()
        g_port_list = menuOptions.scanPorts(g_ip, g_port_range_list, g_timeout, [])
    elif choice == "2":
        g_port_list.clear()
        g_port_list = menuOptions.scanPorts(g_ip, g_port_range_list, g_timeout, ["-s"])
    elif choice == "3":
        g_port_list.clear()
        g_port_list = menuOptions.scanPorts(g_ip, g_port_range_list, g_timeout, ["-v"])
    elif choice == "4":
        g_port_list.clear()
        g_port_list = menuOptions.scanPorts(g_ip, g_known_ports, g_timeout, ["-s"])
    elif choice == "5":
        g_ip = menuOptions.set_ip()
    elif choice == "6":
        g_port_range_list = menuOptions.set_port_range()
    elif choice == "7":
        g_timeout = menuOptions.set_timeout()
    elif choice == "8" and len(g_port_list) > 0:
        menuOptions.print_port_list(g_port_list)
    elif choice == "9" and len(g_port_list) > 0:
        menuOptions.save_results(g_port_list)
    elif choice == "0":
        print(f"{colorama.Fore.YELLOW}Exiting... Goodbye!")
        sys.exit(0)
    else:
        print(f"{colorama.Fore.RED}[Input Error] Invalid option. Please enter a number.")
        return
def main():
    while True:
        os.system("clear")
        global g_port_list
        print(ascii_art)
        print(f"{colorama.Fore.GREEN}1.{colorama.Style.RESET_ALL} Scan Ip For Open Ports")
        print(f"{colorama.Fore.GREEN}2.{colorama.Style.RESET_ALL} Scan Ip For Open Ports (Silent)")
        print(f"{colorama.Fore.GREEN}3.{colorama.Style.RESET_ALL} Scan Ip For Open Ports (Verbose)")
        print(f"{colorama.Fore.GREEN}4.{colorama.Style.RESET_ALL} Scan Known Ports {colorama.Fore.YELLOW}(Ports like shh, http, https, etc.)")
        print(f"{colorama.Fore.GREEN}5.{colorama.Style.RESET_ALL} Set IP {colorama.Fore.YELLOW}(Current IP: {g_ip}.({g_port_range_list[0]}-{g_port_range_list[1]}))")
        print(f"{colorama.Fore.GREEN}6.{colorama.Style.RESET_ALL} Set Port Range {colorama.Fore.YELLOW}(Current Port Range: {g_port_range_list[0]}-{g_port_range_list[1]})")
        print(f"{colorama.Fore.GREEN}7.{colorama.Style.RESET_ALL} Set Timeout {colorama.Fore.YELLOW}(Current Timeout: {g_timeout})")
        if len(g_port_list) > 0:
            print(f"{colorama.Fore.GREEN}8.{colorama.Style.RESET_ALL} Print Port List")
            print(f"{colorama.Fore.GREEN}9.{colorama.Style.RESET_ALL} Save Port List")
        print(f"{colorama.Fore.GREEN}0.{colorama.Style.RESET_ALL} Exit")
        try: 
            option = int(input(f"{colorama.Fore.CYAN}Enter option: {colorama.Style.RESET_ALL}"))
        except ValueError:
            print(f"{colorama.Fore.RED}[Input Error] Invalid option. Please enter a number.")
            continue
        except KeyboardInterrupt:
            print(f"\n{colorama.Fore.YELLOW}Exiting... Goodbye!")
            break
        except EOFError:
            print(f"\n{colorama.Fore.YELLOW}Exiting... Goodbye!")
            break
        menuChoices(str(option))

if __name__ == "__main__":
    main()
