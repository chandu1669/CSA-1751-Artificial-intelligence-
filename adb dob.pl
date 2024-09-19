person(john, date(1990, 15, 5)).                                                                               
person(emma, date(1989, 9, 10)).
person(michael, date(2021, 12, 8)).
dob_for_person(Name, DOB) :- person(Name, DOB).
is_person_in_db(Name) :- person(Name, _).