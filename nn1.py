#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import hashlib
m = hashlib.md5("C:\Users\pandu\Downloads\రోజు.doc".decode('utf-8'))
# m = hashlib.md5("hi")
print m.hexdigest()
# print sys.stdout.encoding
