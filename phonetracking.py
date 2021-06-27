# pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder, carrier
# Change phone_number with your phone number with country code
number = phonenumbers.parse(phone_number)
print(geocoder.description_for_number(number, 'en'))
print(carrier.name_for_number(number, 'en'))