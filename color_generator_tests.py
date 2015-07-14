from color_generator import *

# validate_input_hex tests
assert validate_input_hex("e94297")==True
assert validate_input_hex("#eee")==True
assert validate_input_hex("#eeeeee")==True
assert validate_input_hex("zzzzzzz")==False
assert validate_input_hex("#")==False
assert validate_input_hex(123456)==False
assert validate_input_hex(";asdf;lk'132923af\qwrlaskfd.,m")==False

# validate_num_shades tests
assert validate_num_shades(5)==True
assert validate_num_shades(1)==True
assert validate_num_shades(100)==True
assert validate_num_shades(0)==False
assert validate_num_shades(-5)==False
assert validate_num_shades(5.3)==False
assert validate_num_shades(-203492348)==False
assert validate_num_shades(230491340)==True
assert validate_num_shades("asdsfas")==False
assert validate_num_shades('abc')==False

# hex_to_rgb tests
assert hex_to_rgb("#237dc1") == (35, 125, 193)
assert hex_to_rgb("#3ab496") == (58, 180, 150)
assert hex_to_rgb("#836eb1") == (131, 110, 177)
assert hex_to_rgb("#000") == (0, 0, 0)
assert hex_to_rgb("#ffffff") == (255, 255, 255)

# rgb_to_hex tests
assert rgb_to_hex((35, 125, 193)) == "#237dc1"
assert rgb_to_hex((58, 180, 150)) == "#3ab496"
assert rgb_to_hex((131, 110, 177)) == "#836eb1"
assert rgb_to_hex((0, 0, 0)) == "#000000"
assert rgb_to_hex((255, 255, 255)) == "#ffffff"

# output_shades test
assert isinstance(output_shades("#eeeeee", 5), list), "hex = #eeeeee and num_shades = 5 did not produce a list"
assert isinstance(output_shades("#eee", 19), list), "hex = #eee and num_shades = 19 did not produce a list"
assert isinstance(output_shades("e94297", 5), list), "hex = #e94297 and num_shades = 5 did not produce a list"

# run_color_generator test
assert isinstance(run_color_generator("#eeeeee", 5), list), "hex = #eeeeee and num_shades = 5 did not produce a list"
assert isinstance(run_color_generator("#eee", 19), list), "hex = #eee and num_shades = 19 did not produce a list"
assert isinstance(run_color_generator("e94297", 5), list), "hex = #e94297 and num_shades = 5 did not produce a list"

assert run_color_generator("e94297", 'abc')[0:5] == "error", "non-numeric value for num_shades accepted"
assert run_color_generator("e94297", 5.3)[0:5] == "error", "float num_shades value accepted"
assert run_color_generator("e94297", -5)[0:5] == "error", "negative num_shades value accepted"
assert run_color_generator("zzzzzz", 5)[0:5] == "error", "non-hex value accepted"
assert run_color_generator("#", -5)[0:5] == "error", "non-hex value accepted"
assert run_color_generator(123456, 4)[0:5] == "error", "non-string value accepted"

for i in range(1, 20):
	#print "testing num_shades = %s..." % i
	num = len(run_color_generator("e94297", i))
	assert num-i==0, "ER: num_shades=%s, AR: num_shades=%s" % (i, num)

print "all tests passed!"