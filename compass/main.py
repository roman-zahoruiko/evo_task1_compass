def direction(facing, turn):
    step_of_turn = 45
    if turn % step_of_turn != 0:
        raise ValueError('Turn degree must be a multiple of 45!')
    elif turn > 1080 or turn < -1080:
        raise ValueError('Turn degree must be between -1080 and 1080!')
    else:
        turn_steps = turn // step_of_turn
    base_directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    if facing not in base_directions:
        raise ValueError('Facing must be one of the 8 base directions: N, NE, E, SE, S, SW, W, NW)')
    start_index = base_directions.index(facing)
    finish_index = (start_index + turn_steps) % len(base_directions)
    return base_directions[finish_index]


if __name__ == "__main__":
    print(direction('NW', 45))



