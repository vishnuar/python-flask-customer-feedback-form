create table contact_data (
	id integer primary key autoincrement,
	firstname text not null,
	lastname text not null,
	email text not null,
	phone text not null,
	customerdata text not null
);