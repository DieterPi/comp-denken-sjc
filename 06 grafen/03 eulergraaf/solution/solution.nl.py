def graad( knoop: str, E: list ) -> int:
    count = 0
    for edge in E:
        count += knoop in (edge[0], edge[1])
    
    return count

def euler_graaf( V: list, E: list ) -> bool:
    flag = True
    if len( V ) > 2:
        for v in V:
            flag = flag and graad( v, E ) % 2 == 0
    
    return flag
