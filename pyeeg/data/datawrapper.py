



class DataWrapper(object):
    """
    Base class to provide interface to timeseries data.  
    """
    def getDataMS(self,channels,eventOffsets,DurationMS,OffsetMS,BufferMS,resampledRate=None,filtFreq=None,filtType='stop',filtOrder=4,keepBuffer=False):
        raise NotImplementedError