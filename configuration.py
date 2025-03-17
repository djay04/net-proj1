import configparser

def create_config():
    config = configparser.ConfigParser()

    config["osu"] = {'university': 'The Ohio State University', 'college': 'College of Engineering', 'department': 'Department of Computer Science and Engineering', 'class': 'CSE3461'}

    config['server'] = {'serverHost': '10.134.215.76', 'serverPort': '5782'}

    config['db'] = {'dbHost': '10.129.2.170', 'dbPort': '3232', 'commitInterval': '60'}

    config['logger'] = {'logHost': '10.1.154.241', 'logLevel' : 'info'}

    config['topsecret.server.com'] = {'port': '50022', 'ForwardX11': 'no'}

    with open('configuration.ini','w') as file:
        file.write("#-------------------------------------------\n")
        file.write("#\n")
        file.write("# CSE 3461/5461 Project 1 Configuration File")
        file.write("#\n")
        file.write("#-------------------------------------------\n")

        file.write("[osu]\n")
        file.write("university=The Ohio State University\n")
        file.write("college=College of Engineering\n")
        file.write("department=Department of Computer Science and Engineering\n")
        file.write("class=CSE3461\n")
        
        file.write("\n")

        file.write("[server]\n")
        file.write("# host address\n")
        file.write("serverHost=10.134.215.76\n")
        file.write("\n")
        file.write("# listening port\n")
        file.write("serverPort=5782\n")
        file.write("\n")
        file.write("[db]\n")
        file.write("# host address\n")
        file.write("dbHost=10.129.2.170\n")
        file.write("\n")
        file.write("# listening port\n")
        file.write("dbPort=3232\n")
        file.write("\n")
        file.write("# commit interval\n")
        
        file.write("commitInterval = 60\n")
        
        file.write("\n")

        file.write("[logger]\n")
        file.write("# host address\n")
        file.write("logHost=10.1.154.241\n")
        
        file.write("\n")

        file.write("# default log level\n")
        file.write("logLevel=info\n")

        file.write("\n")
        
        file.write("[topsecret.server.com]\n")
        file.write("Port = 50022\n")
        file.write("ForwardX11 = no")

if __name__ == "__main__":
    create_config()


        

