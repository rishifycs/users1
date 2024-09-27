import xml.etree.ElementTree as ET
import csv

def parse_xml_to_csv(xml_text, csv_file_path):
    # Parse the XML text
    root = ET.fromstring(xml_text)
    # Open a CSV file for writing
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        # Extract column headers from the first XML item
        headers = [child.tag for child in root[0]]
        writer.writerow(headers)
        for item in root:
            row = [child.text for child in item]
            writer.writerow(row)
# Sample XML data (can be replaced with your actual XML)
xml_data = """<data>
  <item>
    <name>sunny</name>
    <age>30</age>
    <city>Mumbai</city>
    <country>India</country>
  </item>
  <item>
    <name>Shivam</name>
    <age>25</age>
    <city>Delhi</city>
    <country>India</country>
  </item>
</data>"""

# Call the function to parse XML and save it to CSV
csv_file_path = 'output.csv'
parse_xml_to_csv(xml_data, csv_file_path)

print(f"Data successfully saved to {csv_file_path}")
