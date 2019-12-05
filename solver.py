
class Solver:
    
    def __init__(self):
        self.solve_stack = [] 
        self.to_solve = False 
    
    def solver(self,ms):
            if len(ms) == 1: 
                for m in ms:
                    self.solve_stack.insert(0,str(m)+"'")  
                
            elif len(ms) == 2:
                if ms[1] == '2': 
                    for i in range(int(ms[1])): 
                        self.solve_stack.insert(0,str(ms[0])+"'") 
                elif ms[1] == "'":
                    self.solve_stack.insert(0,ms[0]) 
                
            elif len(ms) == 3:
                for i in range(int(ms[2])):
                    self.solve_stack.insert(0,str(ms[0]))  
            
                    
            
        
