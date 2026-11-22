# Task 6 — worked notes

CRC errors mean received Ethernet frames failed integrity checks; full duplex has no collisions. Check cable termination, pair faults, connectors, interference and NIC/switch ports.

100BASE-TX uses two pairs (pins 1–2 and 3–6); 1000BASE-T uses all four pairs. Test all pairs, inspect switch and NIC speed, and use ethtool on Linux where available.

ff:ff:ff:ff:ff:ff broadcast; 33:33:00:00:00:01 IPv6 multicast; 3c:52:82:4e:11:07 unicast; first 3 octets form an OUI assigned to a vendor (verify assignment in a current OUI registry).

PoE load: 12 × 25.5 + 10 × 12.95 = 435.5 W > 370 W, short by 65.5 W; choose a larger PoE budget or split loads. Alternative: star uplink cut disconnects downstream switch until repaired; triangle with RSTP can reconverge in ~1–2 s vs classic STP 30–50 s, assuming redundant topology.

**Verification:** Check assumptions and provide your own required evidence before submitting.
