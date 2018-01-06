# Filter
This is microservice accepting collection of docs as json and returning filtered collection.
Filtering rules are defined on application startup, via ENV variable: `FILTERS_JSON`. All of the documents
**matching** filters will be **removed**.

# Rules
Exemplary rules looks like that.  It should be JSON defined as collection of JSON filters.
```json
[
  {
    "name": "find_Luke",
    "type": "contains_text",
    "fields": {
      "name": "Luk"
    }
  }
]
```

# Rule types
As far there are following rule types defined:
- contains text


## contains_text
Rule is matched when field in document matches the text, case sensitive. F.e. following rule:
```json

  {
    "name": "find_Luke",
    "type": "contains_text",
    "fields": {
      "name": "Luk"
    }
  }
```
will match all documents containing field text in any place of the field name.  Following document will be matched:
```json
{
  "name": "Luke Skywalker",
  "other_field": "some text goes here"
}
```

