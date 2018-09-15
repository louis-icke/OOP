class Crop():
  """A generic food crop."""
  #constructor
  def __init__(self,growth_rate, light_need, water_need):
    #set attributres
    self._growth = 0
    self._days_growing = 0
    self._growth_rate = growth_rate
    self._light_need = light_need
    self._water_need = water_need
    self._status = 'Seed'
    self._type = 'Generic'
    #prefixed with '_' to indicate private variable access only within class
  

new_crop = Crop(1,4,3)
print(new_crop._status)
print(new_crop._light_need)