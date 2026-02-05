# ruff: noqa: E402
import asyncio
import logging

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from .config import Settings

_config = Settings.get_config()

from openg2p_fastapi_common.app import Initializer as BaseInitializer
from openg2p_fastapi_common.context import app_registry, component_registry, dbengine
from openg2p_fastapi_common.utils.crypto import KeymanagerCryptoHelper
from openg2p_fastapi_partner_auth.jwt_validation_helper import JWTValidationHelper
from openg2p_spar_mapper_core.helpers import ResponseHelper, StrategyHelper
from openg2p_spar_mapper_core.services import (
    IdFaMappingValidations,
    MapperService,
    RequestValidation,
)
from openg2p_spar_models.models import (
    IdFaMapping, Strategy
)

from .controllers import MapperController

_logger = logging.getLogger(_config.logging_default_logger_name)

# Store ContextVar values in global variables to preserve across async contexts
# This is needed because ContextVar values set during module import don't transfer
# to the async event loop context used by uvicorn for handling requests
_init_dbengine = None


class ContextVarMiddleware(BaseHTTPMiddleware):
    """
    Middleware to copy ContextVar values to each request's async context.
    This is necessary because ContextVar values don't propagate between async tasks,
    and each request handler runs in its own task.
    """

    async def dispatch(self, request: Request, call_next):
        # Copy the component registry and dbengine to this request's context
        if _init_dbengine:
            dbengine.set(_init_dbengine)
        return await call_next(request)


class Initializer(BaseInitializer):
    def initialize(self, **kwargs):
        global _init_component_registry, _init_dbengine
        super().initialize()

        IdFaMappingValidations()
        RequestValidation()
        StrategyHelper()
        MapperService()
        ResponseHelper()
        JWTValidationHelper()
        KeymanagerCryptoHelper()

        # Save ContextVar values to global variables
        _init_dbengine = dbengine.get()
        _logger.info(f"Database engine initialized: {_init_dbengine is not None}")

        MapperController().post_init()

        # Add middleware to copy ContextVars to each request's context
        app = app_registry.get()
        if app:
            app.add_middleware(ContextVarMiddleware)
            _logger.info("Added ContextVarMiddleware")

    def migrate_database(self, args):
        super().migrate_database(args)

        async def migrate():
            _logger.info("Migrating database")
            await IdFaMapping.create_migrate()
            await Strategy.create_migrate()

        asyncio.run(migrate())
