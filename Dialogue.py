from termcolor import colored
import time


def welcomeMessage():
    print("Hello, My name is Jarvis!")
    print("Please enter a command or type help.")


def printWithColor(item, color):
    print(colored(item, color))


def invalidCommand():
    printWithColor('Not a valid command, please try again!', 'red')


def selfDestruct():
    print('Jarvis will now self destruct in ...')
    printWithColor('3', 'green')
    time.sleep(1)
    printWithColor('2', 'blue')
    time.sleep(1)
    printWithColor('1', 'yellow')
    time.sleep(1)
    printWithColor('BOOM!', 'red')


def printHelpScreen(program_names):
    for name in program_names:
        print("\t", end='')
        printWithColor(name, 'yellow')


def fileResults(results):
    if results:
        print("Found these results")
        for result in results:
            printWithColor(result, 'green')
    else:
        print("No results found")

def noResultsFound(name):
    printWithColor("No results found for {}".format(name), 'red')

