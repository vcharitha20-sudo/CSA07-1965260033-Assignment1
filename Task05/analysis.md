# Task 5 — worked notes

Assuming 25 m and 150 m contiguous coverage segments over 900 m: Wi-Fi 36 segments → 35 handovers × 120 ms = 4.2 s; 5G 6 segments → 5 handovers × 15 ms = 75 ms. Count depends on cell overlap and path endpoints.

AMRs need URLLC; cameras eMBB; RFID mMTC. NFC for close-range tags, Bluetooth for nearby peripherals, Zigbee for low-power sensors.

802.11r and OFDMA may reduce contention/roaming but require measured end-to-end deadline compliance; given 120 ms and 15 ms handover times, neither stated handover meets an 8 ms uninterrupted-command requirement.

Alternative: 120 × 200 × 8 = 192 kbps > 100 kbps usable gateway; 800 × 200 × 8 = 1.28 Mbps → at least 13 gateways by aggregate capacity (and 2 for a 120-reader aisle), before overhead and topology constraints.

**Verification:** Check assumptions and provide your own required evidence before submitting.
