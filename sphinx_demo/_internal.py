class Entity:
    pass


class DerivedEntity(Entity):    # autodoc's "show-inheritance" is enabled, the base is shown but not hyperlinked
    @property
    def prop(self) -> int:      # autodoc discards the property type information
        return 123

    def where_is_the_type_information(self, *args: Entity) -> Entity:   # autodoc discards the argument type information
        pass
