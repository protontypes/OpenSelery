def getEmailsAndWeights(dep_list):
    contributor_emails = []
    #TODO:
    # get more information about each contributor
    # number commits
    # time spent on project (calculated from commits)
    # issues closed
    # successful pull requests
    #  
    for dep in dep_list:
        contributor_emails.append(dep["email_list"])

    weights = [1 for i in range(len(contributor_emails))]
    return contributor_emails, weights

def getUniqueDependencies(dependencies_json):
    uniqueList = dict()
    for platform in dependencies_json:
        if not platform["dependencies"]:
            continue
        platform_name = platform["platform"]
        if platform_name not in uniqueList.keys():
            uniqueList[platform_name] = []
        for dep in platform["dependencies"]:
            if dep not in uniqueList[platform_name]:
                uniqueList[platform_name].append(dep)
    return uniqueList

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1