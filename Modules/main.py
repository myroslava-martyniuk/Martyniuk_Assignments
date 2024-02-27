import csv
import sys
import package

if __name__ == '__main__':
    temp = []
    myfile = sys.argv[1]
    with open(myfile, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            temp.append(row)
        
    for dict in temp:
        reading = dict["Reading"]
        if reading[-1] == "C":
            dict["Reading"] = package.temperature.c_to_f(reading[:-3])
        elif reading[-1] == "F":
            dict["Reading"] = package.temperature.f_to_c(reading[:-3])

        distance = dict["Distance"]
        if distance[-1] == "m":
            dict["Distance"] = package.distance.m_to_f(distance[:-1])
        elif distance[-2:] == "ft":
            dict["Distance"] = package.distance.f_to_m(distance[:-2])

    with open('converted.csv', 'w') as file:
        file.write(','.join(temp[0].keys()))
        file.write('\n')
        for row in range (len(temp)):
            file.write(','.join(temp[row].values()))
            file.write('\n')
    


