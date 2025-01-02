# LAWN Helpers

Alliance Auth helpers for LAWN

> **Warning**
> This is built for LAWN specifically. **If you aren't us, you probably shouldn't use this. There will be no warning of updates or changes!**

## Features

| Helper | Purpose |
| ------ | ------- |
| `none` | nothing |

## discord bot cogs

| Cog    | Description |
| ------ | ----------- |
| `none` | nothing     |

## Future features

| Cog    | Purpose |
| ------ | ------- |
| `none` | nothing |

## Install

- Ensure you have installed and configured the Alliance Auth DiscordBot, <https://apps.allianceauth.org/apps/detail/allianceauth-discordbot>
- Install the app with your venv active

```bash
pip install git+https://github.com/swashman/lawn-helpers
```

- Add `'lawn-helpers',` to your INSTALLED_APPS list in local.py.
- Add the below lines to your `local.py` settings file, adjust for which cogs you want. Settings for specific cogs are found in cog setup.
- Run migrations `python manage.py migrate`
- Gather your static files `python manage.py collectstatic` (There should be none from this app)
- Restart your auth

## Settings (local.py)

| Setting   | Default | Description |
| --------- | ------- | ----------- |
| `nothing` |         | nothing     |

## Permissions

| Perm              | Description                       |
| ----------------- | --------------------------------- |
| link.manage_links | Can manage links in the links cog |
