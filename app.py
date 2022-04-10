from vkbotkit import librabot
from vkbotkit.objects import decorators, filters, enums, library_module
import asyncio
import os


async def main():
    # CONFIGURATION
    bot = librabot(os.environ['VKBOTKIT_TOKEN'])
    bot.toolkit.configure_logger(enums.log_level.DEBUG, True, True)
    bot.library.import_library()

    # START POLLING 
    await bot.start_polling()


loop = asyncio.new_event_loop()
loop.run_until_complete(main())