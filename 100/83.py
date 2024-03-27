def solution(data):
    # 종료 시간 기준으로 정렬
    data.sort(key=lambda x: (x['end'], x['start']))
    
    selected_courses = []
    end_time = 0
    max_credits = 0
    
    def convert_time(time_str):
        hour, minute = map(int, time_str.split(':'))
        return hour * 60 + minute
    
    for course in data:
        start_time = convert_time(course['start'])
        end_time = convert_time(course['end'])
        
        # 현재 강의의 시작 시간이 이전 강의의 종료 시간 이후인 경우
        if start_time >= end_time:
            selected_courses.append(course['name'])
            max_credits += course['credit']
            end_time = end_time
    
    return selected_courses