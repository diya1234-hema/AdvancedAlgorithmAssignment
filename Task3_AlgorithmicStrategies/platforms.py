def minimum_platforms(arrival, departure):

    arrival.sort()
    departure.sort()

    platforms = 1
    max_platforms = 1

    i = 1
    j = 0

    while i < len(arrival) and j < len(departure):

        if arrival[i] <= departure[j]:

            platforms += 1
            max_platforms = max(
                max_platforms,
                platforms
            )

            i += 1

        else:

            platforms -= 1
            j += 1

    return max_platforms


# Test Code

arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]

result = minimum_platforms(
    arrival,
    departure
)

print("Minimum Platforms Required:")
print(result)