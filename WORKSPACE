# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "cdf6b84084aad8f10bf20b46b77cb5930314bf5ad4b13ee4d0c922ad6b1d0eb",
    strip_prefix = "rules_python-0.21.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.21.0/rules_python-0.21.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python3_12",
    python_version = "3.12",
)

# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.