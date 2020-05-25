from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Paris", 14.4534, -555.8906)
        assert str(exp.value) == "Invalid latitude, longitude combination"

    with pytest.raises(TypeError) as exp:
        Point(123, 14.4534, -34.8906)
    assert str(exp.value) == "City name provided must be string type"
