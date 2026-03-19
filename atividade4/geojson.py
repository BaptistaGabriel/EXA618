import json

def main():
    features = []
    input_file = 'estabelecimentos.csv'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for i, linha in enumerate(f):
            dados = linha.strip().split(None, 3)
            
            if len(dados) < 4:
                continue

            long_limpa = dados[0].replace(',', '')
            lat_limpa = dados[1].replace(',', '')

            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(long_limpa), float(lat_limpa)]
                },
                "properties": {
                    "nome": dados[3],
                    "tipo": dados[2]
                },
                "id": i
            })

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    with open('geojson.json', 'w', encoding='utf-8') as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)
        
    print("Ok")

if __name__ == '__main__':
    main()