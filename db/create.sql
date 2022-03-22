CREATE TABLE IF NOT EXISTS students (
    pk INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR (255) NOT NULL,
    surname VARCHAR (255) NOT NULL,
    house_num INT NOT NULL,
    postcode VARCHAR (8) NOT NULL
);

CREATE TABLE IF NOT EXISTS classes (
    pk INT PRIMARY KEY AUTO_INCREMENT,
    c_name VARCHAR (255) NOT NULL,
    c_desc VARCHAR (255) NOT NULL
);

CREATE TABLE IF NOT EXISTS enrollment (
    pk INT PRIMARY KEY AUTO_INCREMENT,
    fk_student INT NOT NULL,
    fk_classes INT NOT NULL,
    FOREIGN KEY (fk_student) REFERENCES students(pk),
    FOREIGN KEY (fk_classes) REFERENCES classes(pk)
);

