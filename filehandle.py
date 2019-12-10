
class File(): 
    def __init__(self):
        self.s_times = []   
        self.time_w = False 
        
    def create_file(self): 
        self.filehandler = open(".timefile.csv","a") 
        self.filehandler.close() 
        self.filehandler = open(".timefile.csv", "r")  
        for lines in self.filehandler: 
            self.s_times = list(lines.strip().split(',') )   
        self.filehandler.close() 
        
    def to_file(self):    
        self.filehandler = open(".timefile.csv", "w")
        self.filehandler.write(",".join(self.s_times)) 
        self.filehandler.close()    
        
        
