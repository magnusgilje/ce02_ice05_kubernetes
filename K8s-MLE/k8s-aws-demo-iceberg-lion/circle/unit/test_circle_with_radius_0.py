#pylint: disable=missing-final-newline,missing-module-docstring,import-error,c0325,c0303,c0301,c0115,c0116,w1401,c0413,w0622,r1705,r1716,w0622,w0611,c0411,e1120,r1710,r0903,c0103,e0402,w0612
import sys
import pytest
sys.path.insert(0,"..")
import circle


def test_circle_with_radius_0_2dp():
    with pytest.raises(Exception) as error_info:
        myC = circle.Circle(0)
