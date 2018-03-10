#! python3

import math

sys_clk = 16E6
prescaler = 256
ac_freq = 60

timer_clk = sys_clk / prescaler
ticks_per_zero = timer_clk / (ac_freq * 2)

lookup = []

# integral (sin x) = -cos x + C
# C = 1
# inverse -cos x + 1
# = acos(-(x - 1))

for i in range(256):
    x = i / 255
    lookup.append(math.acos(-(x - 1)))
    lookup[i] = int(lookup[i] * ticks_per_zero / math.pi)

if lookup[255] > 255:
    print("Warning!", str(lookup[255] - 255), "too many cycles")

    for i in range(256):
        lookup[i] = int(lookup[i] / lookup[255] * 255)
    
    MaxPower = str(-math.cos(math.pi * lookup[255] / ticks_per_zero) + 1)
    print("This will result in a max power of", MaxPower)
    
print('{')
for i in range(16):
    print('\t', end='')

    for j in range(16):
        print(lookup[i * 16 + j], end=' ')
        if lookup[i * 16 + j] < 100:
            print(' ', end='')
            if lookup[i * 16 + j] < 10:
                print(' ', end='')
    
    print('\n', end='')

print('}')