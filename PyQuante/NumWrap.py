#!/usr/bin/env python
"""
 NumWrap.py - Interface to Numeric and numpy

 An interface to the Numeric and numpy libraries that will (hopefully)
 make the transformation to numpy go as seamlessly as possible.

 Also interfaces the LinearAlgebra and numpy.linalg libraries, since
 these have to be done consistently with the Numeric/numpy choice
"""

# New project to standardize on numpy names and calling conventions
# step one: import new libraries using old names
# step two: change over to new names
# step three: remove NumWrap
#
# Using the new version will be flagged by the 'test_numpy' variable. Just set this to False
#  to turn everything off

# Cleanup things to do:
#  Make a shorter alias for dot than matrixmultiply (matmult or matmul or mm)?
#  Switch the definitions of SimilarityTransform and STT? Maybe also use a shorter name (simx)

test_numpy = True # This is the cutting edge version
use_numpy = False
import re
pat = re.compile('\D')

if test_numpy:
    # New version: eigenvectors in columns
    if use_numpy:
        from numpy import array,zeros,concatenate,dot,ravel,arange
        from numpy import arcsinh,diagonal,identity,choose,transpose
        from numpy import reshape,take
        from numpy import where
        matrixmultiply = dot

        from numpy.linalg import det as determinant
        from numpy.linalg import eigh
        from numpy.linalg import solve as solve_linear_equations

        # still need to kill these two, which are used by Optimize:
        import numpy.oldnumeric.mlab as MLab
        from numpy.oldnumeric import NewAxis
        import numpy as Numeric
    else:
        from Numeric import array,zeros,concatenate,dot,ravel,matrixmultiply
        from Numeric import arange
        from Numeric import arcsinh,diagonal,identity,choose,transpose
        from Numeric import reshape,take
        from Numeric import where
        from Numeric import NewAxis
        from LinearAlgebra import solve_linear_equations,Heigenvectors
        from LinearAlgebra import determinant
        import Numeric
        import MLab

        def eigh(A):
            val,vec = Heigenvectors(A)
            return val,transpose(vec)
else:
    # Old version: eigenvectors in rows:
    if use_numpy:
        from numpy import array,zeros,concatenate,dot,ravel,arange
        from numpy import arcsinh,diagonal,identity,choose,transpose
        from numpy import reshape,take
        from numpy import where
        from numpy import __version__ as version

        words = map(int,pat.split(version))
        big_version = 100*words[0] + 10*words[1]
        if len(words) > 2: big_version += words[0]

        if big_version >= 100:
            from numpy.oldnumeric.linear_algebra import determinant
            from numpy.oldnumeric.linear_algebra import Heigenvectors
            from numpy.oldnumeric.linear_algebra import solve_linear_equations
            import numpy.oldnumeric.mlab as MLab
            from numpy.oldnumeric import NewAxis
        elif big_version >= 98:
            from numpy.linalg.old import determinant
            from numpy.linalg.old import Heigenvectors
            from numpy.linalg.old import solve_linear_equations
            import numpy.lib.mlab as MLab
        else:
            from numpy.linalg import determinant
            from numpy.linalg import Heigenvectors
            from numpy.linalg import solve_linear_equations
            import numpy.lib.mlab as MLab
            from numpy import NewAxis
        matrixmultiply = dot
        import numpy as Numeric
    
    else:
        from Numeric import array,zeros,concatenate,dot,ravel,matrixmultiply
        from Numeric import arange
        from Numeric import arcsinh,diagonal,identity,choose,transpose
        from Numeric import reshape,take
        from Numeric import where
        from Numeric import NewAxis
        from LinearAlgebra import solve_linear_equations,Heigenvectors
        from LinearAlgebra import determinant
        import Numeric
        import MLab

