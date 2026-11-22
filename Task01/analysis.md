# Task 1 — worked notes

Robot traffic: 60 × 120 × 8 / 0.004 = 14.4 Mbps; RFID: 800 × 200 × 8 / 1,000,000 = 1.28 Mbps; CCTV: 32 × 6 = 192 Mbps; users: 200 × 0.15 × 3 = 90 Mbps.

Zone total 297.68 Mbps; six zones 1786.08 Mbps. CCTV sends most data; robots have strictest 8 ms deadline. A shared 1 Gbps uplink is insufficient for all six zones.

A 50 ms delay is most harmful to robot commands, then interactive users, RFID, then buffered CCTV; safety-monitoring video may merit higher priority.

Alternative: CCTV event clips at 8% give 15.36 Mbps; zone 121.04 Mbps, six zones 726.24 Mbps. Average traffic fits 1 Gbps, but burst headroom/QoS remain important.

**Verification:** Check assumptions and provide your own required evidence before submitting.
