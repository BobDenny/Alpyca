import pytest
import os
import sys
import platform
import ast
import xml.etree.ElementTree as ET

@pytest.fixture(scope="module")
def device(request):
    global d
    n = getattr(request.module, "dev_name")
    print(f'Setup: for {n}')
    c = getattr(sys.modules[f"alpaca.{n.lower()}"], n)  # Creates a device class by string name :-)
    d =  c('localhost:32323', 0)                        # Created an instance of the class
    d.Connected = True
    print(f"Setup: Connected to OmniSim {n} OK")
    return d
#
# Grabs the settings for the device from the OmniSim settings data *once*.
#
@pytest.fixture(scope="module")
def settings(request):
    n = getattr(request.module, "dev_name")
    if platform.system() == "Windows":
        data_file = f"{os.getenv('USERPROFILE')}/.ASCOM/Alpaca/ASCOM-Alpaca-Simulator/{n}/v1/Instance-0.xml"
    else:                       # TODO No MacOS
        if n != "Camera":       # Daniel will fix this (10-Apr_2022)
            n = n.lower()
        data_file = f"{os.getenv('HOME')}/.config/ascom/alpaca/ascom-alpaca-simulator/{n}/v1/instance-0.xml"
    tree = ET.parse(data_file)
    root = tree.getroot()
    s = {}
    for i in root.iter("SettingsPair"):
        k = i.find('Key').text
        v = i.find('Value').text
        try:
            s[k] = ast.literal_eval(v)
        except:
            s[k] = v
    print(f"Setup: {n} OminSim Settings retrieved")
    return s

@pytest.fixture(scope="module")
def disconn(request):
    global d
    yield
    d.Connected = False
    n = getattr(request.module, "dev_name")
    print(f"Teardown: {n} Disconnected")

#
# Common function to get settings for @pytest.mark.skipif() decorators
#
def get_settings(device: str):
    if platform.system() == "Windows":
        data_file = f"{os.getenv('USERPROFILE')}/.ASCOM/Alpaca/ASCOM-Alpaca-Simulator/{device}/v1/Instance-0.xml"
    else:                       # TODO No MacOS
        if device != "Camera":       # Daniel will fix this (10-Apr_2022)
            device = device.lower()
        data_file = f"{os.getenv('HOME')}/.config/ascom/alpaca/ascom-alpaca-simulator/{device}/v1/instance-0.xml"
    tree = ET.parse(data_file)
    root = tree.getroot()
    s = {}
    for i in root.iter("SettingsPair"):
        k = i.find('Key').text
        v = i.find('Value').text
        try:
            s[k] = ast.literal_eval(v)
        except:
            s[k] = v
    return s
