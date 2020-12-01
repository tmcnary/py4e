import requests, json

automate_url = "https://automate.panerabread.com/api/v1/applications/service-groups"

querystring = {"filter":["origin:icafe","origin:sis","environment:prod*"],"pagination.size":"100"}

payload = ""
headers = {'api-token': 'h9QeCIOta9nHXzd7irW4tznHdN4='}

aresponse = requests.request("GET", automate_url, data=payload, headers=headers, params=querystring)

# print(type(response))

sgroups = aresponse.json().get('service_groups')
# print(sgroups)
i = 0
data = {}
for item in sgroups:
    f = sgroups[i]['package'].split("/")
    g = sgroups[i]['release'].split("/")
    package = f[1]
    origin = f[0]
    if 'releases' in g[0]:
        version = g[0]
        release = 'multiple'
    else:
        version = g[0]
        release = g[1]
    print(origin, package, version, release)


    i += 1
print(type(data))
print(data)

bldr_url = "https://bldr.paneracloud.com/v1/depot/pkgs/sis"

querystring = {"range":"9"}

payload = ""
headers = {'api-token': 'h9QeCIOta9nHXzd7irW4tznHdN4='}

bresponse = requests.request("GET", bldr_url, data=payload, headers=headers, params=querystring)

f = bresponse.json().get('data')
print(type(f[0]))
# print(f[0][0])
x = 0
for item in f:
    borigin = f[x]['origin']
    bpackage = f[x]['name']
    bversion = f[x]['version']
    brelease = f[x]['release']
    x += 1
    print(borigin, bpackage, bversion, brelease)


# print(response.text)
