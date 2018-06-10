from mininet.log import setLogLevel
import networkx as nx
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.node import Controller, RemoteController
from mininet.cli import CLI


class CompleteGraphTopo(Topo):

    def build(self, total_node=10):
        graph = nx.complete_graph(total_node)
        edges = edges = [(0, 1), (1, 0), (0, 2), (2, 0), (0, 3), (3, 0),
                       (1, 2), (2, 1), (1, 5), (5, 1), (1, 8), (8, 1),
                       (2, 3), (3,2), (2, 6), (6, 2), (2, 4), (4, 2),
                       (3, 6), (6, 3), (4, 5), (5, 4), (4, 7), (7, 4),
                       (4, 8), (8, 4), (5, 6), (6, 5),(5, 7), (7, 5),
                       (5, 9), (9, 5), (6, 7), (7, 6), (9, 6), (6, 9),
                       (8, 9), (9, 8)]

        for node in range(total_node):
            switch = self.addSwitch('s%s' % (node + 1))
            host = self.addHost('h%s' % (node + 1), cpu=.5 / total_node)
            self.addLink(host, switch)

        for (sw1, sw2) in edges:
            sw1 = int(sw1) + 1
            sw2 = int(sw2) + 1
            self.addLink("s%d" % sw1,  "s%d" % sw2)


def runner():
    topo = CompleteGraphTopo(total_node=10)
    c = RemoteController('c', '127.0.0.1', 6633)
    net = Mininet(topo=topo, controller=c, host=CPULimitedHost, link=TCLink, autoSetMacs=True)
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    runner()

