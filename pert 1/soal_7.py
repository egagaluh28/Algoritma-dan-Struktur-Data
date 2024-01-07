#Muhammmad Galuh Gumelar
#J0403221017

dishes=["pizza","sauerkraut","paelia","hambuerger"]
#4 type data list 
countries=["italy","germany","spain","USA","switzerland"]
#5 type data list 
country_specialities=list(zip(countries, dishes))
#mengembalikan 2 data list dengan method zip
print(country_specialities)
#print country_specialities
country_specialities_dict=dict(country_specialities)
#mengubah data list menjadi data koleksi dictionary
print(country_specialities_dict)
#data liat yang diubah menjadi data kolektif dictionary