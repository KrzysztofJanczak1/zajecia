def read_config(path: str) -> dict[str, str]:
    """Reads config file whose structure is the following:

       key1=value1
       key2=value2
       key3=value3
       key4=value4
       etc.
    """

    result = {}

    with open(path) as f:
        for line in f:
            key, value = line.strip().split('=')
            result[key.strip()] = value.strip()

    return result