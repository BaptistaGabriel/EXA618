import xml.sax
import time

class OSMHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_node = {}
        self.count = 0

    def startElement(self, tag, attributes):
        if tag == "node":
            self.current_node = {
                "lat": attributes.get("lat"),
                "lon": attributes.get("lon"),
                "nome": None,
                "tipo": None
            }
        elif tag == "tag":
            k = attributes.get("k")
            v = attributes.get("v")
            if k == "name":
                self.current_node["nome"] = v
            elif k in ["amenity", "shop"]:
                self.current_node["tipo"] = v

    def endElement(self, tag):
        if tag == "node":
            node = self.current_node
            if node["lat"] and node["lon"] and node["nome"] and node["tipo"]:
                print(f"Lat: {node['lat']}, Lgt: {node['lon']}, Tipo: {node['tipo']}, Nome: {node['nome']}")
                self.count += 1


start_time = time.time()
handler = OSMHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("map.osm")
end_time = time.time()

print(f"\nSAX: {handler.count} estabelecimentos encontrados.")
print(f"Tempo SAX: {end_time - start_time:.4f}s")