import requests,re,random,csv
from bs4 import BeautifulSoup as bs

# total items indexed
max_bikes = 0
indexed = 0
bike_data = []

# Find how many bikes are catalogued on the websites
def find_max():
    global max_bikes
    #res = requests.get('http://thebicyclechain.com/product-list/complete-list-of-availabile-bikes-ps897/')
    res = requests.get('http://thebicyclechain.com/product-list/bikes-1000/')
    soup = bs(res.text,'lxml')
    total_res = soup.select('div[class="setotalrecords"]')[0].text
    match = re.search(r"^(\d+)*",total_res)
    max_bikes = int(match.group(1))

#get information of each bike from bike's dedicated page
def get_bike_data(bikeUrl):
    global bike_data
    sku = re.search(r"(\d+)(-\d)?.htm$",bikeUrl)
    res = requests.get(bikeUrl)
    soup = bs(res.text,'lxml')
    name = soup.select('div[id="seitemdesccolleft"] span')
    if name:
        name = name[0].text.strip()
    else:
        name = "Name Not Available"
    desc = soup.select('div[id="seitemdesccolleft"] p')
    if desc:
        desc = desc[0].text.strip()
    else:
        desc = "description not available"
    rating = soup.select('span[class="prSummaryAverageRatingDecimal"]')
    if rating:
        rating = float(rating[0].text[:2])
    else:
        rating = 0.0
    price = soup.select('div[class="seregularprice"]')
    if price and price[0].text:
        price = float(price[0].text[1:6])#1:5
    else: 
        price = soup.select('div[class="sespecialprice"]')
        if(price and price[0].text):
            price = float(price[0].text[1:6])
        else:
            price = 0.0
    ctype = soup.select('div[class="sebreadcrumb secategorybreadcrumb"] a')
    #print(ctype)
    if ctype:
        ctype = ctype[4].text
    else:
        ctype = "others"
    quantity = random.randrange(10,20)
    imgpath = soup.select('div[class="seitemdetailpicture"] img[src]')
    if imgpath and imgpath[0]:
        imgpath = "http://thebicyclechain.com"+soup.select('div[class="seitemdetailpicture"] img[src]')[0].attrs['src']
    tempList = [sku.group(1),name,desc,rating,price,quantity,ctype,imgpath]
    #print(tempList)
    bike_data.append(tempList)

def walk_through_pagination():
    global indexed
    # for each paginated page
    while(indexed<max_bikes):
        res=requests.get('http://thebicyclechain.com/product-list/bikes-1000/?startRow='+str(indexed))
        if res.status_code != requests.codes.ok:
            print("res state not ok! quiting now at url: http://thebicyclechain.com/product-list/bikes-1000/?startRow="+str(indexed))
            break
        
        # parse data of interest
        soup= bs(res.text,'lxml')
        sedata = soup.select('table[class="seitemlistpagetableitemlist seitemtableleft"] tr td[class="sedata"] a')
        
        # for each bike's url, fetch individual information
        for idx, link in enumerate(sedata):
            if idx%2==0:
                print(idx,link.attrs['href'])
                try:
                    get_bike_data(link.attrs['href'])
                except ConnectionError:
                    return
                indexed+=1

#walk_through_pagination()
if __name__ == "__main__":
#    get_bike_data("http://thebicyclechain.com/product/cannondale-street-24-237900-1.htm")
    find_max()
    print(max_bikes)
    walk_through_pagination()
    with open ('scraped_data.csv','w', newline='') as file:
        writer=csv.writer(file)
        head = ['sku','name','desc','rating','price','quantity','type','image']
        writer.writerow(head)
        for row in bike_data:
            writer.writerow(row)
    print(indexed)