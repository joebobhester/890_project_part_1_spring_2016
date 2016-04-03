import csv

def social_data(var):
    if var == '':
        var = 0 # assigns value of zero when not present in scraped data
    else:
        var = var.replace(',', '') # replaces commas
    return float(var) # converts string to float

def clean_social_data(fin, n):
    """ Creates a Python list with values from social data column.
    fin: file in
    n: column index
    return: list with column name as first item, followed by values
    """
    with open(fin, newline='') as csvfile_in:
        datareader = csv.reader(csvfile_in)
        title = next(datareader)[n] # gets column title, then skips headers line
        data = [title]
        for line in datareader:
            data.append(social_data(line[n]))
        return data

f = '2015_buzz_scrape_Jan.csv'

data = clean_social_data(f, 7)
data_average = sum(data[1:]) / (len(data) - 1)
print('The average of ' + data[0] + ' is ' + str(data_average))

# 154334.31003039514 average impressions for January
