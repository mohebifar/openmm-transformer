import math
import xml.etree.ElementTree as ET
from .BaseTransformer import BaseTransformer


class BuckinghamTransformer(BaseTransformer):
  def __init__(self, src_xml_file):
    BaseTransformer.__init__(self, src_xml_file)
    self.load_energy('buckingham_energy')
    self.define_parameter('a', 'PerParticleParameter', math.sqrt)
    self.define_parameter('b', 'PerParticleParameter', math.sqrt)
    self.define_parameter('c6', 'PerParticleParameter', math.sqrt)
    self.define_parameter('c8', 'PerParticleParameter', math.sqrt)
    self.define_parameter('c10', 'PerParticleParameter', math.sqrt)
    self.define_parameter('gamma', 'PerParticleParameter', lambda x: x/2)
    self.transform()
    self.generate()

  def transform(self):
    for elem in self.tree.findall('BuckinghamForce'):
      elem.tag = 'CustomNonbondedForce'
      elem.attrib['energy'] = self.energy_expression

      for param_elem in elem.findall('Atom'):
        for attr in param_elem.attrib:
          current_param = self.find_parameter(attr, 'PerParticleParameter')
          if current_param is None:
            continue
          value = float(param_elem.attrib[attr])
          normalize = current_param['normalizer']
          param_elem.attrib[attr] = str(normalize(value))

      for parameter in self.parameters:
        def_elem = ET.SubElement(elem, parameter['type'])
        def_elem.attrib['name'] = parameter['name']
