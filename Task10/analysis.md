# Task 10 — worked notes

For 600 km fibre: 3 ms one-way, 6 ms round trip minimum propagation. Compare with observed final hop ~15 ms RTT; remainder includes routing, processing, queueing and other path lengths.

Hop 3 41 ms outlier may be transient queueing or ICMP scheduling. Hop 4 * * * can be ICMP rate limiting/filtering, not necessarily a forwarding fault.

Largest sustained jump appears between hop 4 (no replies) and hop 5 (~14.6 ms); cannot assign exact delay to silent hop.

REQUIRED: run your own Windows ping and tracert and capture packets in Wireshark. Record timestamps, target, interface, RTT and header observations; do not substitute the assignment sample as personal measurements. Alternative: mtr repeated probes reveal persistent loss/jitter more reliably than one traceroute.

**Verification:** Check assumptions and provide your own required evidence before submitting.
