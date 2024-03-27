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
        id VARCHAR(255) PRIMARY KEY
        );
        """
    )

    # create table for droids
    cur.execute(
        """CREATE TABLE IF NOT EXISTS droids (
        id VARCHAR(255) PRIMARY KEY
        );
        """
    )

    # init DROID satellite
    cur.execute(
        """INSERT INTO droids (id) VALUES
        ('DROID')
        """
    )

    # create table for images
    cur.execute(
        """CREATE TABLE IF NOT EXISTS images (
        time_taken TIMESTAMP PRIMARY KEY,
        taken_by VARCHAR(255),
        id_sat VARCHAR(255),
        img bytea,
        CONSTRAINT fk
            FOREIGN KEY (id_sat)
            REFERENCES satellites(id)
        CONSTRAINT fk
            FOREIGN KEY (taken_by)
            REFERENCES droids(id)
        );
        """
    )

    # create table for image-requests
    cur.execute(
        """CREATE TABLE IF NOT EXISTS requests (
        time TIMESTAMP PRIMARY KEY,
        target_sat VARCHAR(255),
        fulfilled BOOLEAN,
        CONSTRAINT fk
            FOREIGN KEY (target_sat)
            REFERENCES satellites(id)
        );
        """
    )

    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
