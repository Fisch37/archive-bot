"""
This module is dedicated to providing converters
from one (usually more complex) type to another (simpler) type.

Converters in this module should exclusively be used by database API.
"""
import discord

def ensure_id(obj: int|discord.abc.Snowflake) -> int:
    if not isinstance(obj, int):
        return obj.id
    else:
        return obj