#pylint: disable=missing-final-newline,missing-module-docstring,import-error,c0325,c0303,c0301,c0115,c0116,w1401,c0413,w0622,r1705,r1716,w0622,w0611,c0411
from enum import Enum
from fastapi import FastAPI
import re
import sys

sys.path.insert(0,"..")
import circle

app= FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Circle"}

@app.get("/area/{radius}")
async def calculate_radius(radius:float):
    try:
        return {"area": circle.Circle(float(radius)).area()}
    except ValueError:
        return {"error": "Radius must be greater than zero"}

@app.get("/circumference/{radius}")
async def calculate_circumference(radius:float):
    try:
        return {"circumference": circle.Circle(float(radius)).perimeter()}
    except ValueError:
        return {"error":"Radius must be greater than zero"}

def read_generalrange(input:str,name:str,func):
    match = re.match('(\d\d*)-(\d\d*)', input)
    if match:
        lower = int(match.group(1))
        higher = int(match.group(2))
        if higher > lower and lower > 0:
            results = []
            for i in range(int(lower),int(higher+1)):
                temp = round(func(i),2)
                results.append(temp)
            return {"results": f"{name} of circles of radius {lower} to {higher} are {results}"}
        elif higher < lower and higher > 0:
            higher, lower = lower, higher
            inverse = []
            for i in range(int(lower),int(higher+1)):
                temp = round(func(i),2)
                inverse.append(temp)
            return {"results": f"{name} of circles of radius {lower} to {higher} are {inverse}"}
    return {"error": "no range specified"}

@app.get("/arearange/{input}")
async def read_arearange(input: str):
    def area(i:int):
        return circle.Circle(i).area()
    return read_generalrange(input, "Area", area)

@app.get("/circumferencerange/{input}")
async def read_circumferencerange(input: str):
    def perimeter(i:int):
        return circle.Circle(i).perimeter()
    return read_generalrange(input, "Circumference", perimeter)
