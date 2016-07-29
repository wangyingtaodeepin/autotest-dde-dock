#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dogtail.tree import *
from Xlib.display import Display
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import dbus
from time import sleep

from lib.properties import dock

appname = "dde-dock"
appdescription = "/usr/bin/dde-dock"

k = PyKeyboard()
m = PyMouse()

resolution = Display().screen().root.get_geometry()

def getDdeDockObject(name = appname, description = appdescription):
    return root.application(name, description)

def getDdeDockSession():
    session_bus = dbus.SessionBus()
    session_obj = session_bus.get_object('com.deepin.dde.daemon.Dock',
                                         '/com/deepin/dde/daemon/Dock')
    return session_obj

def getDdeDockPropertiesInterface():
    session_dock = getDdeDockSession()
    interface = dbus.Interface(session_dock, 
                               dbus_interface=dbus.PROPERTIES_IFACE)
    return interface

def getDdeDockInterface():
    session_dock = getDdeDockSession()
    interface = dbus.Interface(session_dock, 
                               dbus_interface='com.deepin.dde.daemon.Dock')

    return interface

def getDdeDockDisplayMode():
    properties_iface = getDdeDockPropertiesInterface()
    return properties_iface.Get('com.deepin.dde.daemon.Dock', "DisplayMode")
    
def setDdeDockDisplayMode(mode):
    properties_iface = getDdeDockPropertiesInterface()
    properties_iface.Set('com.deepin.dde.daemon.Dock', "DisplayMode", mode)
    sleep(2)

def openFashionMode():
    setDdeDockDisplayMode(dock.fashionmode)

def openEfficientMode():
    setDdeDockDisplayMode(dock.efficientmode)

