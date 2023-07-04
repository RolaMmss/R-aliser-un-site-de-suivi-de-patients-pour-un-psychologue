#!/bin/bash

curl -X PUT 'http://127.17.0.1:9200/notes2' -H 'Content-Type: application/json' -d '
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
}
'

