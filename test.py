with open('ISOCodes.txt', 'rb') as f:
	iso_dictionary = dict((line.split(':')[1].strip('\n').strip().lower(), line.split(':')[0].strip('\n').strip()) for line in f.readlines())

with open('pp-2014.csv', 'rb') as f:
	potential_counties = set([line.split(',')[-2].strip().strip('"').lower() for line in f.readlines()])

potential_iso_sets = set(iso_dictionary.keys())
print "Total found exactly is %d" % len(potential_counties.intersection(potential_iso_sets))
print "Total in potential iso is %d" % len(potential_iso_sets)
print "Total in potential countries is %d" % len(potential_counties)
print potential_counties.difference(potential_iso_sets)
#for entry in potential_counties.difference(potential_iso_sets):
	
