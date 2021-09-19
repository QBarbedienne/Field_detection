class InitialParameters():
    def __init__(self, Val=True, num_itteration=0, paramTot=[0, 0, 0, 0, 0], param_lines=0,  adaptiveThreshold_cts_1=11, adaptiveThreshold_cts_2=8, boot_treshold1=[0, 0], boot_treshold2=[0, 0], team_done=0, min_player=8, display=True, pause=False, threshold_line=5, min_line_lenght=100, max_line_gap=5, init_lines=[0, 0], line_number_init=0):
        self.Val = Val
        self.line_number_init = line_number_init
        self.num_itteration = num_itteration
        self.num_itteration_temp = num_itteration
        self.paramTot = paramTot
        self.param_lines = param_lines
        self.adaptiveThreshold_cts_1 = adaptiveThreshold_cts_1
        self.adaptiveThreshold_cts_2 = adaptiveThreshold_cts_2
        self.boot_treshold1 = boot_treshold1
        self.boot_treshold2 = boot_treshold2
        self.team_done = team_done
        self.min_player = min_player
        self.display = display
        self.pause = pause
        self.threshold_line = threshold_line
        self.min_line_lenght = min_line_lenght
        self.max_line_gap = max_line_gap
        self.init_lines = init_lines
        self.min_hist_line = 0.05
        
    def reset(self, Val=True, num_itteration=0, paramTot=[0, 0, 0, 0, 0], param_lines=0,  adaptiveThreshold_cts_1=11, adaptiveThreshold_cts_2=8, boot_treshold1=[0, 0], boot_treshold2=[0, 0], team_done=0, min_player=8, display=True, pause=False, threshold_line=5, min_line_lenght=100, max_line_gap=5, init_lines=[0, 0], line_number_init=0):
        self.Val = Val
        self.line_number_init = line_number_init
        self.num_itteration = num_itteration
        self.num_itteration_temp = num_itteration
        self.paramTot = paramTot
        self.param_lines = param_lines
        self.adaptiveThreshold_cts_1 = adaptiveThreshold_cts_1
        self.adaptiveThreshold_cts_2 = adaptiveThreshold_cts_2
        self.boot_treshold1 = boot_treshold1
        self.boot_treshold2 = boot_treshold2
        self.team_done = team_done
        self.min_player = min_player
        self.display = display
        self.pause = pause
        self.threshold_line = threshold_line
        self.min_line_lenght = min_line_lenght
        self.max_line_gap = max_line_gap
        self.init_lines = init_lines
        self.min_hist_line = 0.05
