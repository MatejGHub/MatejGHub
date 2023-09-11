"""
import sys


if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])   
"""    
#newtask
"""
import sys

if len(sys.argv) < 2:
    sys.exit("Print too few arguments")

for arg in sys.argv[1:]:
    print("Hello my name is", arg)
"""
#newtask
"""
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
"""
#newtask
"""
import cowsay
import sys

if len(sys.argv) == 2:
    print("Hello my name is" + sys.argv[1])
elif len(sys.argv) != 2:
    print("Invalid")
"""
#newtask
"""
import json
import requests
import sys


if len(sys.argv) != 2:
    sys.exit()

response = requests.get ("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent = 2))
"""
#newtask
"""
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
"""

