#------------------------------------------------------------------------------
#
# PMOS Pcell for extraction
#
# Note: The first argument is always the cellView of the subMaster.
#       All subsequent arguments should have default values and will
#       be passed by name. Each argument should be seperated by a comma
#	and whitespace.
#
#------------------------------------------------------------------------------

# Import the db wrappers
from ui import *

# The entry point. The function name *must* match the filename.
def P_PSM025(cv, ptlist=[[0,0],[1000,0],[1000,1000],[0,1000]]) :
	lib = cv.lib()
	dbu = lib.dbuPerUU()
	# Create the recognition region shape
	npts = len(ptlist)
	xpts = intarray(npts)
	ypts = intarray(npts)
	for i in range (npts) :
		xpts[i] = ptlist[i][0]
		ypts[i] = ptlist[i][1]
	# for
	cv.dbCreatePolygon(xpts, ypts, npts, TECH_Y0_LAYER);
	# Create pins
	gate_net = cv.dbCreateNet("G")
	cv.dbCreatePin("G", gate_net, DB_PIN_INPUT)
	source_net = cv.dbCreateNet("S")
	cv.dbCreatePin("S", source_net, DB_PIN_INOUT)
	drain_net = cv.dbCreateNet("D")
	cv.dbCreatePin("D", drain_net, DB_PIN_INOUT)
	bulk_net = cv.dbCreateNet("B")
	cv.dbCreatePin("B", bulk_net, DB_PIN_INPUT)

	# Update the bounding box
	cv.update()
#
