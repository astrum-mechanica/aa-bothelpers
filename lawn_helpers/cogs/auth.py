# Third Party
from aadiscordbot.app_settings import get_site_url
from discord.colour import Color
from discord.commands import SlashCommandGroup
from discord.embeds import Embed
from discord.ext import commands

# Django
from django.conf import settings

# Alliance Auth
from allianceauth.services.hooks import get_extension_logger

logger = get_extension_logger(__name__)


class Auth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    auth_commands = SlashCommandGroup(
        "auth", "Links for the Auth", guild_ids=[int(settings.DISCORD_GUILD_ID)]
    )

    # LAWN Home
    @auth_commands.command(
        name="home",
        description="LAWN Auth",
        guild_ids=[int(settings.DISCORD_GUILD_ID)],
    )
    async def home(self, ctx):
        """
        Returns a link to the Corp Auth Home
        """
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

    # WIKI
    @auth_commands.command(
        name="wiki",
        description="Corp Wiki",
        guild_ids=[int(settings.DISCORD_GUILD_ID)],
    )
    async def wiki(self, ctx):
        """
        Returns a link to the Corp wiki page
        """

        embed = Embed(title="Corp Wiki")
        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.colour = Color.blurple()

        embed.description = "The wiki contains important Alerts, helpful information, and alliance policies."

        url = get_site_url() + "/wiki/"

        embed.url = url

        return await ctx.respond(embed=embed)

    # character audit
    @auth_commands.command(
        name="audit",
        description="Character audit",
        guild_ids=[int(settings.DISCORD_GUILD_ID)],
    )
    async def audit(self, ctx):
        """
        Returns a link to the Corp character audit page
        """

        embed = Embed(title="Character Audit")
        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.colour = Color.blurple()

        embed.description = "The character audit is what pulls in all the data for your characters. All characters owned by a member must be in this system."

        url = get_site_url() + "/audit/r/"

        embed.url = url

        return await ctx.respond(embed=embed)

    # fittings
    @auth_commands.command(
        name="fittings",
        description="Fittings and Doctrines",
        guild_ids=[int(settings.DISCORD_GUILD_ID)],
    )
    async def fittings(self, ctx):
        """
        Returns a link to the Corp fittings page
        """

        embed = Embed(title="Corp Fittings and Doctrines")
        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.colour = Color.blurple()

        embed.description = "The fittings and doctrines page lists various PVP and PVE fits used by the corp"

        url = get_site_url() + "/fittings/"

        embed.url = url

        return await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Auth(bot))
