import csv

def csv_to_list(x):
    """
    converts csv string to a list
    """
    start = 0
    k_end = x.find(', ', start)
    row = []
    while k_end >= 0:
        k = x[start: k_end]
        row.append(k)
        start = k_end + 2
        k_end = x.find(', ', start)
    k = x[start: len(x)]
    row.append(k)
    return(row)

def get_tags(fin):
    """ Creates a Python dictionary with values from tags column.
    fin: file in
    return: dictionary with counts for each tag
    """
    with open(fin, newline='') as csvfile_in:
        datareader = csv.reader(csvfile_in)
        data = dict()
        for line in datareader:
            tag_list = line[4]
            tags = csv_to_list(tag_list[1:-1])
            for tag in tags:
                data[tag[1:-1]] = data.get(tag[1:-1], 0) + 1
        return data

f = '2015_buzz_scrape_Jan.csv'

data = get_tags(f)
print(data)
