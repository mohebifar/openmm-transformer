# openmm-transformer
> A cleaner way to manage custom forces in OpenMM


This project was initially created to simplify input files for running OpenMM simulations with the Buckingham nonbonded. This package comes with the buckingham force transformer by default.

## Transformers
### BuckinghamForce

Add a `BuckinghamForce` tag to your forcefield file using the following format:

```xml
<BuckinghamForce bondCutoff="3">
  <Atom type="OW" c6="0.003" c8="0.00003" c10="0.0" a="1600000.0" b="42.00" gamma="35.8967" />
  <Atom type="HW" c6="0" c8="0" c10="0" a="0.0" b="0.0" gamma="0" />
  <Atom type="MW" c6="0" c8="0" c10="0" a="0.0" b="0.0" gamma="0"/>
</BuckinghamForce>
```

Then in the simulation script use `BuckinghamTransformer` to prepare the ForceField file for OpenMM's parser:

```python
from openmm_transformer import BuckinghamTransformer
from simtk.openmm import app

with BuckinghamTransformer('my-buckingham-forcefield.xml') as b68:
  forcefield = app.ForceField(b68)
```
