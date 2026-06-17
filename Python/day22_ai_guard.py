class Robot:

    def guard(self):
        print("Area Protected")


class AIGuard(Robot):
    pass

guard1 = AIGuard()
guard1.guard()