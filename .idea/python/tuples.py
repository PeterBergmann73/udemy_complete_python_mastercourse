# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

# imelda = "More Mayhem", "Emilda May", 2011
# metallica  ="Ride the Lightning", "Metallica", 1984
#
# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# # metallica[0] = "Master of Puppets"
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)
#
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)


# imelda = "More Mayhem", "Imelda May", 2011, (
#     [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])
#
# track_index = 3
#
# title, artist, year, tracks = imelda
#
# for i in range(0, len(imelda)):
#     if (i != track_index):
#         print(imelda[i])
#     else:
#         for song in tracks:
#             track, title = song
#             print("\tTrack number {}, Title: {}".format(track, title))
#

imelda = "More Mayhem", "Imelda May", 2011, (
     [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

print(imelda)

imelda[3].append((5, "All For You"))

title, artist, year, tracks = imelda

tracks.append((6, "Eternity"))

print(title)
print(artist)
print(year)

for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))


