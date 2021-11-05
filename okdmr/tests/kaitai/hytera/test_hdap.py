from typing import List

from okdmr.kaitai.hytera.hytera_dmr_application_protocol import (
    HyteraDmrApplicationProtocol,
)
from okdmr.tests.kaitai.tests_utils import prettyprint


def test_hdap():
    hexmessages: List[str] = [
        "11000300040a2338636303",
        "11008000090a2338630000000708d203",
        # this is immediate location with RSSI, currently unsupported PDU
        #"08a0030034000000000a2338630000413131323534303237303932314e353030332e383734364530313432362e35313932302e32323533ff1cae03",
    ]
    for rrs in hexmessages:
        prettyprint(HyteraDmrApplicationProtocol.from_bytes(bytes.fromhex(rrs)))


if __name__ == "__main__":
    test_hdap()