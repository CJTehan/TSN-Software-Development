class InfusionPump:
    def __init__(self):
        self.is_running = False
        self.current_dosage = 0  # in ml/hr
        self.max_dosage = 100  # in ml/hr
    def start_infusion(self, dosage):
        '''
        Starts the infusion pump with the specified dosage.
        '''
        if dosage > self.max_dosage:
            raise ValueError('Dosage exceeds maximum limit.')
        self.current_dosage = dosage
        self.is_running = True
    def stop_infusion(self):
        '''
        Stops the infusion pump.
        '''
        self.current_dosage = 0
        self.is_running = False
    def set_dosage(self, dosage):
        '''
        Sets the dosage of the infusion pump.
        '''
        if dosage > self.max_dosage:
            raise ValueError('Dosage exceeds maximum limit.')
        if self.is_running:
            self.current_dosage = dosage
        else:
            raise Exception('Cannot set dosage while pump is not running.')
    def get_status(self):
        '''
        Returns the current status of the infusion pump.
        '''
        if self.is_running:
            return f'Pump is running at {self.current_dosage} ml/hr.'
        else:
            return 'Pump is stopped.'