import time
from os import wait
#import scapy.all as sp
import ipaddress as ip
import threading
from threading import Thread, Lock

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

    def from_string(str: str):
        print(f"This is an string! {str}")
        return Foo()

    @classmethod
    def create_from_string(cls, str: str):
        pass

def _class_decorators_test() -> None:
    foo = Foo.create()
    foo.create()
    # note that the following will work because we are passing self as the first
    # argument, @classmethod prevents this
    a = foo.from_string()

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

# With statement, context managers
# --> https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
# --> https://docs.python.org/3/reference/datamodel.html#context-managers
def _test_context_protocol():
    pass

# A layer always has a parent
# two layers can have the same parent
# a layer can have multiple parents


# an event just consist of a flag that is either:
#    - set()
#    - clear()
#    - waite()'ed on'

# Service class representation
class Service:
    _class_count: int = 0

    # TODO: pass an action / lambda to the constructor
    def __init__(self, parent = None, name: str | None = None) -> None:
        self.parent = parent
        self.name = Service._generate_name()
        #self.action = _ServiceAction(self, action)
        self.done_event = threading.Event()

    @staticmethod
    def _generate_name() -> str:
        Service._class_count += 1
        return "Service" + str(Service._class_count)

    def _service_run(self) -> None:
        raise NotImplementedError

    def run(self) -> None:
        # this waits for the parent's action to be done, 
        # and potentially triggers the next Service's action
        with self:
            print(f"Running Service {self.name}")
            time.sleep(3)

    # context manager protocol
    def __enter__(self):
        # wait for parent service to finish running
        if self.parent and self.parent.done_event:
            print("Waiting for parent layer to finish...")
            self.parent.done_event.wait()
            print(f"Starting f{self.name}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # set this layer to finish
        print(f"Ending f{self.name}")
        self.done_event.set()

class _ServiceAction:
    def __init__(self, parent_service: Service, action) -> None:
        self.parent_service = parent_service

    def __enter__(self):
        if self.parent_service and self.parent_service.done_event:
            print("Waiting for parent layer to finish...")
            self.parent_service.done_event.wait()
            print(f"Starting f{self.parent_service.name}")

def _service_test():
    s1 = Service(name="First_service")
    s2 = Service(parent=s1, name="Second_service")

    services = [s1, s2]

    for s in services:
        s.run()

def main():
    #_class_decorators_test()
    ##_test_ipaddress()
    #ns = NetStack()
    #ns2 = NetStack()
    #arp = ArpService()
    #ns.add(arp())
    #ns.add(ACService())
    #ns.run()

    #ns.add(arp)
    #ns.run()

    ## Inside NetStack
    #self.parent = parent
    #self.done_event = not done
    #self.
    _service_test()

if __name__ == "__main__":
    main()

