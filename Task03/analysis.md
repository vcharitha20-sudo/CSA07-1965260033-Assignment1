# Task 3 — worked notes

Ethernet II is OSI layer 2 frame; IPv4 layer 3 packet; TCP layer 4 segment; MQTT layer 7 data. TTL 64 to 62 implies two router decrements.

Assuming no IP/TCP options: Ethernet 14 + IPv4 20 + TCP 20 + data 24 + FCS 4 = 82 bytes; overhead 58/82 = 70.73%. With 1460-byte TCP payload: total 1518, overhead 58/1518 = 3.82%. This excludes preamble/interframe gap.

FCS failure: data-link layer; no route: network layer; no listener: transport/application endpoint. Switch layer 2, router layer 3, application firewall may inspect layers 3–7.

Alternative: UDP header 8 vs TCP 20 saves 12 bytes; connection setup and teardown avoid 3 + 4 = 7 TCP control segments per short-lived connection. UDP loses built-in reliable ordered byte stream and congestion control.

**Verification:** Check assumptions and provide your own required evidence before submitting.
