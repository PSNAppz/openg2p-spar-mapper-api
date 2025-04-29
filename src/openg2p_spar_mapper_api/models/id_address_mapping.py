from typing import Any, Dict, List, Optional

from openg2p_fastapi_common.context import dbengine
from openg2p_fastapi_common.models import BaseORMModelWithTimes
from sqlalchemy import JSON, String, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column


class IdAddressMapping(BaseORMModelWithTimes):
    __tablename__ = "id_address_mappings"

    id_value: Mapped[str] = mapped_column(String(), index=True, unique=True)
    address_type: Mapped[str] = mapped_column(String(), index=True)
    country: Mapped[str] = mapped_column(String(), index=True)
    province_or_state_code: Mapped[str] = mapped_column(String(), index=True)
    district_code: Mapped[str] = mapped_column(String(), index=True)
    address_line_1: Mapped[str] = mapped_column(String(), index=True)
    address_line_2: Mapped[str] = mapped_column(String(), index=True)
    post_code: Mapped[str] = mapped_column(String(), index=True)