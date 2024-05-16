from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import OVSSwitch, RemoteController
from mininet.link import TCLink

def create_topology():
    net = Mininet(controller=RemoteController, switch=OVSSwitch, link=TCLink)
    
    # Add switches for each building
    s1 = net.addSwitch('s1')  # Building A
    s2 = net.addSwitch('s2')  # Building B
    s3 = net.addSwitch('s3')  # Building C
    s4 = net.addSwitch('s4')  # Building D
    s5 = net.addSwitch('s5')  # Building E
    server_switch = net.addSwitch('server_switch')  # Server room switch

    # Add hosts (lecture rooms and servers)
    h1 = net.addHost('h1', ip='x.x.110.1/24', mac='00:00:00:00:00:01', vlan=110)
    h2 = net.addHost('h2', ip='x.x.110.2/24', mac='00:00:00:00:00:02', vlan=110)
    h3 = net.addHost('h3', ip='x.x.220.1/24', mac='00:00:00:00:00:03', vlan=220)
    h4 = net.addHost('h4', ip='x.x.220.2/24', mac='00:00:00:00:00:04', vlan=220)
    h5 = net.addHost('h5', ip='x.x.330.1/24', mac='00:00:00:00:00:05', vlan=330)
    h6 = net.addHost('h6', ip='x.x.330.2/24', mac='00:00:00:00:00:06', vlan=330)
    h7 = net.addHost('h7', ip='x.x.440.1/24', mac='00:00:00:00:00:07', vlan=440)
    h8 = net.addHost('h8', ip='x.x.440.2/24', mac='00:00:00:00:00:08', vlan=440)
    h9 = net.addHost('h9', ip='x.x.550.1/24', mac='00:00:00:00:00:09', vlan=550)
    h10 = net.addHost('h10', ip='x.x.550.2/24', mac='00:00:00:00:00:10', vlan=550)
    server1 = net.addHost('server1', ip='12.0.0.1/16', mac='00:00:00:00:00:11')
    server2 = net.addHost('server2', ip='41.0.0.1/16', mac='00:00:00:00:00:12')

    # Connect hosts to respective switches
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(h5, s3)
    net.addLink(h6, s3)
    net.addLink(h7, s4)
    net.addLink(h8, s4)
    net.addLink(h9, s5)
    net.addLink(h10, s5)

    # Connect servers to server room switch
    net.addLink(server1, server_switch)
    net.addLink(server2, server_switch)

    # Connect switches in a ring topology (for example)
    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s3, s4)
    net.addLink(s4, s5)
    net.addLink(s5, s1)

    # Start the network
    net.start()
    CLI(net)  # Start Mininet CLI for testing

    # Stop the network
    net.stop()

if __name__ == '__main__':
    create_topology()
