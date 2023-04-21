def main(csvfile, region):
    # Open the CSV file and read its contents
    with open(csvfile, 'r') as f:
        contents = f.readlines()

    # Get the header row of the CSV file which is the first row
    header = contents[0].strip().split(',')

    # Get the index of columns required for calculations
    name_index = header.index('Name')
    population_index = header.index('Population(2020)')
    net_change_index = header.index('Net Change')
    land_area_index = header.index('Land Area')
    regions_index = header.index('Regions')

    # # Extract the rows for the input region with positive net change

    rows = []
    for row in contents[1:]:
        data = row.strip().split(',')
        if data[regions_index] == region and float(data[net_change_index]) > 0:
            rows.append(data)
    rows2 = []
    for row in contents[1:]:
        data = row.strip().split(',')
        if data[regions_index] == region:
            rows2.append(data)
    # Task 1: Find country with minimum and maximum population in the input region
    min_pop = float("inf")
    max_pop = 0
    min_pop_country = ''
    max_pop_country = ''

    for row in rows:
        population = float(row[population_index])
        if population < min_pop:
            min_pop = population
            min_pop_country = row[name_index]
        if population > max_pop:
            max_pop = population
            max_pop_country = row[name_index]

    MaximumMinimum = [max_pop_country, min_pop_country]

    # Task 2: Calculate average and standard deviation of population in the input region
    # population_list = [float(row[population_index]) for row in rows]

    population_list = []
    for row in rows2:
        population = float(row[population_index])
        population_list.append(population)

    population_average = sum(population_list) / len(population_list)

    population_variance = sum((population - population_average) ** 2 for population in population_list) / (len(
        population_list) - 1)
    population_stddev = population_variance ** 0.5

    StandardDeviationAverage = [round(population_average, 4), round(population_stddev, 4)]

    # Task 3: Calculate density of population for each country in the input region
    result3 = []
    for row in rows:
        population = float(row[population_index])
        area = float(row[land_area_index])
        density = population / area
        result3.append([row[name_index], round(density, 4)])

    def sort_desending_density(x):
        return x[1]

    result3 = sorted(result3, key=sort_desending_density, reverse=True)

    # Task 4: Calculate correlation between population and land area for all countries in the input region

    population_list = []
    area_list = []
    for row in rows2:
        population_list.append(float(row[population_index]))
        area_list.append(float(row[land_area_index]))

    n = len(rows2)

    if n == 0:
        return [], [], [], 0

    population_average = sum(population_list) / n
    area_average = sum(area_list) / n

    # numerator = sum((population_list[i] - population_average) * (area_list[i] - area_average) for i in range(n))
    numerator = 0
    for i in range(n):
        numerator += (population_list[i] - population_average) * (area_list[i] - area_average)

    denominator = ((sum((population_list[i] - population_average) ** 2 for i in range(n))) * (
        sum((area_list[i] - area_average) ** 2 for i in range(n)))) ** 0.5

    if denominator == 0:
        return [], [], [], 0

    result4 = round(numerator / denominator, 4)

    return MaximumMinimum, StandardDeviationAverage, result3, result4


# You can use below line of code in python shell and then see individual results for MaxMin, and all just like sample given in assignment description
# MaxMin, stdvAverage, density, corr = main("countries.csv", "Africa")


