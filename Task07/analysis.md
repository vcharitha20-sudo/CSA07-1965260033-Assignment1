# Task 7 — worked notes

CRC-4 polynomial 10011; show modulo-2 division and syndrome with the supplied test frames in your handwritten working. A degree-4 CRC detects all burst errors of length ≤ 4; a flipped-bit pattern equal to generator polynomial is undetectable.

Two-dimensional even parity detects single flips but misses four flipped bits at the corners of a rectangle.

Internet checksum of 4500 0054 1C46 4000 4001 = 1E64. A swap of two 16-bit words leaves the ones-complement sum unchanged; CRC depends on bit order.

Alternative: checksum can miss reordered words; CRC-4 can miss an error whose polynomial is divisible by 10011. Include specific calculated error cases in final submission.

**Verification:** Check assumptions and provide your own required evidence before submitting.
