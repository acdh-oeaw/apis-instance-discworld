#!/bin/sh
#
poetry run ./manage.py dumpdata apis_ontology apis_relations apis_metainfo --indent=2 --natural-foreign
