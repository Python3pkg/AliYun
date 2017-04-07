#! /usr/bin/env python
# coding: utf-8

import os
import ConfigParser

__author__ = 'ZhouHeng'


class RAMAccount(object):
    """
    配置文件格式
    [Account]
    access_key_id: LTAI***3vAqE****
    access_key_secret: 25QTaQVEQPx***jJolgKuspzPk7***
    internal: false  #  是否为阿里内网
    """

    def __init__(self, conf_path=None, conf_dir=None, conf_name=None, section="Account"):
        if conf_path is None:
            assert conf_dir is not None and conf_name is not None
            self.conf_path = os.path.join(conf_dir, conf_name)
        else:
            self.conf_path = conf_path
        config = ConfigParser.ConfigParser()
        config.read(self.conf_path)
        self.access_key_id = config.get(section, "access_key_id")
        self.access_key_secret = config.get(section, "access_key_secret")
        if config.has_option(section, "internal") is True:
            self.is_internal = config.getboolean(section, "internal")
        else:
            self.is_internal = False

    def assign_access_key(self, obj):
        if hasattr(obj, "access_key_id"):
            obj.access_key_id = self.access_key_id
        if hasattr(obj, "access_key_secret"):
            obj.access_key_secret = self.access_key_secret
