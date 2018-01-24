import csv
import json


wine_data = {}

#Opens csv file to read
with open('winemag-data-130k-v2.csv', 'r') as fp:
    
    #this splits the file into a dict stream object
    wine_stream = csv.DictReader(fp)
    
    #this iterates over the stream object inot lines
    for line_ct, wine_row_dic in enumerate(wine_stream) :
       
        """id,country,description,designation,points,price,province,region_1,region_2,taster_name,taster_twitter_handle,title,variety,winery"""
    
        
        #this builds a data object with a unique of line_ct
        wine_data.update({line_ct: wine_row_dic})
        
        #This is strictly for print to the user screen
        country = wine_row_dic['country']
        province = wine_row_dic['province']
        title = wine_row_dic['title']
        if line_ct < 10:
            print(line_ct, '-----', country, province, title)
            
#the csv file has been closed after the context manager block

            
with open('wine_report.json', 'w') as fp:
    json.dump(wine_data, fp, sort_keys=True, indent=4, separators=(',',':'))
    
print('done with file')
            
        
        


