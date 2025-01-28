def carFleet(target, position, speed):
    d = {}
    for _ in range(len(position)):
        d[position[_]] = speed[_]
    position.sort(reverse=True)
    res = []
    for i in position:
        time = (target - i) / d[i]
        if not res:
            res.append(time)
        else:
            if time > res[-1]:
                res.append(time)
    return len(res)

target = 10
position = [4,1,0,7]
speed = [2,2,1,1]
print(carFleet(target, position, speed)) # 3

#for a car to become a fleet, it must reach the target at the same time as the car in front of it. To do this the
# the position array must be sorted in descending order. The time it takes for each car to reach the target is calculated
# by dividing the difference between the target and the current position by the speed of the car. The time is then
# compared to the time of the car in front of it. If the time is greater than the time of the car in front of it, then
# it will not be able to catch up to the car in front of it and will not be part of the fleet and becomes a fleet of
# it's own. If the time is less than the time of the car in front of it, then it will be part of the fleet.
# The length of the res array is the number of fleets reaching the target.