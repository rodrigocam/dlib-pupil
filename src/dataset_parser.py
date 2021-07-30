folder_path = "/home/shammyz/Downloads/crowdpupil/"
image_path = folder_path + "images/"
annotation = folder_path + "results.csv"

header = """<?xml version='1.0' encoding='ISO-8859-1'?>
<?xml-stylesheet type='text/xsl' href='image_metadata_stylesheet.xsl'?>
<dataset>
<name>imglab dataset</name>
<comment>Created by imglab tool.</comment>
"""

with open(annotation) as file:
    output = open("annotations.xml", 'a')
    output.write(header)
    output.write("<images>\n")
    for line in file.readlines():
        image, x, y = map(str.strip, line.split(";"))
        output.write(f"<image file='{image_path + image}' witdth='1000' height='776'>\n")
        output.write(f"<box top='1' left='1' width='1000' height='776'>\n")
        output.write(f"<part name='0' x='{x}' y='{y}'/>\n")
        output.write(f"</box>\n")
        output.write("</image>\n")
    output.write("</images>\n</dataset>")
