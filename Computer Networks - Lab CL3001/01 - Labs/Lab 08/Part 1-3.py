# Create nodes
nodes = ns.network.NodeContainer()
nodes.Create(4)  # n0, n1, n2, n3

# Install Internet Stack on nodes
stack = ns.internet.InternetStackHelper()
stack.Install(nodes)

# Point-to-point link between n0 and n2 (2 Mbps, 10 ms delay)
p2p_n0_n2 = ns.point_to_point.PointToPointHelper()
p2p_n0_n2.SetDeviceAttribute("DataRate", ns.core.StringValue("2Mbps"))
p2p_n0_n2.SetChannelAttribute("Delay", ns.core.StringValue("10ms"))
devices_n0_n2 = p2p_n0_n2.Install(nodes.Get(0), nodes.Get(2))

# Point-to-point link between n1 and n2 (2 Mbps, 10 ms delay)
p2p_n1_n2 = ns.point_to_point.PointToPointHelper()
p2p_n1_n2.SetDeviceAttribute("DataRate", ns.core.StringValue("2Mbps"))
p2p_n1_n2.SetChannelAttribute("Delay", ns.core.StringValue("10ms"))
devices_n1_n2 = p2p_n1_n2.Install(nodes.Get(1), nodes.Get(2))

# Point-to-point link between n2 and n3 (1.7 Mbps, 20 ms delay)
p2p_n2_n3 = ns.point_to_point.PointToPointHelper()
p2p_n2_n3.SetDeviceAttribute("DataRate", ns.core.StringValue("1.7Mbps"))
p2p_n2_n3.SetChannelAttribute("Delay", ns.core.StringValue("20ms"))
devices_n2_n3 = p2p_n2_n3.Install(nodes.Get(2), nodes.Get(3))

# Assign IP addresses to the nodes on the different networks
address = ns.internet.Ipv4AddressHelper()

# IP addresses for n0-n2 link
address.SetBase(ns.network.Ipv4Address("10.1.1.0"), ns.network.Ipv4Mask("255.255.255.0"))
interfaces_n0_n2 = address.Assign(devices_n0_n2)

# IP addresses for n1-n2 link
address.SetBase(ns.network.Ipv4Address("10.1.2.0"), ns.network.Ipv4Mask("255.255.255.0"))
interfaces_n1_n2 = address.Assign(devices_n1_n2)

# IP addresses for n2-n3 link
address.SetBase(ns.network.Ipv4Address("10.1.3.0"), ns.network.Ipv4Mask("255.255.255.0"))
interfaces_n2_n3 = address.Assign(devices_n2_n3)

# Enable routing
ns.internet.Ipv4GlobalRoutingHelper.PopulateRoutingTables()

# Simulation start and stop times
ns.core.Simulator.Stop(ns.core.Seconds(10.0))

# Run the simulation
ns.core.Simulator.Run()
ns.core.Simulator.Destroy()