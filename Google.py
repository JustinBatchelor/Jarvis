def commandToURL(command_split):
    search_url = "https://www.google.com/search?q="
    for index in range(1, len(command_split)):
        search_url += command_split[index]
        search_url += "+"
    return search_url[:-1]