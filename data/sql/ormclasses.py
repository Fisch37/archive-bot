"""
Classes for the SQL ORM.

The classes here should also implement 
"""
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.ext.asyncio import AsyncSession

from data.sql.engine import Base, may_make_session, may_make_session_with_transaction


class Foo(Base):
    """
    This is an example ORM class.
    
    __tablename__ is always required for ORM classes
    and represents the SQL table that is connnected to it.
    
    See the SQLAlchemy ORM Documentation for more information.
    
    
    Every method on the database should make use of `may_make_session`
    in some shape or form and have an optional `session` parameter.
    (See data.sql.engine.Base)
    This way, the methods can be used in longer transactions fluently.
    """
    __tablename__ = "foo"
    
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        init=False
    )
