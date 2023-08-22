import xml.etree.ElementTree as ET
tree = ET.parse('movie.xml') #parse the moviw.xml file
root = tree.getroot()
for child in root.iter('movie'): # for is created to list all the child tag ineach movie
    print(child.tag, child.attrib)
    for description in root.iter('description'): 
        print(''.join(description.itertext()))
    favourite_count = 0 # variable created to count to the number of the fav
not_fav_count = 0 # variable created to count to the number of the not fav

for movie in root.iter('movie'): # for loop is created to iterate all the movie's in root
    if 'favourite' in movie.attrib: # checking the favourite movie
        if movie.attrib['favourite'] == 'yes':
            favourite_count += 1 # counting to 1
        else:
            not_fav_count += 1 # counting to 1

print('Number of favorite movies: ', favourite_count)
print('Number of non-favorite movies: ', not_fav_count)
