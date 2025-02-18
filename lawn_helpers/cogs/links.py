"""
Links for the Auth bot
"""

# Third Party

# Third Party
from discord import AutocompleteContext, Embed, option
from discord.colour import Color
from discord.ext import commands

# Django
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

# Alliance Auth
from allianceauth.services.hooks import get_extension_logger

# LAWN Helpers
from lawn_helpers.models import Link

logger = get_extension_logger(__name__)


class Links(commands.Cog):
    """
    Helpful links
    """

    def __init__(self, bot):
        self.bot = bot

    async def search_links(self, ctx: AutocompleteContext):
        """Returns a list of links that begin with the characters entered so far."""
        return list(
            Link.objects.filter(name__icontains=ctx.value).values_list(
                "name", flat=True
            )[:10]
        )

    @commands.slash_command(
        pass_context=True,
        description="Display a link",
        guild_ids=[int(settings.DISCORD_GUILD_ID)],
    )
    @option("name", description="Search for a Link!", autocomplete=search_links)
    async def link(self, ctx, name: str):
        """
        Display a link
        """
        try:
            link1 = Link.objects.get(name=name)
            embed = Embed(title=link1.name)
            if link1.thumbnail:
                embed.set_thumbnail(url=link1.thumbnail)
            embed.colour = Color.blurple()

            embed.description = link1.description

            embed.url = link1.url

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
    bot.add_cog(Links(bot))
