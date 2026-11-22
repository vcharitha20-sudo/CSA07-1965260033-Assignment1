# Task 12 — worked notes

80 AMRs added; assignment does not specify AMR command size or frequency, so exact extra Mbps cannot be calculated without an explicit assumption. Under assumed 120 bytes every 4 ms, AMRs add 80×0.24 = 19.2 Mbps. Six-zone baseline would become 1805.28 Mbps if all AMRs counted once warehouse-wide.

Wi-Fi trip 35 handovers × 120 ms = 4.2 s unreachable; 5G trip 5 × 15 ms = 75 ms unreachable. Both per-handover figures exceed the 8 ms command deadline; private 5G alone does not prove zero missed commands.

Modify/redesign: 5G URLLC with engineered make-before-break coverage and on-robot fail-safe control, wired/fibre backbone, isolated robot QoS, Wi-Fi 6 for office, and capacity/resilience monitoring.

Validate 99.9th-percentile end-to-end latency, handover interruption, packet loss and failover under loaded warehouse conditions. Claim “never miss a command” cannot be guaranteed by the provided figures.

**Verification:** Check assumptions and provide your own required evidence before submitting.
