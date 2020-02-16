import webbrowser
f = open('helloworld.html','w')
Y = "DD"
message = """<html>
<head></head>
<body><p>"""+Y+"""</p></body>
</html>"""

f.write(message)
f.close()
filename = '/home/yasser_dx/Desktop/Python/helloworld.html'
webbrowser.open_new_tab(filename)