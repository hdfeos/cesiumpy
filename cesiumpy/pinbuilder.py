#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

import six

import cesiumpy
from cesiumpy.base import _CesiumObject
import cesiumpy.common as com



class PinBuilder(_CesiumObject):

    def __init__(self, color=None, size=48, text=None):

        if color is None:
            # default color, all attrs are mandatory
            color = cesiumpy.color.ROYALBLUE

        self.color = cesiumpy.color.validate_color_or_none(color, key='color')
        self.size = com.validate_numeric(size, key='size')

        # validated in .fromText
        self.text = text

    @classmethod
    def fromColor(self, color, size=48):
        return PinBuilder(color=color, size=size)

    @classmethod
    def fromText(self, text, color=None, size=48):
        text = com.validate_str(text, key='text')
        return PinBuilder(color=color, size=size, text=text)

    @property
    def script(self):
        # ToDo: make global variable?
        if self.text is None:
            rep = """new Cesium.PinBuilder().fromColor({color}, {size})"""
            return rep.format(color=self.color, size=self.size)
        else:
            rep = """new Cesium.PinBuilder().fromText("{text}", {color}, {size})"""
            return rep.format(text=self.text, color=self.color, size=self.size)



