from flask import Flask, jsonify
from elasticsearch import Elasticsearch

# Instancier le client Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port':9200, 'scheme':'http'}])

# Instancier l'application Flask
app = Flask(__name__)

# Route pour afficher les documents de l'index "notes"
@app.route('/notes')
def get_notes():
    # Rechercher tous les documents dans l'index "notes"
    response = es.search(index="notes2", body={"query": {"match_all": {}}})

    # Récupérer les documents à partir de la réponse
    documents = response['hits']['hits']

    # Créer une liste pour stocker les données des documents
    data = []

    # Parcourir les documents et ajouter leurs données à la liste
    for doc in documents:
        data.append(doc['_source'])

    # Retourner les données au format JSON
    return jsonify(data)

# Exécuter l'application Flask
if __name__ == '__main__':
    app.run()
