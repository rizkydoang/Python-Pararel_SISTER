import Pyro4
from datetime import date

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        return ("Hi welcome " + str (name))

    @Pyro4.expose
    def calculateAge(self,birth_year):
        age = int(date.today().year) - int(birth_year)
        if age > 60:
            result = "Kamu udah tua"
        else:
            result = "Kamu masih muda"
        return result

def startServer():
    server = Server()
    # make a Pyro daemon
    daemon = Pyro4.Daemon()             
    # locate the name server running
    ns = Pyro4.locateNS()
    # register the server as a Pyro object
    uri = daemon.register(server)  
    # register the object with a name in the name server
    ns.register("server", uri)   
    # print the uri so we can use it in the client later
    print("Ready. Object uri =", uri)
    # start the event loop of the server to wait for calls
    daemon.requestLoop()                   

if __name__ == "__main__":
    startServer()

