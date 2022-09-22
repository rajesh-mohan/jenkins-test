from os import getenv, environ

print(str(getenv("MY_PASSWORD")))
if "blablapass" == getenv("MY_PASSWORD"):
    print("true")
else:
    print("false")
print(environ["MY_USERNAME"])
