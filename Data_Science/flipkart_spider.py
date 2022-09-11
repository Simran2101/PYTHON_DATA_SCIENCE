from dputils import scrape
import pandas

#step1. get the data as soup object
#step2. create the setup dictionaries (most important)
#step3. pass the dictionaries into the extract_many() function
#step4. repeat step1. to step3. until data keep coming
#step5. check and save data into a file

def getdata(q):
    #step1.
    pos = 1
    url = f'https:www.flipkart.com/search?q={query}&page={pos}'
    soup = scrape.get_webpage_data(url)

#step2.
#target dict, items dict, etc






#step3.
data = scrape.extract_many(soup, target=t, )










#use
laptops = getdata('laptops')
pd.DataFrame(laptops).to_csv('laptop_data.csv')