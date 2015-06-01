# Using functional constructs, and avoiding NaNs

def compute_average(vector):
    vector = filter(lambda x : not math.isnan(x), vector)
    return float(sum(vector))/len(vector) if vector else 0

    a = [2, 3, 4, float('nan')]
    compute_average(a)
    # It should return "3"
