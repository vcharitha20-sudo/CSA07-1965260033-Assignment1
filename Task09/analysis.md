# Task 9 — worked notes

600 km / (2×10^8 m/s) = 3 ms one-way propagation; 1200×8 / 10^9 = 9.6 μs transmission; a=312.5. Stop-and-wait utilization 1/(1+2a)=1/626 ≈ 0.1597%, throughput ≈1.597 Mbps (ignoring ACK transmission).

Minimum full-use window = ceil(1+2a)=626 frames. Go-Back-N sequence bits: ceil(log2(627))=10; Selective Repeat bits: ceil(log2(2×626))=11.

With a full window, GBN may retransmit up to 626 frames following a loss; SR only the lost frame, at cost of buffering/reordering. HDLC uses 01111110 flags and inserts a zero after five consecutive ones.

Alternative: window 400 gives utilization 400/626 = 63.90%, throughput ≈ 638.98 Mbps; GBN retransmission can be much larger than SR.

**Verification:** Check assumptions and provide your own required evidence before submitting.
