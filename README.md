# Filter
This is microservice accepting collection of docs as json and returning filtered collection.
Filtering rules are defined on application startup, via ENV variable: `FILTERS_JSON`. All of the documents
**matching** filters will be **removed**.