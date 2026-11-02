# crystal-defect-py

This is for now specific to tetragonal material titanium beryllide TiBe12.

If a file has 101 in the title it relates to a fault on the {101} plane. If it has 211 in the title it relates to a {211} fault.

Shift in a filename means it makes the fault on the plane by shifting a particular vector.

Transform files will transform from the conventional cell to a new unit cell that has one of its faces on the fault plane type, so that you can use it in something that has a periodic unit cell like DFT or MD code.

Stretch means it will add more unfaulted structure between the faults - effectively padding the spacing between faults so you can generate cells to converge forces against fault spacing.

Castepcell means the output of this is formatted like a .cell file to go into CASTEP. Some files that don't have castepcell in the filename might also output files that are formatted like .cell, I should check (sorry).

2fault configuration means there are 2 faults within the unit cell which add up to a full conventional unit cell vector so the periodic boundaries join up. The faults are at one quarter and three quarters of the way through the unit cell.

1fault configuration means there is 1 fault across the centre which cunningly makes the unit cell boundary that's parallel to the fault into a second fault. This only works because the chosen displacement vector is half a conventional cell vector! You can't use this  hack if it isn't.

