from tabulate import tabulate
from color import color
def display_my_info():
    name = "Gursimran Singh"
    github_url = "https://github.com/gursimran9708"
    linkedin_url = "https://www.linkedin.com/in/gursimransw"
    email = "gursimransinghwadhawan@gmail.com"

    # ASCII art for the tool name "BearBreach"
    name_header = """
██████  ███████  █████  ██████  ██████  ██████  ███████  █████   ██████ ██   ██ 
██   ██ ██      ██   ██ ██   ██ ██   ██ ██   ██ ██      ██   ██ ██      ██   ██ 
██████  █████   ███████ ██████  ██████  ██████  █████   ███████ ██      ███████ 
██   ██ ██      ██   ██ ██   ██ ██   ██ ██   ██ ██      ██   ██ ██      ██   ██ 
██████  ███████ ██   ██ ██   ██ ██████  ██   ██ ███████ ██   ██  ██████ ██   ██ 
-------------------------------------------------------------------------------- 
    """



    # Create a table with contributor information
    table = [
        ["Name", name],
        ["GitHub URL", github_url],
        ["LinkedIn URL", linkedin_url],
        ["Email", email]
    ]

    # Display the tool name and contributor information
    print(color.blue(name_header))
    print(color.bright_yellow(tabulate(table, tablefmt="plain")))

# Call the function to display the information
#display_my_info()

