# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *


def bind(object_name, property_name, type):
    def getter(self):
        return type(self.findChild(QObject, object_name).property(property_name).toPyObject())

    def setter(self):
        self.findChild(QObject, object_name).setProperty(property_name, QVariant(value))

    return property(getter, setter)
