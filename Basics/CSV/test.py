import csv

profiles_read = open("./profiles.csv", mode="r", newline="")
profiles_write = open("./profiles_new.csv", mode="a", newline="")

profiles_reader = csv.reader(profiles_read, delimiter=',')
profiles_writer = csv.writer(profiles_write)

next(profiles_reader)

profiles_writer.writerow([])

for line in profiles_reader:
    x = len(line)
    liste = []
    for _ in range(0, int(x)):
        print(line[_])
        liste.append(line[_])
    profiles_writer.writerow([liste[1], liste[0], "David", "@test",
                              "923781738", "Lel-Strasse 1", "87378", "Heidelberg", "DE"])
    liste.clear()
