# Task 8 — worked notes

For m=11, r=4 since 2^4 ≥ 11+4+1. Hamming(15,11) overhead = 4/15 = 26.67% of transmitted bits (or 4/11 = 36.36% relative to payload).

Use pairwise Hamming distances of the supplied 6-bit codewords to find minimum distance; detection capacity dmin−1, correction floor((dmin−1)/2).

The given Hamming(7,4) received word differs from transmitted word at bit position 6; corrected word is 1100110, data bits positions 3,5,6,7 = 0110.

Alternative: 15-bit code with BER 0.002: probability of at least one error = 1−(0.998)^15 ≈ 2.956%; simple CRC+ARQ has similar initial frame error probability (undetected CRC errors ignored). Retransmission airtime expectation depends on whether 400 ms is per attempt or only retransmission overhead.

**Verification:** Check assumptions and provide your own required evidence before submitting.
