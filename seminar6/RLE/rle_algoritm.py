def compression_rle(data):
    compression_data = ''
    count = 0
    compress_element = data[0]
    for i,s in enumerate(data):
        if compress_element == data[i] and count < 255:
            count += 1
        else:
            compression_data += chr(count) + compress_element
            compress_element = data[i]
            count = 1
        if (i + 1) == len(data):
            compression_data += chr(count) + compress_element
    return compression_data

def recovery_from_rle(data):
    decompression_data = ''
    for i in range(0,len(data),2):
        count = ord(data[i])
        value = data[i+1]
        decompression_data += value * count
    return decompression_data