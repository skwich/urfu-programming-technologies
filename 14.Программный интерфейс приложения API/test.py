import requests
import pandas as pd
import xml.etree.ElementTree as ET

# http://127.0.0.1:8000/scripts/XML_daily.asp?date_req=01/01/2003
BASE_URL = "http://127.0.0.1:8000/scripts/XML_daily.asp"
param = "date_req"

year = 2003
month = 1
response = requests.get(f"{BASE_URL}?{param}=01/{month:02}/{year}")
# df = pd.read_xml(response.text)
tree = ET.ElementTree(ET.fromstring(response.text))
raise Exception(f"{tree.getroot().iter()[0].attrib['Date']}")

