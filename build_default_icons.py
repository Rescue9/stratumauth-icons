#!/usr/bin/env python3

from builder.basic_builder import BasicBuildSettings, build_basic_pack


def main():
    settings = BasicBuildSettings()
    settings.repo_url = "https://github.com/stratumauth/app.git"
    settings.png_glob = ["icons", "*.png"]
    settings.output_name = "default-icons"
    settings.pack_name = "Default Icons"
    settings.pack_description = "The default Stratum icons"
    settings.pack_url = "https://github.com/stratumauth/app"

    build_basic_pack(settings)


if __name__ == "__main__":
    main()
