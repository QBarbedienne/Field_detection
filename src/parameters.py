class InitialParameters():
    def __init__(self, num_itteration=0, paramTot=[0, 0, 0, 0, 0]):
        self.num_itteration = num_itteration
        self.paramTot = paramTot
        self.min_hist_line = 0.05
        
    def reset(self, num_itteration=0, paramTot=[0, 0, 0, 0, 0]):
        self.num_itteration = num_itteration
        self.paramTot = paramTot
        self.min_hist_line = 0.05
