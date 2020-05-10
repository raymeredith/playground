# Introduction to Binary and Hexadecimal

### Binary and Hexadecimal 101

Introduction
- Normal numbers are Base 10 (numbers are powers of 10)
- Binary counts with 2 values, 1 (on) or 0 (off)
    - As you fill placeholders more are added
    - Places: 128, 64, 32, 16, 8, 4, 2, 1
        - If you look at the 8s placeholder, there will be combinations of 1s and 0s such that there are 8 starting with 0 and 8 starting with 1

Converting Binary to Decimal
- 1100 0000
    - Multiply the value by the placeholder itself, example:
    - (1 x 128) + (1 x 64) + (0 x 32) + ... = 192

Converting Decimal to Binary
- 210
    - Start with 128s placeholder (210 - 128 = 82)
    - Then go to 64s placeholder (82 - 64 = 18)
    - Keep moving on through all of them and say YES (1) where you can subtract remainder from placeholder and be left with a positive number, if not, then NO (0)
    - Answer: 1101 0010

Hexadecimal
- Every Hexadecimal value is 4 Binary bits
    - 0 = 0000
    - 1 = 0001
    - 2 = 0010
    - A = 1010 (10 in decimal)
    - F = 1111 (15 in decimal)
    - 10 = 10000 (16 in decimal)
