ipAddress = input("Please enter the IP address: ")
nmbSegments = 0
segmentLength = 0
dot = "."

# we increase segment count at the end of the segment
for i in range(0, len(ipAddress)):
    char = ipAddress[i]
    if i == len(ipAddress) - 1:
        if char != dot:
            segmentLength += 1
            nmbSegments += 1
        else:
            if segmentLength > 0:
                nmbSegments += 1

        if nmbSegments > 0:
            print("Segment number: {0}, segment length: {1}".format(nmbSegments, segmentLength))
    else:
        if char != dot:
            segmentLength += 1
        else:
            if segmentLength > 0:  # closing dot
                nmbSegments += 1
                # restart segment length
                print("Segment number: {0}, segment length: {1}".format(nmbSegments, segmentLength))
                segmentLength = 0

print("Total number of segments: {0}".format(nmbSegments))