from typing import Any, Dict, List, Optional

from openg2p_fastapi_common.context import dbengine
from openg2p_fastapi_common.models import BaseORMModelWithTimes
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class BenefitClassificationCodes(BaseORMModelWithTimes):
    __tablename__ = "benefit_classification_codes"

    benefit_classification_mnemonic: Mapped[str] = mapped_column(String(), index=True, unique=True)
    description: Mapped[str] = mapped_column(String())