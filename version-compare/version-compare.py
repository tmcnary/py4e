import json, requests, urllib.request, urllib.parse, urllib.error

service_url = 'https://bldr.paneracloud.com/v1/depot/pkgs'
headers = {
    'api-token': 'h9QeCIOta9nHXzd7irW4tznHdN4='
}


# List the program will use to build our data structures.
# app_names = []
# app_latest = []
# env_list = []
# ver_list = []
# release_list = []
# diff_list_auto = []
# diff_list_bldr = []

# Builds a slice form a char array starting form the first index to the delimitter passed as an arg
def char_slicer (str, de):
    str_to_list = list(str)
    try:
        index = str_to_list.index(de)
    except:
        return str_to_list
    else:
        list_to_slice = str_to_list[0:index]
        return list_to_slice

# Makes a get api call url and returns a json
def get_call (url):
    raw_data = urllib.request.urlopen(url)
    decoded_data = raw_data.read().decode()
    new_json = json.loads(decoded_data)
    return new_json

# Main function that builds our data structure - a list of dictonaries corresponding to app data from builder.
def get_from_bldr(origin, environment):
    app_names = []
    app_latest = []
    env_list = []
    distinct_url = service_url + '/' + origin + '?distinct=true'
    response_json = get_call(distinct_url)
    crop_list = response_json['data']
    
    # Builds a list of the name of each application within an origin.
    # The list will be used to loop through all the applications in the while loop below.
    for d in crop_list:
        app_names.append(d['name'])

    i = 0
    
    # Builds a list contaning the state and meta data of each app.
    while i < len(app_names):
        app_url = service_url + '/' + app_names[i]
        app_json = get_call(app_url)
        app_detail = app_json['data']
        app_latest.append(app_detail[0])
        i += 1

    dev_qa = False

    # Filters list made by above by environment.  Then builds a final list based on the filter
    for app in app_latest:
        for env in app['channels']:
            if env == environment:
                dev_qa = True
        if dev_qa == True:
            env_list.append(app)
        dev_qa = False
        
    return env_list

#  Gets the the version of an app deployed to an evnironment according to automate.
def get_from_automate(origin, env):
    api_call = "https://automate.panerabread.com/api/v1/applications/service-groups?filter=origin:%s&filter=environment:%s" % (origin, env)
    response = requests.request("GET", api_call, headers=headers)
    json_data = response.json()
    return_data = json_data['service_groups']
    return return_data

# Builds the list of apps that don't match.  Bldr is the source of truth.
def get_diff(origin, env):
    diff_list_auto = []
    diff_list_bldr = []
    bldr_list = get_from_bldr(origin, env)
    automate_list = get_from_automate(origin, env)

    for app_bldr in bldr_list:
        bldr_name = list(app_bldr['name'])
        for app_auto in automate_list:
            auto_name = char_slicer(app_auto['name'], '.')
            if bldr_name == auto_name:
                rel = char_slicer(app_auto['release'], '/')
                ver = list(app_bldr['version'])
                if rel != ver:
                    diff_list_auto.append(app_auto)
                    diff_list_bldr.append(app_bldr)
    return diff_list_auto, diff_list_bldr

print(get_diff('icafe', 'dev'))
print(get_diff('icafe', 'qa'))
print(get_diff('sis', 'dev'))
print(get_diff('sis', 'qa'))
