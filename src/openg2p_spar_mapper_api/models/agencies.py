
from openg2p_fastapi_common.models import BaseORMModelWithTimes
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import UniqueConstraint

class Agencies(BaseORMModelWithTimes):
    __tablename__ = "agencies"

    name: Mapped[str] = mapped_column(String(), index=True, unique=True)
    mnemonic: Mapped[str] = mapped_column(String(), index=True, unique=True)

class BenefitCodeForAgency(BaseORMModelWithTimes):
    __tablename__ = "benefit_code_for_agency"
    __table_args__ = (
        UniqueConstraint("agency_id", "benefit_code_id", name="uq_agency_benefit_code"),
    )

    agency_id: Mapped[int] = mapped_column(Integer())
    benefit_code_id: Mapped[str] = mapped_column(Integer())


    
class BenefitClassificationCodeForAgency(BaseORMModelWithTimes):
    __tablename__ = "benefit_classification_code_for_agency"
    __table_args__ = (
        UniqueConstraint(
            "agency_id", "benefit_classification_code_id", name="uq_agency_benefit_classification_code"
        ),
    )

    agency_id: Mapped[int] = mapped_column(Integer())
    benefit_classification_code_id: Mapped[str] = mapped_column(Integer())