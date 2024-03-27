import psycopg2


def main():
    conn = psycopg2.connect(
        host="localhost",
        dbname="takehome",
        user="takehome",
        password="takehome",
        port="5432",
    )

    cur = conn.cursor()

    # create table for satellites
    cur.execute(
        """CREATE TABLE IF NOT EXISTS satellites (
        user_id VARCHAR(255) PRIMARY KEY
        );
        """
    )

    # create table for images
    cur.execute(
        """CREATE TABLE IF NOT EXISTS images (
        id INT PRIMARY KEY,
        id_sat VARCHAR(255),
        img bytea,
        CONSTRAINT fk
            FOREIGN KEY (id_sat)
            REFERENCES satellites(user_id)
        );
        """
    )

    # create table for image-requests
    cur.execute(
        """CREATE TABLE IF NOT EXISTS requests (
        time TIMESTAMP PRIMARY KEY,
        id_sat VARCHAR(255),
        request TEXT,
        img_returned BOOLEAN,
        CONSTRAINT fk
            FOREIGN KEY (id_sat)
            REFERENCES satellites(user_id)
        );
        """
    )

    # init DROID satellite
    cur.execute(
        """INSERT INTO satellites (user_id) VALUES
        ('DROID')
        """
    )

    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
