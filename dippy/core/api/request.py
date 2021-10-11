from __future__ import annotations as _
from dippy.core.model.fields import Field as _Field
from dippy.core.model.data_models import DataModel as _DataModel
from dippy.core.model.models import Model as _Model
from dippy.core.model.metadata import MetadataProtocol as _MetadataProtocol
from dippy.core.sentinel import Sentinel as _Sentinel
from typing import Any as _Any, Optional as _Optional


NOTSET = _Sentinel("NOTSET")


class JSONArgField(_Field):
    ...


class QueryArgField(_Field):
    ...


class URLArgField(_Field):
    ...


class RequestModel(_DataModel):
    endpoint: str
    method: str
    model: _Optional[_Model] = None

    def _load_fields(self, *args, **kwargs) -> dict[str, _Any]:
        return {
            **self._get_field_args(JSONArgField, args, kwargs),
            **self._get_field_args(QueryArgField, args, kwargs),
            **self._get_field_args(URLArgField, args, kwargs, allow_positional=True),
        }

    @property
    def json_args(self: _MetadataProtocol) -> dict[str, _Any]:
        return self.__dippy_metadata__.get_for(self, JSONArgField)

    @property
    def query_args(self: _MetadataProtocol) -> dict[str, _Any]:
        return self.__dippy_metadata__.get_for(self, QueryArgField)

    @property
    def url_args(self: _MetadataProtocol) -> dict[str, _Any]:
        return self.__dippy_metadata__.get_for(self, URLArgField)

