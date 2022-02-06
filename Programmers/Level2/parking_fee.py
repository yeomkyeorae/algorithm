import math


def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees
    
    car_record_dict = {}
    car_minutes_dict = {}
    
    for r in records:
        time, car_num, in_out = r.split(" ")
        hour, minute = time.split(":")
        minute = int(hour) * 60 + int(minute)
        
        if car_num in car_record_dict.keys():
            if in_out == "OUT":
                parking_minute = minute - car_record_dict[car_num][0]
                car_minutes_dict[car_num] += parking_minute
        else:
            car_minutes_dict[car_num] = 0
        car_record_dict[car_num] = [minute, in_out]
    
    for car_num in car_record_dict.keys():
        minute, in_out = car_record_dict[car_num]
        
        if in_out == "IN":
            car_minutes_dict[car_num] = (60 * 23 + 59) - minute + car_minutes_dict[car_num]
    
    car_nums = list(car_minutes_dict.keys())
    car_nums.sort()
    
    answer = []
    for car_num in car_nums:
        parking_time = car_minutes_dict[car_num]
        
        add_unit_time = parking_time - basic_time
        if add_unit_time < 0:
            add_unit_time = 0
        
        fee = basic_fee + math.ceil(add_unit_time / unit_time) * unit_fee
        answer.append(fee)
        
    return answer