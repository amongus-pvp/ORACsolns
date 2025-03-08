r, c, rose_r, rose_c, scar_r, scar_c = map(int, input().split())

if (rose_r - scar_r + rose_c - scar_c) % 2 == 0:
    print("SCARLET")
else:
    print("ROSE")
