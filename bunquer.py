import xml.etree.ElementTree as xml
import urllib.request as http
import json

def parser():
    request = http.Request("https://api.ccma.cat/audios?version=2.0&programaradio_id=1909&format=json&items_pagina=2000",None,{"Host": "api.ccma.cat","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"})
    casos = http.urlopen(request).read()
    parsed=json.loads(casos)
    return parsed

def get_data_americana(data):
    d = data.split('/');
    return d[1]+'/'+d[0]+'/'+d[2]
    


xml.register_namespace('itunes','http://www.itunes.com/dtds/podcast-1.0.dtd')


tmp = xml.Element("rss")
tmp.set('xmlns:encoder', "java.net.URLEncoder")
tmp.set('xmlns:java', "java")
tmp.set('xmlns:ccma', "http://www.w3.org/TR/html4/")
tmp.set('version','2.0')

can = xml.SubElement(tmp,'channel')
xml.SubElement(can, 'title').text = "El búnquer - complet"
xml.SubElement(can, 'link').text = "https://www.ccma.cat/catradio/alacarta/el-bunquer/"
xml.SubElement(can, 'description').text="En Peyu, Jair Domínguez i Neus Rossell, de dilluns a divendres, a les 9 de la nit, quan ja estan cansats d'haver sigut ciutadans exemplars durant tot el dia, es reuneixen en el seu espai de confiança: una antiga de bodega que han convertit en el seu local clandestí, un lloc gairebé de recés espiritual on poden opinar lliurament de tots els temes que vulguin, sense cap mena de pressió externa."
xml.SubElement(can, 'ttl').text='61'
xml.SubElement(can, 'pubDate').text='Fri, 25 Nov 2022 09:49:59 +0200'
xml.SubElement(can, 'lastBuildDate').text = 'Fri, 24 Mar 2023 11:27:40 +0200'
xml.SubElement(can, 'language').text = 'ca-es'
xml.SubElement(can, 'copyright').text = "Corporació Catalana de Mitjans Audiovisuals, SA"
xml.SubElement(can, 'managingEditor').text = "Catalunya Ràdio"

can2 = xml.SubElement(can, 'image')
xml.SubElement(can2, 'title').text = "El búnquer"
xml.SubElement(can2, 'url').text = "https://img.ccma.cat/multimedia/jpg/0/0/1681215356200.jpg"
xml.SubElement(can2, 'link').text = 'https://www.ccma.cat/catradio/alacarta/el-bunquer/'

xml.SubElement(can, 'category').text = 'Comedy'

parsed = parser()

maxim = parsed["resposta"]["items"]["num"]
elms = parsed["resposta"]["items"]["item"]

for i in range(0,maxim):
    item=xml.SubElement(can, 'item')
    xml.SubElement(item,'title').text=elms[i]["titol"]
    xml.SubElement(item,'description').text=elms[i]["entradeta"]
    xml.SubElement(item,'pubDate').text=get_data_americana(elms[i]["data_publicacio"])
    xml.SubElement(item, '{http://ccma.cat}explicit').text='no'
    xml.SubElement(item,'enclosure', type="audio/mpeg", length="25000000", url='https://audios.ccma.cat/multimedia/'+elms[i]["audios"][0]["text"])
    xml.SubElement(item, 'guid').text='https://audios.ccma.cat/multimedia/'+elms[i]["audios"][0]["text"]
    xml.SubElement(item, '{http://www.itunes.com/dtds/podcast-1.0.dtd}duration').text=elms[i]["audios"][0]["durada"]






tree = xml.ElementTree(tmp)


var = b'<?xml version="1.0" encoding="ISO-8859-1"?> <?xml-stylesheet type="text/xsl" href="https://dinamics.ccma.cat/public/podcast/catradio/xsl/master_tmpl.xsl" version="1.0"?>\n'
f=(var + xml.tostring(tmp, encoding="ISO-8859-1", xml_declaration=False))
fitxer = open('bunquer.xml','wb')
fitxer.write(f)
fitxer.close()
#tree.write('prova.xml',xml_declaration=True, encoding="ISO-8859-1")
