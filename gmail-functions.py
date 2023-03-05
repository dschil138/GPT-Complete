from AppKit import NSWorkspace, NSAppleScript

from config import *

# check open apps for Chrome
def check_apps_for_chrome():
    workspace = NSWorkspace.sharedWorkspace()
    running_apps = workspace.runningApplications()
    chrome_open = False
    chrome_active = False
    for app in running_apps:
        if app.bundleIdentifier() == "com.google.Chrome":
            print("Google Chrome is active.")
            return True


# check open tabs for gmail
def check_tabs_for_gmail(tab_wanted):
    script = NSAppleScript.alloc().initWithSource_("""
        tell application "Google Chrome"
            return URL of active tab of front window
        end tell
        """)
    result, error = script.executeAndReturnError_(None)
    if error:
        print(error)
    else:
        print(result.stringValue())
        tabs_string = result.stringValue()
        if tabs_string.find(tab_wanted) != -1:
            print("found gmail")
            return True
        else:
            return False


def check_system_for_gmail(website_wanted):
    if check_apps_for_chrome():
        if check_tabs_for_gmail(website_wanted):
            print("gmail is active")
            return True
    else:
        print("Google Chrome is not active.")

def create_full_prepend(website_wanted):
    if check_system_for_gmail(website_wanted):
        print("gmail was true")
        full_prepend = (universal_prepend + "finish this email")
    else:
        print("gmail was false")
        full_prepend = universal_prepend
    print(full_prepend)
    return full_prepend
