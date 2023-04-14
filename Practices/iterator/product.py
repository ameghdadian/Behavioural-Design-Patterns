
class Product:
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def __repr__(self):
    return f"Product<" \
            f"id={self.id}," \
            f"name={self.name}>"
