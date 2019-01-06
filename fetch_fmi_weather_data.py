
import xml.etree.ElementTree as ET
import requests



base_url = "http://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=getFeature&storedquery_id="

stored_query = "fmi::observations::weather::cities::simple" #"fmi::observations::weather::monthly::30year::simple&"

starttime = "2019-01-03T00:00:00Z"
endtime = "2019-01-04T00:00:00Z"
parameters = "Temperature"
timestep = "60"

url = "{0}{1}&starttime={2}&endtime={3}&parameters={4}&timestep={5}".format(base_url, stored_query,starttime, endtime, parameters, timestep)
print(url)

response = requests.get(url)
print("Status code: ",response.status_code)
print("Url: ", response.url)
print("Reason: ", response.reason)

data = ET.XML(response.text)
print(data.tag)
for elem in data.findall("BsWfsElement"):
   print(elem.tag, elem.attrib)
