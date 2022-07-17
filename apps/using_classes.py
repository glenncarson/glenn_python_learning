# https://towardsdatascience.com/enhance-your-python-project-code-with-classes-5a19d0e9f841#:~:text=A%20Python%20class%20is%20like,object%20is%20initiated%20from%20scratch.

from socketserver import DatagramRequestHandler
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MinMaxScaler

class CreateProfile: 
    def __init__(self, # called when class is  intantiated
                dataset=None,
                profile=None):
        self.dataset = dataset #this is called a 'class attribute'
        self.profile = profile #can be called after instantiating



new_profile = CreateProfile()
# instantiate the class

# calling the class attribute
new_profile.dataset

# ^^ above would create empty profile that is instantiated


# create individual functions to put into class




