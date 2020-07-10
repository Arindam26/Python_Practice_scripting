"""Check IP Address"""
# import re
# import urllib.request
#
# print("We will try open this url,, in order to get IP Address")
#
# url = "http://www.google.com"
#
# print(url)
# request = urllib.request.urlopen(url).read()
# url_pat = re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", str(request))
# print("Your ip address is : {}".format(url_pat))
import re
import urllib.request

print("We will tyr to open this url, in order to get the IP addresses")
url = 'http://www.google.com'

print(url)

request = urllib.request.urlopen(url).read()
url_pat = re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", str(request))
print("Your IP addresses are : {}".format(url_pat))

