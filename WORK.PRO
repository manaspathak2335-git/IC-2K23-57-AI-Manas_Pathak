domains
    name = symbol
    day = symbol
    time = symbol
    count = integer
    
database
	scheduled(name,name,day,time,name)
	
predicates
	subject(name,name,count)
	room(name)
	slot(day,time)
	
	generate_timetable()
	assign_lecture(name,name,count)
	check_clash(name,name,day,time)
	print_timetable()
	
clauses
	subject(ai,teacher_a,2).
	subject(python,teacher_b,2).
	subject(dbms,teacher_c,1).
	
	room(room_101).
	room(room_102).
	
	slot(monday,"9 AM").
	slot(monday,"10 AM").
	slot(tuesday,"9 AM").
	slot(tuesday,"10 AM").
	slot(wednesday,"9 AM").
	
	check_clash(Teacher,_,Day,Time):-
		scheduled(_,Teacher,Day,Time,_),!,fail.
	check_clash(_,Room,Day,Time):-
		scheduled(_,_,Day,Time,Room),!,fail.
	check_clash(_,_,_,_).
	
	assign_lecture(_,_,0):-!.
	assign_lecture(Subject,Teacher,Lectures):-
		Lectures>0,
		slot(Day,Time),
		room(Room),
		check_clash(Teacher,Room,Day,Time),
		
		assertz(scheduled(Subject,Teacher,Day,Time,Room)),
		NextLectures = Lectures - 1,
		assign_lecture(Subject,Teacher,NextLectures),
		!.
		
	generate_timetable():-
		subject(Subject,Teacher,RequiredLectures),
		assign_lecture(Subject,Teacher,RequiredLectures),
		fail.
	generate_timetable().
	
	print_timetable():-
		scheduled(Subject,Teacher,Day,Time,Room),
		write(Day," ",Time,": ",Subject," | ",Teacher," | ",Room), nl,
		fail.
	print_timetable():-
		write("Status: Timetable generated without techer or room clashes."),nl.
		
goal
	write("GENERATED TIMETABLE"), nl,
	generate_timetable(),
	print_timetable().