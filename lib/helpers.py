from termcolor import colored

def logo():
    print('''
|/////////////////////////////////////////////////////////////////////////////
|		                      ,-,-      
|		                     / / |      
|		   ,-'             _/ / /       
|		  (-_          _,-' `Z_/        
|		   "#:      ,-'_,-.    \  _     
|		    #'    _(_-'_(o)\    \" |    
|		  ,--_,--'                 |    
|		 / ""                      L-'\ 
|		 \,--^---v--v-._        /   \ | 
|		   \_________________,-'     \| 
|		                    \          \   
|		                     \           \  
|				      \       	   \ _ _ _ _ 
|	                _        _        _     _ 
|	    /\/\   __ _| |_ __ _| |_ __ _| |__ (_) {V1.0}
|	   /    \ / _` | __/ _` | __/ _` | '_ \| |
|	  / /\/\ \ (_| | || (_| | || (_| | |_) | |
|	  \/    \/\__,_|\__\__,_|\__\__,_|_.__/|_|
|				-- By D-Ashwin
-------------------------------------------------------------------------------------
“Never underestimate the determination of a kid who is time-rich and cash-poor.”
								― Cory Doctorow
-------------------------------------------------------------------------------------
	''')

def hash_identifier():
	hash = input(">>")
	print("\nThe type of hash for the value :",hash)
	print("Type :\n")

def ddos():
	print("-Select DDoS Options :")
	print("\t1-DDoS Explained")
	print("\t2-Type of DDoS")
	print("\t3-Avaiable DDoS")
	ddos_input = input(">>")
	if ddos_input == '1':
		ddos_explained()

	elif ddos_input == '2':
		ddos_list()

	else:
		print("Yasssss!")

def ddos_explained():
	print("DDoS : Denial Of Service")

def ddos_list():
	print("List of DDoS attacks:")
	print("\nDDoS Broadly divided into three types:")
	print("1. Volume based DDoS attack")
	print("2. Protocol based attack")
	print("3. Application based attack")
	print("\nSpecific DDoS Attack Types")
	print("• SYN flood")
	print("• SYN-ACK flood")
	print("• ACK flood")
	print("• Fragmented ACK flood")
	print("• RST/FIN flood")
	print("• Same source/destn flood (land attack)")
	print("• Fake session attack")
	print("• UPD flood")
	print("• Non-spoof UDP flood")
	print("• ICMP flood")
	print("• ICMP fragmentation flood")
	print("• Ping flood")
	print("• TOS flood")
	print("• IP NULL /TCP NULL attack")
	print("• Smurf/Fraggle Attack")
	print("• DNS flood DNS Amplified / reflection attack")
	print("• NTP flood")
	print("• Slow session attack")
	print("• Slow read attack")
	print("• HTTP attack")
	print("• HTTP GET flood")
	print("• Excessive verb single attack")
	print("• Multiple verb-single attack")
	print("• Recursive GET attack")
	print("• Random recursive GET")
	print("• Specially crafted packet")
	print("• Stack Attacks")
	print("• Advanced Evasion technique")
	print("• Lack of protocol “state awareness attack”")
