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
	
def number_of_new_builds(year):
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
		new_value = 1 if new.strip('"') == "N" else 0
		try:
			data_dictionary[address_7.strip('"').strip().lower()].append(new_value)
		except:
			data_dictionary[address_7.strip('"').strip().lower()] = [new_value]
	final_results = dict((lookup_dictionary[key], sum(value)) for key,value in data_dictionary.iteritems() if key in lookup_dictionary)
	return final_results
	
def best_selling_month(year):
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
		month = int(date.strip('"').split('-')[1])
		try:
			data_dictionary[address_7.strip('"').strip().lower()][month].append(int(price.strip('"')))
		except:
			try:
				data_dictionary[address_7.strip('"').strip().lower()][month] = [int(price.strip('"'))]
			except:
				data_dictionary[address_7.strip('"').strip().lower()] = {month : [int(price.strip('"'))]}

		for region in data_dictionary.keys():
			max_checker = [(index,len(thing)) for index, thing in enumerate(data_dictionary[region].keys())]
			## Get best month for sales and for revenue
				
	return final_results
	
			
class slider_test:
    def GET(self):
		result_dictionary = number_of_new_builds(2014)
		return render.slider_test(result_dictionary)
         
    def POST(self):
		data = web.data()
		key, year = data.split('=')
		return average_price(year)
 
if __name__ == '__main__':
    app.run()
