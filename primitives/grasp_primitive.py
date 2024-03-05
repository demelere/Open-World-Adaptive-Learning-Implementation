class GraspPrimitive:
    def __init__(self, strength, width):
        self.strength = strength  # Grasp strength, e.g., force applied
        self.width = width  # Grasp width, e.g., distance between gripper fingers

    def execute(self, robot):
        # Use robot API to set gripper width and apply grasp strength
        robot.set_gripper_width(self.width)
        success = robot.apply_grasp_force(self.strength)
        return success
