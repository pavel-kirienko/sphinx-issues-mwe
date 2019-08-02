"""
The members of this module are ordered incorrectly.
Autodoc is configured to keep the source ordering which is as follows:

- DATA_ENTITY
- Entity
- DerivedEntity
- MyDataclass

However, you can see that the resulting ordering is different (alphabetical).
"""

from ._internal import DATA_ENTITY as DATA_ENTITY
from ._internal import Entity as Entity
from ._internal import DerivedEntity as DerivedEntity
from ._internal import MyDataclass as MyDataclass
