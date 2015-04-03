from __future__ import absolute_import # only needed for python 2.7
from ladon.ladonizer import ladonize


class Calculator(object):

    @ladonize(int,int,rtype=int)
    def add(self,a,b):
        return a+b
