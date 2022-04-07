from visualisation import View as v

def restartFunction(obj):
    obj.quit()
    newobj = v.View()
    newobj.restart.config(command=lambda obj=newobj: restartFunction(obj))
    newobj.start()

view = v.View()
view.restart.config(command=lambda obj=view: restartFunction(obj))
view.start()