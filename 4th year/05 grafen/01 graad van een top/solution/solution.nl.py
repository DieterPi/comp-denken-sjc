def graad( knoop: str, E: list ) -> int:
    count = 0
    for edge in E:
        count += knoop in (edge[0], edge[1])
    
    return count
