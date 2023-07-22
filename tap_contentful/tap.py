"""Contentful tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_contentful import streams


class TapContentful(Tap):
    """Contentful tap class."""

    name = "tap-contentful"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "space_id",
            th.StringType,
            required=True,
            description="Space ID to replicate",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.ContentfulStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.EntriesStream(self),
        ]


if __name__ == "__main__":
    TapContentful.cli()
