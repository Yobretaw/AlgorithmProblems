"""
    Find the total area covered by two rectilinear rectangles in a 2D plane.


        ^                                 (C, D)
        |        +--------------------------+
        |        |                          |
        |        |                          |           (G, H)
        |        |                +---------|-------------+ 
        |        |                |         |             |
        |        |                |         |             |
        |        +--------------------------+             |
        |     (A, B)              |                       |
        |                         |                       |
        |                         |                       |
        |                         +-----------------------+
        |                      (E, F)
        |
        +-------------------------------------------------------------->
     (0, 0)
"""
def compute_area(A, B, C, D, E, F, G, H):
    total = (C - A) * (D - B) + (G - E) * (H - F)

    width = max(0, min(C, G) - max(A, E))
    height = max(0, min(D, H) - max(B, F))

    return total - width * height


if __name__ == '__main__':
    print compute_area(0, 0, 0, 0, -2, -2, 2, 2) == 16
    print compute_area(-2, -2, 2, 2, 3, 3, 4 ,4) == 17
