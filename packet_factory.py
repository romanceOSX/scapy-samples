from _typeshed import Self
from dataclasses import dataclass, field
import scapy.all as sp

@dataclass
class Node:
    "Class that represents a node participating a Network"
    hostname: str           = ""
    ip_addr: list[str]      = field(default_factory=list)
    ip6_addr: list[str]     = field(default_factory=list)
    mac: str                = "00:00:00:00:00:00"

class Layer:
    "Layer interface that defines methods for populating layer's fields on-demand"

    name: str = "Base Layer"

    def __init__(self, parent: Self) -> None:
        self.parent: Self | None = None

    def set_parent(self, parent: Self):
        self.parent = parent

    def calculate_parent_fields(self):
        raise Exception("Not implemented!")

class PacketBuilder:
    def __init__(self, node: Node) -> None:
        self.node: Node             = node
        self._layers: list[Layer]   = []

    def add_layer(self, layer: Layer):
        layer.set_parent(self)
        self._layers.append(layer)

    def build(self) -> sp.Packet:
        for l in self._layers:
            l.calculate_parent_fields()

def build_acf_over_ip4(acf: bytes):
    return b'213123'

def test_interface() -> None:
    acf = bytes.fromhex('223242afe')
    p = build_acf_over_ip4(acf)
    pass

def test_packet_crafter() -> None:
    ip4_acf_packet = PacketBuilder(host).add_layer(IPv4(dst=""))
    pass

def test_dataclasses() -> None:
    n = Node()
    print(n)

def main() -> None:
    test_dataclasses()

if __name__ == "__main__":
    main()

