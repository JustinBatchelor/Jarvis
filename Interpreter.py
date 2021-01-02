import sys
import webbrowser
import Find
import Dialogue
import Google
import subprocess
import signal
import psutil
import os

from os.path import expanduser
from subprocess import Popen



class Interpreter(object):
    program_names = ["google", "help", "open", "find", "rerun", "quit", "close"]

    def __init__(self):
        self.command = ""
        self.command_split = []
        self.lastCommand = ""
        self.lastCommandSplit = []

    def setCommand(self, passed_command):
        if self.validateCommand(passed_command):
            self.lastCommand = self.command
            self.lastCommandSplit = self.command_split
            self.command = passed_command
            self.command_split = self.command.split()
            return True
        return False

    def validateCommand(self, passed_command):
        cmd_string = str(passed_command).lower()
        cmd_split = cmd_string.split() # split up by whitespace
        if len(cmd_split) == 0:
            return False
        for command in self.program_names:
            if cmd_split[0] == command:
                return True
        return False

    def determineCommand(self):
        # self.command_split[0] is the key word to determine what jarvis should do
        cmd_key = self.command_split[0].lower()

        if cmd_key == "quit":
            Dialogue.selfDestruct()
            sys.exit()

        elif cmd_key == "help":
            Dialogue.printHelpScreen(self.program_names)

        elif cmd_key == "rerun":
            self.setCommand(self.lastCommand)
            self.determineCommand()

        elif cmd_key == "find":
            flag = self.command_split[1]
            if flag == "-f": # find a file
                print("Looking for files '{}'".format(Find.prepareName(2, self.command_split)))
                Dialogue.fileResults(Find.findFile(expanduser("~"), Find.prepareName(2, self.command_split)))
            elif flag == "-d": # find a directory
                print("Looking for files '{}'".format(Find.prepareName(2, self.command_split)))
                Dialogue.fileResults(Find.findDirectory(expanduser("~"), Find.prepareName(2, self.command_split)))
            else:
                Dialogue.printWithColor("Jarvis didn't recognize the flag for the 'find' command.", 'red')
                Dialogue.printWithColor("The syntax should look like $find -f|-d.. file_name'", 'red')
                Dialogue.printWithColor("For more information please type help", 'red')

        elif cmd_key == "open":
            try:
                subprocess.check_call(['open', Find.prepareName(1, self.command_split)])
            except RuntimeError as e:
                Dialogue.printWithColor("subprocess.check_call() ran into an error.", 'red')
                Dialogue.printWithColor(e, 'red')

        elif cmd_key == "google":
            webbrowser.open(Google.commandToURL(self.command_split))

        elif cmd_key == "close":
            name = Find.prepareName(1, self.command_split)
            display_results = []
            Dialogue.printWithColor("Searching for processes that contain {}".format(name), 'cyan')
            for process in psutil.process_iter():
                process_pid = process.pid
                process_name = process.name()
                process_status = process.status()
                if name in process_name.lower():
                    display_results.append([process_pid, process_name, process_status])

            if len(display_results) > 1:
                Dialogue.printWithColor("Jarvis found multiple results", 'cyan')
                for results in display_results:
                    Dialogue.printWithColor(
                        "PID: {}\t Name: {}\t Status: {}\t".format(results[0], results[1], results[2]), 'yellow')
                response = input("Please enter the PID you would like to close: ")
                if response.lower() == "all":
                    for results in display_results:
                        try:
                            print("Jarvis is killing PID {}".format(results[0]))
                            os.kill(results[0], signal.SIGKILL)
                        except ProcessLookupError as e:
                            print("Jarvis ran into a runtime error trying to kill {}".format(results))
                else:
                    for results in display_results:
                        if str(results[0]) == response:
                            try:
                                print("Jarvis is killing PID {}".format(results[0]))
                                os.kill(results[0], signal.SIGKILL)
                            except RuntimeError as e:
                                print("Jarvis ran into a runtime error trying to kill {}".format(results))
                            return

            elif len(display_results) == 1:
                try:
                    print("Jarvis is killing PID {}".format(display_results[0]))
                    os.kill(display_results[0][0], signal.SIGKILL)
                except RuntimeError as e:
                    print("Jarvis ran into a runtime error trying to kill {}".format(display_results[0]))
                return
            else:
                Dialogue.noResultsFound(name)


        else:
            print("Error command not found")




    def getCommand(self):
        return self.command

    def getCommandSplit(self):
        return self.command_split

    def getLastCommand(self):
        return self.lastCommand

    def getNextCommand(self):
        return input("Jarvis ~ % ")
