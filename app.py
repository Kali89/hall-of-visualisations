import web
 
urls = ('/', 'slider_test')
render = web.template.render('templates/')
 
app = web.application(urls, globals())

def average_price(year):
	with open('ISOCodes.txt', 'rb') as f:
		lookup_dictionary = dict((line.split(':')[1].strip('\n').strip().lower(), line.split(':')[0].strip('\n').strip()) for line in f.readlines())
	data_dictionary = {}
	with open('pp-' + str(year) + '.csv', 'rb') as f:
		lines = f.readlines()[1:]
	for line in lines:
		try:
			identifier,price,date,postcode,type_of_house,new,freehold_or_leasehold,address_1,address_2,address_3,address_4,address_5,address_6,address_7,letter = line.strip().strip('\n').split(',')
		except:
			continue
		try:
			data_dictionary[address_7.strip('"').strip().lower()].append(int(price.strip('"')))
		except:
			data_dictionary[address_7.strip('"').strip().lower()] = [int(price.strip('"'))]
	final_results = dict((lookup_dictionary[key], sum(value)/float(len(value))) for key,value in data_dictionary.iteritems() if key in lookup_dictionary)
	return final_results
			
class slider_test:
    def GET(self):
		result_dictionary = average_price(2014)
		return render.slider_test(result_dictionary)
         
    def POST(self):
		data = web.data()
		key, year = data.split('=')
		return average_price(year)
 
if __name__ == '__main__':
    app.run()
