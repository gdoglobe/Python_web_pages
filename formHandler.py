#coding:utf-8
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()


print ("Content-Type: text/html; charset=utf-8\n\n")
 
html = """ 
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<h1>Message : </h1>
"""
print(html)

try:
    if (form.getvalue("userNameInput") and form.getvalue("messageText")):
        username = form.getvalue("userNameInput")
        message = form.getvalue("messageText")
        email = form.getvalue("emailInput")
        phone = form.getvalue("phoneInput")
        print(f"<p>Expediteur : {username}</p>")
        print(f"<p>Email : {email}</p>")
        print(f"<p>tel : {phone}</p>")
        print(f"<p>Message : {message}</p>")
    else:
        raise Exception("Nom non transmis")
except:
    print("Nom ou message non transmis. Pour la sécurité de votre système Yperia ne souhaite pas traitrer ce message.\n Nous vous prions de nous excuser pour cet incident. L'équipe technique est actuellement entrain de le résoudre.\n à bientôt...")



html = """
</body>
</html>
"""
print(html)