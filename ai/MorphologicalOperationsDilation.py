def dilate_image(image):
    rows = len(image)
    if not rows:
        return 0
    cols = len(image[0])

    dilated_image = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if image[r][c] == 1:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        new_r, new_c = r + i, c + j
                        if 0 <= new_r < rows and 0 <= new_c < cols:
                            dilated_image[new_r][new_c] = 1

    pixel_count = sum(row.count(1) for row in dilated_image)
    
    return pixel_count

binary_image = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

result_count = dilate_image(binary_image)
print(result_count)