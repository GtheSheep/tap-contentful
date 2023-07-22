from singer_sdk.pagination import BaseOffsetPaginator


class ContentfulPaginator(BaseOffsetPaginator):

    @staticmethod
    def has_more(response):
        data = response.json()
        return data["skip"] + data["limit"] < data["total"]
