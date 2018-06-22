import re
from tkinter import *
root = Tk()
root.title('格式调整')
root.geometry('500x400+500+150')
t = Text()
t.pack(ipadx='200', ipady='24', padx='5', pady='1')
def sort():
    data = t.get('1.0', END)
    obj = data.split('\n')
    result = obj[0]
    for i in range(1, len(obj)):
        result += '\n' + ','.join(re.findall(r'(\w+)', obj[i]))
    t.delete('1.0', END)
    t.insert('1.0', result)
Button(root, text='press', command=sort).pack(fill=X, side=BOTTOM)
root.mainloop()
