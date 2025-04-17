import scapy.all as sp
import ipaddress as ip

class MyClass:
    def __init__(self) -> None:
        pass
    
    def __repr__(self) -> str:
        return "This is MyClass repr!"

    def __str__(self) -> str:
        return "MyClass str"

# --> https://docs.python.org/3/library/ipaddress.html
def _test_ipaddress() -> None:
    pass

def main():
    a = 32
    my_class = MyClass()
    # '=' are used to also print the variable name
    print(f"Printing normal built-in type {a=}")
    # This should call the type's repr
    print(f"Printing my class repr {my_class=!r}")
    print(f"Printing my class repr {my_class=!s}")

    ip_addr = ip.ip_address("xe80::1")

if __name__ == "__main__":
    main()

