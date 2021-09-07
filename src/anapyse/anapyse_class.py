'''
Created on 7 Sep 2021

@author: oqb
'''
from asn1crypto.tsp import MetaData
from comtypes.tools.typedesc_base import Constructor
from curses.has_key import system
from scipy.ndimage import measurements
from sqlalchemy.sql.expression import case

class Measurement_Campaign(object):
    '''
    A class to hold the measurement campaign information.
    
    Will include an ID Object that contains ID data (length, period length, etc)
    Will include an array of one or more Measurement System Objects that describes the state of the measurement system (e.g. Hall Probe calibrations etc)
    Will include an array of one or more Background Measurement Objects (possibly as a simple array)
    Will include an array of one or more Measurement and Analysis Objects (Class will contain metadata of measurement state (gap, shift, comments etc))
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
        
class Undulator_Data(object):
    ''' 
    A class to hold Undulator MetaData
    '''
    def __init__(self,params):
        '''
        Constructor
        '''
        
class Measurement_System(object):
    '''
        A class that holds data about the measurement system
    '''
    
    def __init__(self,params):
        '''
        Constructor
        '''
        
class Background_Measurement(object):
    '''
        A class that holds information about Background measurements
    '''
    
    def __init__(self,params):
        '''
        Constructor
        '''
        
class Measanalyse(object):
    '''
    A class that holds all the measurement and processed data for a single measurement case
    '''
    
    def __init__(self,params):
        '''
        Constructor
        '''