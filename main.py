import scapy.all as sp
import ipaddress as ip

class MyClass:
    def __init__(self) -> None:
        pass
    
    def __repr__(self) -> str:
        return "This is MyClass repr!"

    def __str__(self) -> str:
        return "MyClass str"

# Naming convention:
# factory functions start with ip_*:
# ip_address, ip_network, ip_interface...

# --> https://docs.python.org/3/library/ipaddress.html
def _test_ipaddress() -> None:
    # we can create addresses from a generic factory function
    ip4_addr = ip.ip_address("127.0.0.1")
    ip6_addr = ip.ip_address("fe80::1")
    # there is no __bytes__ magic method, use packed instead
    print(ip4_addr.packed)

    # or directly
    ip4_specific_addr = ip.IPv4Address(1)
    print(f"Directly from ipv4 class: {ip4_specific_addr=}")

    # we can also create networks
    my_network = ip.ip_network("172.16.0.0/24")
    #my_network = ip.ip_network("172.16.0.17/24") # <-- fails, note that we should not declare host bits
    network_hosts = my_network.hosts()
    #for host in network_hosts:
    #    print(host)

def _test_formatting() -> None:
    a = 32
    my_class = MyClass()
    # '=' are used to also print the variable name
    print(f"Printing normal built-in type {a=}")
    # This should call the type's repr
    print(f"Printing my class repr {my_class=!r}")
    print(f"Printing my class repr {my_class=!s}")

    # testing width allignment
    print(f"Alligning the following text: {"some random text":😂^30} then extra text...")
    print(f"Printing hex values: {256:😳^30x} then extra text...")

    ip_addr = ip.ip_address("fe80::1")

def main():
    _test_ipaddress()

if __name__ == "__main__":
    main()

