import argparse
from pymol import cmd
p=argparse.ArgumentParser()
p.add_argument("--receptor",required=True)
p.add_argument("--ligand",required=True)
p.add_argument("--output",required=True)
a=p.parse_args()
cmd.load(a.receptor,"receptor")
cmd.load(a.ligand,"ligand")
cmd.hide("everything","all")
cmd.show("cartoon","receptor")
cmd.show("sticks","ligand")
cmd.png(a.output,ray=True)
