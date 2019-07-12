# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        str = f"""
            \n------------------------------
            \n{self.title}
            \n   {self.description}
            \n      {self._get_exits_string()}
            \n         {self._get_item_string()}\n"""
        return str

    def _get_item_string(self):
        return "Item(s) in Room: " + ", ".join([item.name for item in self.items])

    def _get_exits_string(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.n_to is not None:
            exits.append("s")
        if self.n_to is not None:
            exits.append("e")
        if self.n_to is not None:
            exits.append("w")
        return "Possible Exits: " + ", ".join(exits)

        # LIST COMPREHENTION
        # FORMAT // COLLECTION // CONDITION //
