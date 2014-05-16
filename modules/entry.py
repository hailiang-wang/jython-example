"""
module to access RTC resources.
"""

import sys
import os

# flag to identify the path correction
is_arrow_path_adjusted = False

# RTC jars must add into path at first.
def fix_path():
    global is_arrow_path_adjusted
    if( not is_arrow_path_adjusted ):
        arrow_lib = os.path.join(os.environ["ARROW_HOME"], "lib")
        [ sys.path.append(os.path.join(arrow_lib, x)) 
                for x in os.listdir(arrow_lib) if x.endswith(".jar") or 
                    x.endswith(".zip")]
        is_arrow_path_adjusted = True

fix_path()

import java.util.Date as Date


class RJC(object):

    def __init__(self, repository_address, username, password):
        self.repository_address = repository_address
        self.username = username
        self.password = password 
    
    def login(self):
        print self.repository_address 
        print Date()

if __name__ == "__main__":
    rjc = RJC("https://hub.jazz.net/ccm01","bar","foo") 
    rjc.login()
