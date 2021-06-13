def get_target(num_repetitions, num_zeros):
    return f"b{num_zeros*'0'}da"*num_repetitions

def save_result(path, string):
    f = open(path, "w")
    f.write(string)
    f.close()
