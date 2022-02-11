#pylint: disable=missing-final-newline,missing-module-docstring,import-error,c0325,c0303,c0301,c0115,c0116,w1401,c0413,w0622,r1705,r1716,w0622,w0611,c0411,e1120,r1710,r0903,c0103,e0402,w0612
import sys
sys.path.insert(0,"..")
import circle

def test_circle_with_radius_1_2dp():
    myC = circle.Circle(1)
    assert round(myC.area(),2) == 3.14
    assert round(myC.perimeter(),2) == 6.28
