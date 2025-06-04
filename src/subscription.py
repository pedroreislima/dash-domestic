import random as rnd
import datetime
import calendar
import decimal
from decimal import Decimal, getcontext
getcontext().prec = 2
from utils import get_weekdays

class Subscription():
    '''

    
    Attributes:

    '''    
    def __init__(self, id:str, possible_values:list[Decimal], dist_values:list[float], dist_week:str = 'constant'):
        self.id = id
        self.possible_values = possible_values
        self.dist_values = dist_values
        self.day_distributions = {
        'wknd': [0.1,0.1,0.1,0.1,0.1,0.25,0.25],
        'quinta': [0,0,0,1,0,0,0],
        'constant': [1/7 for x in range(7)],
        'monthly': []
    }
        self.dist_week = self.day_distributions[dist_week]
        
    def generate_expense_test(self, year, month):
        '''
        Generate monthly expense from subscription.
        
        Return:
            dict row with Id,Value and Date.
        '''
        
        return [self.id, entry_value, entry_date]
    