from at3 import converter_massa_lunar, converter_massa_marte

def test_converter_massa_lunar():
  assert converter_massa_lunar(10) == (10 / 6)

def test_converter_massa_marte():
  assert converter_massa_marte(10) == (10 * 0.378)
  