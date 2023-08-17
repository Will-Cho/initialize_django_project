# System
from rest_framework.pagination import CursorPagination
from urllib import parse
from base64 import b64encode


class CursorPagination(CursorPagination):
    cursor_query_param = "cursor"
    page_size = 10
    ordering = "-id"
    page_size_query_param = "limit"
    max_page_size = 80

    def encode_cursor(self, cursor):
        tokens = {}
        if cursor.offset != 0:
            tokens["o"] = str(cursor.offset)
        if cursor.reverse:
            tokens["r"] = "1"
        if cursor.position is not None:
            tokens["p"] = cursor.position

        querystring = parse.urlencode(tokens, doseq=True)
        encoded = b64encode(querystring.encode("ascii")).decode("ascii")

        return encoded

    def get_paginated_response(self, data):
        return {"page": {"cursor": self.get_next_link()}, "results": data}


custom_cursor_paginator = CursorPagination()
