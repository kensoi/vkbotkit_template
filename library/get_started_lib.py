from vkbotkit.objects import decorators, filters, enums, library_module


HELLO_ME = """
Hello, world
Programmed to work and not to feel
Not even sure that this is real
"""


class Main(library_module):
    @decorators.callback(filters.whichUpdate({enums.events.message_new,}))
    async def send_hello(self, package):
        await package.toolkit.send_reply(package, HELLO_ME)