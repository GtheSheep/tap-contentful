"""Stream type classes for tap-contentful."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_contentful.client import ContentfulStream


class EntriesStream(ContentfulStream):

    name = "entries"
    path = "/entries"
    primary_keys = ["id"]
    replication_key = "updated_at"
    replication_key_param = "sys.updatedAt"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("metadata", th.ObjectType(
            th.Property("tags", th.ArrayType(th.StringType))
        )),
        th.Property("sys", th.ObjectType(
            th.Property("space", th.ObjectType(
                th.Property("sys", th.ObjectType(
                    th.Property("type", th.StringType),
                    th.Property("linkType", th.StringType),
                    th.Property("id", th.StringType)
                )),
            )),
            th.Property("id", th.StringType),
            th.Property("type", th.StringType),
            th.Property("createdAt", th.DateTimeType),
            th.Property("updatedAt", th.DateTimeType),
            th.Property("environment", th.ObjectType(
                th.Property("sys", th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("linkType", th.StringType),
                ))
            )),
            th.Property("revision", th.IntegerType),
            th.Property("contentType", th.ObjectType(
                th.Property("sys", th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("linkType", th.StringType),
                ))
            )),
            th.Property("locale", th.StringType),
        )),
        th.Property("fields", th.ArrayType(th.ObjectType())),
        th.Property("updated_at", th.DateTimeType)
    ).to_dict()

    def post_process(self, row: dict, context: dict | None) -> dict | None:
        row["id"] = row["sys"]["id"]
        row["updated_at"] = row["sys"]["updatedAt"]
        return row


class ContentTypesStream(ContentfulStream):

    name = "content_types"
    path = "/content_types"
    primary_keys = ["id"]
    replication_key = "updated_at"
    replication_key_param = "sys.updatedAt"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("displayField", th.StringType),
        th.Property("name", th.StringType),
        th.Property("description", th.StringType),
        th.Property("sys", th.ObjectType(
            th.Property("space", th.ObjectType(
                th.Property("sys", th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("linkType", th.StringType)
                ))
            )),
            th.Property("id", th.StringType),
            th.Property("type", th.StringType),
            th.Property("createdAt", th.DateTimeType),
            th.Property("updatedAt", th.DateTimeType),
            th.Property("revision", th.IntegerType),
            th.Property("environment", th.ObjectType(
                th.Property("sys", th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("linkType", th.StringType)
                ))
            )),
        )),
        th.Property("fields", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("name", th.StringType),
                th.Property("type", th.StringType),
                th.Property("localized", th.BooleanType),
                th.Property("required", th.BooleanType),
                th.Property("disabled", th.BooleanType),
                th.Property("omitted", th.BooleanType),
                th.Property("linkType", th.StringType),
                th.Property("validations", th.ArrayType(th.ObjectType(
                    th.Property("linkContentType", th.ArrayType(th.StringType))
                ))),
            )
        ))
    ).to_dict()

    def post_process(self, row: dict, context: dict | None) -> dict | None:
        row["id"] = row["sys"]["id"]
        row["updated_at"] = row["sys"]["updatedAt"]
        return row
