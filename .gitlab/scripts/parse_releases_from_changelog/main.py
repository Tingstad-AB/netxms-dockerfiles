import re as regex # To split the original file based on specific astrisks 
import json # To output the result as JSON

changeLogFile = open("/mnt/c/Users/MBeckett/Documents/Repositories/netxms-dockerfiles/changelog/ChangeLog", "r").read()
flatChangeList = list()

# Regex breakdown:
    # | divides two seperate regex statements
    # ^ finds start of string, $ finds end of string, characters between these are matched
    # \ escapes the * as * is a special character in regex and we want to match '*' or '* '
for change in regex.split(r'^\*$|^\* $', changeLogFile, flags=regex.MULTILINE):
    if change != '\n': # Strip blank lines
        if change != '': # Strip blank lines
            flatChangeList.append(change) # Create flat list containing version numbers and patch notes
        
changeList = list(zip(flatChangeList[0::2], flatChangeList[1::2])) # Split the list into a list of tuples containing (Version, Patch Notes)

OutDict = dict() # Create to dict to be output as JSON
for change in changeList:
    # Strip extra new lines and asterisk in change version/change text
    changeVersion = change[0].lstrip("\n* ").rstrip("\n")
    ChangeText = change[1].lstrip("\n").rstrip("\n")
    if "CURRENT" in changeVersion:
        continue
    OutDict[changeVersion] = ChangeText # Add each version to dict

# Write file out to JSON
with open('releases_from_changelog.json', 'w') as file:
    file.write(json.dumps(OutDict))