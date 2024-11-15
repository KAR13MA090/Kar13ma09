"""This module provides functions to check inputs."""
import base64
import os
import sys
from typing import Union
import requests
from colorama import Fore as F
from requests.exceptions import ConnectionError, InvalidURL, ReadTimeout

from tools.addons.ip_tools import __get_local_host_ips, set_target_http


def check_method_input() -> str:
    """Check if the method name is valid.

    Args:
        None

    Returns:
        - method - A valid method name
    """
    while (method := input(f"{F.RED}│   ├─── METHOD: {F.RESET}").lower()) not in [
        "http",
        "http-proxy",
        "slowloris",
        "slowloris-proxy",
        "syn-flood",
        "arp-spoof",
        "disconnect",
    ] or (method in ["syn-flood", "arp-spoof", "disconnect"] and os.name == "nt"):
        print(f"{F.YELLOW}│   ├───{F.MAGENTA} [!] {F.BLUE}Nhập một phương pháp hợp lệ!{F.RESET}")

    if method in ["syn-flood", "arp-spoof", "disconnect"] and os.getuid() != 0:
        print(
            f"{F.YELLOW}│   ├───{F.MAGENTA} [!] {F.BLUE}Cuộc tấn công này cần quyền Super User!"
        )
        print(
            f"{F.YELLOW}│   └───{F.MAGENTA} [!] {F.BLUE}Run: {F.GREEN}sudo {os.popen('which python').read()[:-1]} kar13ma09.py\n{F.RESET}"
        )
        sys.exit(1)

    return method


def check_number_input(x: str) -> int:
    """Check if an input is an integer number greater than zero.

    Args:
        - x - The name of the input field

    Returns:
        - y - A valid value
    """
    y: Union[str, int]

    while True:
        y = input(f"{F.YELLOW}│   ├─── {x.upper()}: {F.RESET}")
        try:
            y = int(y)
            if y <= 0:
                raise ValueError
        except ValueError:
            print(
                f"{F.YELLOW}│   ├───{F.MAGENTA} [!] {F.BLUE}Giá trị này phải là một số nguyên lớn hơn không!{F.RESET}"
            )
        else:
            return y


def check_http_target_input() -> str:
    """Check if the target is listening on HTTP port (80).

    Args:
        None

    Returns:
        - target - A valid target
    """
    while True:
        target = input(f"{F.RED}│   ├─── URL: {F.RESET}")
        try:
            requests.get("https://google.com", timeout=4)
            try:
                requests.get(set_target_http(target), timeout=4)
            except Exception as exc:
                raise InvalidURL from exc
        except (ConnectionError, ReadTimeout):
            print(
                f"{F.RED}│   ├───{F.MAGENTA} [!] {F.BLUE}Thiết bị không được kết nối với internet!{F.RESET}"
            )
        except InvalidURL:
            print(f"{F.RED}│   ├───{F.MAGENTA} [!] {F.BLUE}URL không hợp lệ!{F.RESET}")
        else:
            return target


def check_local_target_input() -> str:
    """Check if the target is in the local network.

    Args:
        None

    Returns:
        - target - A valid target
    """
    hosts = __get_local_host_ips()
    while (target := input(f"{F.RED}│   ├─── IP: {F.RESET}")) not in hosts:
        print(
            f"{F.RED}│   ├───{F.MAGENTA} [!] {F.BLUE}Không thể kết nối đến {F.CYAN}{target}{F.BLUE} trên mạng nội bộ!{F.RESET}{F.RESET}"
        )

    return target
