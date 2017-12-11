ipAddress = input("Please enter the IP address: ")
segmentNmb = 1
segmentLength = 0
dot = "."

if ipAddress[-1] != dot:
    ipAddress += dot

# we define a segment as somethin that ends with a "."
# we increase segment count at the end of the segment
for char in ipAddress:
    if char == dot:
        print("segment {} contains {} charachters".format(segmentNmb, segmentLength))
        segmentNmb += 1
        segmentLength = 0
    else:
        segmentLength += 1