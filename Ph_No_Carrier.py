import phonenumbers

# carrier: to know the name of
# service provider of that phone number
from phonenumbers import carrier


service_provider = phonenumbers.parse("+917903180526")
# Indian phone number example: +91**********
# Nepali phone number example: +977**********

	
# this will print the service provider name
print(carrier.name_for_number(service_provider,'en'))
