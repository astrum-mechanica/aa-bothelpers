"""
AUTH COMMANDS
"""

# Third Party
from aadiscordbot.app_settings import get_all_servers, get_site_url
from discord import AutocompleteContext, Embed
from discord.colour import Color
from discord.commands import option
from discord.ext import commands

# Django
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

# Alliance Auth
from allianceauth.services.hooks import get_extension_logger

# Bot Helpers
from bothelpers.models import Link

logger = get_extension_logger(__name__)


class Auth(commands.Cog):
    """Auth Commands"""

    def __init__(self, bot):
        self.bot = bot

    async def search_auth_links(self, ctx: AutocompleteContext):
        """Returns a list of links that begin with the characters entered so far."""
        return list(
            Link.objects.filter(auth=True, name__icontains=ctx.value).values_list(
                "name", flat=True
            )[:10]
        )

    @commands.slash_command(
        pass_context=True,
        description="Display an auth link",
        guild_ids=get_all_servers(),
    )
    @option("name", description="Search for a Link!", autocomplete=search_auth_links)
    async def auth(self, ctx, name: str = None):
        """
        Display a link
        """
        if not name:
            # returns a link to home
            embed = Embed(title=settings.SITE_NAME + " Auth")
            if ctx.guild.icon:
                embed.set_thumbnail(url=ctx.guild.icon.url)
            embed.colour = Color.blurple()

            embed.description = (
                "All Authentication functions for "
                + settings.SITE_NAME
                + " are handled through our Auth."
            )

            url = get_site_url()

            embed.url = url

            return await ctx.respond(embed=embed)
        try:
            link = Link.objects.get(name=name)
            embed = Embed(title=link.name)
            if link.thumbnail:
                embed.set_thumbnail(url=link.thumbnail)
            embed.colour = Color.blurple()

            embed.description = link.description

            embed.url = link.url

            return await ctx.respond(embed=embed)
        except Link.DoesNotExist:
            return await ctx.respond(
                f"Link **{name}** does not exist in our Auth system"
            )
        except ObjectDoesNotExist:
            return await ctx.respond(f"**{name}** is does not exist")


def setup(bot):
    """
    Load the cog
    """

    bot.add_cog(Auth(bot))
