def nested_loops_example(data):
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                result.append(data[i] * data[j] - data[k])
    return result

data = [i for i in range(100)]
nested_loops_example(data)
