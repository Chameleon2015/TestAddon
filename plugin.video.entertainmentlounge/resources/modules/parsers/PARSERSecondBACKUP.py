import urllib2, re
#from resources.modules import modules
from bs4 import BeautifulSoup

ART = 'http://chameleon.x10host.com/test/ELicons/'
BaseUrl = 'http://chameleon.x10host.com/test/links/newtest/?list='
#-------------------------------------------------------------------------------------
def Categories(url):
    
    OpenURL = urllib2.urlopen(BaseUrl+url)
    soup = BeautifulSoup(OpenURL)
    OpenURL.close()

    GetCategories = soup.find_all('div', {'id': 'CategorySection'})    
    for category in GetCategories:

        CatData = []

        GetCategoryTitle = category.find_all('title', {'class': 'Category'})
        for title in GetCategoryTitle:
            title = re.findall(r'<title class="Category">(.*?)</title>',str(title))
            for Title in title:
                CatData.append(Title)


        Icon = category.find_all('a', {'class': 'CategoryIcon'})
        for icon in Icon:
            icon = re.findall(r'<a class="CategoryIcon">(.*?)</a>',str(icon))
            for Icon in icon:
                CatData.append(Icon)
                
        Fanart = category.find_all('a', {'class': 'CategoryFanart'})
        for fanart in Fanart:
            fanart = re.findall(r'<a class="CategoryFanart">(.*?)</a>',str(fanart))
            for Fanart in fanart:
                CatData.append(Fanart)
        
        category = CatData[0]
        icon = CatData[1]
        fanart = CatData[2]
        #modules.addDir(category,BaseUrl+category,34,ART+icon,ART+fanart,'')
    
    #modules.AUTO_VIEW('500')


def Category(name, url):
    
    OpenURL = urllib2.urlopen(url)
    soup = BeautifulSoup(OpenURL)
    OpenURL.close()
    GetCategory = soup.find_all('div', {'class': name})

    for item in GetCategory:
        GetItem = item.find_all('div', {'class': 'Online'})
        for item in GetItem:
            DataList = []
            UrlList = []
            
            GetTitle = item.find_all('title', {'class': 'Name'})
            for title in GetTitle:
                title = re.findall(r'<title class="Name">(.*?)</title>',str(title))
                for Title in title:
                    DataList.append(Title)
            
            
            GetUrl = item.find_all('a', {'class': 'Link'})
            for link in GetUrl:
                link1 = re.findall(r'<a class="Url">(.*?)</a>',str(link))
                print 'Link String'
                print link1
                for Link1 in link1:
                    print 'Link Before Append'
                    print Link1
                    UrlList.append(Link1)
            
            
            
            
            

            GetMode = item.find_all('title', {'class': 'Mode'})
            for mode in GetMode:
                mode = re.findall(r'<title class="Mode">(.*?)</title>',str(mode))
                for Mode in mode:
                    DataList.append(Mode)
                    
            GetIcon = item.find_all('a', {'class': 'Icon'})
            for icon in GetIcon:
                icon = re.findall(r'<a class="Icon">(.*?)</a>',str(icon))
                for Icon in icon:
                    DataList.append(Icon)
            
            GetFanart = item.find_all('a', {'class': 'Fanart'})
            for fanart in GetFanart:
                fanart = re.findall(r'<a class="Fanart">(.*?)</a>',str(fanart))
                for Fanart in fanart:
                    DataList.append(Fanart)
            
            GetDesc = item.find_all('p', {'class': 'Description'})
            for Desc in GetDesc:
                Description = re.findall(r'<p class="Description">(.*?)</p>',str(Desc))
                for description in Description:
                    DataList.append(description)
                
            
            
            title = DataList[0]
            #url = DataList[1]
            mode = int(DataList[1])
            icon = DataList[2]
            fanart = DataList[3]
            if len(DataList)>=5:
                    info = DataList[4]
            else:
                info = 'Sorry this description is currently unavailable'
            
            urllink = UrlList[0]

            print 'END'
            
            #modules.AddTestDir(title,urllink,mode,icon,description=info,isFolder=False, background=fanart)
            
            
    
        #modules.setView('movies', 'MAIN')

Category('Radio', BaseUrl)         
