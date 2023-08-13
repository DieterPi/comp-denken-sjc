def graad( knoop: str, E: list ) -> int:
    count = 0
    for edge in E:
        count += edge[0] == knoop or edge[1] == knoop
    
    return count
