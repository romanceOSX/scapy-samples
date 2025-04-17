import scapy.all as sp
import ipaddress as ip

class MyClass:
    def __init__(self) -> None:
        pass
    
    def __repr__(self) -> str:
        return "This is MyClass repr!"

    def __str__(self) -> str:
        return "MyClass str"

class Foo:
    # the staticmethod decorator makes the function available both
    # in instances and non-instances
    # in the docs it is described as "disables the first implicit self argument"
    @staticmethod
    def create():
        return Foo()

def _class_decorators_test() -> None:
    foo = Foo.create()
    foo.create()

# Naming convention:
# factory functions start with ip_*:
# ip_address, ip_network, ip_interface...

# --> https://docs.python.org/3/library/ipaddress.html
def _test_ipaddress() -> None:
    # we can create addresses from a generic factory function
    # note that a standalone address does not describe a network
    ip4_addr = ip.ip_address("127.0.0.1")
    ip6_addr = ip.ip_address("fe80::1")
    # there is no __bytes__ magic method, use packed instead
    print(ip4_addr.packed)

    # or directly
    ip4_specific_addr = ip.IPv4Address(1)
    print(f"Directly from ipv4 class: {ip4_specific_addr=}")

    # we can also create networks
    # note that a network does not describe specific addresses
    my_network = ip.ip_network("172.16.0.0/24")
    print(f"{my_network.with_netmask=}")
    print(f"{my_network.broadcast_address}")
    #my_network = ip.ip_network("172.16.0.17/24") # <-- fails, note that we should not declare host bits
    network_hosts = my_network.hosts()
    #for host in network_hosts:
    #    print(host)

    # an interface encapsulates both an specific address that lives inside a network
    
    #my_interface = ip.ip_interface("172.16.0.3/24")
    my_interface = ip.ip_interface(ip4_addr)
    if isinstance(ip4_addr, (bytes, int)):
        print("It is instance!")
    print(f"{my_interface=}")

# how does it get constructed internally?
# you can pass different objects to initialize the ip.Interface class
# these constructors get evaluated through calling @classmethods at the interface.__init__
# in this way we can evaluate from where we are constructor
# effectively immitating the overload rulesof c++

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
    _class_decorators_test()
    #_test_ipaddress()

if __name__ == "__main__":
    main()

