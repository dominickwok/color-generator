from color_generator import hex_shades

# tests
print hex_shades("#eeeeee", 5)
print hex_shades("#eee", 20)
print hex_shades("e94297", 5)
assert hex_shades("e94297", 'abc')[0:5] == "error", "non-numeric value for num_shades accepted"
assert hex_shades("e94297", 5.3)[0:5] == "error", "float num_shades value accepted"
assert hex_shades("e94297", -5)[0:5] == "error", "negative num_shades value accepted"
assert hex_shades("zzzzzz", 5)[0:5] == "error", "non-hex value accepted"
assert hex_shades("#", -5)[0:5] == "error", "non-hex value accepted"
assert hex_shades(123456, 4)[0:5] == "error", "non-string value accepted"

for i in range(1, 21):
	#print "testing num_shades = %s..." % i
	num = len(hex_shades("e94297", i))
	assert num-i==0, "ER: num_shades=%s, AR: num_shades=%s" % (i, num)

print "all tests passed!"