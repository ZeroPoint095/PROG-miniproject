import tkinter as tk
frameList=[]
activeFrames=[]

#function which is responsible for the ability to scroll through your frames
def scroll(*value):
    global activeFrames
    global frameList
    #removes the current frames from the mainframe (mFrame)
    for i in activeFrames:
        frameList[i][0].grid_forget()


    try:
        # if there is a value (assigned by pressing on of the two Buttons it will set perc))
        if (value[0]==-1 and activeFrames[0]>0) or (value[0]==1 and activeFrames[9]<len(frameList)-1):
            #raises or lowers the grid by one unit if it is not already at the border
            perc=activeFrames[0] + value[0]

            #I would like to set mScale to fit to the activeFrames, but this gets problematic
            #if you have 10000 frames because every time you click up or down it will run the code
            #than set it to the according percentage, but because it can't  handle floats it will
            #round it and thus run this script again with a new percentage.
            #thus you wouldn't be enabled to read some part of the code.


        else:
            #uses mScale.get() as percentage and calculates the starting frame with it
            perc=int((len(frameList)-10)*(mScale.get()/100))
    except:
        #see above
        perc=int((len(frameList)-10)*(mScale.get()/100))

    #resets activeFrames for another use
    activeFrames=[]

    #grids the new active frames and set them
    for i in range(perc,perc+10):
        frameList[i][0].grid()
        activeFrames.append(i)


mGui=tk.Tk()
mFrame=tk.Frame(mGui)

ScaleUp=tk.Button(mGui,text="UP",command=lambda  : scroll(-1))
mScale=tk.Scale(mGui,command =lambda event : scroll())
ScaleDown=tk.Button(mGui,text="Down",command= lambda : scroll(1))

mFrame.grid(row=0,column=1,rowspan=3)
ScaleUp.grid(row=0,column=0)
mScale.grid(row=1,column=0)
ScaleDown.grid(row=2,column=0)

#creates every frame
for i in range (1000):
    partList=[]
    partList.append(tk.Frame(mFrame))
    partList.append(tk.Button(partList[0],text=i))
    partList[1].pack()
    frameList.append(partList)


mGui.mainloop()
