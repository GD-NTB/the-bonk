def abacaba(n):
    output = ""
    for i in range(n):
        output = "{0}{1}{2}".format(output, chr(65+i).lower(), output)
    return output