from xml.dom.minidom import parse
import time

start_time = time.time()
dom = parse("map.osm")
nodes = dom.getElementsByTagName("node")
count = 0

print("Starting DOM Parser...")
for node in nodes:
    lat = node.getAttribute("lat")
    lon = node.getAttribute("lon")
    nome = None
    tipo = None
    
    tags = node.getElementsByTagName("tag")
    for tag in tags:
        k = tag.getAttribute("k")
        v = tag.getAttribute("v")
        if k == "name":
            nome = v
        if k in ["amenity", "shop"]:
            tipo = v
            
    if lat and lon and nome and tipo:
        print(f"Lat: {lat}, Lgt: {lon}, Tipo: {tipo}, Nome: {nome}")
        count += 1

end_time = time.time()
print(f"\nDOM: {count} estabelecimentos encontrados.")
print(f"Tempo DOM: {end_time - start_time:.4f}s")