from color_generator import hex_shades
from color_generator import shade_bounds

# tests
assert isinstance(hex_shades("#eeeeee", 5), list), "hex = #eeeeee and num_shades = 5 did not produce a list"
assert isinstance(hex_shades("#eee", 19), list), "hex = #eee and num_shades = 19 did not produce a list"
assert isinstance(hex_shades("e94297", 5), list), "hex = #e94297 and num_shades = 5 did not produce a list"
assert hex_shades("e94297", 'abc')[0:5] == "error", "non-numeric value for num_shades accepted"
assert hex_shades("e94297", 5.3)[0:5] == "error", "float num_shades value accepted"
assert hex_shades("e94297", -5)[0:5] == "error", "negative num_shades value accepted"
assert hex_shades("zzzzzz", 5)[0:5] == "error", "non-hex value accepted"
assert hex_shades("#", -5)[0:5] == "error", "non-hex value accepted"
assert hex_shades(123456, 4)[0:5] == "error", "non-string value accepted"

for i in range(1, 20):
	#print "testing num_shades = %s..." % i
	num = len(hex_shades("e94297", i))
	assert num-i==0, "ER: num_shades=%s, AR: num_shades=%s" % (i, num)

print "all tests passed!"

# shade_bounds tests
for i in range (1, 20):
	result = shade_bounds(i)
	assert result[0] > 0, "ER: start_index is greater than zero, AR: start_index = %s" % (result[0])
	assert result[1] < 21, "ER: end_index less than max, AR: end_index = %s" % (result[1])
	assert result[2] == 1 or result[2] == 2, "ER: step is 1 or 2; AR: step = %s" % (result[2])