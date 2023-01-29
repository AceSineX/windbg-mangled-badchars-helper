# windbg-mangled-badchars-helper
Find if a windbg output blob of badcharacters is mangled.
The script ASSUMES you sent the bad characters in ascending order!

Put a WinDbg blob into a file
Example:
```
0277ea84  00544547 00000000 00000000 00000000  GET.............
0277ea94  00000000 00000000 5d5c5b2f 61605f5e  ......../[\]^_`a
0277eaa4  65646362 69686766 6d6c6b6a 71706f6e  bcdefghijklmnopq
0277eab4  75747372 79787776 7d7c7b7a 81807f7e  rstuvwxyz{|}~...
0277eac4  85848382 89888786 8d8c8b8a 91908f8e  ................
0277ead4  95949392 99989796 9d9c9b9a a1a09f9e  ................
0277eae4  a5a4a3a2 a9a8a7a6 adacabaa b1b0afae  ................
0277eaf4  b5b4b3b2 b9b8b7b6 bdbcbbba c1c0bfbe  ................
```

# Usage:
>python3 parse_bc.py 71

>python3 parse_bc.py 71 /path/to/file
