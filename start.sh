export FLASK_DEBUG=1
export FLASK_APP=web_filter_app.py
export FILTER_RULES_JSON="[{\"name\":\"find_Luke\",\"type\":\"contains_text\",\"fields\":{\"name\":\"Luk\"}}]"
flask run
