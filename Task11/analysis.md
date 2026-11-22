# Task 11 — worked notes

Use fibre aggregation/backbone, shielded wired robot cells or verified private 5G URLLC, Wi-Fi 6 for office users, separate VLANs/QoS for robot, camera, RFID and office traffic.

Provision >1.786 Gbps for six-zone uncompressed baseline (e.g. 10 GbE aggregation with headroom); 1 Gbps may suffice for six zones only under 8%-duty CCTV scenario (726.24 Mbps average).

Use Ethernet FCS for local error detection, appropriate transport recovery for non-real-time data, QoS and redundant uplinks for control reliability. Robot deadlines need end-to-end testing, not theoretical bandwidth alone.

Risks: RF interference/roaming and shared uplink failures. Six warehouses require per-site capacity plus engineered WAN aggregation. Alternative: SD-WAN broadband for noncritical stock/e-mail; dedicated SLA path for latency-sensitive control if control crosses WAN.

**Verification:** Check assumptions and provide your own required evidence before submitting.
