import random as rnd
import datetime
import calendar
import decimal
from decimal import Decimal, getcontext
getcontext().prec = 2

class Expense():
    '''
    Represents a possible expense for an ID and some possible values to be determined by some probability distribution.
    
    Attributes:
        id: name that represents the expense
        possible_values: possible "bundle" value of the type of expense.
        dist_value: probability of each bundle to be consumed.
        dis_week: distribution of the possible consumption throughout the week
    '''
    
    
    def __init__(self, id:str, value:Decimal, start_date, end_date):
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
        Generate expense row for id in certain date, with value based on given distribution.
        
        Return:
            dict row with Id,Value and Date.
        '''
        entry_value = rnd.choices(self.possible_values, weights = self.dist_values)[0]
        if len(self.dist_week) == 7:
            # weekly distribution
            week_day = rnd.choices([x for x in range(7)], weights = self.dist_week)[0]
            entry_possibilities = get_weekdays(year, month, week_day)
            entry_date = rnd.choice(entry_possibilities)
        else:
            # month distribution
            entry_day = rnd.choice([x+1 for x in range(calendar.monthrange(year,month)[-1])])
            entry_date = datetime.date(year,month,entry_day)
        
        return [self.id, entry_value, entry_date]
    