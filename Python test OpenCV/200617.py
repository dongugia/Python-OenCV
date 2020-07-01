import tkinter
from tkinter.constants import *

top = tkinter.Tk(className='Test')
frame = tkinter.Frame(top)
frame.pack(fill = BOTH,expand = 1)
label = tkinter.Label(frame,text= 'Hello World')
label.pack(fill = X, expand= 1)
button = tkinter.Button(frame,text = 'Exit',command = top.destroy)
button.pack(side = BOTTOM)
message= tkinter.Message(text='Hello World')
top.mainloop()

import numpy as np
n=np.percentile([1,2,3,4],50)
print(n)