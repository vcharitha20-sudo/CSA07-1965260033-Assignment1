# Task 4 — worked notes

70 m near drives: properly grounded Cat6A S/FTP or fibre for severe EMI. 130 m office: fibre, because standard twisted-pair Ethernet channel max is 100 m. 700 m floor–hall: single-mode fibre (trap: exceeds cited 550 m multimode limit). 600 km: carrier leased optical service.

Shannon C = B log2(1+10^(SNR/10)): at 500 MHz, 35 dB ≈ 5.814 Gbps; at 12 dB ≈ 2.036 Gbps. Theoretical limits, not guaranteed Ethernet rates. Shield continuity, compatible connectors and correct bonding/grounding are required.

Single-mode link margin from code: 0.7 km 16.55 dB, 10 km 12.90 dB, 40 km 2.00 dB FAIL for 3 dB minimum. With 4 connectors and 6 splices maximum = 38.29 km.

Alternative: 80 MHz Wi-Fi at 18 dB Shannon limit ≈ 479.5 Mbps; capacity alone cannot guarantee 8 ms latency under roaming, contention and EMI.

**Verification:** Check assumptions and provide your own required evidence before submitting.
