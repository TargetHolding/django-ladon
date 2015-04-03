from ladon.ladonizer import ladonize


class Calculator(object):

    @ladonize(int,int,rtype=int)
    def add(self,a,b):
        return a+b
