#while loop with use of continue and break statements :

mixed_count = [1, 2, 'three', 4, 5.5, 6, 7, 8, 9, 10, 11, 12]

print("\nWhile Loop Example (Only Integers):")
count = 0
while count < len(mixed_count):
    num = mixed_count[count]
    if not isinstance(num, int): 
        count += 1
        continue
    if num % 3 == 0: 
        count += 1
        continue
    if num > 10: 
        break
    print(num, end=' ') 
    count += 1