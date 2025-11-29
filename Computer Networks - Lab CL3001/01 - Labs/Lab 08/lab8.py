import ns.applications as apps
import ns.core as core
import ns.internet as internet
import ns.network as network
import ns.point_to_point as p2p
import ns.internet_apps as internet_apps

# Create network nodes
nodes = network.NodeContainer()
nodes.Create(4)  # n0, n1, n2, n3

# Set up Internet stack
internet_stack = internet.InternetStackHelper()
internet_stack.Install(nodes)

# Define the point-to-point links and their attributes
p2p_n0_n2 = p2p.PointToPointHelper()
p2p_n0_n2.SetDeviceAttribute("DataRate", core.StringValue("2Mbps"))
p2p_n0_n2.SetChannelAttribute("Delay", core.StringValue("10ms"))

p2p_n1_n2 = p2p.PointToPointHelper()
p2p_n1_n2.SetDeviceAttribute("DataRate", core.StringValue("2Mbps"))
p2p_n1_n2.SetChannelAttribute("Delay", core.StringValue("10ms"))

p2p_n2_n3 = p2p.PointToPointHelper()
p2p_n2_n3.SetDeviceAttribute("DataRate", core.StringValue("1.7Mbps"))
p2p_n2_n3.SetChannelAttribute("Delay", core.StringValue("20ms"))

# Install network devices on the nodes
devices_n0_n2 = p2p_n0_n2.Install(nodes.Get(0), nodes.Get(2))
devices_n1_n2 = p2p_n1_n2.Install(nodes.Get(1), nodes.Get(2))
devices_n2_n3 = p2p_n2_n3.Install(nodes.Get(2), nodes.Get(3))

# Set DropTail queue with max size 10 packets
queue = core.StringValue("ns3::DropTailQueue<Packet>")
devices_n0_n2.Get(0).SetAttribute("TxQueue", queue)
devices_n1_n2.Get(0).SetAttribute("TxQueue", queue)
devices_n2_n3.Get(0).SetAttribute("TxQueue", queue)

# Assign IP addresses
address = internet.Ipv4AddressHelper()

address.SetBase(core.Ipv4Address("10.1.1.0"), core.Ipv4Mask("255.255.255.0"))
interfaces_n0_n2 = address.Assign(devices_n0_n2)

address.SetBase(core.Ipv4Address("10.1.2.0"), core.Ipv4Mask("255.255.255.0"))
interfaces_n1_n2 = address.Assign(devices_n1_n2)

address.SetBase(core.Ipv4Address("10.1.3.0"), core.Ipv4Mask("255.255.255.0"))
interfaces_n2_n3 = address.Assign(devices_n2_n3)

# TCP connection between n1 (client) and n3 (server)
tcp_source = apps.BulkSendHelper("ns3::TcpSocketFactory", core.InetSocketAddress(interfaces_n2_n3.GetAddress(1), 9))
tcp_source.SetAttribute("MaxBytes", core.UintegerValue(0))
source_app = tcp_source.Install(nodes.Get(1))
source_app.Start(core.Seconds(0.5))
source_app.Stop(core.Seconds(4.0))

tcp_sink = apps.PacketSinkHelper("ns3::TcpSocketFactory", core.InetSocketAddress(core.Ipv4Address.GetAny(), 9))
sink_app = tcp_sink.Install(nodes.Get(3))
sink_app.Start(core.Seconds(0.0))
sink_app.Stop(core.Seconds(5.0))

# UDP connection between n0 and n3
udp_source = apps.OnOffHelper("ns3::UdpSocketFactory", core.InetSocketAddress(interfaces_n2_n3.GetAddress(1), 10))
udp_source.SetAttribute("PacketSize", core.UintegerValue(1024))  # 1 KB
udp_source.SetAttribute("DataRate", core.StringValue("100kbps"))
udp_source.SetAttribute("StartTime", core.TimeValue(core.Seconds(0.1)))
udp_source.SetAttribute("StopTime", core.TimeValue(core.Seconds(4.5)))
udp_app = udp_source.Install(nodes.Get(0))

udp_sink = apps.PacketSinkHelper("ns3::UdpSocketFactory", core.InetSocketAddress(core.Ipv4Address.GetAny(), 10))
udp_sink_app = udp_sink.Install(nodes.Get(3))

# Enable routing
ipv4_routing = internet.Ipv4GlobalRoutingHelper.PopulateRoutingTables()

# Enable packet tracing
p2p_n0_n2.EnablePcap("n0_n2", devices_n0_n2.Get(0), True)
p2p_n1_n2.EnablePcap("n1_n2", devices_n1_n2.Get(0), True)
p2p_n2_n3.EnablePcap("n2_n3", devices_n2_n3.Get(0), True)

# Run the simulation
core.Simulator.Run()
core.Simulator.Destroy()
