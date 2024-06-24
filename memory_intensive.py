def generate_large_list():
    return [i for i in range(1000000)]

def process_large_list(large_list):
    return [x * 2 for x in large_list]

large_list = generate_large_list()
processed_list = process_large_list(large_list)
