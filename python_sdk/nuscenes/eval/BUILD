py_library(
    name = "nuscenes_eval",
    srcs = glob(["**/*.py"]),  # maybe actually this is not enough because these files include files on a higher level
    deps = [],
    visibility = ["//visibility:public"],
    imports = [
        "third_party/nuscenes_devkit/python_sdk"  # yes, this is the directory I want to have in my PYTHONPATH
    ]
)
