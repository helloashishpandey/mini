from mininet.node import Controller, OVSKernelAP
from mininet.log import setLogLevel
from mininet.wifi.cli import CLI_wifi
from mininet.wifi.net import Mininet_wifi
from mininet.wifi.node import OVSKernelAP
from mininet.wifi.wmediumdConnector import WmediumdStarter

def topology():
    "Create a network."
    net = Mininet_wifi(controller=Controller, accessPoint=OVSKernelAP, wmediumd_mode=1, wmediumd_log_level=0,
                       topo='linear', switch=OVSKernelAP, link=wmediumd, enable_interference=True)
    
    print("*** Creating nodes")
    # Add ad hoc hosts
    adhoc1 = net.addAdhoc('adhoc1', ssid='adhoc', mode='g', position='20,5,0', range=5, antennaHeight='5', antennaGain='0')
    adhoc2 = net.addAdhoc('adhoc2', ssid='adhoc', mode='g', position='20,5,0', range=5, antennaHeight='5', antennaGain='0')
    adhoc3 = net.addAdhoc('adhoc3', ssid='adhoc', mode='g', position='20,5,0', range=5, antennaHeight='5', antennaGain='0')
    adhoc4 = net.addAdhoc('adhoc4', ssid='adhoc', mode='g', position='20,5,0', range=5, antennaHeight='5', antennaGain='0')
    adhoc5 = net.addAdhoc('adhoc5', ssid='adhoc', mode='g', position='20,5,0', range=5, antennaHeight='5', antennaGain='0')
    adhoc6 = net.addAdhoc('adhoc6', ssid='adhoc', mode='g', position='20,5,0', range=5, antennaHeight='5', antennaGain='0')

    print("*** Starting network")
    net.build()
    net.start()

    print("*** Running CLI")
    CLI_wifi(net)

    print("*** Stopping network")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
