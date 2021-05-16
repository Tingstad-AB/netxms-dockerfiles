import os
import gitlab
import json

return_object = dict()

try:
    gitlab = gitlab.Gitlab('http://gitlab.com', job_token=os.environ['CI_JOB_TOKEN'])
except KeyError:
    gitlab = gitlab.Gitlab('http://gitlab.com', private_token=os.environ['PRIVATE_TOKEN'])

project = gitlab.projects.get(int(os.environ['PROJECT_ID']))

image_registry = project.repositories.list()
for registry in image_registry:
    return_object.update({
        registry.path : {
            "tags" : list()
        },
    })
    for tag in registry.tags.list():
        sliced_version = tag.name.split("-")
        try:
            for index, slice in enumerate(sliced_version):
                sliced_version[index] = int(slice)
        except Exception:
            break
        tag.name = tag.name.replace("-", ".")
        return_object[registry.path]["tags"].append(tag.name)

with open('container_registry_tags.json', 'w') as output:
    json.dump(return_object, output)
