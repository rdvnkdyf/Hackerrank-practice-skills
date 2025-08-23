def count_8_connected_objects(image):
    rows = len(image)
    if not rows:
        return 0
    cols = len(image[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or image[r][c] == '0':
            return
        
        visited[r][c] = True
        
        dfs(r - 1, c - 1)
        dfs(r - 1, c)
        dfs(r - 1, c + 1)
        dfs(r, c - 1)
        dfs(r, c + 1)
        dfs(r + 1, c - 1)
        dfs(r + 1, c)
        dfs(r + 1, c + 1)

    for r in range(rows):
        for c in range(cols):
            if image[r][c] == '1' and not visited[r][c]:
                count += 1
                dfs(r, c)
    return count

binary_image = [
    "000110001010",
    "111011110001",
    "111010010010",
    "100000000100"
]

object_count = count_8_connected_objects(binary_image)
print(object_count)