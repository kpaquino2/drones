from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_up(120)

tello.curve_xyz_speed(50, 50, 0, 200, 0, 0, 40)
tello.curve_xyz_speed(-50, -50, 0, -200, 0, 0, 40)
tello.curve_xyz_speed(-50, 50, 0, -200, 0, 0, 40)
tello.curve_xyz_speed(50, -50, 0, 200, 0, 0, 40)

tello.land()