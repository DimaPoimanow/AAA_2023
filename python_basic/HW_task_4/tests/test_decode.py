import pytest

from morse import decode


@pytest.mark.parametrize(
    "msg,decoded_msg",
    [
        ("... --- ...", "SOS"),
        ("", ""),
        ("..--- ----- ..--- ...--", "2023"),
        ("-- .- -- .- .--. .- .--. .- -.-- .- -.-- .-", "MAMAPAPAYAYA"),
    ],
)
def test_decode(msg, decoded_msg):
    assert decode(msg) == decoded_msg
