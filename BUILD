# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.

load("@rules_python//python:defs.bzl", "py_library", "py_binary", "py_test")

py_library(
    name = "aetherforge_lib",
    srcs = glob(["src/aetherforge/*.py"]),
    visibility = ["//visibility:public"],
)

py_binary(
    name = "aetherforge_cli",
    srcs = ["src/aetherforge/cli.py"],
    deps = [":aetherforge_lib"],
)

py_test(
    name = "aetherforge_test",
    srcs = ["tests/test_aetherforge.py"],
    deps = [":aetherforge_lib"],
)

# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.