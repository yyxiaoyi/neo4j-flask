from .views import app
from .models import graph

uniqueness_constraints = {
        "User":"username",
        "Tag": "name",
        "Post": "id"
        }

for label, unique_property in uniqueness_constraints.items():
    if unique_property not in graph.schema.get_uniqueness_constraints(label):
        graph.schema.create_uniqueness_constraint(label, unique_property)
