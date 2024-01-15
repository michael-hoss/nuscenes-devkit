from .nuscenes import NuScenes, NuScenesExplorer

"""
Issue around making nuscenes_devkit/python_sdk just one single bazel py_library and then letting
my own bazel targets depend on it (where I want to import and call arbitrary functions):

If I leave all __init__ files as they are, then the files in python_sdk/nuscenes/ that are not mentioned
here in python_sdk/nuscenes/__init__.py are not available for import from somewhere else.
This would exclude e.g. the dirs `eval` or `lidarseg`.

If I empty this __init__ file, then by default, only all functions from python_sdk/nuscenes/nuscenes.py
are made available for import from somewhere else (file name equal to module name).
This would also exclude e.g. the dirs `eval` or `lidarseg`.

If I explicitly specify e.g. `from . import eval` here in the __init__ file, then I get a circular dependency
because inside `eval`, `nuscenes` is already imported. Then we cannot also do it the other way round
(inside `nuscenes`, import `eval`).

This lets me question whether this approach of just making the entire nuscenes_devkit/python_sdk just one
big py_library is suitable at all. Maybe it's also not very bazel-like. If
`nuscenes_devkit/python_sdk/nuscenes/eval/tracking/evaluate.py`
is meant to be called from the CLI, then this should probably be a py_binary.
"""
