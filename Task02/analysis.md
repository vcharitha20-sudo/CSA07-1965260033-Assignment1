# Task 2 — worked notes

Original: hub A 10 PCs = 1 collision domain; hub B = 1; 4 cameras = 4; switch-to-router = 1; router-to-second-switch = 1; six printers = 6; total 14 collision domains. Router separates 2 broadcast domains.

Hubs repeat at layer 1; switches forward by MAC at layer 2; routers route at layer 3. Switches flood broadcasts within VLANs; routers do not forward ordinary layer-2 broadcasts.

Hub segments are shared multipoint; dedicated switch links are point-to-point. Standards: TIA/EIA-568 cabling (TIA), IEEE 802.11ax (IEEE), TCP RFC 9293 (IETF), ISO/IEC 7498-1 (ISO/IEC), Bluetooth (Bluetooth SIG), 5G NR (3GPP).

Alternative: 20 PCs + 4 cameras + 6 printers = 30 host switch ports plus router trunk = 31 collision domains, assuming each host uses a dedicated full-duplex link. Three VLANs = 3 broadcast domains with router-on-a-stick; fixes shared-media collisions and segments broadcasts, not link failures or congestion.

**Verification:** Check assumptions and provide your own required evidence before submitting.
