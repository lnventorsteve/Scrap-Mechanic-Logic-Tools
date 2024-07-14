import time
import block_list
import sm_helpers as sm
import color_list
start = time.perf_counter()

blocks = block_list.blocks()  # list of usable blocks
objects = block_list.objects()  # list of usable objects
colors = color_list.colors()  # list of Scrap Mechanic Colors

ID = sm.ID()  # init ID class
blueprint = sm.Blueprint(ID)  # init Blueprint class

# simple pulse generator

blueprint.fill_block(blocks.Spaceship_Block,(0,0,0),(4,5,1))  # make a base

sw_xor = sm.LogicGate(blueprint, "xor", (1, 3, 1), "up", "up", colors.Blue)  # sw_xor as output and flip-flop
tick_and = sm.LogicGate(blueprint, "and", (1, 2, 1), "up", "up")  # and gate for 1 tick pulse
tick_nor = sm.LogicGate(blueprint, "nor", (1, 1, 1), "up", "up")  # nor gate for 1 tick pulse
timer = sm.Timer(blueprint, 0, 39, (2, 2, 1), "north", "up", colors.Black)  # timer to set the pulse length
button = sm.Button(blueprint, (2, 1, 1), "up", "up", colors.Green)  # button to trigger the pulse

# connections
sw_xor.connect(sw_xor)  # self wire the xor
button.connect(tick_nor)  # connect the button to tick_nor
button.connect(tick_and)  # connect the button to tick_and
tick_nor.connect(tick_and)  # connect tick_nor to the tick_and
tick_and.connect(sw_xor)  # connect tick_and to the sw_xor
tick_and.connect(timer)  # connect tick_and to the timer
timer.connect(sw_xor)  # connect timer to the sw_xor

blueprint.export_blueprint()  # save blueprint file


print(time.perf_counter()-start)
