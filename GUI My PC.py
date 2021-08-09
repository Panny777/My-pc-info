import platform
import psutil
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter.ttk import Combobox

OS = platform.system()
REl = platform.release()
ED = platform.win32_edition()
VER = platform.version()

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


    
root= tk.Tk()
root.geometry('490x350')
root.title("My PC")

l = Label(root, text="My PC", font=('verdana', 9, 'bold'), bg="white", fg="Blue")
l.place(x=10, y=9)

# Display Operating System
l1 = Label(root, text="Operating Sytem_____________________________________",
 font=('Sans',12, 'italic'))
l1.place(x=10, y=30)

l2 = Label(root, text=OS + "  " + REl + "  " + ED + "  " + VER, font=('verdana', 8 ))
l2.place(x=17, y= 55)


# Displaying System Type, Architecture and Processor 
l3 = Label(root, text="System____________________________________________",
 font=('Sans', 12, 'italic'))
l3.place(x=10, y=100)

# Processor
l4 = Label(root, text="Processor:              " + platform.processor(), font=('verdana',9))
l4.place(x=17, y=130)

# Architecture
l5 = Label(root, text=platform.architecture(), font=('verdana',8))
l5.place(x=17, y=75)

# Machine
l6 = Label(root, text="Machine Type:        " + platform.machine(), font=('verdana',9))
l6.place(x=17, y=150)

# Node name
l7 = Label(root, text="Node name:    " + platform.node(), font=('verdana',9))
l7.place(x=17, y=170)

# RAM

svmem =psutil.virtual_memory()
l8 = Label(root, text=f"Installed Memory(RAM):         {get_size(svmem.total)} Usable", font=('verdana', 9))
l8.place(x= 17 , y=190)

# Disk Information
l9 =Label(root, text="Disk Information", font=('verdana', 9, 'italic'))
l9.place(x=10, y=210)

partitions = psutil.disk_partitions()
for partition in partitions:
    l10 = Label(root, text=f" Disk  {partition.device}", font=('verdana', 9))
    l10.place(x=17, y=230)

    l10 = Label(root, text=f" Disk  {partition.mountpoint}", font=('verdana', 9))
    l10.place(x=17, y=250)
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    l11 = Label(root, text=f"  Total Size: {get_size(partition_usage.total)}", font=('verdana', 9))
    l11.place(x=17, y=270)
    
    l12 = Label(root, text=f"  Used Size: {get_size(partition_usage.used)}", font=('verdana', 9))
    l12.place(x=17, y=290)

    l13 = Label(root, text=f"  Free Size: {get_size(partition_usage.free)}", font=('verdana', 9))
    l13.place(x=17, y=310)

disk_io = psutil.disk_io_counters()
l14 = Label(root, text=f"Total read: {get_size(disk_io.read_bytes)}", font=('verdana', 9))
l14.place(x=17, y=330)

l15 = Label(root, text=f"Total write: {get_size(disk_io.write_bytes)}", font=('verdana', 9))
l15.place(x=17, y=350)


root.mainloop()