class element:
    def __init__(self,canvas,y,x,x2,y2,color):
        self.canvas=canvas
        self.rec=canvas.create_rectangle(x,y,x2,y2,fill=color,outline='black')