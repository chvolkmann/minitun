import pytest

import minitun


class TestPortSpecParsing:
    def test_accepts_one_arg(self) -> None:
        spec = minitun.PortSpec.parse("1234")
        assert spec.to_tuple() == ("localhost", 1234, "localhost", 1234)
        assert spec.to_ssh_arg() == "1234:localhost:1234"

    def test_accepts_two_args(self) -> None:
        spec = minitun.PortSpec.parse("1234:2345")
        assert spec.to_tuple() == ("localhost", 1234, "localhost", 2345)
        assert spec.to_ssh_arg() == "1234:localhost:2345"

    def test_accepts_three_args(self) -> None:
        spec = minitun.PortSpec.parse("1234:1.2.3.4:2345")
        assert spec.to_tuple() == ("localhost", 1234, "1.2.3.4", 2345)
        assert spec.to_ssh_arg() == "1234:1.2.3.4:2345"

    def test_accepts_four_args(self) -> None:
        spec = minitun.PortSpec.parse("1.1.1.1:1234:2.2.2.2:2345")
        assert spec.to_tuple() == (
            "1.1.1.1",
            1234,
            "2.2.2.2",
            2345,
        )

    def test_rejects_otherwise(self) -> None:
        with pytest.raises(ValueError):
            minitun.PortSpec.parse("1:2:3:4:5")

        with pytest.raises(ValueError):
            minitun.PortSpec.parse("")
