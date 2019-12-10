
class File(): 
    def __init__(self):
        self.s_times = ['0']
        self.time_w = False 
        
    def create_file(self):
        self.filehandler = open("timefile.csv","a")
        self.filehandler.close()
        self.filehandler = open("timefile.csv", "w+") 
    
    def from_file():
        self.s_times = filehandler.readline().strip().split(',') 
    
    def to_file(self):
        self.filehandler.write(",".join(self.s_times)) 
        print("written to file")  
        self.filehandler.close() 
        
        
