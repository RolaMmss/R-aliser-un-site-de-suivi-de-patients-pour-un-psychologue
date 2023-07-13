#!/bin/bash

curl -X PUT 'http://0.0.0.0:9200/notes2' -H 'Content-Type: application/json' -d '
{
  "mappings": {
    "properties": {
      "patient_lastname": {
        "type": "keyword"
      },
      "patient_firstname": {
        "type": "keyword"
      },
      "text": {
        "type": "text",
        "analyzer": "standard"
      },
      "date": {
        "type": "date"
      },
      "patient_left": {
        "type": "boolean"
      },
      "emotion": {
        "type": "keyword"
      },
      "confidence": {
        "type": "float"
      }
    } 
  }
}'

# to see all my indices:
# http://localhost:9200/_cat/indices?v




curl -X PUT "localhost:9200/notes" -H 'Content-Type: application/json' -d'
{
  "index.blocks.read_only_allow_delete": null,
  "index.blocks.read_only": false
}
'
