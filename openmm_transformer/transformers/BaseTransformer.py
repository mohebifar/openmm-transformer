import os
from ..utilities.prepare_expression import prepare
import xml.etree.ElementTree as ET
try:
  from StringIO import StringIO
except ImportError:
  from io import StringIO

EXPRESSIONS_PATH = os.path.realpath(
    os.path.join(
        os.path.realpath(os.path.dirname(__file__)), '..', 'expressions'
    )
)


class BaseTransformer(StringIO):
  def __init__(self, src_xml_file):
    StringIO.__init__(self)
    self.src_xml_file = src_xml_file
    self.parameters = []
    self.tree = ET.parse(src_xml_file)

  def load_energy(self, energy_file):
    normalized_path = energy_file
    if not os.path.exists(energy_file):
      normalized_path = os.path.join(EXPRESSIONS_PATH, energy_file)
    self.energy_file_path = normalized_path

    with open(normalized_path, 'r') as energy_expression_f:
      energy_expression = energy_expression_f.read()
      corrected_energy_expression = prepare(energy_expression)
      self.energy_expression = corrected_energy_expression

  def define_parameter(self, parameter_name, parameter_type, parameter_normalizer=lambda x: x):
    self.parameters.append({
        'name': parameter_name,
        'type': parameter_type,
        'normalizer': parameter_normalizer
    })

  def find_parameter(self, parameter_name, parameter_type):
    try:
      return next(item for item in self.parameters if item['name'] == parameter_name and item['type'] == parameter_type)
    except StopIteration:
      return None

  def generate(self):
    self.tree.write(self, encoding="unicode")
    self.seek(0)
