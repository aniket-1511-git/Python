'''
The “North” kingdom and the “South” kingdom both keep ledgers of gold reserves. Suddenly, there’s a war—when they merge, the South’s gold value should overwrite the North’s wherever the city names match! What do the ledgers look like after the kingdoms unite?
Input: north = {'Winterfell': 1000, 'The Eyrie': 800}, south = {'The Eyrie': 1200, "King's Landing": 2500}
Expected Output: {'Winterfell': 1000, 'The Eyrie': 1200, "King's Landing": 2500}
'''
north = {'Winterfell': 1000, 'The Eyrie': 800}
south = {'The Eyrie': 1200, "King's Landing": 2500}
north_south=north|south
print(north_south)
