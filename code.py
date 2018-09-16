from termcolor import colored

print(colored("""
\t\t\t+++++++++++++++++++++++++++++++++++++++++++++++
\t\t\t+                                             +
\t\t\t+ \t\t PROJECT MATATABI             +
\t\t\t+                                             +
\t\t\t+++++++++++++++++++++++++++++++++++++++++++++++
""",'green'))
print(colored("Select one option:",'red'))
print("1. Google Dork Generator")
print("2. Hash Identifier")
print("3. etc")
var1= input(">> ")
if var1=='1':
    def gdgr():
        print("""
        -------------------------------------------
        ++++++++++ Google Dork Generator ++++++++++
        -------------------bY--Hax0r 45H-----------
        """)


    print("Select country:")
    cntry_dict = {"cntry" :{1:"Afghanistan",2:"Australia",3:"Bangladesh",4:"Canada",5:"China",6:"India",7:"Japan",8:"Kenya",9:"Korea",10:"Kuwait",11:"Malaysia",12:"Nepal",13:"Pakistan",14:"Srilanka",15:"Thailand",16:"U.A.E"},"cntrycode":{1:"AF",
    2:"AU",3:"BG",4:"CA",5:"CN",6:"IN",7:"JP",8:"KE",9:"KR",10:"KW",11:"MY",12:"NP",13:"PK",14:"LK",15:"TH",16:"AE"}}
    for list in cntry_dict.cntrycode:
        print(list)
    # print(cntry_dict)
    sel_ctry = input()
    print(sel_ctry)

else:
    print("No")

