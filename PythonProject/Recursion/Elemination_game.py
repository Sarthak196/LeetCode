def eliminate_game(n):
    # l = [i for i in range(1, n + 1)]
    # step = 0
    # def remove_element(l, step):
    #     if len(l) == 1:
    #         return l[0]
    #     elif step % 2 == 0:
    #         l = remove_first_from_left(l)
    #     else:
    #         l = remove_first_from_right(l)
    #     return remove_element(l, step + 1)
    #
    # def remove_first_from_left(l):
    #     return l[1::2]
    #
    # def remove_first_from_right(l):
    #     l.reverse()
    #     l = l[1::2]
    #     return list(reversed(l))
    #
    # return remove_element(l, step)
    remaining = n
    step = 1
    head = 1
    left_to_right = True

    while remaining > 1:
        # If we're moving from left or it's an odd count, update the head
        if left_to_right or remaining % 2 == 1:
            head += step
        # Reduce the number of elements remaining
        remaining //= 2
        # Double the step size (distance between remaining numbers)
        step *= 2
        # Alternate the direction
        left_to_right = not left_to_right

    return head

print(eliminate_game(6))