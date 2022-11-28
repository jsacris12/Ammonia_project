# Ammonia_project
in_lmp_NH3: input file for the lammps simulation 
NH3_CHA.data: data file containing LJ parameters and and positions of Chabazite pore and ammonia molecule
checck_pos.py: code which gets the positions of all the atoms and finds the Mean Squared displacements for the nitrogen atom also can plot the a 3d graph of all the positions of the atoms. Requires a .lammpstrj file
check_mobil.py: finds the number of unique .2^3 angstrom cubes the nitrogen atom accesses. Also erquires .lammpstrj file.
converge.py: checks the energies of the system to ensure convergence
