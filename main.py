import Dialogue

from Interpreter import Interpreter









# This will be the main program loop for Jarvis

"""

"""
if __name__ == '__main__':
    Dialogue.welcomeMessage()
    obj = Interpreter()
    while True:
        if obj.setCommand(obj.getNextCommand()):
            obj.determineCommand()
        else:
            Dialogue.invalidCommand()