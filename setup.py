"""C extension build configuration for probert (libnl bindings)."""

import subprocess

from setuptools import Extension, setup


def pkgconfig(package):
    return {
        "extra_compile_args": subprocess.check_output(
            ["pkg-config", "--cflags", package]
        ).decode("utf8").split(),
        "extra_link_args": subprocess.check_output(
            ["pkg-config", "--libs", package]
        ).decode("utf8").split(),
    }


setup(
    ext_modules=[
        Extension(
            "probert._rtnetlink",
            ["probert/_rtnetlinkmodule.c"],
            **pkgconfig("libnl-route-3.0"),
        ),
        Extension(
            "probert._nl80211",
            ["probert/_nl80211module.c"],
            **pkgconfig("libnl-genl-3.0"),
        ),
    ],
)
