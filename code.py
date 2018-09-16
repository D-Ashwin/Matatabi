from termcolor import colored, cprint
from lib.helpers import logo, hash_identifier, ddos
import os

def select_option():
    os.getcwd()
    # os.system('')
    # print("[+] Options are as follows:-")
    # for option in range(1,10):
    #     print("\toption",format(option) )
    
def start_matatabi():
    #For logo
    # logo()

    print(colored("\nSelect one option:",'yellow'))
    print("1. Google Dork Generator")
    print("2. Hash Identifier")
    print("3. DDos")
    print("4. exit()")
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

    elif var1 =='2':
        print("Please Input hashed value:")
        hash_identifier()
        main()

    elif var1 =='3':
        ddos()

    elif var1=='4':
        print(colored("./logout","white"))
        exit()
    else:
        print("Please Select From above options -")
        main()

def main():
    start_matatabi()
    

if __name__ == '__main__':
    logo()
    main()








