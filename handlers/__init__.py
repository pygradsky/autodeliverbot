from handlers.cmds.cmd_start import router as cmd_start_router
from handlers.cmds.cmd_offers import router as cmd_offers_router

from handlers.callbacks.nitro.nitro_basic import router as callback_nitro_basic_router
from handlers.callbacks.nitro.nitro_full import router as callback_nitro_full_router
from handlers.callbacks.nitro.nitro_offer import router as callback_nitro_offer_router
from handlers.callbacks.back_to_offers import router as callback_back_to_offers_router

__all_routers__ = [
    # Commands
    cmd_start_router,
    cmd_offers_router,

    # Callbacks
    callback_nitro_offer_router,
    callback_nitro_basic_router,
    callback_nitro_full_router,
    callback_back_to_offers_router
]
