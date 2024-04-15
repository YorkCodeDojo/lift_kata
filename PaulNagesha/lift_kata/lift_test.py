import unittest

from lift import Lift, Direction


class MyTestCase(unittest.TestCase):
    def test_given_on_floor0_when_press_0_then_stay_on_floor_0(self):
        lift = Lift()
        lift.push_floor_button(0)

        self.assertEqual(0, len(lift.target_floor))
        self.assertEqual(0, lift.current_floor)

    def test_press_0_on_floor_1(self):
        lift = Lift()
        lift.push_floor_button(1)

        self.assertEqual(1, lift.target_floor[0])

    def test_press_3_then_80_when_on_floor_6(self):
        lift = Lift(6)
        lift.push_floor_button(3)
        lift.push_floor_button(80)

        self.assertEqual([3, 80], lift.target_floor)
        self.assertEqual(Direction.DOWN, lift.direction)

    def test_press_3_and_80_and_12_when_on_floor_6(self):
        lift = Lift(6)
        lift.push_floor_button(3)
        lift.push_floor_button(80)
        lift.push_floor_button(12)

        self.assertEqual([3, 12, 80], lift.target_floor)
        self.assertEqual(Direction.DOWN, lift.direction)

    def test_press_80_and_3_and_12_when_on_floor_6(self):
        lift = Lift(6)
        lift.push_floor_button(80)
        lift.push_floor_button(3)
        lift.push_floor_button(12)

        self.assertEqual([12, 80, 3], lift.target_floor)
        self.assertEqual(Direction.UP, lift.direction)

    def test_press_80_and_3_and_12_and_6_when_on_floor_6(self):
        lift = Lift(6)
        lift.push_floor_button(80)
        lift.push_floor_button(3)
        lift.push_floor_button(12)
        lift.push_floor_button(6)

        self.assertEqual([12, 80, 3], lift.target_floor)
        self.assertEqual(Direction.UP, lift.direction)

    def test_press_18_and_1_and_85_and_8_when_on_floor_14(self):
        lift = Lift(14)
        lift.push_floor_button(18)
        lift.push_floor_button(1)
        lift.push_floor_button(85)
        lift.push_floor_button(85)
        lift.push_floor_button(85)
        lift.push_floor_button(8)
        lift.push_floor_button(8)
        lift.push_floor_button(8)
        lift.push_floor_button(8)
        lift.push_floor_button(8)
        lift.push_floor_button(8)

        self.assertEqual([18, 85, 8, 1], lift.target_floor)
        self.assertEqual(Direction.UP, lift.direction)

    @staticmethod
    def set_up_lift_buttons_presses(lift: Lift):
        lift.push_floor_button(18)
        lift.push_floor_button(1)
        lift.push_floor_button(19)
        lift.push_floor_button(19)
        lift.push_floor_button(19)
        lift.push_floor_button(8)
        lift.push_floor_button(8)
        lift.push_floor_button(8)
        lift.push_floor_button(8)
        lift.push_floor_button(8)
        lift.push_floor_button(8)

        return lift

    def test_move_lift(self):
        lift = self.set_up_lift_buttons_presses(Lift(14))

        self.assertEqual(14, lift.current_floor)

    def test_move_lift_1(self):
        lift = self.set_up_lift_buttons_presses(Lift(14))
        lift.move()

        self.assertEqual([18, 19, 8, 1], lift.target_floor)
        self.assertEqual(15, lift.current_floor)
        self.assertEqual(Direction.UP, lift.direction)

    def test_move_lift_2(self):
        num_moves = 2
        lift = self.set_up_lift_buttons_presses(Lift(14))

        for _ in range(num_moves):
            lift.move()

        self.assertEqual(16, lift.current_floor)
        self.assertEqual(Direction.UP, lift.direction)

    def test_move_lift_3(self):
        num_moves = 3
        lift = self.set_up_lift_buttons_presses(Lift(14))

        for _ in range(num_moves):
            lift.move()

        self.assertEqual(17, lift.current_floor)
        self.assertEqual(Direction.UP, lift.direction)

    def test_move_lift_4(self):
        num_moves = 4
        lift = self.set_up_lift_buttons_presses(Lift(14))

        for _ in range(num_moves):
            lift.move()

        self.assertEqual(18, lift.current_floor)
        self.assertEqual(Direction.UP, lift.direction)
        self.assertEqual([19, 8, 1], lift.target_floor)

    def test_move_lift_5(self):
        num_moves = 5
        lift = self.set_up_lift_buttons_presses(Lift(14))

        for _ in range(num_moves):
            lift.move()

        self.assertEqual(19, lift.current_floor)
        self.assertEqual(Direction.DOWN, lift.direction)
        self.assertEqual([8, 1], lift.target_floor)

    def test_move_lift_6(self):
        num_moves = 6
        lift = self.set_up_lift_buttons_presses(Lift(14))

        for _ in range(num_moves):
            lift.move()

        lift.push_floor_button(90)
        lift.push_floor_button(10)

        self.assertEqual(18, lift.current_floor)
        self.assertEqual(Direction.DOWN, lift.direction)
        self.assertEqual([10, 8, 1, 90], lift.target_floor)

    def test_move_lift_7(self):
        num_moves = 6
        lift = self.set_up_lift_buttons_presses(Lift(14))

        for _ in range(num_moves):
            lift.move()

        lift.push_floor_button(90)
        lift.push_floor_button(10)

        for _ in range(10):
            lift.move()

        self.assertEqual(8, lift.current_floor)
        self.assertEqual(Direction.DOWN, lift.direction)
        self.assertEqual([1, 90], lift.target_floor)


if __name__ == '__main__':
    unittest.main()
