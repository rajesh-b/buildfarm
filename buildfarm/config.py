#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2009 TUBITAK/UEKAE
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Please read the COPYING file.

import ConfigParser

class Config(object):
    """Configuration class for /etc/buildfarm/buildfarm.conf."""
    def __init__(self, conf_file="/etc/buildfarm/buildfarm.conf"):
        self.__items = dict()

        self.configuration = ConfigParser.ConfigParser()
        self.configuration.read(conf_file)
        self.read()

    def read(self):
        for s in self.configuration.sections():
            # FIXME: Handle multiple values separated with ,
            self.__items.update(dict(self.configuration.items(s)))

    def __getattr__(self, attr):
        return self.__items.get(attr, None)
