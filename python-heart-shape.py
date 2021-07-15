text = input("Enter your preferred text: ")
print('\n'.join([''.join([(text[(x-y) % len(text)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-25,30)]) for y in range(30,-30,-1)]))
