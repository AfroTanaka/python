def better_than_average(class_points, your_points):
    # Your code here
    sumPoints = (sum(class_points)+your_points)
    print('sumPoints', sumPoints)
    avgPoints = (sumPoints) / (len(class_points)+1)
    print('avgPoints', avgPoints)
    return avgPoints < your_points

print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))