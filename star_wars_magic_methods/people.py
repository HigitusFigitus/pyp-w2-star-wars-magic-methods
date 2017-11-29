class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self._dark_side = dark_side
    
    @property
    def dark_side(self):
        return self._dark_side
    
    @dark_side.setter
    def dark_side(self, ds_value):
        self._dark_side = ds_value
     
    @property
    def light_side(self):
        return not self.dark_side
    
    @light_side.setter
    def light_side(self, value):
        self._light_side = not value


        
        # def call():
        #     return 'Help me ' + self.name + ', you\'re my only hope.'
    
    
        def __str__():
            return self.name
        
        
            
        
        