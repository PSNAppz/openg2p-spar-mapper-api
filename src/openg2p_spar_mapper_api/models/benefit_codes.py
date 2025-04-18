from typing import Any, Dict, List, Optional

from openg2p_fastapi_common.context import dbengine
from openg2p_fastapi_common.models import BaseORMModelWithTimes
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

import enum

class BenefitTypesEnum(enum.Enum):
    CASH = "CASH"
    COMMODITY = "COMMODITY"
    SERVICE = "SERVICE"
    COMBINATION = "COMBINATION"
   


class BenefitCodes(BaseORMModelWithTimes):
    __tablename__ = "benefit_codes"

    benefit_mnemonic: Mapped[str] = mapped_column(String(), index=True, unique=True)
    benefit_type: Mapped[BenefitTypesEnum] = mapped_column(SqlEnum(BenefitTypesEnum))
    benefit_classification_id: Mapped[int] = mapped_column(Integer())
    benefit_description: Mapped[str] = mapped_column(String())
    measurement_unit: Mapped[str] = mapped_column(String())