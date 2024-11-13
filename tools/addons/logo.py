"""This module provides a function that prints the logo's application."""
import base64
import os

from colorama import Fore as F


def show_logo() -> None:
    """Print the application logo.

    Args:
        None

    Returns:
        None
    """
    logo = """
███╗   ██╗████████╗████████╗████████╗ 
████╗  ██║╚══██╔══╝╚══██╔══╝╚══██╔══╝ 
██╔██╗ ██║   ██║      ██║      ██║     
██║╚██╗██║   ██║      ██║      ██║  
██║ ╚████║   ██║      ██║      ██║     
╚═╝  ╚═══╝   ╚═╝      ╚═╝      ╚═╝        
  """

    print(f"{F.YELLOW}{logo}")
    print("├─── Công Cụ Tấn Công")
    print("Dev By KAR13MA09")
    print("├─── AVAILABLE METHODS")
    print("├─── LAYER 7: HTTP | HTTP-PROXY | SLOWLORIS | SLOWLORIS-PROXY")
    if os.name!= "nt":
        print("├─── LAYER 4: SYN-FLOOD")
        print("├─── LAYER 2: ARP-SPOOF | DISCONNECT")
    print("├───┐")
