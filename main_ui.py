from tkinter import Button,Label,Entry,Tk
from stegano import lsb
class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder=None):
        super().__init__(master)

        if placeholder is not None:
            self.placeholder = placeholder
            self.placeholder_color = 'grey'
            self.default_fg_color = self['fg']

            self.bind("<FocusIn>", self.focus_in)
            self.bind("<FocusOut>", self.focus_out)

            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def focus_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def focus_out(self, *args):
        if not self.get():
            self.put_placeholder()

def create():
    print("Created")
    to_create = lsb.hide(path_png.get(), text_to_png.get())
    to_create.save("./new_png_with_text.png")
def read():
    png_to_text['text'] = lsb.reveal(path_png.get())
    print("Read")
root = Tk()

#text to png
text_to_png = EntryWithPlaceholder(root, 'Text to insert in png')
text_to_png.grid(row=1,column=0)

path_png = EntryWithPlaceholder(root, 'Path to png')
path_png.grid(row=2,column=0)

create_button = Button(text='Create',command=create)
create_button.grid(row=1,column=1)
#png to text
png_to_text = Label(text='Text from png')
png_to_text.grid(row=0,column=1)
read_button = Button(text=' Read ',command=read)
read_button.grid(row=2,column=1)
root.mainloop()