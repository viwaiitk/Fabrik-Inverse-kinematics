from fabrikSolver import FabrikSolver2D, FabrikSolver3D

arm = FabrikSolver3D()

arm.addSegment(23, 0, 0)
arm.addSegment(15, 0, 0)

arm.compute(7, 0, 0)

arm.plot()

