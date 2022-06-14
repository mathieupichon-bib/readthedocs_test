from uuid import uuid4

from example_package import *


def test_init():
    inpt = []
    for _ in range(5):
        inpt.append(uuid4().hex)

    elem = AClass(*inpt)

    assert list(elem.__dict__.values()) == inpt
