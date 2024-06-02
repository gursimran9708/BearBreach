import shutil

columns = shutil.get_terminal_size().columns



class color:
    RESET = "\033[0m"
    
    
    def black(text):
        return "\033[30m" + str(text) + color.RESET
    def red(text):
        return "\033[31m" + str(text) + color.RESET
    def green(text):
        return "\033[32m" + str(text) + color.RESET
    def yellow(text):
        return "\033[33m" + str(text) + color.RESET
    def blue(text):
        return "\033[34m" + str(text) + color.RESET
    def magenta(text):
        return "\033[35m" + str(text) + color.RESET
    def cyan(text):
        return "\033[36m" + str(text) + color.RESET
    def white(text):
        return "\033[37m" + str(text) + color.RESET
    def bright_black(text):
        return "\033[90m" + str(text) + color.RESET
    def bright_red(text):
        return "\033[91m" + str(text) + color.RESET
    def bright_green(text):
        return "\033[92m" + str(text) + color.RESET 
    def bright_yellow(text):
        return "\033[93m" + str(text) + color.RESET
    def bright_blue(text):
        return "\033[94m" + str(text) + color.RESET
    def bright_magenta(text):
        return "\033[95m" + str(text) + color.RESET
    def bright_cyan(text):
        return "\033[96m" + str(text) + color.RESET
    def bright_white(text):
        return "\033[97m" + str(text) + color.RESET
"""
# Example usage
print(color.red("This is red text"))
print(color.green("This is green text"))
print(color.yellow("This is yellow text"))
print(color.bright_blue("This is Brigh Cyan"))
"""
print()


