py_library(
    name = "nuscenes_format",
    srcs = [
        "nuscenes_format.py",
        "nuscenes_format_utils.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//python-sdk/nuscenes/utils/geometry",
    ],
)

py_test(
    name = "nuscenes_format_test",
    srcs = ["nuscenes_format_test.py"],
    visibility = ["//visibility:public"],
    deps = [
        ":nuscenes_format",
    ],
    imports = ["../../../.."], # add this to PYTHONPATH, relative to this BUILD file
)

py_binary(
    name = "evaluate_tracking",
    srcs = ["evaluate_tracking.py"],
    visibility = ["//visibility:public"],
    deps = [
        ":nuscenes_format",
        "//python-sdk/nuscenes/eval/tracking:evaluate",
    ],
)

py_test(
    name = "evaluate_tracking_unit_test",
    srcs = ["evaluate_tracking_unit_test.py"],
    visibility = ["//visibility:public"],
    deps = [
        ":evaluate_tracking",
        ":nuscenes_format",
    ],
    imports = ["../../../.."], # add this to PYTHONPATH, relative to this BUILD file
)
