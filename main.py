import getCSV
doubanURL="https://book.douban.com/top250?start=0"
doubanURL_front="https://book.douban.com/top250?start="
doubanTree=getCSV.GetDoubanHtmlTree(doubanURL)
getCSV.GetBookName(doubanTree)
getCSV.GetBookPriceandYears(doubanTree)
BookNames,Prices,Years,Presses,Nations,Authors=getCSV.GetAllIno(doubanURL_front)