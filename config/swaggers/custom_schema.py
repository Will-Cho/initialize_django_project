# System
from drf_yasg.inspectors import SwaggerAutoSchema
from collections import OrderedDict


class CustomSwaggerAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        """
        Get tags with the value of the swagger_tags in the ViewSet.
        Source: lib/python3.6/site-packages/drf_yasg/inspectors/view.py:377
        """
        tags = self.overrides.get("tags", None) or getattr(self.view, "swagger_tags", [])
        if not tags:
            tags = [operation_keys[0]]

        return tags

    def split_summary_from_description(self, description):
        """
        Replace the summary with the first line of the description.
        Source: lib/python3.6/site-packages/drf_yasg/inspectors/view.py:321
        """
        summary = description.split("\n")[0]
        return summary, description

    def get_response_serializers(self):
        manual_responses = self.overrides.get("responses", None) or {}
        manual_responses = OrderedDict((str(sc), resp) for sc, resp in manual_responses.items())

        responses = OrderedDict()
        if not any(self.is_success(sc) for sc in manual_responses if sc != "default"):
            responses = self.get_default_responses()

        responses.update((str(sc), resp) for sc, resp in manual_responses.items())
        return responses

    def is_success(self, code):
        code = str(code).split(" ")[0]
        return 200 <= int(code) <= 299
