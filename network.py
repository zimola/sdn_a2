from mininet.topo import Topo

class CustomTopo(Topo):
    "Assignment 1 Question 1"
    def __init__(self):
        Topo.__init__(self)
        # add 5 switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')

        # add 5 hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')

        # connect hosts and switches
        self.addLink(h1,s1)
        self.addLink(h2,s2)
        self.addLink(h3,s3)
        self.addLink(h4,s4)
        self.addLink(h5,s5)

        # connect switches
        self.addLink(s1,s2)
        self.addLink(s1,s3)
        self.addLink(s1,s4)
        self.addLink(s1,s5)
        self.addLink(s2,s3)
        self.addLink(s2,s4)
        self.addLink(s2,s5)
        self.addLink(s3,s4)
        self.addLink(s3,s5)
        self.addLink(s4,s5)
        
    
topos = {'topo1': ( lambda: CustomTopo() ) }
