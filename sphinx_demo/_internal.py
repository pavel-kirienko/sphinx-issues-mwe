import dataclasses

#: This entity is ignored by autodoc.
DATA_ENTITY = {'abc', 'def'}


class Entity:
    pass


class DerivedEntity(Entity):
    """
    The base class is not hyper-linked.
    """

    @property
    def prop(self) -> int:
        """
        This property is type-annotated, but the type information is discarded by autodoc.
        """
        return 123

    def where_is_the_type_information(self, *args: Entity) -> Entity:
        """
        The argument is type-annotated as ``*args: Entity``, but the annotation is discarded by autodoc.
        """
        pass


@dataclasses.dataclass
class MyDataclass:
    # This field will not be documented unless I added a doc comment despite :undoc-members:
    undocumented_field: int

    #: This field is documented.
    well_documented_field: int
