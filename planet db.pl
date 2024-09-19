planet('mercury', rocky, 0.39, 88).
planet('venus', rocky, 0.72, 225).
planet('earth', rocky, 1, 365).
planet('mars', rocky, 1.52, 687).
planet('jupiter', gas_giant, 5.2, 4333).
planet('saturn', gas_giant, 9.58, 10759).
planet('uranus', ice_giant, 19.22, 30687).
planet('neptune', ice_giant, 30.05, 60190).
planet_info(Name,Type,Distance,OrbitDays):-
planet(Name,Type,Distance,OrbitDays).