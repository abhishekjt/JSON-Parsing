import json
#Reading JSON FILE
config = json.loads(open('C:/Python27/Parsing JSON/readme.json').read())
print("The PAGEID is:")
print(config['query']['pages']['1808130']['pageid'])
print("----------")
print("The TITLE is:")
print(config['query']['pages']['1808130']['title'])
print("----------")
strconfig = config['query']['pages']['1808130']['revisions'][0]['*']
#print(strconfig)

i=strconfig.index("See also")
k=strconfig.rfind("==")

i=i+10
k=k-12
#print i,k
substr=strconfig[i:k]
print("SEE ALSO:")
threefile=(substr.replace("[","")).replace("]","")

print((threefile.replace("*","https://en.wikipedia.org/wiki/")).replace(" ","_"))

